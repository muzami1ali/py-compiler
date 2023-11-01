grammar Expr;
prog : function EOF;
function: 'print' paren Number paren Newline ;
Number : [0-9]+;
Newline : [\n];
paren : '(' | ')';