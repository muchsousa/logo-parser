from ply.yacc import yacc

from lexer import lexer, tokens
from grammar import *

def testCaseExpr():
    print('\nExample > expr.logo\n')

    SOURCE = 'b = ( 5 > 9 )'

    lex = lexer()
    parser = yacc(start='program')
    program = parser.parse(SOURCE, lex, tracking=False)

    print(program)

def testCaseIfElse():
    print('\nExample > ifelse.logo\n')

    SOURCE = '''
# some comment
a = 5
b = 3
if ( 5 > 4 )
then
    if ( :a > 5 and :b < 5 )
    then
        write 'TRUE'
    else
        write 'FALSE'
            write "Yes, it is"
    end
end
    '''

    lex = lexer()
    parser = yacc(start='program')
    program = parser.parse(SOURCE, lex, tracking=False)

    print(program)

def testCaseMinimal():
    print('\nExample > minimal.logo\n')

    SOURCE = '''
a = 1 - (2 + 3 * 4) * 3
b = :a + 4 * 2 * 3
write :b
'''

    lex = lexer()
    parser = yacc(start='program')
    program = parser.parse(SOURCE, lex, tracking=False)

    print(program)

def testCaseSquare():
    print('\nExample > square.logo\n')

    SOURCE = '''
TO SQUARE :length
    FORWARD :length
    RIGHT 90
    FORWARD :length
    RIGHT 90
    FORWARD :length
    RIGHT 90
    FORWARD :length
    RIGHT 90
END

SETXY 20
SQUARE 30
'''

    lex = lexer()
    parser = yacc(start='program')
    program = parser.parse(SOURCE, lex, tracking=False)

    print(program)

def testCaseWhile():
    print('\nExample > square.logo\n')

    SOURCE = '''
a = 5
WHILE (:a > 0) a = :a - 1 END
'''

    lex = lexer()
    parser = yacc(start='program')
    program = parser.parse(SOURCE, lex, tracking=False)

    print(program)

if __name__ == "__main__":
    # testCaseExpr()
    testCaseIfElse()
    # testCaseMinimal()
    # testCaseSquare()
    # testCaseWhile()