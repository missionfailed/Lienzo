class MemoryRegisters:
    
    def __init__(self):
        self.registers = {}
        self.registers[""] = {}
    
    def newFunction(self, nameOfFunction):
        self.registers[nameOfFunction] = {}
        self.registers[""][nameOfFunction] = GlobalRegister()
    
    def createMemoryRegister(self, nameOfVariable, nameOfFunction):
        register = None
        if nameOfFunction == "":
            register = GlobalRegister()
        else:
            register = LocalRegister()
        self.registers[nameOfFunction][nameOfVariable] = register
        return self.registers[nameOfFunction][nameOfVariable]
    
    def getMemoryRegister(self, nameOfVariable, nameOfFunction):
        if nameOfVariable in self.registers[nameOfFunction]:
            return self.registers[nameOfFunction][nameOfVariable]
        else:
            return self.registers[""][nameOfVariable]
        
class TemporalRegister:
    c = 0
    
    def __init__(self):
        self.counter = TemporalRegister.c
        TemporalRegister.c += 1
    
    def __repr__(self):
        return 't' + str(self.counter)

class GlobalRegister():
    c = 0
    
    def __init__(self):
        self.counter = GlobalRegister.c
        GlobalRegister.c += 1
    
    def __repr__(self):
        return 'g' + str(self.counter)
        
class LocalRegister():
    c = 0
    
    def __init__(self):
        self.counter = LocalRegister.c
        LocalRegister.c += 1
    
    def __repr__(self):
        return 'l' + str(self.counter)