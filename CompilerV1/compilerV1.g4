grammar compilerV1;
// java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 compilerV1.g4

// Program
program : 'program' ID ';' vars_ funcs 'main' body 'end';

// Vars
vars_ :  'var' vars_helper | ;
vars_helper : id_var ':' type_ ';' vars_helper* ;
id_var : ID (',' id_var)?;

// Type
type_ : 'int' | 'float' ;

// Funcs
funcs : func (funcs)?;
func : 'void' ID '(' param ')' '[' vars_ body ']' ';' ;
param : ID ':' type_ (',' param)? | ;

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