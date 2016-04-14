import turtle
from cuadruplos import *
from MemoryRegister import *

BOOL = 0
NUMBER = 1
STRING = 2
TEMPORAL = 3
GLOBAL = 4
LOCAL = 5
pila = [[[],[]]]

def executeVM(dirProc, listaCuadruplos):
    global pila
    
    for i, c in enumerate(listaCuadruplos):
        print(i,c)
        op=c[0]
        valor1=c[1]
        valor2=c[2]
        variable=c[3]
        
        if op==ASSIGN:
            if Tipo(variable)==GLOBAL:
                if len(pila[0][0])<=variable.counter:
                    pila[0][0].append(None)
                pila[0][0][variable.counter] = Valor(valor1)
            elif Tipo(variable)==LOCAL:
                if len(pila[len(pila)-1][0])<=variable.counter:
                    pila[len(pila)-1][0].append(None)
                pila[len(pila)-1][0][variable.counter] = Valor(valor1)
            elif Tipo(variable)==TEMPORAL:
                if len(pila[len(pila)-1][1])<=variable.counter:
                    pila[len(pila)-1][1].append(None)            
                pila[len(pila)-1][1][variable.counter] = Valor(valor1)
                
        elif op==TIMES:
            if Tipo(variable)==GLOBAL:
                if len(pila[0][0])<=variable.counter:
                    pila[0][0].append(None)
                pila[0][0][variable.counter] = Valor(valor1) * Valor(valor2)
            elif Tipo(variable)==LOCAL:
                if len(pila[len(pila)-1][0])<=variable.counter:
                    pila[len(pila)-1][0].append(None)
                pila[len(pila)-1][0][variable.counter] = Valor(valor1) * Valor(valor2)
            elif Tipo(variable)==TEMPORAL:
                if len(pila[len(pila)-1][1])<=variable.counter:
                    pila[len(pila)-1][1].append(None)            
                pila[len(pila)-1][1][variable.counter] = Valor(valor1) * Valor(valor2)

        elif op==PLUS:
            if Tipo(variable)==GLOBAL:
                if len(pila[0][0])<=variable.counter:
                    pila[0][0].append(None)
                pila[0][0][variable.counter] = Valor(valor1) + Valor(valor2)
            elif Tipo(variable)==LOCAL:
                if len(pila[len(pila)-1][0])<=variable.counter:
                    pila[len(pila)-1][0].append(None)
                pila[len(pila)-1][0][variable.counter] = Valor(valor1) + Valor(valor2)
            elif Tipo(variable)==TEMPORAL:
                if len(pila[len(pila)-1][1])<=variable.counter:
                    pila[len(pila)-1][1].append(None)            
                pila[len(pila)-1][1][variable.counter] = Valor(valor1) + Valor(valor2)

        elif op==MINUS:
            if Tipo(variable)==GLOBAL:
                if len(pila[0][0])<=variable.counter:
                    pila[0][0].append(None)
                pila[0][0][variable.counter] = Valor(valor1) - Valor(valor2)
            elif Tipo(variable)==LOCAL:
                if len(pila[len(pila)-1][0])<=variable.counter:
                    pila[len(pila)-1][0].append(None)
                pila[len(pila)-1][0][variable.counter] = Valor(valor1) - Valor(valor2)
            elif Tipo(variable)==TEMPORAL:
                if len(pila[len(pila)-1][1])<=variable.counter:
                    pila[len(pila)-1][1].append(None)            
                pila[len(pila)-1][1][variable.counter] = Valor(valor1) - Valor(valor2)
                
        elif op==DIVIDE:
            if Tipo(variable)==GLOBAL:
                if len(pila[0][0])<=variable.counter:
                    pila[0][0].append(None)
                pila[0][0][variable.counter] = Valor(valor1) / Valor(valor2)
            elif Tipo(variable)==LOCAL:
                if len(pila[len(pila)-1][0])<=variable.counter:
                    pila[len(pila)-1][0].append(None)
                pila[len(pila)-1][0][variable.counter] = Valor(valor1) / Valor(valor2)
            elif Tipo(variable)==TEMPORAL:
                if len(pila[len(pila)-1][1])<=variable.counter:
                    pila[len(pila)-1][1].append(None)            
                pila[len(pila)-1][1][variable.counter] = Valor(valor1) / Valor(valor2)

        elif op==MODULO:
            if Tipo(variable)==GLOBAL:
                if len(pila[0][0])<=variable.counter:
                    pila[0][0].append(None)
                pila[0][0][variable.counter] = Valor(valor1) % Valor(valor2)
            elif Tipo(variable)==LOCAL:
                if len(pila[len(pila)-1][0])<=variable.counter:
                    pila[len(pila)-1][0].append(None)
                pila[len(pila)-1][0][variable.counter] = Valor(valor1) % Valor(valor2)
            elif Tipo(variable)==TEMPORAL:
                if len(pila[len(pila)-1][1])<=variable.counter:
                    pila[len(pila)-1][1].append(None)            
                pila[len(pila)-1][1][variable.counter] = Valor(valor1) % Valor(valor2)            
            
        elif op==AND:
            if Tipo(variable)==GLOBAL:
                if len(pila[0][0])<=variable.counter:
                    pila[0][0].append(None)
                pila[0][0][variable.counter] = Valor(valor1) and Valor(valor2)
            elif Tipo(variable)==LOCAL:
                if len(pila[len(pila)-1][0])<=variable.counter:
                    pila[len(pila)-1][0].append(None)
                pila[len(pila)-1][0][variable.counter] = Valor(valor1) and Valor(valor2)
            elif Tipo(variable)==TEMPORAL:
                if len(pila[len(pila)-1][1])<=variable.counter:
                    pila[len(pila)-1][1].append(None)            
                pila[len(pila)-1][1][variable.counter] = Valor(valor1) and Valor(valor2)  

        elif op==OR:
            if Tipo(variable)==GLOBAL:
                if len(pila[0][0])<=variable.counter:
                    pila[0][0].append(None)
                pila[0][0][variable.counter] = Valor(valor1) or Valor(valor2)
            elif Tipo(variable)==LOCAL:
                if len(pila[len(pila)-1][0])<=variable.counter:
                    pila[len(pila)-1][0].append(None)
                pila[len(pila)-1][0][variable.counter] = Valor(valor1) or Valor(valor2)
            elif Tipo(variable)==TEMPORAL:
                if len(pila[len(pila)-1][1])<=variable.counter:
                    pila[len(pila)-1][1].append(None)            
                pila[len(pila)-1][1][variable.counter] = Valor(valor1) or Valor(valor2)  
                
    print(pila)
    

def Tipo(valor1):

    if isinstance(valor1, bool):
        return BOOL
    elif isinstance(valor1, float):
        return NUMBER
    elif isinstance(valor1, int):
        return NUMBER
    elif isinstance(valor1, (str)):
        return STRING                     
    elif isinstance(valor1, TemporalRegister):
        return TEMPORAL
    elif isinstance(valor1, GlobalRegister):
        return GLOBAL
    elif isinstance(valor1, LocalRegister):
        return LOCAL


def Valor(valor1):
    global pila
    aux = Tipo(valor1)
    if(aux==GLOBAL):
        return pila[0][0][valor1.counter]
    elif (aux==LOCAL):
        return pila[len(pila)-1][0][valor1.counter]
    elif (aux==TEMPORAL):
        return pila[len(pila)-1][1][valor1.counter]
    else:
        return valor1
        