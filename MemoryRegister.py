class MemoryRegisters:
    
    def __init__():
        registers = {}
    
    def newFunction(self, nameOfFunction):
        registers[nameOfFunction] = {}
    
    def createMemoryRegister(self, nameOfVariable, nameOfFunction):
        registers[nameOfFunction][nameOfVariable] = MemoryRegister()
    
    def getMemoryRegister(self, nameOfVariable, nameOfFunction):
        return registers[nameOfFunction][nameOfVariable]
        
class MemoryRegister:

    def __init__(self):
        content = None
    
    def write(self, c):
        content = c
        
    def read(self):
        return content