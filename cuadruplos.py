class Cuadruplos:
    def __init__(self):
        listaCuadruplos = []
    
    def addCuadruplo(self, operator, op1, op2):
        t = MemoryRegister()
        listaCuadruplos.append((operator, op1, op2, t))
        return t
        
