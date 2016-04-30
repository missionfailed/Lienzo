grammar Lienzo;

options {
    language=Python3;
}

@header {
from namespace import NamespaceTable
from collections import defaultdict
from MemoryRegister import MemoryRegisters
from cuadruplos import *
import VM

namespaceTable = NamespaceTable()
currentFunctionName = ""
currentTipoFunc = ""
hasReturn = False

memoryregisters = MemoryRegisters()
cuadruplos = Cuadruplos()

BOLEANO = "boleano"
TEXTO = "texto"
NUMERO = "numero"

cubo = {}
cubo[BOLEANO] = {}
cubo[TEXTO] = {}
cubo[NUMERO] = {}

# Boleanos
cubo[BOLEANO]['+'] = defaultdict(lambda: None, {})
cubo[BOLEANO]['-'] = defaultdict(lambda: None, {})
cubo[BOLEANO]['*'] = defaultdict(lambda: None, {})
cubo[BOLEANO]['/'] = defaultdict(lambda: None, {})
cubo[BOLEANO]['%'] = defaultdict(lambda: None, {})
cubo[BOLEANO]['<'] = defaultdict(lambda: None, {})
cubo[BOLEANO]['>'] = defaultdict(lambda: None, {})
cubo[BOLEANO]['<='] = defaultdict(lambda: None, {})
cubo[BOLEANO]['>='] = defaultdict(lambda: None, {})
cubo[BOLEANO]['=='] = defaultdict(lambda: None, {BOLEANO : BOLEANO})
cubo[BOLEANO]['!='] = defaultdict(lambda: None, {BOLEANO : BOLEANO})
cubo[BOLEANO]['&'] = defaultdict(lambda: None, {BOLEANO : BOLEANO})
cubo[BOLEANO]['|'] = defaultdict(lambda: None, {BOLEANO : BOLEANO})

# Mensajes
cubo[TEXTO]['+'] = defaultdict(lambda: None, {TEXTO : TEXTO})
cubo[TEXTO]['-'] = defaultdict(lambda: None, {})
cubo[TEXTO]['*'] = defaultdict(lambda: None, {NUMERO : TEXTO})
cubo[TEXTO]['/'] = defaultdict(lambda: None, {})
cubo[TEXTO]['%'] = defaultdict(lambda: None, {})
cubo[TEXTO]['<'] = defaultdict(lambda: None, {TEXTO : BOLEANO})
cubo[TEXTO]['>'] = defaultdict(lambda: None, {TEXTO : BOLEANO})
cubo[TEXTO]['<='] = defaultdict(lambda: None, {TEXTO : BOLEANO})
cubo[TEXTO]['>='] = defaultdict(lambda: None, {TEXTO : BOLEANO})
cubo[TEXTO]['=='] = defaultdict(lambda: None, {TEXTO : BOLEANO})
cubo[TEXTO]['!='] = defaultdict(lambda: None, {TEXTO : BOLEANO})
cubo[TEXTO]['&'] = defaultdict(lambda: None, {})
cubo[TEXTO]['|'] = defaultdict(lambda: None, {})

# Numero
cubo[NUMERO]['+'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['-'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['*'] = defaultdict(lambda: None, {NUMERO : NUMERO, TEXTO : TEXTO})
cubo[NUMERO]['/'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['%'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['<'] = defaultdict(lambda: None, {NUMERO : BOLEANO})
cubo[NUMERO]['>'] = defaultdict(lambda: None, {NUMERO : BOLEANO})
cubo[NUMERO]['<='] = defaultdict(lambda: None, {NUMERO : BOLEANO})
cubo[NUMERO]['>='] = defaultdict(lambda: None, {NUMERO : BOLEANO})
cubo[NUMERO]['=='] = defaultdict(lambda: None, {NUMERO : BOLEANO})
cubo[NUMERO]['!='] = defaultdict(lambda: None, {NUMERO : BOLEANO})
cubo[NUMERO]['&'] = defaultdict(lambda: None, {})
cubo[NUMERO]['|'] = defaultdict(lambda: None, {})

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def error(linea, mensaje):
    print("Error: linea", linea, ":", mensaje)
}

program:
	declaracion* (tamanoLienzo colorLienzo)?
{
cuadruplos.addCuadruplo("", GOTO, None, None, None, False)
cuadruplos.pushPilaSaltos(cuadruplos.last())
} funcion*
{
cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(), cuadruplos.current())
} instruccion_aux* EOF
{
cuadruplos.addCuadruplo("", END, None, None, None, False)
VM.executeVM(namespaceTable.getDirProc(), cuadruplos.getCuadruplos())
}
	;

colorLienzo:
	COLOR DE LIENZO '=' color ';'
{
cuadruplos.addCuadruplo("", CANVAS_COLOR, $color.start.text, None, None, False)
}
	;

color:
	ROJO
	| VERDE
	| AMARILLO
	| AZUL
	| BLANCO
	| NEGRO
	| MORADO
	| NARANJA
	| CAFE
	| GRIS
	;

tamanoLienzo:
	TAMANO DE LIENZO '=' largo=ss_expresion POR ancho=ss_expresion ';'
{
if $largo.type != NUMERO:
    error($largo.start.line, "Largo del lienzo debe ser una expresion entera")
elif $ancho.type != NUMERO:
    error($ancho.start.line, "Ancho del lienzo debe ser una expresion entera")
else:
    cuadruplos.addCuadruplo("", CANVAS_SIZE, $largo.valor, $ancho.valor, None, False)
}
	;
    
declaracion:
    declaracion_variable | declaracion_arreglo
    ;

declaracion_variable:
	tipo ID
{
if namespaceTable.idAlreadyTaken($ID.text, currentFunctionName):
    error($ID.line, ": Identificador " + $ID.text + " ya fue declarado")
}   '=' ss_expresion ';'
{
if $ss_expresion.type != $tipo.text:
    error($ID.line, "Variable " + $ID.text + " es de tipo " + $tipo.text)
else:
    namespaceTable.addVariable($ID.text, $tipo.text, currentFunctionName)
    idcontent = memoryregisters.createMemoryRegister($ID.text, currentFunctionName, $tipo.text)
    cuadruplos.addCuadruplo(currentFunctionName, ASSIGN, $ss_expresion.valor, None, idcontent, False)
}
	;

declaracion_arreglo:
    tipo '[' INTEGRAL_CONSTANT ']' ID ';'
{
if namespaceTable.idAlreadyTaken($ID.text, currentFunctionName):
    error($ID.line, ": Identificador " + $ID.text + " ya fue declarado")
else:
    length = num($INTEGRAL_CONSTANT.text)
    if length == 0:
        error($ID.line, ": La longitud del arreglo " + $ID.text + " debe ser mayor a 0")
    else:
        namespaceTable.addArray($ID.text, $tipo.text, length, currentFunctionName)
        idcontents = memoryregisters.createMemoryRegisterForArray($ID.text, $tipo.text, length, currentFunctionName)
        valorInicial = 0
        if $tipo.text == BOLEANO:
            valorInicial = False
        elif $tipo.text == TEXTO:
            valorInicial = ""
        for i in idcontents:
            cuadruplos.addCuadruplo(currentFunctionName, ASSIGN, valorInicial, None, i, False)
}
    ;
    
funcion:
	tipoFunc ID
{
global currentFunctionName
global currentTipoFunc
currentFunctionName = $ID.text
currentTipoFunc = $tipoFunc.text
if not namespaceTable.addFunction(currentFunctionName, $tipoFunc.text, cuadruplos.current()):
    error($ID.line, "Funcion " + $ID.text + " ya fue declarada")
else:
    mr = memoryregisters.newFunction(currentFunctionName, $tipoFunc.text)
    valorInicial = 0
    if $tipoFunc.text == BOLEANO:
        valorInicial = False
    elif $tipoFunc.text == TEXTO:
        valorInicial = ""
    cuadruplos.addCuadruplo("", ASSIGNFUNC, valorInicial, None, mr, False)
}
'(' (parametro (',' parametro)*)? ')' '{' cuerpo '}'
{
global hasReturn
if currentTipoFunc != "nada" and not hasReturn:
    error($ID.line, "Funcion " + $ID.text + " debe tener valor de retorno")
else:
    hasReturn = False
cuadruplos.addCuadruplo(currentFunctionName, RET, None, None, None, False)
currentFunctionName = ""
currentTipoFunc = ""
}
	;
   
tipoFunc:
    tipo | NADA
    ;

parametro:
    tipo MODIFICABLE? ID
{
modificable = False
if $MODIFICABLE.text:
    modificable = True
if not namespaceTable.addParameter(currentFunctionName, $ID.text, $tipo.text, modificable):
    error($ID.line, "Parametro " + $ID.text + " ya fue declarado")
else:
    memoryregisters.createMemoryRegister($ID.text, currentFunctionName)
}
    ;

cuerpo:
    declaracion* instruccion_aux*
    ;

bloque_instrucciones:
    instruccion_aux | '{' instruccion_aux* '}'
    ;

instruccion_aux:
    ((
        asignacion
        | llamadaFuncionPredefinida
        | llamadaFuncion
        | regresar
	) ';') | condicional | mientrasQue
	;

regresar:
    REGRESAR ss_expresion
{
global hasReturn
hasReturn = True    
if currentTipoFunc == "nada":
    error($REGRESAR.line, "Funcion " + currentFunctionName + " no debe tener valor de retorno")
elif $ss_expresion.type != currentTipoFunc:
    error($REGRESAR.line, "Funcion " + currentFunctionName + " tiene valor de retorno de tipo incorrecto. Se esperaba un " + currentTipoFunc)
else:
    cuadruplos.addCuadruplo(currentFunctionName, RETURN, $ss_expresion.valor, None, None, False)
    cuadruplos.addCuadruplo(currentFunctionName, RET, None, None, None, False)
}
    ;

llamadaFuncionPredefinida:
    lectura
    | escritura
    | imprimir
    | mover_adelante
    | mover_atras
    | girar_izquierda
    | girar_derecha
    | cambio_color
    | subir_pluma
    | bajar_pluma
    ;
    
lectura:
    LEER ID
{
idcontent=memoryregisters.getMemoryRegister($ID.text,currentFunctionName)
cuadruplos.addCuadruplo(currentFunctionName, READ, None, None, idcontent)
}
    ;
    
escritura:
	ESCRIBIR ss_expresion
{
cuadruplos.addCuadruplo(currentFunctionName, WRITE, $ss_expresion.valor, None, None, False)
}
	;
    
imprimir:
    IMPRIMIR ss_expresion
{
cuadruplos.addCuadruplo(currentFunctionName, PRINT, $ss_expresion.valor, None, None, False)
}
    ;

mover_adelante:
    MOVER ADELANTE ss_expresion
{
cuadruplos.addCuadruplo(currentFunctionName, FORWARD, $ss_expresion.valor, None, None, False)
}
    ;
    
mover_atras:
    MOVER ATRAS ss_expresion
{
cuadruplos.addCuadruplo(currentFunctionName, BACKWARD, $ss_expresion.valor, None, None, False)
}
    ;
    
girar_derecha:
    GIRAR DERECHA ss_expresion
{
cuadruplos.addCuadruplo(currentFunctionName, RIGHT, $ss_expresion.valor, None, None, False)
}
    ;

girar_izquierda:
    GIRAR IZQUIERDA ss_expresion
{
cuadruplos.addCuadruplo(currentFunctionName, LEFT, $ss_expresion.valor, None, None, False)
}
    ;
    
subir_pluma:
    LEVANTAR PLUMA
{
cuadruplos.addCuadruplo(currentFunctionName, PENUP, None, None, None, False)
}
    ;
    
bajar_pluma:
    BAJAR PLUMA
{
cuadruplos.addCuadruplo(currentFunctionName, PENDOWN, None, None, None, False)
}
    ;
    
cambio_color:
    COLOR DE PLUMA '=' color
{
cuadruplos.addCuadruplo(currentFunctionName, COLOR_CHANGE, $color.text, None, None, False)
}
    ;

asignacion:
	ID (arr='[' indice=ss_expresion ']')? '=' lhs=ss_expresion
{
# regresa el tipo, no importa si es arreglo o variable
idType = namespaceTable.getVariableType($ID.text, currentFunctionName)
if not $arr:
    if not idType:
        error($ID.line, "Variable " + $ID.text + " no ha sido declarada")
    elif $lhs.type != idType:
        error($ID.line, "Variable " + $ID.text + " es de tipo " + idType)
    else:
        idcontent = memoryregisters.getMemoryRegister($ID.text, currentFunctionName)
        cuadruplos.addCuadruplo(currentFunctionName, ASSIGN, $lhs.valor, None, idcontent)
else:
    if not idType:
        error($ID.line, "Arreglo " + $ID.text + " no ha sido declarado")
    elif $lhs.type != idType:
        error($ID.line, "Arreglo " + $ID.text + " es de tipo " + idType)
    else:
        cuadruplos.addCuadruplo(currentFunctionName, CHECK_BOUNDS, $indice.valor, namespaceTable.getArrayLength($ID.text, currentFunctionName), None, False)
        idcontent = memoryregisters.getArrayMemoryRegister($ID.text, $indice.valor, currentFunctionName)
        cuadruplos.addCuadruplo(currentFunctionName, ASSIGN, $lhs.valor, None, idcontent)
}
	;

tipo:
	TEXTO
	| BOLEANO
	| NUMERO
	;
    
condicional:
	SI ss_expresion
{
if $ss_expresion.type != BOLEANO:
    error($ss_expresion.start.line, "el estatuto 'si' necesita una boleano")
else:
    cuadruplos.addCuadruplo(currentFunctionName, GOTOF, $ss_expresion.valor, None, None, False)
    cuadruplos.pushPilaSaltos(cuadruplos.last())
}
    bloque_instrucciones
    (SINO
{
cuadruplos.addCuadruplo(currentFunctionName, GOTO,None,None,None,False)
cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(),cuadruplos.current())
cuadruplos.pushPilaSaltos(cuadruplos.last())
}
    bloque_instrucciones    
    )?
{
cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(),cuadruplos.current())
}
	;

mientrasQue:
	MIENTRAS QUE
{
cuadruplos.pushPilaSaltos(cuadruplos.current())
}
    ss_expresion
{
if $ss_expresion.type != BOLEANO:
    error($ss_expresion.start.line, "el estatuto 'mientras que' necesita una boleano")
else:
    cuadruplos.addCuadruplo(currentFunctionName, GOTOF,$ss_expresion.valor,None,None,False)
    cuadruplos.pushPilaSaltos(cuadruplos.last())
}    
    bloque_instrucciones
{
pop1 = cuadruplos.popPilaSaltos()
pop2 = cuadruplos.popPilaSaltos()
cuadruplos.addCuadruplo(currentFunctionName, GOTO,None,None,pop2,False)
cuadruplos.editCuadruplo(pop1,cuadruplos.current())
}
	;

llamadaFuncion returns [valor,type]:
	ID
{
functionType = namespaceTable.getFunctionType($ID.text)
if not functionType:
    print("Error: linea", $ID.line, ": llamada a funcion", $ID.text, "inexistente")
    $valor = None
else:
    $type = None if functionType == "nada" else functionType
    cuadruplos.addCuadruplo(currentFunctionName, ERA, $ID.text, None, None, False)
    $valor = memoryregisters.getMemoryRegister($ID.text, "")
}
    '('
{
k = 0
}
    (ss_exp1=ss_expresion
{
if namespaceTable.argumentAgree($ID.text, k, $ss_exp1.text, $ss_exp1.type):
    cuadruplos.addCuadruplo(currentFunctionName, PARAM, $ss_exp1.valor, None, None, False)
else:
    error($ss_exp1.start.line, ": argumento #" + k + "no concuerda con el parametro esperado")
k += 1
}
    
    (',' ss_exp2=ss_expresion
{
if namespaceTable.argumentAgree($ID.text, k, $ss_exp2.text, $ss_exp2.type):
    cuadruplos.addCuadruplo(currentFunctionName, PARAM, $ss_exp2.valor, None, None, False)
else:
    error($ss_exp1.start.line, ": argumento #" + k + "no concuerda con el parametro esperado")
k += 1
}
    )*)? paren=')'
{
amountOfParameters = namespaceTable.getParameterAmount($ID.text)
if k != amountOfParameters:
    error($paren.line, "Se esperaban" + amountOfParameters + " parametros, se recibieron " + k)
else:
    cuadruplos.addCuadruplo(currentFunctionName, GOSUB, namespaceTable.getDireccionInicio($ID.text), None, None, False)
}
	;

ss_expresion returns [type,valor]:
    s_exp1=s_expresion 
{
$type = $s_exp1.type
$valor = $s_exp1.valor
}
    (op=('&' | '|') s_exp2=s_expresion
{
tipo = cubo[$type][$op.text][$s_exp2.type]
if not tipo:
    print("Error: linea", $op.line, ": operador", $op.text, "no puede ser aplicado a", $type, "y a", $s_exp2.type)
else:
    namespaceTable.addTemporal(currentFunctionName, tipo)
    $valor = cuadruplos.addCuadruplo(currentFunctionName, $op.text,$valor,$s_exp2.valor)
$type = tipo
}
    )*
	;
    
s_expresion returns [type,valor]:
	exp1=expresion
{
$type = $exp1.type
$valor = $exp1.valor
}
    (
    (op=('==' | '!=' | '>' | '<' | '>=' | '<=') exp2=expresion)
{
tipo = cubo[$type][$op.text][$exp2.type]
if not tipo:
    print("Error: linea", $op.line, ": operador", $op.text, "no puede ser aplicado a", $type, "y a", $exp2.type)
else:
    $valor = cuadruplos.addCuadruplo(currentFunctionName, $op.text,$valor,$exp2.valor)
    namespaceTable.addTemporal(currentFunctionName, tipo)
$type = tipo
}
    )*
	;
	
expresion returns [type,valor]:
	term1=termino 
{
$type = $term1.type
$valor = $term1.valor
}
    (
    (op=('+'|'-') term2=termino)
{
tipo = cubo[$type][$op.text][$term2.type]
if not tipo:
    print("Error: linea", $op.line, ": operador", $op.text, "no puede ser aplicado a", $type, "y a", $term2.type)
else:
    $valor = cuadruplos.addCuadruplo(currentFunctionName, $op.text,$valor,$term2.valor)
    namespaceTable.addTemporal(currentFunctionName, tipo)
$type = tipo
}
    )*
	;

termino returns [type,valor]:
	factor1=factor 
{
$type = $factor1.type
$valor = $factor1.valor
}
    (op=('*'|'/'|'%') factor2=factor
{
tipo = cubo[$type][$op.text][$factor2.type]
if not tipo:
    print("Error: linea", $op.line, ": operador", $op.text, "no puede ser aplicado a", $type, "y a", $factor2.type)
else:
    $valor = cuadruplos.addCuadruplo(currentFunctionName, $op.text,$valor,$factor2.valor)
    namespaceTable.addTemporal(currentFunctionName, tipo)
$type = tipo
}
    )*
	;

factor returns [type,valor]:
    (neg='!'? factor_aux)
{
$type = $factor_aux.type
if $neg.text and $factor_aux.type != BOLEANO:
    error($neg.line, "operador " + $neg.text + " no puede ser aplicado a " + $factor_aux.type)
    $type = None
else:
    if $neg.text:
        $valor = cuadruplos.addCuadruplo(currentFunctionName, $neg.text, $factor_aux.valor, None)
        namespaceTable.addTemporal(currentFunctionName, $type)
    else:
        $valor = $factor_aux.valor
} | (neg='-'? n=(NUMERIC_CONSTANT|INTEGRAL_CONSTANT))
{
$type = NUMERO

if $neg.text:
    $valor = cuadruplos.addCuadruplo(currentFunctionName, $neg.text, num($n.text), None)
    namespaceTable.addTemporal(currentFunctionName, $type)
else:
    $valor = num($n.text)
} | STRING_CONSTANT
{
$type = TEXTO
$valor = $STRING_CONSTANT.text[1:-1]
}
	;

factor_aux returns[type,valor]:
    ID (arr='[' ss_expresion ']')?
{
# no importa si es arreglo o variable, regresa el tipo correcto
$type = namespaceTable.getVariableType($ID.text, currentFunctionName)
if not $arr:
    if $type:
        $valor = memoryregisters.getMemoryRegister($ID.text, currentFunctionName)
    else:
        $valor = None
        error($ID.line, "variable " + $ID.text + " no ha sido declarada")
else:
    if $type:
        cuadruplos.addCuadruplo(currentFunctionName, CHECK_BOUNDS, $ss_expresion.valor, namespaceTable.getArrayLength($ID.text, currentFunctionName), None, False)
        $valor = memoryregisters.getArrayMemoryRegister($ID.text, $ss_expresion.valor, currentFunctionName)
    else:
        $valor = None
        error($ID.line, "Arreglo " + $ID.text + " no ha sido declarado")  
} | BOOLEAN_CONSTANT
{
$type = BOLEANO
$valor = True if $BOOLEAN_CONSTANT.text == 'verdadero' else False
} | lf=llamadaFuncion
{
functionType = $llamadaFuncion.type
$type = functionType if functionType != "nada" else None
$valor = cuadruplos.addCuadruplo(currentFunctionName, ASSIGN, $lf.valor, None)
} | '(' ss_expresion ')'
{
$type = $ss_expresion.type
if $type:
    $valor = $ss_expresion.valor
else:
    $valor = None
}
    ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newline

ROJO : 'rojo' ;
VERDE : 'verde' ;
AMARILLO : 'amarillo' ;
AZUL : 'azul' ;
BLANCO : 'blanco' ;
NEGRO : 'negro' ;
MORADO : 'morado' ;
NARANJA : 'naranja' ;
CAFE : 'cafe' ;
GRIS : 'gris' ;
COLOR : 'color' ;
LIENZO : 'lienzo' ;
EQUALS : '=' ;
TAMANO : 'tamano' ;
POR : 'por' ;
DE : 'de' ;
EN : 'en' ;
MOVER : 'mover' ;
ADELANTE : 'adelante' ;
ATRAS : 'atras' ;
GIRAR : 'girar' ;
DERECHA : 'derecha' ;
IZQUIERDA : 'izquierda' ;
LEVANTAR : 'levantar' ;
BAJAR : 'bajar' ;
PLUMA : 'pluma' ;
DIBUJO : 'dibujo' ;
DORMIR : 'dormir' ;
MIENTRAS : 'mientras' ;
REGRESAR: 'regresar';
QUE : 'que' ;
SI : 'si' ;
SINO : 'sino' ;
TEXTO : 'texto' ;
LEER : 'leer';
BOLEANO : 'boleano' ;
NUMERO : 'numero' ;
ESCRIBIR : 'escribir' ;
IMPRIMIR : 'imprimir' ;
NADA : 'nada' ;
BOOLEAN_CONSTANT : 'verdadero' | 'falso' ;
MODIFICABLE : 'modificable' ;
INTEGRAL_CONSTANT : [0-9]+ ;
NUMERIC_CONSTANT : [0-9]+'.'[0-9]+ ;
STRING_CONSTANT : '"' ~('"')* '"' ;
ID : [A-Za-z][A-Za-z0-9]*;