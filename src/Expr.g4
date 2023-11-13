grammar Expr;
prog : func EOF;
func: atom | func op func;
atom : INT ;
INT : [0-9]+ ;
WS : [ \t\n\r]+ -> skip ;
op: '+' | '-' | '/' | '*' ;