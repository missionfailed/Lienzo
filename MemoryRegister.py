class MemoryRegisters:
    
    def __init__(self):
        self.registers = {}
        self.registers[""] = {}
    
    def newFunction(self, nameOfFunction):
        self.registers[nameOfFunction] = {}
    
    def createMemoryRegister(self, nameOfVariable, nameOfFunction):
        self.registers[nameOfFunction][nameOfVariable] = MemoryRegister()
        return self.registers[nameOfFunction][nameOfVariable]
    
    def getMemoryRegister(self, nameOfVariable, nameOfFunction):
        if nameOfVariable in self.registers[nameOfFunction]:
            return self.registers[nameOfFunction][nameOfVariable]
        else:
            return self.registers[""][nameOfVariable]
        
class MemoryRegister:

    def __init__(self):
        self.content = None
    
    def write(self, c):
        self.content = c
        
    def read(self):
        return self.content