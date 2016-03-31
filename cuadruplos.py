from MemoryRegister import *

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


class Cuadruplos:
    def __init__(self):
        self.listaCuadruplos = []
        self.pilaSaltos = []
    
    def addCuadruplo(self, operator, op1, op2, t=None, generateT=True):
        if not t and generateT:
            t = MemoryRegister()
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
    
    def printCuadruplos(self):
        for i, c in enumerate(self.listaCuadruplos):
            print(i,c)
        
        
        
        
        
    
        
