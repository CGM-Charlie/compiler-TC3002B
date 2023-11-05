// Carlos Gabriel Mora Madrigal - A01379575

// To generate the parser and lexer for python, run next line in terminal
// java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 compilerV1.g4
// python compilerV1Driver.py input.txt

grammar compilerV1;

@parser::header { 
from variableTable import *
}

// Program
program : {addFunction("global", {}, 0)} {initMainFuncQuad()} 'program' ID ';' vars_ funcs 'main' {setFuncQuadStart(True)} body {printFuncTable()} 'end' {printExpression()} ;

// Vars
vars_ : 'var' vars_helper | ;
vars_helper : id_var ':' type_ ';' {addVar($type_.text, $type_.start.line)} vars_helper* ;
id_var : ID {addID($ID.text)} (',' id_var)?;

// Type
type_ : 'int' | 'float' ;

// Funcs
funcs : func (funcs)?;
func : 'void' ID {addFunction($ID.text, {}, $ID.line)} '(' param ')' '[' vars_ {setFuncQuadStart(False)} body {setFuncQuadEnd()} ']' ';' ;
param : ID {addID($ID.text)} ':' type_ {addVar($type_.text, $type_.start.line)} (',' param)? | ;

// Body
body : '{' statement* '}';

// Statement
statement : assign | condition | cycle | f_call | print_;

// Assign
assign : ID {quadAddOperand($ID.text, $ID.line, True)} '=' {quadAddOperator("=")} expression {quadCheckAssign()} ';';

// Expression
expression : exp {quadCheckBoolean()} (('<' {quadAddOperator("<")} | '>' {quadAddOperator(">")} | '!=' {quadAddOperator("!=")}) expression)? ;
exp : term {quadCheckSumOrSub()} (('+' {quadAddOperator("+")} | '-' {quadAddOperator("-")}) exp)? ;
term : factor {quadCheckMultOrDiv()} (('*' {quadAddOperator("*")} | '/' {quadAddOperator("/")}) term)? ;
factor : '(' {quadAddOperator("(")} expression ')' {quadPopOperator()} | factor_sign ID {quadAddOperand("{}{}".format($factor_sign.text, $ID.text), $ID.line, True)} | factor_sign cte {quadAddOperand("{}{}".format($factor_sign.text, $cte.text), $factor_sign.start.line)};

// Factor Sign
factor_sign : '+' | '-' | ;

// Condition
condition : 'if' '(' expression ')' {quadCheckIf()} body else_statement ';' {quadEndIf()} ;
else_statement : {quadCheckElse()} 'else' body | ;

// Cycles
cycle : 'while' {quadCheckWhile()} body 'do' '(' expression ')' {quadEvaluateWhile()} ';';

// F_Call
f_call : ID '(' f_call_exp ')' {quadInitFunctionCall($ID.text)} ';';
f_call_exp : expression (',' f_call_exp)? | ;

// Print
print_ : 'print' '(' print_exp ')' ';' ;
print_exp : print_exp_arg (',' print_exp)?;
print_exp_arg : expression {quadPrintExpression()} | STRING {quadPrintString($STRING.text)};

// Constants
cte : INT | FLOAT ;
STRING : '"' .*? '"';
ID : [a-zA-Z] ([a-zA-Z] | [0-9])* ;
INT : [0-9] ([0-9])* ;
FLOAT : [0-9] ([0-9])* '.' [0-9] ([0-9])* ;

// Skip whitespace
WS : [ \t\n\r]+ -> skip ;