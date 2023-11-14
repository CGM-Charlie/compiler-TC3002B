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
    temp_vars: []
    quad_start: int
    quad_end: int

    def get_var(self, key: str) -> any:
        return self.vars.get(key, None)
    
    def get_var_as_quad_arg(self, key: str) -> QuadArg:
        temp_var = self.vars.get(key, None)
        return QuadArg(value=temp_var.name, kind=temp_var.kind)

    def set_var(self, key: str, value: any) -> None:
        self.vars[key] = value

    def element_exists(self, key: str) -> bool:
        return key in self.vars

# Semantic Cube
semantic_cube = {
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
funcs_table = []
quads_table = []
current_function = -1

# Temporary Variables
id_queue = []

# Quadruples Variables
quad_jumps = []
operator = []
operand = []
temporary_var_index = 0

# Prints raw data for the function table and variable table
def print_funcs_table():
    global funcs_table
    # for func in funcs_table:
    #     print("FUNC -> ", func.id, func.quad_end)

# Check if function exists in the Functions Table
def function_exists(name) -> bool:
    for func in funcs_table:
        if func.id == name:
            return True
    
    return False

# Add a new function to the functions table
def add_function(name, vars, exec_line):
    global funcs_table, current_function, temporary_var_index
    current_function += 1
    
    if function_exists(name):
        raise Exception(f"Multiple Redeclaration of {name} at {exec_line}")

    funcs_table.append(Func(id=name, vars=vars, temp_vars=[], quad_start=0, quad_end=0))

def set_func_quad_start(is_main_function: bool):
    global funcs_table, current_function, quads_table

    if is_main_function:
        current_function = 0
        quads_table[0].target = len(quads_table)
        funcs_table[0].quad_start = len(quads_table)
    else:
        funcs_table[current_function].quad_start = len(quads_table)

def set_func_quad_end():
    global funcs_table, current_function, quads_table, temporary_var_index
    quads_table.append(Quadruple(operation="GOTO", arg1=None, arg2=None, target=None))
    funcs_table[current_function].quad_end = len(quads_table)
    temporary_var_index = 0

def init_main_func_quad():
    global quads_table
    quads_table.append(Quadruple(operation="GOTO", arg1=None, arg2=None, target=None))

# Stores the ID while finding the data type it belongs
def add_id(id):
    global id_queue
    id_queue.append(id)

# Add the stored variables into a Variables Table for the current function
# Kind -> Variable Kind (int | float)
# exec_line -> Current line of execution, required for error checking
def add_var(kind, exec_line):
    global funcs_table, current_function, id_queue

    while id_queue:
        name = id_queue.pop(0)
        
        if funcs_table[current_function].element_exists(name):
            raise Exception(f"Multiple Redeclaration of {name} at line {exec_line}")

        funcs_table[current_function].set_var(name, Var(name=name, kind=kind))

# TODO: Find the name and data type in the vars table and use that if it is an ID, else, check the data type with a cast
# in the meantime just store it
def quad_add_operand(name, exec_line, is_var: bool = False):
    global operand

    temp_var: QuadArg

    # Check the sign also with constants lmao 
    if is_var:
        index_plus = name.find('+')
        index_minus = name.find('-')

        if index_plus != -1 or index_minus != -1:
            if not funcs_table[current_function].element_exists(name[1:]):
                raise Exception(f"Unknown variable {name[1:]} at {exec_line}")
            
            temp_var = funcs_table[current_function].get_var_as_quad_arg(name[1:])
            temp_var.value = name
        else:
            if not funcs_table[current_function].element_exists(name):
                raise Exception(f"Unknown variable {name} at {exec_line}")
            
            temp_var = funcs_table[current_function].get_var_as_quad_arg(name)
    else:
        if name.find('.') != -1:
            temp_var = QuadArg(value=name, kind="float")
        else:
            temp_var = QuadArg(value=name, kind="int")

    operand.append(temp_var)

def quad_add_operator(name):
    global operator
    operator.append(name)

def quad_pop_operator():
    global operator
    operator.pop()

def quad_check_mult_or_div():
    global quads_table, operator, operand, temporary_var_index

    if not operator:
        return

    if operator[-1] == '*' or operator[-1] == '/':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()
        
        result_kind = semantic_cube[op][left_operand.kind][right_operand.kind]
        if result_kind == 'null':
            raise Exception(f"Type Mismatch between {right_operand.value} at {left_operand.value}")

        result = QuadArg(value="_t{}".format(temporary_var_index), kind=result_kind) # Check this
        quads_table.append(Quadruple(op, right_operand, left_operand, result))
        operand.append(result)
        temporary_var_index += 1

def quad_check_sum_or_sub():
    global quads_table, operator, operand, temporary_var_index

    if not operator:
        return

    if operator[-1] == '+' or operator[-1] == '-':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()

        result_kind = semantic_cube[op][left_operand.kind][right_operand.kind]
        if result_kind == 'null':
            raise Exception(f"Type Mismatch between {right_operand.value} at {left_operand.value}")

        result = QuadArg(value="_t{}".format(temporary_var_index), kind=result_kind)
        quads_table.append(Quadruple(op, right_operand, left_operand, result))
        operand.append(result)
        temporary_var_index += 1

def quad_check_boolean():
    global quads_table, operator, operand, temporary_var_index

    if not operator:
        return

    if operator[-1] == '<' or operator[-1] == '>' or operator[-1] == '!=':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()
        result = QuadArg(value="_t{}".format(temporary_var_index), kind="bool")
        quads_table.append(Quadruple(op, right_operand, left_operand, result))
        operand.append(result)
        temporary_var_index += 1

def quad_check_assign():
    global quads_table, operator, operand, temporary_var_index

    if not operator:
        return

    if operator[-1] == '=':
        left_operand = operand.pop()
        right_operand = operand.pop()
        op = operator.pop()

        result_kind = semantic_cube[op][left_operand.kind][right_operand.kind]
        if result_kind == 'null':
            raise Exception(f"Type Mismatch between {right_operand.value} at {left_operand.value}")

        quads_table.append(Quadruple(op, left_operand, None, right_operand))

def quad_check_if():
    global quads_table, operator, operand, quad_jumps

    if quads_table[-1].target.kind != 'bool':
        raise Exception(f"Type Mismatch at if condition")
    
    operand.pop()
    quads_table.append(Quadruple(operation="GOTOF", arg1=quads_table[-1].target, arg2=None, target = None))
    quad_jumps.append(len(quads_table)-1)

def quad_check_else():
    global quads_table, operator, operand, quad_jumps
    quads_table.append(Quadruple(operation="GOTO", arg1=quads_table[-1].target, arg2=None, target = None))
    false = quad_jumps.pop()
    quad_jumps.append(len(quads_table)-1)
    quads_table[false].target = len(quads_table)

def quad_end_if():
    global quads_table, operator, operand, quad_jumps
    end = quad_jumps.pop()
    quads_table[end].target = len(quads_table)

def quad_check_while():
    global quads_table, operator, operand, quad_jumps
    quad_jumps.append(len(quads_table))

def quad_evaluate_while():
    global quads_table, operator, operand, quad_jumps

    if quads_table[-1].target.kind != 'bool':
        raise Exception(f"Type Mismatch at if condition")    

    operand.pop()
    end = quad_jumps.pop()
    quads_table.append(Quadruple(operation="GOTOT", arg1=quads_table[-1].target, arg2=None, target = end))

def quad_print_expression():
    global quads_table, operand
    result = operand.pop()
    quads_table.append(Quadruple(operation="PRINT", arg1=result, arg2=None, target=None))

def quad_print_string(text: str):
    global quads_table
    quads_table.append(Quadruple(operation="PRINT", arg1=QuadArg(value=text, kind='str'), arg2=None, target=None))

def get_function_call(id: str):
    global funcs_table, quads_table

    for func in funcs_table:
        if func.id == id:
            return func

    return None  

def quad_init_function_call(id: str):
    global funcs_table, quads_table, operand

    temp_func = get_function_call(id=id)

    if temp_func == None:
        raise Exception(f"Unknown '{id}' function call")
    
    # TODO: To properly check the arguments of the functions, try to implement a funcArgs variable list independent of the main one, or add an extra parameter
    # to indicate the number of parameters

    # if len(operand) != len(temp_func.vars):
    #     raise Exception(f"Valieron los argumentos raza")

    counter = len(operand)

    for i in temp_func.vars:
        if counter <= 0:
            break
        
        tempOperand = operand.pop(0)
        target = QuadArg(value=temp_func.vars[i].name, kind=temp_func.vars[i].kind)
        quads_table.append(Quadruple(operation="=", arg1=tempOperand, arg2=QuadArg(value=temp_func.id, kind="function"), target=target))
        counter -= 1

    quads_table.append(Quadruple(operation="GOTO", arg1=None, arg2=None, target=temp_func.quad_start))
    quads_table[temp_func.quad_end-1].target = len(quads_table)

# Notes for execution
# If any goto function target goes out of bounds, it means that main function is empty or that the code already ended the execution

# Virtual Machine Segment - CarLang

# Function id refers to the current function that is currently being executed
current_function_id = 0
instruction_pointer = 0

def run_quads():
    global quads_table, instruction_pointer, funcs_table

    print("Quads")
    for i in range(0, len(quads_table)):
        print(i, quads_table[i])
    print()

    while instruction_pointer < len(quads_table):
        execute_quad(quads_table[instruction_pointer])
        instruction_pointer += 1
        # print(funcs_table[current_function_id].temp_vars)
        # input()

def execute_quad(quad: Quadruple):
    global instruction_pointer, current_function_id, funcs_table, quads_table

    if quad.operation == "=":
        value = format_expression_argument(quad.arg1)
        funcs_table[current_function_id].get_var(quad.target.value).value = value

    elif quad.operation == "+":
        # Get values for the arguments
        left_operand = format_expression_argument(quad.arg1)
        right_operand = format_expression_argument(quad.arg2)        
        index = int(quad.target.value[2:])

        if index < len(funcs_table[current_function_id].temp_vars):
            if quad.target.kind == "int":
                funcs_table[current_function_id].temp_vars[index] = int(left_operand + right_operand)
            else:
                funcs_table[current_function_id].temp_vars[index] = float(left_operand + right_operand)
        else:
            if quad.target.kind == "int":
                funcs_table[current_function_id].temp_vars.append(int(left_operand + right_operand))
            else:
                funcs_table[current_function_id].temp_vars.append(float(left_operand + right_operand))


    elif quad.operation == "-":
        # Get values for the arguments
        left_operand = format_expression_argument(quad.arg1)
        right_operand = format_expression_argument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcs_table[current_function_id].temp_vars):
            if quad.target.kind == "int":
                funcs_table[current_function_id].temp_vars[index] = int(left_operand - right_operand)
            else:
                funcs_table[current_function_id].temp_vars[index] = float(left_operand - right_operand)
        else:
            if quad.target.kind == "int":
                funcs_table[current_function_id].temp_vars.append(int(left_operand - right_operand))
            else:
                funcs_table[current_function_id].temp_vars.append(float(left_operand - right_operand))

    elif quad.operation == "*":
        # Get values for the arguments
        left_operand = format_expression_argument(quad.arg1)
        right_operand = format_expression_argument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcs_table[current_function_id].temp_vars):
            if quad.target.kind == "int":
                funcs_table[current_function_id].temp_vars[index] = int(left_operand * right_operand)
            else:
                funcs_table[current_function_id].temp_vars[index] = float(left_operand * right_operand)
        else:
            if quad.target.kind == "int":
                funcs_table[current_function_id].temp_vars.append(int(left_operand * right_operand))
            else:
                funcs_table[current_function_id].temp_vars.append(float(left_operand * right_operand))

    elif quad.operation == "/":
        # Get values for the arguments
        left_operand = format_expression_argument(quad.arg1)
        right_operand = format_expression_argument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcs_table[current_function_id].temp_vars):
            if quad.target.kind == "int":
                funcs_table[current_function_id].temp_vars[index] = int(left_operand / right_operand)
            else:
                funcs_table[current_function_id].temp_vars[index] = float(left_operand / right_operand)
        else:
            if quad.target.kind == "int":
                funcs_table[current_function_id].temp_vars.append(int(left_operand / right_operand))
            else:
                funcs_table[current_function_id].temp_vars.append(float(left_operand / right_operand))

    elif quad.operation == "<":
        # Get values for the arguments
        left_operand = format_expression_argument(quad.arg1)
        right_operand = format_expression_argument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcs_table[current_function_id].temp_vars):
            funcs_table[current_function_id].temp_vars[index] = left_operand < right_operand
        else:
            funcs_table[current_function_id].temp_vars.append(left_operand < right_operand)

    elif quad.operation == ">":
        # Get values for the arguments
        left_operand = format_expression_argument(quad.arg1)
        right_operand = format_expression_argument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcs_table[current_function_id].temp_vars):
            funcs_table[current_function_id].temp_vars[index] = left_operand > right_operand
        else:
            funcs_table[current_function_id].temp_vars.append(left_operand > right_operand)

    elif quad.operation == "!=":
        # Get values for the arguments
        left_operand = format_expression_argument(quad.arg1)
        right_operand = format_expression_argument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcs_table[current_function_id].temp_vars):
            funcs_table[current_function_id].temp_vars[index] = left_operand != right_operand
        else:
            funcs_table[current_function_id].temp_vars.append(left_operand != right_operand)

    elif quad.operation == "PRINT":
        if quad.arg1.kind == 'str':
            print(quad.arg1.value.replace('"', ''))
        else:
            print(format_expression_argument(quad.arg1))

    elif quad.operation == "GOTO":
        # To properly assign the instruction_pointer, it is required to sub -1 the target to compensate the
        # update of the instruction_pointer at the next iteration
        instruction_pointer = quad.target - 1

    elif quad.operation == "GOTOF":
        # To properly assign the instruction_pointer, it is required to sub -1 the target to compensate the
        # update of the instruction_pointer at the next iteration
        if not format_expression_argument(quad.arg1):
            instruction_pointer = quad.target - 1

    elif quad.operation == "GOTOT":
        # To properly assign the instruction_pointer, it is required to sub -1 the target to compensate the
        # update of the instruction_pointer at the next iteration
        if format_expression_argument(quad.arg1):
            instruction_pointer = quad.target - 1

def format_expression_argument(quad_arg: QuadArg) -> any:
    global current_function_id, funcs_table
    
    value = None

    # Check if quad_arg is a variable
    if quad_arg.value[0] == "_":
        value = funcs_table[current_function_id].temp_vars[int(quad_arg.value[2:])]

    # Check if quad_arg is a number
    elif quad_arg.value[0].isdigit() or quad_arg.value[0] == "+" and quad_arg.value[1].isdigit() or quad_arg.value[0] == "-" and quad_arg.value[1].isdigit():
        if quad_arg.kind == 'int':
            value = int(quad_arg.value)
        else:
            value = float(quad_arg.value)
    
    # Default to a constant
    else:
        if quad_arg.value[0] == "+":
            value = funcs_table[current_function_id].get_var(quad_arg.value[1:]).value
        elif quad_arg.value[0] == "-":
            value = funcs_table[current_function_id].get_var(quad_arg.value[1:]).value * -1
        else:
            value = funcs_table[current_function_id].get_var(quad_arg.value).value
    
    return value
