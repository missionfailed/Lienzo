class VariablesTable:
    
    def __init__(self):
        self.lista = []
    
    def add(self, nameOfVariable, typeOfVariable):
        if nameOfVariable in self.lista:
            error("YA FUE DECLARADA")
        else:
            self.lista.append(nameOfVariable)
            print("variable added", nameOfVariable, ", type: ", typeOfVariable)
            
class FunctionsTable:

    def __init__(self):
        self.lista = []
    
    def add(self, nameOfFunction, typeOfFunction):
        if nameOfFunction in self.lista:
            error("YA FUE DECLARADA")
        else:
            self.lista.append(nameOfFunction)
            print("function added", nameOfFunction, ", type: ", typeOfFunction)
    
    
        