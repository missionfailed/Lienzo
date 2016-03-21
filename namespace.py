import re

class Variable:
    ''' Una variable tiene nombre y tipo'''
    def __init__(self,nameOfVariable,typeOfVariable,ref):
        self.name=nameOfVariable
        self.type=typeOfVariable
        self.reference=ref
        
class Parameter:
    ''' Una variable tiene nombre y tipo'''
    def __init__(self,nameOfVariable,typeOfVariable,ref):
        self.name=nameOfVariable
        self.type=typeOfVariable
        self.reference=ref

class Function:
    '''Una funcion tiene nombre, tipo y variables, que pueden ser variables o parametros'''
    def __init__(self,nameOfFunction,typeOfFunction):
        self.name = nameOfFunction
        self.type = typeOfFunction
        self.variables = []
        self.parameters = []
        
    def addVariable(self,nameOfVariable,typeOfVariable,ref):
        auxiliar = Variable(nameOfVariable,typeOfVariable,ref)
        self.variables.append(auxiliar)
    
    def addParameter(self,nameOfVariable,typeOfVariable,ref):
        auxiliar = Parameter(nameOfVariable,typeOfVariable,ref)
        self.parameters.append(auxiliar)

    def addVariableObject(self,auxiliar):
        self.variables.append(auxiliar)
    
    def addParameterObject(self,auxiliar):
        self.parameters.append(auxiliar)    

    def searchVariable(self,variablename):
        for f in self.variables + self.parameters:
            if variablename==f.name:
                return True               
        return False
    
    def getType(self,variablename):
        for f in self.variables+ self.parameters:
            if variablename==f.name:
                return f.type
        return None        
		
class NamespaceTable:
    
    def __init__(self):
        self.tabla = {}
								
    """Metodo que agrega una funcion a la tabla de funciones. 
    Regresa True si la operacion fue exitosa, False si no."""
    def addFunction(self, nameOfFunction, typeOfFunction, parameterList):	
        if self.functionExists(nameOfFunction):
            return False
        else:
            auxiliar = Function(nameOfFunction,typeOfFunction)
            "Nombre del parametro, Tipo del parametro, Booleano Referencia True Valor False"
            for item in parameterList:
                auxiliar.addParameter(item[0],item[1],item[2])
            self.tabla[nameOfFunction]=auxiliar
            return True
    
    """Metodo que agrega una variable a la tabla de variables en el ambito de la funcion dada.
    Regresa True si la operacion fue exitosa, False si no."""
    def addVariable(self, nameOfVariable, typeOfVariable, nameOfFunction):
        if self.functionExists(nameOfFunction):
            if self.tabla[nameOfFunction].searchVariable(nameOfVariable):
                return False
            else:
                auxiliar=Variable(nameOfVariable,typeOfVariable,False)
                self.tabla[nameOfFunction].addVariableObject(auxiliar)
                return True
        else:
            return False

    
    """Regresa true si la variable ya fue declarada (si ya existe dentro de la tabla de variables en el ambito de la funcion dada)"""
    def variableExists(self, nameOfVariable, nameOfFunction):
        if self.functionExists(nameOfFunction):
            return self.tabla[nameOfFunction].searchVariable(nameOfVariable)
        else:
            return False
	
    def functionExists(self, name):
        '''Metodo que busca una funcion en la tabla de funciones'''
        if name in self.tabla:
            return True
        else:
            return False

    def getVariableType(self, nameOfVariable, nameOfFunction):
        if self.variableExists(nameOfVariable,nameOfFunction):
            return self.tabla[nameOfFunction].getType(nameOfVariable)
        else:
            return None
            
    def getFunctionType(self, nameOfFunction):
        if self.functionExists(nameOfFunction):
            return self.tabla[nameOfFunction].type
        else:
            return None
    
    def argumentsAgree(self, nameOfFunction, argumentList):
        tamano = len(argumentList)
        pattern = re.compile("[A-Za-z]+$")
        if tamano == len(self.tabla[nameOfFunction].parameters):
            for i,j in list(zip(self.tabla[nameOfFunction].parameters,argumentList)):
                if i.type != j[1]:
                    return False
                else:
                    '''Por referencia'''
                    if i.reference:
                        "Hacer match para regexp por ref"
                        if not pattern.match(j[0]):
                            return False                  
            return True                
        else:
            return False
