from ply.yacc import yacc

from lexer import lexer, tokens
from grammar import *

if __name__ == "__main__":
    import sys

    # read source file
    with (
        open(sys.argv[1], "rt") if len(sys.argv) > 1 else sys.stdin
    ) as source_file:
        SOURCE = "\n".join(source_file.readlines())
    
    lex = lexer()
    parser = yacc(start='program')
    program = parser.parse(SOURCE, lex, tracking=False)

    print(program)
