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
currentFunction = -1

# Temporary Variables
idQueue = []

# Prints raw data for the function table and variable table
def printFuncTable():
    global funcsTable
    for func in funcsTable:
        print("FUNC -> ", func.id, func.vars)

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

        funcsTable[currentFunction].set_var(name, kind)
    