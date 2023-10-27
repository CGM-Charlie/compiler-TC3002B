# Carlos Gabriel Mora Madrigal - A01379575

import sys
from antlr4 import *
from compilerV1Lexer import compilerV1Lexer
from compilerV1Parser import compilerV1Parser

# pip install antlr4-python3-runtime==4.11.1  
# pip install antlr4-python3-runtime==4.9.2

# To test the parser with the input file, run the following command in terminal
# python compilerV1Driver.py input.txt

# Expected result:
# if no errors found: No response in terminal
# if parse errors found: Log of each error detected by the parser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = compilerV1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = compilerV1Parser(stream)
    tree = parser.program()

if __name__ == '__main__':
    main(sys.argv)