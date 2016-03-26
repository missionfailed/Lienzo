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
currentArgumentList = []

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
	lienzo declaracion* funcion* dibujo EOF
	;

lienzo:
	LIENZO '{' colorLienzo ';' tamanoLienzo ';' '}'
	;

colorLienzo:
	COLOR DE LIENZO '=' color
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
	TAMANO DE LIENZO '=' largo=ss_expresion POR ancho=ss_expresion
{
if $largo.type != NUMERO:
    error($largo.start.line, "Largo del lienzo debe ser una expresion entera")
elif $ancho.type != NUMERO:
    error($ancho.start.line, "Ancho del lienzo debe ser una expresion entera")
}
	;
    
declaracion_global:
    tipo GLOBAL ID
{
if namespaceTable.variableExists($ID.text, "global"):
    error($ID.line, ": Variable " + $ID.text + " ya fue declarada")
}   '=' ss_expresion ';'
{
if $ss_expresion.type != $tipo.text:
    error($ID.line, "Variable " + $ID.text + " es de tipo " + $tipo.text)
else:
    namespaceTable.addVariable($ID.text, $tipo.text, "global")
    idcontent= memoryregisters.createMemoryRegister($ID.text, "global")
    cuadruplos.addCuadruplo('=', $ss_expresion.valor,None,idcontent)
}
	;

funcion:
	tipoFunc ID '(' (parametro (',' parametro)*)? ')' {
global currentFunctionName
global currentParameterList
currentFunctionName = $ID.text
if not namespaceTable.addFunction(currentFunctionName, $tipoFunc.text, currentParameterList):
    error($ID.line, "Funcion " + $ID.text + " ya fue declarada")
else:
    memoryregisters.newFunction(currentFunctionName)
currentParameterList = []
}
'{' cuerpo '}'
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
}
    ;

cuerpo:
    declaracion* instruccion_aux*
    ;

declaracion:
	tipo ID
{
if namespaceTable.variableExists($ID.text, currentFunctionName):
    error($ID.line, ": Variable " + $ID.text + " ya fue declarada")
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

instruccion_aux:
    (
        asignacion
        | condicional
        | mientrasQue
        | llamadaFuncionPredefinida
        | llamadaFuncion
	) ';'
	;

llamadaFuncionPredefinida:
    lectura
    | escritura
    | imprimir
    ;
    
lectura:
    LEER ID
{
idcontent=memoryregisters.getMemoryRegister($ID.text,currentFunctionName)
cuadruplos.addCuadruplo(READ,None,None,idcontent)
}    
    ;
    
escritura:
	ESCRIBIR ss_expresion EN expresion ',' expresion
{
if $ss_expresion.type == TEXTO:
    cuadruplos.addCuadruplo(PRINT, $ss_expresion.valor, None)
else:
    error($ss_expresion.start.line, "solo se pueden imprimir texto")
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
    
imprimir:
    IMPRIMIR ss_expresion
    ;
    
condicional:
	SI '(' ss_expresion ')'
{
if $ss_expresion.type != BOLEANO:
    error($ss_expresion.start.line, "el estatuto 'si' necesita una boleano")
}
    '{' (instruccion_aux)* '}' (SINO '{' (instruccion_aux)* '}')?
	;

mientrasQue:
	MIENTRAS QUE '(' ss_expresion ')' 
{
if $ss_expresion.type != BOLEANO:
    error($ss_expresion.start.line, "el estatuto 'mientras que' necesita una boleano")
}
    '{' instruccion_aux* '}'
	;

llamadaFuncion returns [type]:
	ID
{
functionType = namespaceTable.getFunctionType($ID.text)
if not functionType:
    print("Error: linea", $ID.line, ": llamada a funcion", $ID.text, "inexistente")
else:
    $type = None if functionType == "nada" else functionType
}
    '(' (ss_exp1=ss_expresion
{
global currentArgumentList
currentArgumentList.append(($ss_exp1.text, $ss_exp1.type))
}
    
    (',' ss_exp2=ss_expresion
{
currentArgumentList.append(($ss_exp2.text, $ss_exp2.type))
}
    )*)? ')'
{
if not namespaceTable.argumentsAgree($ID.text, currentArgumentList):
    print("Error: linea", $ID.line, ": llamada a funcion", $ID.text, ": argumentos incorrectos")
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
$type = cubo[$type][$op.text][$s_exp2.type]
if not type:
    print("Error: linea", $op.line, ": operador", $op.text, "no puede ser aplicado a", $type, "y a", $s_exp2.type)
else:
    $valor = cuadruplos.addCuadruplo($op.text,$valor,$s_exp2.valor)
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
$type = cubo[$type][$op.text][$exp2.type]
if not type:
    print("Error: linea", $op.line, ": operador", $op.text, "no puede ser aplicado a", $type, "y a", $exp2.type)
else:
    $valor = cuadruplos.addCuadruplo($op.text,$valor,$exp2.valor)
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
type = cubo[$type][$op.text][$term2.type]
if not type:
    print("Error: linea", $op.line, ": operador", $op.text, "no puede ser aplicado a", $type, "y a", $term2.type)
else:
    $valor = cuadruplos.addCuadruplo($op.text,$valor,$term2.valor)
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
type = cubo[$type][$op.text][$factor2.type]
if not type:
    print("Error: linea", $op.line, ": operador", $op.text, "no puede ser aplicado a", $type, "y a", $factor2.type)
else:
    $valor = cuadruplos.addCuadruplo($op.text,$valor,$factor2.valor)
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
    else:
        $valor = $factor_aux.valor
} |
    (neg='-'? NUMERIC_CONSTANT)
{
$type = NUMERO

if $neg.text:
    $valor = cuadruplos.addCuadruplo($neg.text,num($NUMERIC_CONSTANT.text),None)
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
else:
    $valor = None
    errir($ID.line, "variable " + $ID.text + " no ha sido declarada")

} | BOOLEAN_CONSTANT 
{
$type = BOLEANO
$valor = True if $BOOLEAN_CONSTANT.text == 'verdadero' else False
}
| llamadaFuncion
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
}
    ;

dibujo:
    DIBUJO {
global currentFunctionName
currentFunctionName = $DIBUJO.text
namespaceTable.addFunction(currentFunctionName, "nada", [])
memoryregisters.newFunction(currentFunctionName)
}
    '{' cuerpo '}'
	;
    
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newline

GLOBAL : 'global' ;
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
DIBUJO : 'dibujo' ;
DORMIR : 'dormir' ;
MIENTRAS : 'mientras' ;
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
NUMERIC_CONSTANT : [1-9][0-9]*('.'[0-9]+)? ;
STRING_CONSTANT : '"' ~('"')* '"' ;
ID : [A-Za-z]+ ;