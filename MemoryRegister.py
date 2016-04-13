class MemoryRegisters:
    
    def __init__(self):
        self.registers = {}
        self.registers[""] = {}
        self.nextLocalCounter = {}
    
    def newFunction(self, nameOfFunction):
        self.registers[nameOfFunction] = {}
        self.nextLocalCounter[nameOfFunction] = 0
        self.registers[""][nameOfFunction] = GlobalRegister()
    
    def createMemoryRegister(self, nameOfVariable, nameOfFunction):
        register = None
        if nameOfFunction == "":
            register = GlobalRegister()
        else:
            register = LocalRegister(self.nextLocalCounter[nameOfFunction])
            self.nextLocalCounter[nameOfFunction] += 1
        self.registers[nameOfFunction][nameOfVariable] = register
        return self.registers[nameOfFunction][nameOfVariable]
    
    def getMemoryRegister(self, nameOfVariable, nameOfFunction):
        if nameOfVariable in self.registers[nameOfFunction]:
            return self.registers[nameOfFunction][nameOfVariable]
        else:
            return self.registers[""][nameOfVariable]
        
class TemporalRegister:
    
    nextCounter = {}

    def __init__(self, nameOfFunction):
        if nameOfFunction not in TemporalRegister.nextCounter:
            TemporalRegister.nextCounter[nameOfFunction] = 0
        self.counter = TemporalRegister.nextCounter[nameOfFunction]
        TemporalRegister.nextCounter[nameOfFunction] += 1
    
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
    
    def __init__(self, next):
        self.counter = next
    
    def __repr__(self):
        return 'l' + str(self.counter)