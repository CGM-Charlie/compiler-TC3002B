// Carlos Gabriel Mora Madrigal - A01379575

// To generate the parser and lexer for python, run next line in terminal
// java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 compilerV1.g4

grammar compilerV1;

@parser::header { 
from variableTable import *
}

// Program
program : {addFunction("global", {}, 0)} 'program' ID ';' vars_ funcs 'main' body {printFuncTable()}'end';

// Vars
vars_ : 'var' vars_helper | ;
vars_helper : id_var ':' type_ ';' {addVar($type_.text, $type_.start.line)} vars_helper* ;
id_var : ID {addID($ID.text)} (',' id_var)?;

// Type
type_ : 'int' | 'float' ;

// Funcs
funcs : func (funcs)?;
func : 'void' ID {addFunction($ID.text, {}, $ID.line)} '(' param ')' '[' vars_ body ']' ';' ;
param : ID {addID($ID.text)} ':' type_ {addVar($type_.text, $type_.start.line)} (',' param)? | ;

// Body
body : '{' statement* '}';

// Statement
statement : assign | condition | cycle | f_call | print_;

// Assign
assign : ID '=' expression ';';

// Expression
expression : exp (('<' | '>' | '!=') exp)? ;
exp : term (('+' | '-') exp)? ;
term : factor (('*' | '/') term)? ;
factor : '(' expression ')' | factor_sign ID | factor_sign cte;

// Factor Sign
factor_sign : '+' | '-' | ;

// Condition
condition : 'if' '(' expression ')' body else_statement ';' ;
else_statement : 'else' body | ;

// Cycles
cycle : 'while' body 'do' '(' expression ')' ';';

// F_Call
f_call : ID '(' f_call_exp ')' ';';
f_call_exp : expression (',' f_call_exp)? | ;

// Print
print_ : 'print' '(' print_exp ')' ';' ;
print_exp : print_exp_arg (',' print_exp)?;
print_exp_arg : expression | STRING;

// Constants
cte : INT | FLOAT ;
STRING : '"' .*? '"';
ID : [a-zA-Z] ([a-zA-Z] | [0-9])* ;
INT : [0-9] ([0-9])* ;
FLOAT : [0-9] ([0-9])* '.' [0-9] ([0-9])* ;

// Skip whitespace
WS : [ \t\n\r]+ -> skip ;