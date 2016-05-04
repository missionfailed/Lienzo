from MemoryRegister import *

# operaciones que soporta la maquina virtual
CANVAS_SIZE = "CANVAS_SIZE"
CANVAS_COLOR = "CANVAS_COLOR"
SETSPEED = "SET_SPEED"
READ = "READ"
WRITE = "WRITE"
PRINTLN = "PRINTLN"
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
ASSIGNFUNC = "_=_"
EQUALS = "=="
NOT_EQUALS = '!='
LESS_THAN = "<"
GREATER_THAN = ">"
LESS_THAN_EQUAL = "<="
GREATER_THAN_EQUAL = ">="
AND = "&"
OR = "|"
NOT = "!"
CHECK_BOUNDS = "CHB"
PEN_POSX = "PEN_POSX"
PEN_POSY = "PEN_POSY"
END = "END"

class Cuadruplos:
    def __init__(self):
        self.listaCuadruplos = []
        self.pilaSaltos = []

    '''Regresa la lista de cuadruplos para que sea ejecutada por la maquina virtual'''
    def getCuadruplos(self):
        return self.listaCuadruplos

    '''agrega un cuadruplo a la lista de cuadruplos'''
    def addCuadruplo(self, functionName, operator, op1, op2, t=None, generateT=True):
        if not t and generateT:
            t = TemporalRegister(functionName)
        self.listaCuadruplos.append([operator, op1, op2, t])
        return t
        
    '''edita un cadruplos que quedo pendiente'''
    def editCuadruplo(self, indice, t):
        self.listaCuadruplos[indice][3]=t
    
    '''regresa el indice del ultimo cuadruplo'''
    def last(self):
        return len(self.listaCuadruplos)-1

    '''anade el indice de un cuadruplo a la lista de cuadruplos'''
    def pushPilaSaltos(self, indice):
        self.pilaSaltos.append(indice)
    
    '''elimina el ultimo elemento de la pila saltos'''    
    def popPilaSaltos(self):
        return self.pilaSaltos.pop()
    
    '''regresa el indice actual de la lista de cuadruplos'''
    def current(self):
        return len(self.listaCuadruplos)
