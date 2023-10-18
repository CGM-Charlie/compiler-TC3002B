import sys
from antlr4 import *
from compilerV1Lexer import compilerV1Lexer
from compilerV1Parser import compilerV1Parser

# With dis you can generate the stuff
# pip install antlr4-python3-runtime==4.11.1  
# pip install antlr4-python3-runtime==4.9.2
# java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 Calc.g4
# python compilerV1Driver.py input.txt

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = compilerV1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = compilerV1Parser(stream)
    tree = parser.program()

if __name__ == '__main__':
    main(sys.argv)