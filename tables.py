class VarsTable(object):
    
    def __init__(self):
        self.lista = []
    
    def add(self, nameOfVariable):
        if nameOfVariable in self.lista:
            error("YA FUE DECLARADA")
        else:
            self.lista.append(nameOfVariable) 
            print("added", nameOfVariable) 
    
    
        