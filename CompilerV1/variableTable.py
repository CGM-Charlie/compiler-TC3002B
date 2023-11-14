# Carlos Gabriel Mora Madrigal - A01379575

from dataclasses import dataclass

# Data Classes
@dataclass
class Var:
    name: str
    kind: str
    value: any = 0

@dataclass
class Quadruple:
    operation: str
    arg1: any
    arg2: any
    target: any

@dataclass
class QuadArg:
    value: str
    kind: str

@dataclass
class Func:
    id: str
    vars: dict
    tempVars: []
    quadStart: int
    quadEnd: int

    def get_var(self, key: str) -> any:
        return self.vars.get(key, None)
    
    def get_var_as_quadArg(self, key: str) -> QuadArg:
        tempVar = self.vars.get(key, None)
        return QuadArg(value=tempVar.name, kind=tempVar.kind)

    def set_var(self, key: str, value: any) -> None:
        self.vars[key] = value

    def element_exists(self, key: str) -> bool:
        return key in self.vars

# Semantic Cube
semanticCube = {
    '+': {
        'int': {
            'int': 'int',
            'float': 'float',
            'bool': 'null'
        },
        'float': { 
            'int': 'float',
            'float': 'float',
            'bool': 'null'
        },
        'bool': {
            'int': 'null',
            'float': 'null',
            'bool': 'null'
        }
    },
    '-': {
        'int': {
            'int': 'int',
            'float': 'float',
            'bool': 'null'
        },
        'float': { 
            'int': 'float',
            'float': 'float',
            'bool': 'null'
        },
        'bool': {
            'int': 'null',
            'float': 'null',
            'bool': 'null'
        }
    },
    '*': {
        'int': {
            'int': 'int',
            'float': 'float',
            'bool': 'null'
        },
        'float': { 
            'int': 'float',
            'float': 'float',
            'bool': 'null'
        },
        'bool': {
            'int': 'null',
            'float': 'null',
            'bool': 'null'
        }
    },
    '/': {
        'int': {
            'int': 'int',
            'float': 'float',
            'bool': 'null'
        },
        'float': { 
            'int': 'float',
            'float': 'float',
            'bool': 'null'
        },
        'bool': {
            'int': 'null',
            'float': 'null',
            'bool': 'null'
        }
    },
    '=': {
        'int': {
            'int': 'int',
            'float': 'null',
            'bool': 'null'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'bool': 'null'
        },
        'bool': {
            'int': 'null',
            'float': 'null',
            'bool': 'bool'
        }
    }
}

# Global Variables
funcsTable = []
quadTable = []
currentFunction = -1

# Temporary Variables
idQueue = []

# Quadruples - Assign
quadJumps = []
operator = []
operand = []
resultsIndex = 0

# Prints raw data for the function table and variable table
def printFuncTable():
    global funcsTable
    # for func in funcsTable:
    #     print("FUNC -> ", func.id, func.quadEnd)

# Check if function exists in the Functions Table
def function_exists(name) -> bool:
    for func in funcsTable:
        if func.id == name:
            return True
    
    return False

# Add a new function to the functions table
def addFunction(name, vars, execLine):
    global funcsTable, currentFunction, resultsIndex
    currentFunction += 1
    
    if function_exists(name):
        raise Exception(f"Multiple Redeclaration of {name} at {execLine}")

    funcsTable.append(Func(id=name, vars=vars, tempVars=[], quadStart=0, quadEnd=0))

def setFuncQuadStart(isMainFunction: bool):
    global funcsTable, currentFunction, quadTable

    if isMainFunction:
        currentFunction = 0
        quadTable[0].target = len(quadTable)
        funcsTable[0].quadStart = len(quadTable)
    else:
        funcsTable[currentFunction].quadStart = len(quadTable)

def setFuncQuadEnd():
    global funcsTable, currentFunction, quadTable, resultsIndex
    quadTable.append(Quadruple(operation="GOTO", arg1=None, arg2=None, target=None))
    funcsTable[currentFunction].quadEnd = len(quadTable)
    resultsIndex = 0

def initMainFuncQuad():
    global quadTable
    quadTable.append(Quadruple(operation="GOTO", arg1=None, arg2=None, target=None))

# Stores the ID while finding the data type it belongs
def addID(id):
    global idQueue
    idQueue.append(id)

# Add the stored variables into a Variables Table for the current function
# Kind -> Variable Kind (int | float)
# execLine -> Current line of execution, required for error checking
def addVar(kind, execLine):
    global funcsTable, currentFunction, idQueue

    while idQueue:
        name = idQueue.pop(0)
        
        if funcsTable[currentFunction].element_exists(name):
            raise Exception(f"Multiple Redeclaration of {name} at line {execLine}")

        funcsTable[currentFunction].set_var(name, Var(name=name, kind=kind))

# TODO: Find the name and data type in the vars table and use that if it is an ID, else, check the data type with a cast
# in the meantime just store it
def quadAddOperand(name, execLine, isVar: bool = False):
    global operand

    tempVar: QuadArg

    # Check the sign also with constants lmao 
    if isVar:
        indexPlus = name.find('+')
        indexMinus = name.find('-')

        if indexPlus != -1 or indexMinus != -1:
            if not funcsTable[currentFunction].element_exists(name[1:]):
                raise Exception(f"Unknown variable {name[1:]} at {execLine}")
            
            tempVar = funcsTable[currentFunction].get_var_as_quadArg(name[1:])
            tempVar.value = name
        else:
            if not funcsTable[currentFunction].element_exists(name):
                raise Exception(f"Unknown variable {name} at {execLine}")
            
            tempVar = funcsTable[currentFunction].get_var_as_quadArg(name)
    else:
        if name.find('.') != -1:
            tempVar = QuadArg(value=name, kind="float")
        else:
            tempVar = QuadArg(value=name, kind="int")

    operand.append(tempVar)

def quadAddOperator(name):
    global operator
    operator.append(name)

def quadPopOperator():
    global operator
    operator.pop()

def quadCheckMultOrDiv():
    global quadTable, operator, operand, resultsIndex

    if not operator:
        return

    if operator[-1] == '*' or operator[-1] == '/':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()
        
        resultKind = semanticCube[op][left_operand.kind][right_operand.kind]
        if resultKind == 'null':
            raise Exception(f"Type Mismatch between {right_operand.value} at {left_operand.value}")

        result = QuadArg(value="_t{}".format(resultsIndex), kind=resultKind) # Check this
        quadTable.append(Quadruple(op, right_operand, left_operand, result))
        operand.append(result)
        resultsIndex += 1

def quadCheckSumOrSub():
    global quadTable, operator, operand, resultsIndex

    if not operator:
        return

    if operator[-1] == '+' or operator[-1] == '-':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()

        resultKind = semanticCube[op][left_operand.kind][right_operand.kind]
        if resultKind == 'null':
            raise Exception(f"Type Mismatch between {right_operand.value} at {left_operand.value}")

        result = QuadArg(value="_t{}".format(resultsIndex), kind=resultKind)
        quadTable.append(Quadruple(op, right_operand, left_operand, result))
        operand.append(result)
        resultsIndex += 1

def quadCheckBoolean():
    global quadTable, operator, operand, resultsIndex

    if not operator:
        return

    if operator[-1] == '<' or operator[-1] == '>' or operator[-1] == '!=':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()
        result = QuadArg(value="_t{}".format(resultsIndex), kind="bool")
        quadTable.append(Quadruple(op, right_operand, left_operand, result))
        operand.append(result)
        resultsIndex += 1

def quadCheckAssign():
    global quadTable, operator, operand, resultsIndex

    if not operator:
        return

    if operator[-1] == '=':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()

        resultKind = semanticCube[op][left_operand.kind][right_operand.kind]
        if resultKind == 'null':
            raise Exception(f"Type Mismatch between {right_operand.value} at {left_operand.value}")

        quadTable.append(Quadruple(op, left_operand, None, right_operand))

def quadCheckIf():
    global quadTable, operator, operand, quadJumps

    if quadTable[-1].target.kind != 'bool':
        raise Exception(f"Type Mismatch at if condition")
    
    operand.pop()
    quadTable.append(Quadruple(operation="GOTOF", arg1=quadTable[-1].target, arg2=None, target = None))
    quadJumps.append(len(quadTable)-1)

def quadCheckElse():
    global quadTable, operator, operand, quadJumps
    quadTable.append(Quadruple(operation="GOTO", arg1=quadTable[-1].target, arg2=None, target = None))
    false = quadJumps.pop()
    quadJumps.append(len(quadTable)-1)
    quadTable[false].target = len(quadTable)

def quadEndIf():
    global quadTable, operator, operand, quadJumps
    end = quadJumps.pop()
    quadTable[end].target = len(quadTable)

def quadCheckWhile():
    global quadTable, operator, operand, quadJumps
    quadJumps.append(len(quadTable))

def quadEvaluateWhile():
    global quadTable, operator, operand, quadJumps

    if quadTable[-1].target.kind != 'bool':
        raise Exception(f"Type Mismatch at if condition")    

    operand.pop()
    end = quadJumps.pop()
    # TODO: CHECK IF THE QUAD IS GOTOF OR GOTOT
    quadTable.append(Quadruple(operation="GOTOT", arg1=quadTable[-1].target, arg2=None, target = end))

def quadPrintExpression():
    global quadTable, operand
    result = operand.pop()
    quadTable.append(Quadruple(operation="PRINT", arg1=result, arg2=None, target=None))

def quadPrintString(text: str):
    global quadTable
    quadTable.append(Quadruple(operation="PRINT", arg1=QuadArg(value=text, kind='str'), arg2=None, target=None))

def GetFunctionCall(id: str):
    global funcsTable, quadTable

    for func in funcsTable:
        if func.id == id:
            return func

    return None  

def quadInitFunctionCall(id: str):
    global funcsTable, quadTable, operand

    tempFunc = GetFunctionCall(id=id)

    if tempFunc == None:
        raise Exception(f"Unknown '{id}' function call")
    
    # TODO: To properly check the arguments of the functions, try to implement a funcArgs variable list independent of the main one, or add an extra parameter
    # to indicate the number of parameters

    # if len(operand) != len(tempFunc.vars):
    #     raise Exception(f"Valieron los argumentos raza")

    counter = len(operand)

    for i in tempFunc.vars:
        if counter <= 0:
            break
        
        tempOperand = operand.pop(0)
        target = QuadArg(value=tempFunc.vars[i].name, kind=tempFunc.vars[i].kind)
        quadTable.append(Quadruple(operation="=", arg1=tempOperand, arg2=QuadArg(value=tempFunc.id, kind="function"), target=target))
        counter -= 1

    quadTable.append(Quadruple(operation="GOTO", arg1=None, arg2=None, target=tempFunc.quadStart))
    quadTable[tempFunc.quadEnd-1].target = len(quadTable)

# Notes for execution
# If any goto function target goes out of bounds, it means that main function is empty or that the code already ended the execution

# Virtual Machine Segment - CarLang

# Function id refers to the current function that is currently being executed
current_function_id = 0
instruction_pointer = 0

def runQuads():
    global quadTable, instruction_pointer, funcsTable

    print("Quads")
    for i in range(0, len(quadTable)):
        print(i, quadTable[i])
    print()

    while instruction_pointer < len(quadTable):
        executeQuad(quadTable[instruction_pointer])
        instruction_pointer += 1
        # print(funcsTable[current_function_id].tempVars)
        # input()

def executeQuad(quad: Quadruple):
    global instruction_pointer, current_function_id, funcsTable, quadTable

    if quad.operation == "=":
        value = formatExpressionArgument(quad.arg1)
        funcsTable[current_function_id].get_var(quad.target.value).value = value

    elif quad.operation == "+":
        # Get values for the arguments
        left_operand = formatExpressionArgument(quad.arg1)
        right_operand = formatExpressionArgument(quad.arg2)        
        index = int(quad.target.value[2:])

        if index < len(funcsTable[current_function_id].tempVars):
            if quad.target.kind == "int":
                funcsTable[current_function_id].tempVars[index] = int(left_operand + right_operand)
            else:
                funcsTable[current_function_id].tempVars[index] = float(left_operand + right_operand)
        else:
            if quad.target.kind == "int":
                funcsTable[current_function_id].tempVars.append(int(left_operand + right_operand))
            else:
                funcsTable[current_function_id].tempVars.append(float(left_operand + right_operand))


    elif quad.operation == "-":
        # Get values for the arguments
        left_operand = formatExpressionArgument(quad.arg1)
        right_operand = formatExpressionArgument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcsTable[current_function_id].tempVars):
            if quad.target.kind == "int":
                funcsTable[current_function_id].tempVars[index] = int(left_operand - right_operand)
            else:
                funcsTable[current_function_id].tempVars[index] = float(left_operand - right_operand)
        else:
            if quad.target.kind == "int":
                funcsTable[current_function_id].tempVars.append(int(left_operand - right_operand))
            else:
                funcsTable[current_function_id].tempVars.append(float(left_operand - right_operand))

    elif quad.operation == "*":
        # Get values for the arguments
        left_operand = formatExpressionArgument(quad.arg1)
        right_operand = formatExpressionArgument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcsTable[current_function_id].tempVars):
            if quad.target.kind == "int":
                funcsTable[current_function_id].tempVars[index] = int(left_operand * right_operand)
            else:
                funcsTable[current_function_id].tempVars[index] = float(left_operand * right_operand)
        else:
            if quad.target.kind == "int":
                funcsTable[current_function_id].tempVars.append(int(left_operand * right_operand))
            else:
                funcsTable[current_function_id].tempVars.append(float(left_operand * right_operand))

    elif quad.operation == "/":
        # Get values for the arguments
        left_operand = formatExpressionArgument(quad.arg1)
        right_operand = formatExpressionArgument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcsTable[current_function_id].tempVars):
            if quad.target.kind == "int":
                funcsTable[current_function_id].tempVars[index] = int(left_operand / right_operand)
            else:
                funcsTable[current_function_id].tempVars[index] = float(left_operand / right_operand)
        else:
            if quad.target.kind == "int":
                funcsTable[current_function_id].tempVars.append(int(left_operand / right_operand))
            else:
                funcsTable[current_function_id].tempVars.append(float(left_operand / right_operand))

    elif quad.operation == "<":
        # Get values for the arguments
        left_operand = formatExpressionArgument(quad.arg1)
        right_operand = formatExpressionArgument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcsTable[current_function_id].tempVars):
            funcsTable[current_function_id].tempVars[index] = left_operand < right_operand
        else:
            funcsTable[current_function_id].tempVars.append(left_operand < right_operand)

    elif quad.operation == ">":
        # Get values for the arguments
        left_operand = formatExpressionArgument(quad.arg1)
        right_operand = formatExpressionArgument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcsTable[current_function_id].tempVars):
            funcsTable[current_function_id].tempVars[index] = left_operand > right_operand
        else:
            funcsTable[current_function_id].tempVars.append(left_operand > right_operand)

    elif quad.operation == "!=":
        # Get values for the arguments
        left_operand = formatExpressionArgument(quad.arg1)
        right_operand = formatExpressionArgument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcsTable[current_function_id].tempVars):
            funcsTable[current_function_id].tempVars[index] = left_operand != right_operand
        else:
            funcsTable[current_function_id].tempVars.append(left_operand != right_operand)

    elif quad.operation == "PRINT":
        if quad.arg1.kind == 'str':
            print(quad.arg1.value.replace('"', ''))
        else:
            print(formatExpressionArgument(quad.arg1))

    elif quad.operation == "GOTO":
        # To properly assign the instruction_pointer, it is required to sub -1 the target to compensate the
        # update of the instruction_pointer at the next iteration
        instruction_pointer = quad.target - 1

    elif quad.operation == "GOTOF":
        # To properly assign the instruction_pointer, it is required to sub -1 the target to compensate the
        # update of the instruction_pointer at the next iteration
        if not formatExpressionArgument(quad.arg1):
            instruction_pointer = quad.target - 1

    elif quad.operation == "GOTOT":
        # To properly assign the instruction_pointer, it is required to sub -1 the target to compensate the
        # update of the instruction_pointer at the next iteration
        if formatExpressionArgument(quad.arg1):
            instruction_pointer = quad.target - 1

def formatExpressionArgument(quadArg: QuadArg) -> any:
    global current_function_id, funcsTable
    
    value = None

    # Check if QuadArg is a variable
    if quadArg.value[0] == "_":
        value = funcsTable[current_function_id].tempVars[int(quadArg.value[2:])]

    # Check if QuadArg is a number
    elif quadArg.value[0].isdigit() or quadArg.value[0] == "+" and quadArg.value[1].isdigit() or quadArg.value[0] == "-" and quadArg.value[1].isdigit():
        if quadArg.kind == 'int':
            value = int(quadArg.value)
        else:
            value = float(quadArg.value)
    
    # Default to a constant
    else:
        if quadArg.value[0] == "+":
            value = funcsTable[current_function_id].get_var(quadArg.value[1:]).value
        elif quadArg.value[0] == "-":
            value = funcsTable[current_function_id].get_var(quadArg.value[1:]).value * -1
        else:
            value = funcsTable[current_function_id].get_var(quadArg.value).value
    
    return value
