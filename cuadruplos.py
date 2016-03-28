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

class Cuadruplos:
    def __init__(self):
        self.listaCuadruplos = []
    
    def addCuadruplo(self, operator, op1, op2, t=None, generateT=True):
        if not t and generateT:
            t = MemoryRegister()
        self.listaCuadruplos.append((operator, op1, op2, t))
        print((operator, op1, op2, t))
        return t
        
