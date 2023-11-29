grammar Lang;

// lexer rules 
COMMENTS: '#' .*? [\n\r] -> skip;
INT : [0-9]+ ;
WS : [ \t\n\r]+ -> skip ;

// parser rules
prog : func EOF;
func :
     | atom
    //  | func '/' func
     | func '*' func
     | func '-'<assoc=right> func 
     | func '+' func
     ;
atom : INT ;