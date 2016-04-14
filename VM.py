import turtle
from cuadruplos import *
from MemoryRegister import *

BOOLEAN = 0
NUMBER = 1
STRING = 2
TEMPORAL_REGISTER = 3
GLOBAL_REGISTER = 4
LOCAL_REGISTER = 5
pila = [[[],[]]]

GLOBAL = 0

GLOBALS = 0
LOCALS = 0
TEMPORALS = 1

def store(variable, respuesta):
    if Tipo(variable) == GLOBAL_REGISTER:
        if len(pila[GLOBAL][GLOBALS]) <= variable.counter:
            pila[GLOBAL][GLOBALS].append(None)
        pila[GLOBAL][GLOBALS][variable.counter] = respuesta
    else:
        current = len(pila) - 1
        if Tipo(variable) == LOCAL_REGISTER:
            if len(pila[current][LOCALS]) <= variable.counter:
                pila[current][LOCALS].append(None)
            pila[current][LOCALS][variable.counter] = respuesta
        elif Tipo(variable) == TEMPORAL_REGISTER:
            if len(pila[current][TEMPORALS]) <= variable.counter:
                pila[current][TEMPORALS].append(None)          
            pila[current][TEMPORALS][variable.counter] = respuesta

def executeVM(dirProc, listaCuadruplos):
    global pila
    
    screen = turtle.Screen()
    tortuga = turtle.Turtle()
    
    for i, c in enumerate(listaCuadruplos):
        print(i, c)
        op = c[0]
        valor1 = c[1]
        valor2 = c[2]
        variable = c[3]
        
        if op == ASSIGN:
            store(variable, Valor(valor1))
                
        elif op == PLUS:
            store(variable, Valor(valor1) + Valor(valor2))

        elif op == MINUS:
            store(variable, Valor(valor1) - Valor(valor2))

        elif op == TIMES:
            store(variable, Valor(valor1) * Valor(valor2))
                
        elif op == DIVIDE:
            store(variable, Valor(valor1) / Valor(valor2))

        elif op == MODULO:
            store(variable, Valor(valor1) % Valor(valor2))   
            
        elif op == AND:
            store(variable, Valor(valor1) and Valor(valor2))

        elif op == OR:
            store(variable, Valor(valor1) or Valor(valor2)) 
        
        elif op == NOT:
            store(variable, not Valor(valor1))
        
        elif op == EQUALS:
            store(variable, Valor(valor1) == Valor(valor2))
        
        elif op == NOT_EQUALS:
            store(variable, Valor(valor1) != Valor(valor2))
        
        elif op == LESS_THAN:
            store(variable, Valor(valor1) < Valor(valor2))
        
        elif op == GREATER_THAN:
            store(variable, Valor(valor1) > Valor(valor2))
        
        elif op == LESS_THAN_EQUAL:
            store(variable, Valor(valor1) <= Valor(valor2))
            
        elif op == GREATER_THAN_EQUAL:
            store(variable, Valor(valor1) >= Valor(valor2))
        
        elif op == CANVAS_SIZE:
            screen.setup(Valor(valor1), Valor(valor2))
        
        elif op == CANVAS_COLOR:
            #valor1 es el color en string, pero esta en espanol, cambiar en ingles
            screen.bgcolor("orange")
        
        elif op == FORWARD:
            tortuga.forward(Valor(valor1))
            
        elif op == BACKWARD:
            tortuga.backward(Valor(valor1))
        
        elif op == LEFT:
            tortuga.left(Valor(valor1))
        
        elif op == RIGHT:
            tortuga.right(Valor(valor1))
                
    print(pila)
    screen.mainloop()
    

def Tipo(valor1):

    if isinstance(valor1, bool):
        return BOOLEAN
    elif isinstance(valor1, float):
        return NUMBER
    elif isinstance(valor1, int):
        return NUMBER
    elif isinstance(valor1, (str)):
        return STRING                     
    elif isinstance(valor1, TemporalRegister):
        return TEMPORAL_REGISTER
    elif isinstance(valor1, GlobalRegister):
        return GLOBAL_REGISTER
    elif isinstance(valor1, LocalRegister):
        return LOCAL_REGISTER


def Valor(valor1):
    global pila
    aux = Tipo(valor1)
    if aux == GLOBAL_REGISTER:
        return pila[GLOBAL][GLOBALS][valor1.counter]
    else:
        current = len(pila) - 1
        if aux == LOCAL_REGISTER:
            return pila[current][LOCALS][valor1.counter]
        elif aux == TEMPORAL_REGISTER:
            return pila[current][TEMPORALS][valor1.counter]
        else:
            return valor1
        