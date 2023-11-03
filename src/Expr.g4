grammar Expr;
prog : function EOF;
print: 'print';
function: print paren num paren newl ;
num : Number;
newl: Newline;
Number : [0-9]+;
Newline : [\n];
paren : '(' | ')';