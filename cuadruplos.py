from MemoryRegister import *

CANVAS_SIZE = "CANVAS_SIZE"
CANVAS_COLOR = "CANVAS_COLOR"
READ = "READ"
WRITE = "WRITE"
PRINT = "PRINT"
PENUP = "PENUP"
PENDOWN = "PENDOWN"
FORWARD = "FORWARD"
BACKWARD = "BACKWARD"
LEFT = "LEFT"
RIGHT = "RIGHT"
COLOR_CHANGE = "COLOR_CHANGE"
GOTOF = "GOTOF"
GOTO = "GOTO"
END = "END"
RETURN = "RETURN"
ERA = "ERA"
PARAM = "PARAM"
GOSUB = "GOSUB"
RET = "RET"
PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"
MODULO = "%"
ASSIGN = "="
EQUALS = "=="
NOT_EQUALS = '!='
LESS_THAN = "<"
GREATER_THAN = ">"
LESS_THAN_EQUAL = "<="
GREATER_THAN_EQUAL = ">="
AND = "&"
OR = "|"
NOT = "!"

class Cuadruplos:
    def __init__(self):
        self.listaCuadruplos = []
        self.pilaSaltos = []
    
    def getCuadruplos(self):
        return self.listaCuadruplos
   
    def addCuadruplo(self, functionName, operator, op1, op2, t=None, generateT=True):
        if not t and generateT:
            t = TemporalRegister(functionName)
        self.listaCuadruplos.append([operator, op1, op2, t])
        return t
        
    def editCuadruplo(self, indice, t):
        self.listaCuadruplos[indice][3]=t
    
    def last(self):
        return len(self.listaCuadruplos)-1
        
    def pushPilaSaltos(self, indice):
        self.pilaSaltos.append(indice)
    
    def popPilaSaltos(self):
        return self.pilaSaltos.pop()
        
    def current(self):
        return len(self.listaCuadruplos)