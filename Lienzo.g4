grammar Lienzo;

options {
    language=Python3;
}

@header {
from namespace import NamespaceTable
from collections import defaultdict
from MemoryRegister import MemoryRegisters
from cuadruplos import *

namespaceTable = NamespaceTable()
currentFunctionName = ""
currentParameterList = []

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
cubo[TEXTO]['*'] = defaultdict(lambda: None, {})
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
cubo[NUMERO]['*'] = defaultdict(lambda: None, {NUMERO : NUMERO})
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
	declaracion* colorLienzo tamanoLienzo funcion* instruccion_aux* EOF
{
cuadruplos.printCuadruplos()
}
	;

colorLienzo:
	COLOR DE LIENZO '=' color ';'
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
}
	;
    
declaracion:
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
    idcontent= memoryregisters.createMemoryRegister($ID.text, currentFunctionName)
    cuadruplos.addCuadruplo('=', $ss_expresion.valor,None,idcontent)
}
	;

funcion:
	tipoFunc ID '(' (parametro (',' parametro)*)? ')' {
global currentFunctionName
global currentParameterList
currentFunctionName = $ID.text
if not namespaceTable.addFunction(currentFunctionName, $tipoFunc.text, cuadruplos.current(), currentParameterList):
    error($ID.line, "Funcion " + $ID.text + " ya fue declarada")
else:
    memoryregisters.newFunction(currentFunctionName)
currentParameterList = []
}
'{' cuerpo (REGRESAR ss_expresion ';')?

{
if $REGRESAR:
    if $tipoFunc.text == "nada":
        error($ID.line, "Funcion " + $ID.text + " no debe tener valor de retorno")
    elif $ss_expresion.type != $tipoFunc.text:
        error($ID.line, "Funcion " + $ID.text + " tiene valor de retorno de tipo incorrecto. Se esperaba un " + $tipoFunc.text)
    else:
        cuadruplos.addCuadruplo(RETURN,$ss_expresion.valor,None,None,False)
else:
    if $tipoFunc.text == "nada":
        cuadruplos.addCuadruplo(RETURN,None,None,None,False)
    else:
        error($ID.line, "Funcion " + $ID.text + " debe tener valor de retorno")      
}
'}'
{
cuadruplos.addCuadruplo(RET, None, None, None, False)
}
	;
   
tipoFunc:
    tipo | NADA
    ;

parametro:
    tipo MODIFICABLE? ID {
global currentParameterList
if $ID.text in [parameter[0] for parameter in currentParameterList]:
    error($ID.line, "Parametro " + $ID.text + " ya fue declarado")
else:
    modificable = False
    if $MODIFICABLE.text:
        modificable = True
    currentParameterList.append(($ID.text, $tipo.text, modificable))
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
	) ';') | condicional | mientrasQue
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
cuadruplos.addCuadruplo(READ, idcontent, None, idcontent)
}    
    ;
    
escritura:
	ESCRIBIR ss_expresion
{
cuadruplos.addCuadruplo(WRITE, $ss_expresion.valor, None, None, False)
}
	;
    
imprimir:
    IMPRIMIR ss_expresion
{
cuadruplos.addCuadruplo(PRINT, $ss_expresion.valor, None, None, False)
}
    ;

mover_adelante:
    MOVER ADELANTE ss_expresion
{
cuadruplos.addCuadruplo(FORWARD, $ss_expresion.valor, None, None, False)
}
    ;
    
mover_atras:
    MOVER ATRAS ss_expresion
{
cuadruplos.addCuadruplo(BACKWARD, $ss_expresion.valor, None, None, False)
}
    ;
    
girar_derecha:
    GIRAR DERECHA ss_expresion
{
cuadruplos.addCuadruplo(RIGHT, $ss_expresion.valor, None, None, False)
}
    ;

girar_izquierda:
    GIRAR IZQUIERDA ss_expresion
{
cuadruplos.addCuadruplo(LEFT, $ss_expresion.valor, None, None, False)
}
    ;
    
subir_pluma:
    LEVANTAR PLUMA
{
cuadruplos.addCuadruplo(PENUP, None, None, None, False)
}
    ;
    
bajar_pluma:
    BAJAR PLUMA
{
cuadruplos.addCuadruplo(PENDOWN, None, None, None, False)
}
    ;
    
cambio_color:
    COLOR DE PLUMA '=' color
{
cuadruplos.addCuadruplo(COLOR_CHANGE, None, None, None, False)
}
    ;

asignacion:
	ID '=' ss_expresion
{
idType = namespaceTable.getVariableType($ID.text, currentFunctionName)
if not idType:
    error($ID.line, "Variable " + $ID.text + " no ha sido declarada")
elif $ss_expresion.type != idType:
   error($ID.line, "Variable " + $ID.text + " es de tipo " + idType)
else:
    idcontent = memoryregisters.getMemoryRegister($ID.text, currentFunctionName)
    cuadruplos.addCuadruplo('=', $ss_expresion.valor, None, idcontent)
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
    cuadruplos.addCuadruplo(GOTOF, $ss_expresion.valor, None, None, False)
    cuadruplos.pushPilaSaltos(cuadruplos.last())
}
    bloque_instrucciones
    (SINO
{
if $SINO:
    cuadruplos.addCuadruplo(GOTO,None,None,None,False)
    cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(),cuadruplos.current())
    cuadruplos.pushPilaSaltos(cuadruplos.last())
}
    bloque_instrucciones
{
cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(),cuadruplos.current())
}    
    
)?
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
    cuadruplos.addCuadruplo(GOTOF,$ss_expresion.valor,None,None,False)
    cuadruplos.pushPilaSaltos(cuadruplos.last())
}    
    bloque_instrucciones
{
pop1 = cuadruplos.popPilaSaltos()
pop2 = cuadruplos.popPilaSaltos()
cuadruplos.addCuadruplo(GOTO,None,None,pop2,False)
cuadruplos.editCuadruplo(pop1,cuadruplos.current())
}
	;

llamadaFuncion returns [type]:
	ID
{
functionType = namespaceTable.getFunctionType($ID.text)
if not functionType:
    print("Error: linea", $ID.line, ": llamada a funcion", $ID.text, "inexistente")
else:
    $type = None if functionType == "nada" else functionType
    functionSize = namespaceTable.getFunctionSize($ID.text)
    cuadruplos.addCuadruplo(ERA, functionSize, None, None, False)
}
    '('
{
k = 0
}
    (ss_exp1=ss_expresion
{
if namespaceTable.argumentAgree($ID.text, k, $ss_exp1.text, $ss_exp1.type):
    cuadruplos.addCuadruplo(PARAM, $ss_exp1.valor, None, "param" + str(k))
else:
    error($ss_exp1.start.line, ": argumento #" + k + "no concuerda con el parametro esperado")
k += 1
}
    
    (',' ss_exp2=ss_expresion
{
if namespaceTable.argumentAgree($ID.text, k, $ss_exp2.text, $ss_exp2.type):
    cuadruplos.addCuadruplo(PARAM, $ss_exp2.valor, None, "param" + str(k))
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
    cuadruplos.addCuadruplo(GOSUB, $ID.text, namespaceTable.getDireccionInicio($ID.text), None, False)
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
    $valor = cuadruplos.addCuadruplo($op.text,$valor,$s_exp2.valor)
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
    $valor = cuadruplos.addCuadruplo($op.text,$valor,$exp2.valor)
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
    $valor = cuadruplos.addCuadruplo($op.text,$valor,$term2.valor)
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
    $valor = cuadruplos.addCuadruplo($op.text,$valor,$factor2.valor)
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
        $valor = cuadruplos.addCuadruplo($neg.text, $factor_aux.valor, None)
        namespaceTable.addTemporal(currentFunctionName, $type)
    else:
        $valor = $factor_aux.valor
} | (neg='-'? NUMERIC_CONSTANT)
{
$type = NUMERO

if $neg.text:
    $valor = cuadruplos.addCuadruplo($neg.text, num($NUMERIC_CONSTANT.text), None)
    namespaceTable.addTemporal(currentFunctionName, $type)
else:
    $valor = num($NUMERIC_CONSTANT.text)
} | STRING_CONSTANT
{
$type = TEXTO
$valor = $STRING_CONSTANT.text[1:-1]
}
	;

factor_aux returns[type,valor]:
    ID
{
$type = namespaceTable.getVariableType($ID.text, currentFunctionName)

if $type:
    $valor = memoryregisters.getMemoryRegister($ID.text, currentFunctionName)
    namespaceTable.addTemporal(currentFunctionName, $type)
else:
    $valor = None
    error($ID.line, "variable " + $ID.text + " no ha sido declarada")
} | BOOLEAN_CONSTANT
{
$type = BOLEANO
$valor = True if $BOOLEAN_CONSTANT.text == 'verdadero' else False
} | llamadaFuncion
{
functionType = $llamadaFuncion.type
$type = functionType if functionType != "nada" else None
if functionType:
    pass
else:
    $valor = None
} | '(' ss_expresion ')'
{
$type = $ss_expresion.type
if $type:
    $valor = $ss_expresion.valor
else:
    $valor = None
} | llamadaFuncionPredefinida
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
NUMERIC_CONSTANT : [0-9]+('.'[0-9]+)? ;
STRING_CONSTANT : '"' ~('"')* '"' ;
ID : [A-Za-z][A-Za-z0-9]*;