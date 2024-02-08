// https://docs.python.org/3/reference/index.html
grammar Lang;

// lexer rules 
@lexer::members {    self.nesting = 0}
COMMENT: '#' ~[\r\n]* -> skip;
BOOL: 'True' | 'False';
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
HID: '__' ID '__';
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
KWD: 'def' | 'if' | 'elif' | 'else' | 'and' | 'or' | 'not' ;
SYM : '!' | '*' | '-' | '/' | '+' | '=' | '>' | '<' | ':' 
   | '_' | '.' | '%' | '|' 
    ;
//IGNORE_NEWLINE: '\r'? '\n' {self.nesting>0}? -> skip;
LPAREN: '(' {self.nesting += 1} ;
RPAREN: ')' {self.nesting -= 1} ;
LBRACK: '[' {self.nesting += 1} ;
RBRACK: ']' {self.nesting -= 1} ;
NEWLINE: '\r'? '\n' {self.nesting==0}? ;
INDENT: '    '+ | '\t';
WS : [ ] -> skip ;
LINE_ESCAPE: '\\' '\r'? '\n' -> skip ;

// ###########################################################

// parser rules
newl_ignore : (NEWLINE)*;
prog : newl_ignore file newl_ignore EOF;
file :  (exp (NEWLINE)+)*;

exp : var_decl | a_op | b_op | func_call | if_statement;

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
    | b_op 'and' b_op
    | b_op 'or' b_op
    | 'not' b_op
    | bool
    | var
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

indent: INDENT;
block_end: (indent exp);
block_stmt: indent exp NEWLINE;
block_middle: block_stmt*;
exp_block: block_middle block_stmt | block_middle block_end ;

if_param: (( '(' b_op ')' ) | b_op ) ':';
if: 'if' if_param NEWLINE exp_block;
elif: 'elif' if_param NEWLINE exp_block;
else: 'else' ':' NEWLINE exp_block;
if_statement: if elif* else?;








