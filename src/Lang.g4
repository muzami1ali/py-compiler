// https://docs.python.org/3/reference/index.html
grammar Lang;

// lexer rules 
tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from LangParser import LangParser
}
@lexer::members {    
    self.nesting = 0
class LangDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: LangLexer = lexer

    def pull_token(self):
        return super(LangLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.LangDenter(self, self.NEWLINE, LangParser.INDENT, LangParser.DEDENT, False)
    return self.denter.next_token()

}
KWD: 'def' | 'if' | 'elif' | 'else' | 'and' | 'or' | 'not' 
    | 'while' | 'continue' | 'break' | 'int' | 'float' | 'bool' | 'None' 
    | 'return' | 'len' 
    ;
STRING:  '"' (~'"')* '"' 
      | '\'' (~'\'')* '\'' 
      ;
COMMENT: '#' ~[\r\n]* -> skip;
BOOL: 'True' | 'False';
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
HID: '__' ID '__';
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
SYM : '!' | '*' | '-' | '/' | '+' | '=' | '>' | '<' | ':' 
   | '_' | '.' | '%' | '|' 
    ;
LPAREN: '(' {self.nesting += 1} ;
RPAREN: ')' {self.nesting -= 1} ;
LBRACK: '[' {self.nesting += 1} ;
RBRACK: ']' {self.nesting -= 1} ;
NEWLINE: '\r'? '\n' ' '* {self.nesting==0}? ;
WS : [ ]+ -> skip ;
LINE_ESCAPE: '\\' '\r'? '\n' -> skip ;

// ###########################################################

// parser rules
prog : newl_ignore file newl_ignore EOF;
file :  (exp | function)*;

function: 'def' var args '->' ret_type ':' exp_block ;
ret_smt: 'return' (func_call | a_op | b_op);
exp_block:  INDENT exp+ DEDENT ;
exp : exp_stmt | stmt | if_statement | while_statement;
exp_stmt: stmt NEWLINE;
stmt: func_call | var_decl | a_op | b_op | ret_smt | list_set | list_append | list_get;

len_func: 'len' '(' var ')';
list : '[' (a_op (',' a_op)*)? ']';
type : 'int' | 'float' | 'bool';
ret_type: type | 'None';
format: '.' 'format' '(' a_op (',' a_op)* ')';
str_literal: STRING;
str: str_literal format?;
var : ID;
int : INT;
float : FLOAT;
bool : BOOL;
// break: 'break';
//continue: 'continue';
list_get : var '[' a_op ']';
list_set : var '[' a_op ']' '=' a_op;
list_append: var '.append' '(' a_op ')';

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
    | len_func
    | list_get
    | func_call
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
    | func_call
    | var
    ;

func_call: var params ;
arg: var ':' type;
args:  '(' (arg (',' arg)*)? ')';
param: str | len_func | var | a_op | b_op | func_call | list_get;
params: '(' (param (',' param)* )? ')';


list_var : var '=' list;
aop_var : var '=' a_op;
int_var : var '=' int;
float_var: var '=' float;
bool_var : var '=' b_op;

var_decl : list_var | int_var | float_var | bool_var | aop_var;

if_param: (( '(' b_op ')' ) | b_op ) ':';
if: 'if' if_param exp_block;
elif: 'elif' if_param exp_block;
else: 'else' ':' exp_block;
if_statement: if elif* else?;

while_statement: 'while' if_param exp_block  ('else' ':' exp_block)?;

newl_ignore : (NEWLINE)*;





