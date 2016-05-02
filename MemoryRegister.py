class MemoryRegisters:
    
    def __init__(self):
        self.registers = {}
        self.registers[""] = {}
        self.nextLocalCounter = {}
    
    def newFunction(self, nameOfFunction, typeOfFunction):
        self.registers[nameOfFunction] = {}
        self.nextLocalCounter[nameOfFunction] = 0
        return self.createMemoryRegister(nameOfFunction, "", typeOfFunction)
    
    def createMemoryRegister(self, nameOfVariable, nameOfFunction, typeOfVariable=None):
        register = None
        if nameOfFunction == "":
            register = GlobalRegister(typeOfVariable)
        else:
            register = LocalRegister(self.nextLocalCounter[nameOfFunction], typeOfVariable)
            self.nextLocalCounter[nameOfFunction] += 1
        self.registers[nameOfFunction][nameOfVariable] = register
        return register
    
    def createRefRegister(self, nameOfVariable, typeOfVariable, nameOfFunction):
        self.registers[nameOfFunction][nameOfVariable] = RefRegister(self.nextLocalCounter[nameOfFunction], typeOfVariable)
        self.nextLocalCounter[nameOfFunction] += 1
        return self.registers[nameOfFunction][nameOfVariable]
        
    def createMemoryRegisterForArray(self, nameOfArray, typeOfArray, length, nameOfFunction):
        registers = []
        if nameOfFunction == "":
            for i in range(0, length):
                registers.append(GlobalRegister(typeOfArray))
        else:
            for i in range(0, length):
                registers.append(LocalRegister(self.nextLocalCounter[nameOfFunction], typeOfArray))
                self.nextLocalCounter[nameOfFunction] += 1
        self.registers[nameOfFunction][nameOfArray] = registers
        return registers
    
    def getMemoryRegister(self, nameOfVariable, nameOfFunction):
        if nameOfVariable in self.registers[nameOfFunction]:
            return self.registers[nameOfFunction][nameOfVariable]
        else:
            return self.registers[""][nameOfVariable]
    
    def getArrayMemoryRegister(self, nameOfArray, index, nameOfFunction):
        if nameOfArray in self.registers[nameOfFunction]:
            return (self.registers[nameOfFunction][nameOfArray], index)
        else:
            return (self.registers[""][nameOfArray], index)

class RefRegister:
    def __init__(self, next, tipo=None):
        self.counter = next
        self.type = tipo
    
    def __repr__(self):
        return 'lr' + str(self.counter)
            
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
    
    def __init__(self, tipo = None):
        self.counter = GlobalRegister.c
        self.tipo = tipo
        GlobalRegister.c += 1
    
    def __repr__(self):
        return 'g' + str(self.counter)
        
class LocalRegister():
    
    def __init__(self, next, tipo = None):
        self.counter = next
        self.type = tipo
    
    def __repr__(self):
        return 'l' + str(self.counter)