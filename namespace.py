class NamespaceTable:
    
    def __init__(self):
        self.tabla = {} 
    
    """Metodo queagrega una funcion a la tabla de funciones. 
    Regresa True si la operacion fue exitosa, False si no."""
    def addFunction(self, nameOfFunction, typeOfFunction):
        if nameOfFunction in self.tabla:
            return False
        else:
            self.tabla[nameOfFunction] = {}
            return True
    
    """Metodo que agrega una variable a la tabla de variables en el ambito de la funcion dada.
    Regresa True si la operacion fue exitosa, False si no."""
    def addVariable(self, nameOfVariable, typeOfVariable, nameOfFunction):
        if nameOfVariable in self.tabla[nameOfFunction]:
            return False
        else:
            self.tabla[nameOfFunction][nameOfVariable] = typeOfVariable
            return True
    
    """metodo que agrega un parametro a la tabla de variables en el ambito de la funcion dada.
    Regresa True si la operacion fue exitosa, False si no."""
    def addParameter(self, nameOfParameter, typeOfParameter, mode, nameOfFunction):
        if nameOfParameter in self.tabla[nameOfFunction]:
            return False
        else:
            self.tabla[nameOfFunction][nameOfParameter] = typeOfParameter
            #if (mode == None):
            #    print("parametro", nameOfParameter, "de tipo", typeOfParameter, "por valor agregado en el ambito de", nameOfFunction)
            #else:
            #   print("parametro", nameOfParameter, "de tipo", typeOfParameter, "por referencia agregado en el ambito de", nameOfFunction)
            return True
    
    """Regresa true si la variable ya fue declarada (si ya existe dentro de la tabla de variables en el ambito de la funcion dada)"""
    def variableExists(self, nameOfVariable, nameOfFunction):
        return nameOfVariable in self.tabla[nameOfFunction]
    
    """Regresa True si la funcion ya fue definida (si ya existe dentro de la tabla de funciones)"""
    def functionExists(self, nameOfFunction):
        return nameOfFunction in self.tabla