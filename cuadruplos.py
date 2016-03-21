from MemoryRegister import *

PRINT = "PRINT"
LEER = "LEER"

class Cuadruplos:
    def __init__(self):
        self.listaCuadruplos = []
    
    def addCuadruplo(self, operator, op1, op2, t=None):
        if not t:
            t = MemoryRegister()
        self.listaCuadruplos.append((operator, op1, op2, t))
        print((operator, op1, op2, t))
        return t
        