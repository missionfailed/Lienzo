import re
BOLEANO = "boleano"
TEXTO = "texto"
NUMERO = "numero"
NADA = "nada"

class Variable:
    ''' Una variable tiene nombre y tipo'''
    def __init__(self,nameOfVariable,typeOfVariable,ref):
        self.name=nameOfVariable
        self.type=typeOfVariable
        self.reference=ref

'''clase donde se guardan los atributos de un arreglo en especifico'''
class Array:
    def __init__(self, nameOfArray, typeOfArray, lengthOfArray):
        self.name = nameOfArray
        self.type = typeOfArray
        self.length = lengthOfArray
        
class Parameter:
    ''' Una parametro tiene nombre, tipo y referencia'''
    def __init__(self,nameOfVariable,typeOfVariable,ref):
        self.name=nameOfVariable
        self.type=typeOfVariable
        self.reference=ref

class Function:
    '''Una funcion tiene nombre, tipo y variables, que pueden ser variables o parametros'''
    def __init__(self,nameOfFunction,typeOfFunction,dirInicio):
        self.name = nameOfFunction
        self.type = typeOfFunction
        self.variables = []
        self.parameters = []
        self.arrays = []
        self.functionVariables = []
        self.direccionInicio = dirInicio
        self.tipos = {NUMERO: 0, BOLEANO: 0, TEXTO: 0}
        
    '''Recibe los atributos de una variable, la crea y agrega a la funcion'''    
    def addVariable(self,nameOfVariable,typeOfVariable,ref):
        auxiliar = Variable(nameOfVariable,typeOfVariable,ref)
        self.addVariableObject(auxiliar)
    
    '''Recibe los atributos de un parametro, lo crea y agrega a la funcion'''
    def addParameter(self,nameOfVariable,typeOfVariable,ref):
        auxiliar = Parameter(nameOfVariable,typeOfVariable,ref)
        self.parameters.append(auxiliar)

    '''Agrega directamebte una variable ya creada (objeto tipo variable) a la funcion'''    
    def addVariableObject(self,auxiliar):
        self.variables.append(auxiliar)
        self.addType(auxiliar.type)
    
    def addFunctionVariableObject(self, auxiliar):
        self.functionVariables.append(auxiliar)
    
    '''Agrega directamebte un parametro ya creado (objeto tipo parametro) a la funcion'''    
    def addParameterObject(self,auxiliar):
        self.parameters.append(auxiliar)
            
    def addArrayObject(self, auxiliar):
        self.arrays.append(auxiliar)
    
    '''Busca el nombre de una variable dentro de la funcion'''
    def searchVariable(self,variablename):
        for f in self.variables + self.parameters + self.arrays:
            if variablename == f.name:
                return True
        return False
        
    def searchParameter(self, parameterName):
        for f in self.parameters:
            if f.name == parameterName:
                return True
        return False
    
    '''Regresa el tipo del nombre de la variable dada'''
    def getType(self,variablename):
        for f in self.variables + self.parameters + self.arrays:
            if variablename == f.name:
                return f.type
        return None

    '''regresa la longitud de uno de sus arreglos'''    
    def getArrayLength(self, arrayName):
        for a in self.arrays:
            if a.name == arrayName:
                return a.length
        return 0
        
    def addType(self,type):
        self.tipos[type]+=1;
		
class NamespaceTable:
    
    def __init__(self):
        self.tabla = {}
        self.tabla[""] = Function("", NADA, 0)

    '''regresa el directorio de procedimientos'''    
    def getDirProc(self):
        return self.tabla
        
    """Metodo que agrega una funcion a la tabla de funciones. 
    Regresa True si la operacion fue exitosa, False si no."""   
    def addFunction(self, nameOfFunction, typeOfFunction, dirInicio):	
        if nameOfFunction in self.tabla or self.tabla[""].searchVariable(nameOfFunction):
            return False
        else:
            auxiliar = Function(nameOfFunction,typeOfFunction,dirInicio)
            # Nombre del parametro, Tipo del parametro, Booleano Referencia True Valor False
            self.tabla[nameOfFunction]=auxiliar
            if typeOfFunction != NADA:
                self.tabla[""].addFunctionVariableObject(Variable(nameOfFunction, typeOfFunction, False))
            return True
    
    '''Metodo que agrega un parametro a la funcion'''	
    def addParameter(self, nameOfFunction, parameterName, typeOfParameter, modificable):
        if self.tabla[nameOfFunction].searchParameter(parameterName):
            return False
        else:
            self.tabla[nameOfFunction].addParameter(parameterName, typeOfParameter, modificable)
            return True
    
    """Metodo que agrega una variable a la tabla de variables en el ambito de la funcion dada.
    Regresa True si la operacion fue exitosa, False si no."""
    def addVariable(self, nameOfVariable, typeOfVariable, nameOfFunction):
        if self.tabla[nameOfFunction].searchVariable(nameOfVariable) or self.tabla[""].searchVariable(nameOfVariable):
            return False
        else:
            auxiliar=Variable(nameOfVariable,typeOfVariable,False)
            self.tabla[nameOfFunction].addVariableObject(auxiliar)
            return True
    
    '''Metodo que agrega un arreglo al directorio de variables'''
    def addArray(self, nameOfArray, typeOfArray, lengthOfArray, nameOfFunction):
        auxiliar = Array(nameOfArray, typeOfArray, lengthOfArray)
        self.tabla[nameOfFunction].addArrayObject(auxiliar)
    
    """Metodo que se encarga de actualizar tamano cuando hay variables temporales"""
    def addTemporal(self,nameOfFunction,typeOfVariable):
        if self.functionExists(nameOfFunction):
            self.tabla[nameOfFunction].addType(typeOfVariable)
        else:
            return False;
    
    '''Metodo que regresa la longitud del arreglo que se usa dentro de cierta funcion''' 
    def getArrayLength(self, nameOfArray, nameOfFunction):
        answer = self.tabla[nameOfFunction].getArrayLength(nameOfArray)
        if answer == 0:
            answer = self.tabla[""].getArrayLength(nameOfArray)
        return answer
        
    """Regresa true si la variable ya fue declarada (si ya existe dentro de la tabla de variables en el ambito de la funcion dada)"""
    def idAlreadyTaken(self, nameOfVariable, nameOfFunction):
        return nameOfVariable in self.tabla or self.tabla[nameOfFunction].searchVariable(nameOfVariable) or self.tabla[""].searchVariable(nameOfVariable)
	
    '''Metodo que busca una funcion en la tabla de funciones'''
    def functionExists(self, name):
        return name in self.tabla
    
    '''Metodo que regresa el tipo de una variable que se usa dentro de una funcion. Regresa None si la variable no existe'''    
    def getVariableType(self, nameOfVariable, nameOfFunction):
        if self.tabla[nameOfFunction].searchVariable(nameOfVariable):
            return self.tabla[nameOfFunction].getType(nameOfVariable)
        elif self.tabla[""].searchVariable(nameOfVariable):
            return self.tabla[""].getType(nameOfVariable)
        else:
            return None

    '''regresa el tipo de la funcion, si existe. Si no existe, regresa None'''        
    def getFunctionType(self, nameOfFunction):
        if self.functionExists(nameOfFunction):
            return self.tabla[nameOfFunction].type
        else:
            return None

    '''regresa la cantidad de parametros que tiene definidos una funcion'''	    
    def getParameterAmount(self,nameOfFunction):
        return len(self.tabla[nameOfFunction].parameters)
    
    '''regresa si el paraemtro es por referencia. True si si, False si no'''
    def parameterReference(self, nameOfFunction, k):
        return self.tabla[nameOfFunction].parameters[k].reference
    
    """Metodo que checa si los argumentos concuerdan"""
    def argumentAgree(self, nameOfFunction, argumentPos, argumentName, argumentType):
        pattern = re.compile("[A-Za-z]+$")
        if(argumentPos >= len(self.tabla[nameOfFunction].parameters)):
            return False
        else:
            if self.tabla[nameOfFunction].parameters[argumentPos].type != argumentType:
                return False
            else:
                '''Por referencia'''
                if self.tabla[nameOfFunction].parameters[argumentPos].reference:
                    "Hacer match para regexp por ref"
                    if not pattern.match(argumentName):
                        return False                  
                return True
    
    '''regresa el indice del cuadruplo a partir del cual inicia una funcion'''
    def getDireccionInicio(self,nameOfFunction):
        return self.tabla[nameOfFunction].direccionInicio
