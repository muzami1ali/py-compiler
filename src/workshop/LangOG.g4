// https://docs.python.org/3/reference/index.html
grammar Lang;

// lexer rules 
COMMENT: '#' .*? [\n\r] -> skip;
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
NUM  : [0-9]+ 
     | [0-9]+ '.' [0-9]*
     | '.' [0-9]+
     ; 
BOOL: 'True' | 'False';
WS : [ \t\n\r]+ -> skip ;

// parser rules
prog : file EOF;
file : statement*;



//statements
statement: assignment_stmt | arithmetic_stmt | boolean_stmt | print_stmt;
assignment_stmt: id '=' (arithmetic_stmt | boolean_stmt);
print_stmt: 'print''('(arithmetic_stmt | boolean_stmt)')';
arithmetic_stmt: num
               | arithmetic_stmt '/' arithmetic_stmt
               | arithmetic_stmt '*' arithmetic_stmt
               | arithmetic_stmt '-' arithmetic_stmt 
               | arithmetic_stmt '+' arithmetic_stmt
               ;
boolean_stmt   : bool
               | arithmetic_stmt '>'  arithmetic_stmt
               | arithmetic_stmt '>=' arithmetic_stmt
               | arithmetic_stmt '<'  arithmetic_stmt
               | arithmetic_stmt '<=' arithmetic_stmt
               | arithmetic_stmt '==' arithmetic_stmt
               | arithmetic_stmt '!=' arithmetic_stmt
               ;

//Atoms
num : NUM;
id: ID;
bool: BOOL;