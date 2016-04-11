class MemoryRegisters:
    
    def __init__(self):
        self.registers = {}
        self.registers[""] = {}
    
    def newFunction(self, nameOfFunction):
        self.registers[nameOfFunction] = {}
        self.registers[""][nameOfFunction] = MemoryRegister()
    
    def createMemoryRegister(self, nameOfVariable, nameOfFunction):
        self.registers[nameOfFunction][nameOfVariable] = MemoryRegister()
        return self.registers[nameOfFunction][nameOfVariable]
    
    def getMemoryRegister(self, nameOfVariable, nameOfFunction):
        if nameOfVariable in self.registers[nameOfFunction]:
            return self.registers[nameOfFunction][nameOfVariable]
        else:
            return self.registers[""][nameOfVariable]
        
class MemoryRegister:
    c = 0
    
    def __init__(self):
        self.content = None
        self.counter = MemoryRegister.c
        MemoryRegister.c += 1
        
    
    def write(self, c):
        self.content = c
        
    def read(self):
        return self.content
    
    def __repr__(self):
        return 't' + str(self.counter)