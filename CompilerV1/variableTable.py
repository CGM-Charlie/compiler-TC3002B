# Carlos Gabriel Mora Madrigal - A01379575

from dataclasses import dataclass

# Data Classes
@dataclass
class Func:
    id: str
    vars: dict

    def get_var(self, key: str) -> any:
        return self.vars.get(key, None)
    
    def set_var(self, key: str, value: any) -> None:
        self.vars[key] = value

    def element_exists(self, key: str) -> bool:
        return key in self.vars

@dataclass
class Var:
    name: str
    kind: str

@dataclass
class Quadruple:
    operation: str
    arg1: any
    arg2: any
    target: any

# Semantic Cube
semanticCube = {
    '+': {
        'int': {
            'int': 'int',
            'float': 'float'
        },
        'float': { 
            'int': 'float',
            'float': 'float'
        }
    },
    '-': {
        'int': {
            'int': 'int',
            'float': 'float'
        },
        'float': { 
            'int': 'float',
            'float': 'float'
        }
    },
    '*': {
        'int': {
            'int': 'int',
            'float': 'float'
        },
        'float': { 
            'int': 'float',
            'float': 'float'
        }
    },
    '/': {
        'int': {
            'int': 'int',
            'float': 'float'
        },
        'float': { 
            'int': 'float',
            'float': 'float'
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

operator = []
operand = []
resultsIndex = 0

# TODO: Find the name and data type in the vars table and use that if it is an ID, else, check the data type with a cast
# in the meantime just store it
def quadAddOperand(name):
    global operand
    operand.append(name)

def quadAddOperator(name):
    global operator
    operator.append(name)

def quadPopOperator():
    global operator
    operator.pop()

def quadCheckMultOrDiv():
    global quadTable, operator, operand, resultsIndex

    if operator[-1] == '*' or operator[-1] == '/':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()
        test = "t{}".format(resultsIndex)
        quadTable.append(Quadruple(op, right_operand, left_operand, test))
        operand.append(test)
        resultsIndex += 1

def quadCheckSumOrSub():
    global quadTable, operator, operand, resultsIndex

    if operator[-1] == '+' or operator[-1] == '-':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()
        test = "t{}".format(resultsIndex)
        quadTable.append(Quadruple(op, right_operand, left_operand, test))
        operand.append(test)
        resultsIndex += 1

def quadCheckBoolean():
    global quadTable, operator, operand, resultsIndex

    if operator[-1] == '<' or operator[-1] == '>' or operator[-1] == '!=':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()
        test = "t{}".format(resultsIndex)
        quadTable.append(Quadruple(op, right_operand, left_operand, test))
        operand.append(test)
        resultsIndex += 1

def quadCheckAssign():
    global quadTable, operator, operand, resultsIndex

    if operator[-1] == '=':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()
        quadTable.append(Quadruple(op, left_operand, "", right_operand))

def printExpression():
    global quadTable, operand, operator

    print("Operands", operand)
    print("Operators", operator)

    print("Quads") 
    for quad in quadTable:
        print(quad)

    operand = []
    operator = []
    
    print("\n")
