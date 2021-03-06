'''clase de registros de memoria. administra la memoria que se genera para los cuadruplos'''
class MemoryRegisters:
    
    def __init__(self):
        self.registers = {}
        self.registers[""] = {}
        self.nextLocalCounter = {}

    '''se agrega una nueva funcion y se establece el contador de dicha funcion a 0'''
    def newFunction(self, nameOfFunction, typeOfFunction):
        self.registers[nameOfFunction] = {}
        self.nextLocalCounter[nameOfFunction] = 0
        return self.createMemoryRegister(nameOfFunction, "", typeOfFunction)
    
    '''se crea un registro de memoria para una variable en una funcion'''
    def createMemoryRegister(self, nameOfVariable, nameOfFunction, typeOfVariable=None):
        register = None
        if nameOfFunction == "":
            register = GlobalRegister(typeOfVariable)
        else:
            register = LocalRegister(self.nextLocalCounter[nameOfFunction], typeOfVariable)
            self.nextLocalCounter[nameOfFunction] += 1
        self.registers[nameOfFunction][nameOfVariable] = register
        return register

    '''se crea un registro falso para las variables de referencia'''   
    def createRefRegister(self, nameOfVariable, typeOfVariable, nameOfFunction):
        self.registers[nameOfFunction][nameOfVariable] = RefRegister(self.nextLocalCounter[nameOfFunction], typeOfVariable)
        self.nextLocalCounter[nameOfFunction] += 1
        return self.registers[nameOfFunction][nameOfVariable]
    
    '''se crea un registro para un arreglo'''    
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
    
    '''regresa el registro de memoria asociado a una variable'''
    def getMemoryRegister(self, nameOfVariable, nameOfFunction):
        if nameOfVariable in self.registers[nameOfFunction]:
            return self.registers[nameOfFunction][nameOfVariable]
        else:
            return self.registers[""][nameOfVariable]
    
    '''regresa el registro de memoria asociado a un arreglo'''
    def getArrayMemoryRegister(self, nameOfArray, index, nameOfFunction):
        if nameOfArray in self.registers[nameOfFunction]:
            return (self.registers[nameOfFunction][nameOfArray], index)
        else:
            return (self.registers[""][nameOfArray], index)

'''clase para representar un registro falso donde se guardan las variables por referencia'''
class RefRegister:
    def __init__(self, next, tipo=None):
        self.counter = next
        self.type = tipo
    
    def __repr__(self):
        return 'lr' + str(self.counter)

'''clase para representar un registro temporal donde se guardan los temporales'''
class TemporalRegister:
    
    nextCounter = {}

    def __init__(self, nameOfFunction):
        if nameOfFunction not in TemporalRegister.nextCounter:
            TemporalRegister.nextCounter[nameOfFunction] = 0
        self.counter = TemporalRegister.nextCounter[nameOfFunction]
        TemporalRegister.nextCounter[nameOfFunction] += 1
    
    def __repr__(self):
        return 't' + str(self.counter)

'''clase para guardar los registros globales que estan disponibles para todas las funciones'''
class GlobalRegister():
    c = 0
    
    def __init__(self, tipo = None):
        self.counter = GlobalRegister.c
        self.tipo = tipo
        GlobalRegister.c += 1
    
    def __repr__(self):
        return 'g' + str(self.counter)

'''clase para guardar los registros locales'''
class LocalRegister():
    
    def __init__(self, next, tipo = None):
        self.counter = next
        self.type = tipo
    
    def __repr__(self):
        return 'l' + str(self.counter)
