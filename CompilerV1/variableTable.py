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

# Prints raw data for the function table and variable table
def printFuncTable():
    global funcsTable
    # for func in funcsTable:
    #     print("FUNC -> ", func.id, func.vars)

# Check if function exists in the Functions Table
def function_exists(name) -> bool:
    for func in funcsTable:
        if func.id == name:
            return True
    
    return False

# Add a new function to the functions table
def addFunction(name, vars, execLine):
    global funcsTable, currentFunction
    currentFunction += 1
    
    if function_exists(name):
        raise Exception(f"Multiple Redeclaration of {name} at {execLine}")

    funcsTable.append(Func(name, vars))

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
    

# Quadruples - Assign
quadJumps = []
operator = []
operand = []
resultsIndex = 0

# TODO: Find the name and data type in the vars table and use that if it is an ID, else, check the data type with a cast
# in the meantime just store it
def quadAddOperand(name, execLine, isVar: bool = False):
    global operand

    tempVar: QuadArg

    if isVar:
        indexPlus = name.find('+')
        indexMinus = name.find('-')

        if indexPlus != -1 or indexMinus != -1:
            if not funcsTable[currentFunction].element_exists(name[1:]):
                raise Exception(f"Unknown variable {name[1:]} at {execLine}")
            
            tempVar = funcsTable[currentFunction].get_var_as_quadArg(name[1:])
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

        result = QuadArg(value="t{}".format(resultsIndex), kind="int")
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

        result = QuadArg(value="t{}".format(resultsIndex), kind=resultKind)
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
        result = QuadArg(value="t{}".format(resultsIndex), kind="bool")
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
    quadTable.append(Quadruple(operation="GOTOF", arg1=quadTable[-1].target, arg2=None, target = end))

def printExpression():
    global quadTable, operand, operator

    # print("Operands", operand)
    # print("Operators", operator)

    print("Quads") 
    for quad in quadTable:
        print(quad)

    print("\n")
