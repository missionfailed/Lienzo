import sys

class NamespaceTable:
    
    def __init__(self):
        self.tabla = {}
    
    """metodo que se llama cuando se lee que se esta declarando una funcion en el programa prueba
    nameOfFunction = nombre de la funcion
    typeOfFunction = tipo de retorno de la funcion
    """
    def addFunction(self, nameOfFunction, typeOfFunction):
        if nameOfFunction in self.tabla:
            error("Funcion ya existe")
        else:
            self.tabla[nameOfFunction] = {}
            print("funcion", nameOfFunction, "de tipo", typeOfFunction, "agregada")
    
    """metodo que se llama cuando se lee que se esta declarando una variable
    nameOfFunction es el nombre de la funcion en cuyo cuerpo se esta declarando esa variable"""
    def addVariable(self, nameOfVariable, typeOfVariable, nameOfFunction):
        if nameOfVariable in self.tabla[nameOfFunction]:
            error("Variable ya existe")
        else:
            self.tabla[nameOfFunction][nameOfVariable] = typeOfVariable
            print("variable", nameOfVariable, "de tipo", typeOfVariable, "agregada en el ambito de", nameOfFunction)
    
    """metodo que se llama cuando se lee que una funcion recibe parametros
    si es por referencia, mode vale 'referencia'
    nameOfFunction es el nombre de la funcion a la que pertenece el parametro"""
    def addParameter(self, nameOfParameter, typeOfParameter, mode, nameOfFunction):
        if nameOfParameter in self.tabla[nameOfFunction]:
            error("Variable ya existe")
        else:
            self.tabla[nameOfFunction][nameOfParameter] = typeOfParameter
            if (mode == None):
                print("parametro", nameOfParameter, "de tipo", typeOfParameter, "por valor agregado en el ambito de", nameOfFunction)
            else:
                print("parametro", nameOfParameter, "de tipo", typeOfParameter, "por referencia agregado en el ambito de", nameOfFunction)
   

"""class VariablesTable:
    
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
    
    
"""        