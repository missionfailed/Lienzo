from antlr4 import *
from LienzoLexer import LienzoLexer
from LienzoParser import LienzoParser
from LienzoListener import LienzoListener
import sys

class DibujoPrinter(LienzoListener):
	def exitProgram(self, ctx):
		print("Programa parseado con exito")

def main(argv):
    input = FileStream(argv[1])
    lexer = LienzoLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LienzoParser(stream)
    tree = parser.program()
    printer = DibujoPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)

