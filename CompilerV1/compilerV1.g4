// Carlos Gabriel Mora Madrigal - A01379575

// To generate the parser and lexer for python, run next line in terminal
// java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 compilerV1.g4
// python compilerV1Driver.py input.txt

grammar compilerV1;

@parser::header { 
from variableTable import *
}

// Program
program : {add_function("global", {}, 0)} {init_main_func_quad()} 'program' ID ';' vars_ funcs? 'main' {set_func_quad_start(True)} body {print_funcs_table()} 'end' {run_quads()} ;

// Vars
vars_ : 'var' vars_helper | ;
vars_helper : id_var ':' type_ ';' {add_var($type_.text, $type_.start.line, False)} vars_helper* ;
id_var : ID {add_id($ID.text)} (',' id_var)?;

// Type
type_ : 'int' | 'float' ;

// Funcs
funcs : func (funcs)?;
func : 'void' ID {add_function($ID.text, {}, $ID.line)} '(' param ')' '[' vars_ {set_func_quad_start(False)} body {set_func_quad_end()} ']' ';' ;
param : ID {add_id($ID.text)} ':' type_ {add_var($type_.text, $type_.start.line, True)} (',' param)? | ;

// Body
body : '{' statement* '}';

// Statement
statement : assign | condition | cycle | f_call | print_;

// Assign
assign : ID {quad_add_operand($ID.text, $ID.line, True)} '=' {quad_add_operator("=")} expression {quad_check_assign()} ';';

// Expression
expression : exp {quad_check_boolean()} (('<' {quad_add_operator("<")} | '>' {quad_add_operator(">")} | '!=' {quad_add_operator("!=")}) expression)? ;
exp : term {quad_check_sum_or_sub()} (('+' {quad_add_operator("+")} | '-' {quad_add_operator("-")}) exp)? ;
term : factor {quad_check_mult_or_div()} (('*' {quad_add_operator("*")} | '/' {quad_add_operator("/")}) term)? ;
factor : '(' {quad_add_operator("(")} expression ')' {quad_pop_operator()} | factor_sign ID {quad_add_operand("{}{}".format($factor_sign.text, $ID.text), $ID.line, True)} | factor_sign cte {quad_add_operand("{}{}".format($factor_sign.text, $cte.text), $factor_sign.start.line)};

// Factor Sign
factor_sign : '+' | '-' | ;

// Condition
condition : 'if' '(' expression ')' {quad_check_if()} body else_statement ';' {quad_end_if()} ;
else_statement : {quad_check_else()} 'else' body | ;

// Cycles
cycle : 'while' {quad_check_while()} body 'do' '(' expression ')' {quad_evaluate_while()} ';';

// F_Call
f_call : ID '(' f_call_exp ')' {quad_init_function_call($ID.text)} ';';
f_call_exp : expression (',' f_call_exp)? | ;

// Print
print_ : 'print' '(' print_exp ')' ';' ;
print_exp : print_exp_arg (',' print_exp)?;
print_exp_arg : expression {quad_print_expression()} | STRING {quad_print_string($STRING.text)};

// Constants
cte : INT | FLOAT ;
STRING : '"' .*? '"';
ID : [a-zA-Z] ([a-zA-Z] | [0-9])* ;
INT : [0-9] ([0-9])* ;
FLOAT : [0-9] ([0-9])* '.' [0-9] ([0-9])* ;

// Skip whitespace
WS : [ \t\n\r]+ -> skip ;