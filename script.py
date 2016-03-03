from antlr4 import *
from LienzoLexer import LienzoLexer
from LienzoParser import LienzoParser
from KeyPrinter import KeyPrinter
import sys

def main(argv):
    input = FileStream(argv[1])
    lexer = LienzoLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LienzoParser(stream)
    tree = parser.program()
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)