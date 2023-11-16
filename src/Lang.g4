grammar Lang;

// lexer rules 
INT : [0-9]+ ;
WS : [ \t\n\r]+ -> skip ;

// parser rules
prog : func EOF;
func :
     | atom
    //  | func '/' func
     | func '*' func
     | func '-' func 
     | func '+' func
     ;
atom : INT ;