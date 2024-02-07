// https://docs.python.org/3/reference/index.html
grammar Lang;

// lexer rules 
COMMENT: '#' .*? [\n\r] -> skip;
BOOL: 'True' | 'False';
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
HID: '__' ID '__';
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
KWD: 'def' | 'if' ;
SYM : '!' | '*' | '-' | '/' | '+' | '=' | '>' | '<' | ':' 
   | '_' | '.' | '%' | '|' 
    ;
PAREN: '(' | ')';
WS : [ \t\n\r]+ -> skip ;

// ###########################################################

// parser rules
prog : file EOF;
file :  exp*;

exp : var_decl | a_op | b_op | func_call;

var : ID;
int : INT;
float : FLOAT;
bool : BOOL;

a_op: a_op '-' aop3
    | a_op '+' aop3
    | aop3
    ;
aop3: aop2 '/' aop3
    | aop2 '*' aop3
    | aop2 '%' aop3
    | aop2 '//' aop3
    | aop2
    ;
aop2: aop1 '**' aop2
    | aop1 
    ;
aop1: int 
    | var
    | float
    ;

b_op : a_op '>' a_op
    | a_op '<' a_op
    | a_op '<=' a_op
    | a_op '>=' a_op
    | a_op '==' a_op
    | a_op '!=' a_op
    | bool
    ;

param: var | a_op | b_op;

params: '(' (param (',' param)* )* ')';

func_call: var params ;

aop_var : var '=' a_op;
int_var : var '=' int;
float_var: var '=' float;
bool_var : var '=' b_op;

var_decl : int_var | float_var | bool_var | aop_var;

function: 'def' var params ':' exp+ ;

main_func: 'if __name__ == "__main__" :' exp+;








