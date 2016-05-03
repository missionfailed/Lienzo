import turtle
from cuadruplos import *
from MemoryRegister import *
import sys

BOOLEAN = 0
NUMBER = 1
STRING = 2
TEMPORAL_REGISTER = 3
GLOBAL_REGISTER = 4
LOCAL_REGISTER = 5
pila = [([],[])]

GLOBAL = 0

GLOBALS = 0
LOCALS = 0
TEMPORALS = 1

def translateColor(color):
    translatedcolor="white"
    
    if color == "rojo":
        translatedcolor="red"
    elif color == "azul":
        translatedcolor="blue"
    elif color == "verde":
        translatedcolor="green"
    elif color =="amarillo":
        translatedcolor="yellow"
    elif color == "naranja":
        translatedcolor="orange"
    elif color == "blanco":
        translatedcolor="white"
    elif color == "negro":
        translatedcolor="black"
    elif color == "violeta":
        translatedcolor="violet"
    elif color == "cafe":
        translatedcolor="brown"
    elif color == "gris":
        translatedcolor="gray"
    
    return translatedcolor

def store(variable, respuesta):
    if isinstance(variable, tuple):
        store(variable[0][Valor(variable[1])], respuesta)
    elif Tipo(variable) == GLOBAL_REGISTER:
        while len(pila[GLOBAL][GLOBALS]) <= variable.counter:
            pila[GLOBAL][GLOBALS].append(None)
        pila[GLOBAL][GLOBALS][variable.counter] = respuesta
    else:
        current = len(pila) - 1
        if Tipo(variable) == LOCAL_REGISTER:
            while len(pila[current][LOCALS]) <= variable.counter:
                pila[current][LOCALS].append(None)
            registro = pila[current][LOCALS][variable.counter]
            if isinstance(registro, list) and isinstance(registro[0], int):
                pila[registro[0]][0][registro[1]] = respuesta
                pila[current][LOCALS][variable.counter][2] = respuesta
            else:
                pila[current][LOCALS][variable.counter] = respuesta
        elif Tipo(variable) == TEMPORAL_REGISTER:
            while len(pila[current][TEMPORALS]) <= variable.counter:
                pila[current][TEMPORALS].append(None)          
            pila[current][TEMPORALS][variable.counter] = respuesta

def executeVM(dirProc, listaCuadruplos):
    global pila
    
    functionRegisters = []
    nextContext = None
    jumpStack = []
    showScreen = False
    
    screen = turtle.Screen()
    tortuga = turtle.Turtle()
    
    i = 0
    c = listaCuadruplos[i]
    op = c[0]
    while op != END:
        
        valor1 = c[1]
        valor2 = c[2]
        variable = c[3]
        
        if op == GOTOF and not Valor(valor1):
            i = Valor(variable);

        elif op == GOTO:
            i = Valor(variable)
        
        elif op == GOSUB:
            jumpStack.append(i + 1)
            pila.append(nextContext)
            i = Valor(valor1)
        
        elif op == RET:
            i = jumpStack.pop()
            pila.pop()
            functionRegisters.pop()
            
        else:
            if op == ASSIGN:
                store(variable, Valor(valor1))
            
            if op == ASSIGNFUNC:
                functionRegisters.append(variable)
                store(functionRegisters[len(functionRegisters)-1], Valor(valor1))
                    
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

            elif op == READ:
                aux = input()
                if variable.tipo == "texto":
                    store(variable, aux)
                elif variable.tipo == "boleano":
                    if aux == 'verdadero':
                        aux = True
                    else:
                        aux = False
                    store(variable, aux)
                else:
                    try:
                        aux = int(aux)
                        store(variable, aux)
                    except ValueError:
                        try:
                            aux = float(s)
                            store(variable, aux)
                        except:
                            print("Error: se esperaba un ", variable.tipo)
                            sys.exit(0)
                
            elif op == WRITE:
                tortuga.write(Valor(valor1),True)
            
            elif op == PRINTLN:
                print(Valor(valor1))
                
            elif op == PRINT:
                print(Valor(valor1), end="")
            
            elif op == CHECK_BOUNDS:
                v1 = Valor(valor1)
                v2 = Valor(valor2)
                if v1 >= v2:
                    print("Error: intentando acceder al indice", v1, ": el arreglo es de solo", v2, "elementos.")
                    sys.exit(0)

            elif op == ERA:
                nextContext = ([], [])
            
            elif op == PARAM:
                if not valor2:
                    nextContext[0].append(Valor(valor1))
                elif Tipo(valor1) == LOCAL_REGISTER:
                    nextContext[0].append([len(pila)-1, valor1.counter, Valor(valor1), valor1])
                else:
                    nextContext[0].append([0, valor1.counter, Valor(valor1), valor1])
            
            elif op == RETURN:
                store(functionRegisters[len(functionRegisters)-1], Valor(valor1))
                
            else:
                showScreen = True
                
                if op == CANVAS_SIZE:
                    screen.setup(Valor(valor1), Valor(valor2))
            
                elif op == CANVAS_COLOR:
                    translatedcolor = translateColor(Valor(valor1))
                    #valor1 es el color en string, pero esta en espanol, cambiar a ingles
                    screen.bgcolor(translatedcolor)
                
                elif op == FORWARD:
                    tortuga.forward(Valor(valor1))
                    
                elif op == BACKWARD:
                    tortuga.backward(Valor(valor1))
                
                elif op == LEFT:
                    tortuga.left(Valor(valor1))
                
                elif op == RIGHT:
                    tortuga.right(Valor(valor1))
                
                elif op == PENUP:
                    tortuga.penup()
                
                elif op == PENDOWN:
                    tortuga.pendown()
                    
                elif op == COLOR_CHANGE:
                    translatedcolor = translateColor(Valor(valor1))
                    tortuga.pencolor(translatedcolor)
                
                elif op == SETSPEED:
                    velocidad = Valor(valor1)
                    if 0 > velocidad or velocidad > 10:
                        print("Error: intentando poner velocidad de", velocidad, ": la velocidad solo puede ser entre 0 y 10")
                    tortuga.speed(velocidad)
                
                elif op == PEN_POSX:
                    tortuga.setx(Valor(valor1))
                
                elif op == PEN_POSY:
                    tortuga.sety(Valor(valor1))
                
            i += 1
            
        c = listaCuadruplos[i]
        op = c[0]
        #input()
            
    if showScreen:
        screen.mainloop()
    

def Tipo(valor1):
    if isinstance(valor1, bool):
        return BOOLEAN
    elif isinstance(valor1, float):
        return NUMBER
    elif isinstance(valor1, int):
        return NUMBER
    elif isinstance(valor1, str):
        return STRING                     
    elif isinstance(valor1, TemporalRegister):
        return TEMPORAL_REGISTER
    elif isinstance(valor1, GlobalRegister):
        return GLOBAL_REGISTER
    elif isinstance(valor1, LocalRegister):
        return LOCAL_REGISTER
    elif isinstance(valor1, list) and isinstance(valor1[0], int):
        return Tipo(valor1[3])
    else:
        return Tipo(valor1[0][Valor(valor1[1])])


def Valor(valor1):
    global pila
    if isinstance(valor1, tuple):
        return Valor(valor1[0][Valor(valor1[1])])
    else:
        aux = Tipo(valor1)
        if aux == GLOBAL_REGISTER:
            return pila[GLOBAL][GLOBALS][valor1.counter]
        else:
            current = len(pila) - 1
            if aux == LOCAL_REGISTER:
                registro = pila[current][LOCALS][valor1.counter]
                if isinstance(registro, list) and isinstance(registro[0], int):
                    return registro[2]
                else:
                    return registro
            elif aux == TEMPORAL_REGISTER:
                return pila[current][TEMPORALS][valor1.counter]
            else:
                return valor1