import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

# With dis you can generate the stuff
# pip install antlr4-python3-runtime==4.11.1  
# pip install antlr4-python3-runtime==4.9.2
# java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 Calc.g4

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.start_()

if __name__ == '__main__':
    main(sys.argv)