grammar Expr;
prog : func EOF;
func: atom op atom;
atom : INT ;
INT : [0-9]+ ;
WS : [ \t\n\r]+ -> skip ;
op: '+' | '-' | '/' | '*' ;