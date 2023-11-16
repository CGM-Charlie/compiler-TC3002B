# Carlos Gabriel Mora Madrigal - A01379575

from dataclasses import dataclass

# Data classes

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
    arguments: []
    temp_vars: []
    quad_start: int
    quad_end: int

    # Get a single Var object from vars dictionary
    def get_var(self, key: str) -> any:
        return self.vars.get(key, None)
    
    # Get a single Var object from vars dictionary as a QuadArg object
    def get_var_as_quad_arg(self, key: str) -> QuadArg:
        temp_var = self.vars.get(key, None)
        return QuadArg(value=temp_var.name, kind=temp_var.kind)

    # Set a new var into the vars dictionary
    def set_var(self, key: str, value: any) -> None:
        self.vars[key] = value

    # Check if a Var exists in the vars dictionary
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
# name -> Name of the function
# vars -> Dictionary of variables
# exec_line -> Current line of the input file. Just for debbuggin purposes
def add_function(name, vars, exec_line):
    global funcs_table, current_function, temporary_var_index
    current_function += 1
    
    if function_exists(name):
        raise Exception(f"Multiple Redeclaration of {name} at {exec_line}")

    funcs_table.append(Func(id=name, vars=vars, arguments=[], temp_vars=[], quad_start=0, quad_end=0))

# Set the starting point of a function
def set_func_quad_start(is_main_function: bool):
    global funcs_table, current_function, quads_table

    if is_main_function:
        current_function = 0
        quads_table[0].target = len(quads_table)
        funcs_table[0].quad_start = len(quads_table)
    else:
        funcs_table[current_function].quad_start = len(quads_table)

# Set the ending point of a function
def set_func_quad_end():
    global funcs_table, current_function, quads_table, temporary_var_index
    quads_table.append(Quadruple(operation="GOTO", arg1=None, arg2=None, target=None))
    funcs_table[current_function].quad_end = len(quads_table)
    temporary_var_index = 0

# Initialize the starting GOTO Quadruple to jump to the start function
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
def add_var(kind: str, exec_line: str, is_function: bool):
    global funcs_table, current_function, id_queue

    while id_queue:
        name = id_queue.pop(0)
        
        if funcs_table[current_function].element_exists(name):
            raise Exception(f"Multiple Redeclaration of {name} at line {exec_line}")
        
        if is_function:
            funcs_table[current_function].arguments.append(QuadArg(value=name, kind=kind))

        funcs_table[current_function].set_var(name, Var(name=name, kind=kind))

# Add an operand to the operand stack
# Function checks if operand is a constant or a target and considers factor_sign
# Example: +constant, -constant, +1, -1
def quad_add_operand(name, exec_line, is_var: bool = False):
    global operand

    temp_var: QuadArg

    # Check the sign also with constants
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

# Add a new operator to the operator stack
# Name -> Operator sign, Ex. +, -, =, !=
def quad_add_operator(name):
    global operator
    operator.append(name)

# Pop the last operator of the operator stack
def quad_pop_operator():
    global operator
    operator.pop()

# Check if there is a pending multiplication or division to solve in the operator stack
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

# Check if there is a pending addition or substraction to solve in the opeartor stack
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

# Check if there is a pending boolean evaluation to solve in the operator stack
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

# Check if there is a pending assign evaluation to make in the operator stack
def quad_check_assign():
    global quads_table, operator, operand, temporary_var_index

    if not operator:
        return

    if operator[-1] == '=':
        right_operand = operand.pop()
        left_operand = operand.pop()
        op = operator.pop()

        result_kind = semantic_cube[op][left_operand.kind][right_operand.kind]
        if result_kind == 'null':
            raise Exception(f"Type Mismatch between {left_operand.value} at {right_operand.value}")

        quads_table.append(Quadruple(op, right_operand, None, left_operand))

# Initialize a condition quadruple. This evaluates the last element in the operand stack.
# In this functions only initializes the if section of the conditional
def quad_check_if():
    global quads_table, operator, operand, quad_jumps

    if quads_table[-1].target.kind != 'bool':
        raise Exception(f"Type Mismatch at if condition")
    
    operand.pop()
    quads_table.append(Quadruple(operation="GOTOF", arg1=quads_table[-1].target, arg2=None, target = None))
    quad_jumps.append(len(quads_table)-1)

# Initialize the else branch for the condition quadruple.
def quad_check_else():
    global quads_table, operator, operand, quad_jumps

    quads_table.append(Quadruple(operation="GOTO", arg1=None, arg2=None, target = None))
    false = quad_jumps.pop()
    quad_jumps.append(len(quads_table)-1)
    quads_table[false].target = len(quads_table)

# Ends the condition quadruples declaration.
# Generates at the end of the branch a GOTO to jump to the next line of the condition branch
def quad_end_if():
    global quads_table, operator, operand, quad_jumps
    end = quad_jumps.pop()
    quads_table[end].target = len(quads_table)

# Initialize the cycle quadruples declaration.
def quad_check_while():
    global quads_table, operator, operand, quad_jumps
    quad_jumps.append(len(quads_table))

# Create the branching of the while cycle
# In the function creates the GOTOT quadruple to check the evaluation of the while cycle
def quad_evaluate_while():
    global quads_table, operator, operand, quad_jumps

    if quads_table[-1].target.kind != 'bool':
        raise Exception(f"Type Mismatch at if condition")    

    operand.pop()
    end = quad_jumps.pop()
    quads_table.append(Quadruple(operation="GOTOT", arg1=quads_table[-1].target, arg2=None, target = end))

# Create the print quadruple for an expression
def quad_print_expression():
    global quads_table, operand
    result = operand.pop()
    quads_table.append(Quadruple(operation="PRINT", arg1=result, arg2=None, target=None))

# Create the print quadruple for a string constant
def quad_print_string(text: str):
    global quads_table
    quads_table.append(Quadruple(operation="PRINT", arg1=QuadArg(value=text, kind='str'), arg2=None, target=None))

# Helper method to get a single function from the funcs_list
def get_function_call(id: str):
    global funcs_table, quads_table

    for func in funcs_table:
        if func.id == id:
            return func

    return None

# Helper method to get the index from a single function from the funcs_list
def get_function_index(id: str):
    global funcs_table, quads_table

    for i in range(len(funcs_table)):
        if funcs_table[i].id == id:
            return i

    return None

# Creates the quadruples for a function call.
# Checks that the function that is call exists
# Checks the arguments of the function
# If the function has arguments, creates the assign quadruples to initialize the variables in the right variable table
# Creates the GOTO table to jump to the function quadruples in the quadruples list
def quad_init_function_call(id: str):
    global funcs_table, quads_table, operand

    temp_func = get_function_call(id=id)

    # Check if function exists
    if temp_func == None:
        raise Exception(f"Unknown '{id}' function call")

    # Check missing or extra arguments of the function
    if len(operand) != len(temp_func.arguments):
        raise Exception(f"Missing or extra arguments at function call {temp_func.id}")

    counter = len(operand)

    for i in temp_func.vars:
        if counter <= 0:
            break
        
        temp_operand = operand.pop(0)
        target = QuadArg(value=temp_func.vars[i].name, kind=temp_func.vars[i].kind)
        quads_table.append(Quadruple(operation="=", arg1=temp_operand, arg2=QuadArg(value=temp_func.id, kind="function"), target=target))
        counter -= 1

    quads_table.append(Quadruple(operation="GOTO", arg1=QuadArg(temp_func.id, kind="function"), arg2=None, target=temp_func.quad_start))

# ----- Virtual Machine Segment -----

# Notes for execution
# If any goto function target goes out of bounds, it means that main function is empty or that the code already ended the execution

# Current function that is being excecuted from the funcs_list. 0 means main function is being excecuted
current_function_id = 0
# Instruction pointer. Indicates the current quadruple that is being excecuted
instruction_pointer = 0

# Initialize the Virtual Machine for the quadruples
def run_quads():
    global quads_table, instruction_pointer, funcs_table

    # Debbuging function to print the complete quadruples list
    print("Quads")
    for i in range(0, len(quads_table)):
        print(i, quads_table[i])
    print()

    while instruction_pointer < len(quads_table):
        # print(instruction_pointer, quads_table[instruction_pointer])
        execute_quad(quads_table[instruction_pointer])
        instruction_pointer += 1
        # input()

# Excecute the quadruple code
def execute_quad(quad: Quadruple):
    global instruction_pointer, current_function_id, funcs_table, quads_table

    # Assign operation
    # If the argument 2 is None, assigns the argument of a function
    # Else, regular assign of a variable in the current function context
    if quad.operation == "=":
        if quad.arg2 == None:
            value = format_expression_argument(quad.arg1)
            funcs_table[current_function_id].get_var(quad.target.value).value = value
        else:
            function_index = get_function_index(quad.arg2.value)
            value = format_expression_argument(quad.arg1)
            funcs_table[function_index].get_var(quad.target.value).value = value

    # Addition operation
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

    # Subtraction operation
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

    # Multiplication operation
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

    # Division operation
    # Supports integer division by making division with only integers
    # Supports decimal division by making division with only float numbers
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

    # < boolean evaluation
    elif quad.operation == "<":
        # Get values for the arguments
        left_operand = format_expression_argument(quad.arg1)
        right_operand = format_expression_argument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcs_table[current_function_id].temp_vars):
            funcs_table[current_function_id].temp_vars[index] = left_operand < right_operand
        else:
            funcs_table[current_function_id].temp_vars.append(left_operand < right_operand)

    # > boolean evaluation
    elif quad.operation == ">":
        # Get values for the arguments
        left_operand = format_expression_argument(quad.arg1)
        right_operand = format_expression_argument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcs_table[current_function_id].temp_vars):
            funcs_table[current_function_id].temp_vars[index] = left_operand > right_operand
        else:
            funcs_table[current_function_id].temp_vars.append(left_operand > right_operand)

    # != boolean evaluation
    elif quad.operation == "!=":
        # Get values for the arguments
        left_operand = format_expression_argument(quad.arg1)
        right_operand = format_expression_argument(quad.arg2)
        index = int(quad.target.value[2:])

        if index < len(funcs_table[current_function_id].temp_vars):
            funcs_table[current_function_id].temp_vars[index] = left_operand != right_operand
        else:
            funcs_table[current_function_id].temp_vars.append(left_operand != right_operand)

    # Print evaluation
    elif quad.operation == "PRINT":
        if quad.arg1.kind == 'str':
            print(quad.arg1.value.replace('"', ''))
        else:
            print(format_expression_argument(quad.arg1))

    # GOTO Jump. Updates the instruction pointer address to jump to another region of quadruples to excecute
    # If the arg1 of the quadruple is None, the jump is addressed to the main function
    # Else, the jump is addressed to a function
    elif quad.operation == "GOTO":
        # To properly assign the instruction_pointer, it is required to sub -1 the target to compensate the
        # update of the instruction_pointer at the next iteration

        if quad.arg1 == None:
            current_function_id = 0
        else:
            temp_func = get_function_call(quad.arg1.value)

            if current_function_id == 0:
                quads_table[temp_func.quad_end-1].target = instruction_pointer + 1

            current_function_id = get_function_index(quad.arg1.value)

        instruction_pointer = quad.target - 1

    # GOTO False jump. Updates the instruction pointer address to jump if the expressio result is false
    elif quad.operation == "GOTOF":
        # To properly assign the instruction_pointer, it is required to sub -1 the target to compensate the
        # update of the instruction_pointer at the next iteration
        if not format_expression_argument(quad.arg1):

            # Create the temporary variables memory space in case else branch is selected
            for i in range(instruction_pointer + 1, quad.target-1):
                if type(quads_table[i].target) == QuadArg:
                    if quads_table[i].target.value[0] == "_":
                        funcs_table[current_function_id].temp_vars.append(0)

            instruction_pointer = quad.target - 1

    # GOTO True jump. Updates the instruction pointer address to jump if the expressio result is true
    elif quad.operation == "GOTOT":
        # To properly assign the instruction_pointer, it is required to sub -1 the target to compensate the
        # update of the instruction_pointer at the next iteration
        if format_expression_argument(quad.arg1):
            instruction_pointer = quad.target - 1

# Format the quadruple argument to fetch the values of variables, constants or temporals from memory
def format_expression_argument(quad_arg: QuadArg) -> any:
    global current_function_id, funcs_table
    
    value = None

    # Check if quad_arg is a temp variable
    if quad_arg.value[0] == "_":
        value = funcs_table[current_function_id].temp_vars[int(quad_arg.value[2:])]

    # Check if quad_arg is a number
    elif quad_arg.value[0].isdigit() or quad_arg.value[0] == "+" and quad_arg.value[1].isdigit() or quad_arg.value[0] == "-" and quad_arg.value[1].isdigit():
        if quad_arg.kind == 'int':
            value = int(quad_arg.value)
        else:
            value = float(quad_arg.value)
    
    # Default to a variable
    else:
        if quad_arg.value[0] == "+":
            value = funcs_table[current_function_id].get_var(quad_arg.value[1:]).value
        elif quad_arg.value[0] == "-":
            value = funcs_table[current_function_id].get_var(quad_arg.value[1:]).value * -1
        else:
            value = funcs_table[current_function_id].get_var(quad_arg.value).value
    
    return value
