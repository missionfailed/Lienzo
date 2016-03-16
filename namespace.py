class Variable:
	''' Una variable tiene nombre y tipo'''
	def __init__(self,nameOfVariable,typeOfVariable):
		self.name=nameOfVariable;
		self.type=typeOfVariable;

class Parameter:
	'''Un parametro es una variable con tipo de referencia'''
	def __init__(self,nameOfVariable,typeOfVariable,ref):
		self.variable = Variable(nameOfVariable,typeOfVariable);
		self.referenceType = ref;

class Function:
	'''Una funcion tiene nombre, tipo y variables, que pueden ser variables o parametros'''
	def __init__(self,nameOfFunction,typeOfFunction):
		self.name = nameOfFunction;
		self.type = typeOfFunction;
		self.variables = [];
		
	def addParameter(self,nameOfVariable,typeOfVariable,ref):
		auxiliar = Parameter(nameOfVariable,typeOfVariable,ref);
		self.variables.append(auxiliar);
	
	def addVariables():
		auxiliar = Variable(nameOfVariable,typeOfVariable);
		self.variables.append(auxiliar);	
		
		

class NamespaceTable:
    
    def __init__(self):
        self.tabla = ();
	
    def searchVariable(self,nameOfVariable,nameOfFunction):
        '''Metodo que busca una variable dentro de una funcion'''
        for f in self.tabla:
            if(f.name == nameOfFunction):
                if nameOfVariable in f.variables:
                    return true;
                else:
                    return false;
								
    """Metodo que agrega una funcion a la tabla de funciones. 
    Regresa True si la operacion fue exitosa, False si no."""
    def addFunction(self, nameOfFunction, typeOfFunction, parameterList):	
        if functionExists(nameOfFunction):
            return False
        else:
            auxiliar = Function(nameOfFunction,typeOfFunction);
            "Nombre del parametro, Tipo del parametro, Booleano Referencia o Valor"
            for item in parameterList:
                auxiliar.addParameter(item[0],item[1],item[2]);
            self.tabla.append(auxiliar);
            return True
    
    """Metodo que agrega una variable a la tabla de variables en el ambito de la funcion dada.
    Regresa True si la operacion fue exitosa, False si no."""
    def addVariable(self, nameOfVariable, typeOfVariable, nameOfFunction):
        if nameOfVariable in self.tabla[nameOfFunction]:
            return False
        else:
            auxiliar=Variable(nameOfVariable,typeOfVariable);
            if nameOfFunction in self.tabla:
                '''La tabla de funciones contiene los objetos funcion'''
                self.tabla[nameOfFunction][auxiliar.name] = auxiliar;
                return True;
            else:
                return False;
    
    """Regresa true si la variable ya fue declarada (si ya existe dentro de la tabla de variables en el ambito de la funcion dada)"""
    def variableExists(self, nameOfVariable, nameOfFunction):
        return nameOfVariable in self.tabla[nameOfFunction]
	
    def functionExists(self, name):
        '''Metodo que busca una funcion en la tabla de funciones'''
        for f in self.tabla:
            if(f.name == name):
                return true;
        return false;
    