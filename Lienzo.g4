grammar Lienzo;

options {
    language=Python3;
}

@header {
from namespace import NamespaceTable
from collections import defaultdict
from cuadruplos import Cuadruplos


namespaceTable = NamespaceTable()
currentFunctionName = ""
currentParameterList = []
currentArgumentList = []

cuadruplos = Cuadruplos()
diccionario_ids = {}

CONDICION = "condicion"
MENSAJE = "mensaje"
NUMERO = "numero"

cubo = {}
cubo[CONDICION] = {}
cubo[MENSAJE] = {}
cubo[NUMERO] = {}

# Condiciones
cubo[CONDICION]['+'] = defaultdict(lambda: None, {})
cubo[CONDICION]['-'] = defaultdict(lambda: None, {})
cubo[CONDICION]['*'] = defaultdict(lambda: None, {})
cubo[CONDICION]['/'] = defaultdict(lambda: None, {})
cubo[CONDICION]['%'] = defaultdict(lambda: None, {})
cubo[CONDICION]['<'] = defaultdict(lambda: None, {})
cubo[CONDICION]['>'] = defaultdict(lambda: None, {})
cubo[CONDICION]['<='] = defaultdict(lambda: None, {})
cubo[CONDICION]['>='] = defaultdict(lambda: None, {})
cubo[CONDICION]['=='] = defaultdict(lambda: None, {CONDICION : CONDICION})
cubo[CONDICION]['!='] = defaultdict(lambda: None, {CONDICION : CONDICION})
cubo[CONDICION]['&'] = defaultdict(lambda: None, {CONDICION : CONDICION})
cubo[CONDICION]['|'] = defaultdict(lambda: None, {CONDICION : CONDICION})

# Mensajes
cubo[MENSAJE]['+'] = defaultdict(lambda: None, {MENSAJE : MENSAJE})
cubo[MENSAJE]['-'] = defaultdict(lambda: None, {})
cubo[MENSAJE]['*'] = defaultdict(lambda: None, {})
cubo[MENSAJE]['/'] = defaultdict(lambda: None, {})
cubo[MENSAJE]['%'] = defaultdict(lambda: None, {})
cubo[MENSAJE]['<'] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['>'] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['<='] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['>='] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['=='] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['!='] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['&'] = defaultdict(lambda: None, {})
cubo[MENSAJE]['|'] = defaultdict(lambda: None, {})

# Numero
cubo[NUMERO]['+'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['-'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['*'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['/'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['%'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['<'] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['>'] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['<='] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['>='] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['=='] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['!='] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['&'] = defaultdict(lambda: None, {})
cubo[NUMERO]['|'] = defaultdict(lambda: None, {})
}

program:
	DIBUJO '{' materiales escenario funciones animacion '}' EOF
	;

materiales:
	MATERIALES '{' material* '}'
	;

material:
	(NUMERIC_CONSTANT tipoFigura color LLAMADO NOMBRE_PROPIO DE expresion POR expresion ';')
	;

tipoFigura:
	OVALO
	| RECTANGULO
	| TRIANGULO
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

escenario:
	ESCENARIO '{' colorLienzo ';' tamanoLienzo ';' (posicion ';')* '}'
	;

colorLienzo:
	COLOR DE LIENZO '=' color
	;

tamanoLienzo:
	TAMANO DE LIENZO '=' expresion POR expresion
	;

posicion:
	POSICION coord DE figura '=' expresion
	;

coord:
	X
	| Y
	;

animacion:
	ANIMACION {
global currentFunctionName
currentFunctionName = "animacion"
namespaceTable.addFunction(currentFunctionName, "nada", [])
cuadruplos.newFunction(currentFunctionName)
} 
'{' cuerpo '}'
	;

cuerpo:
    declaracion* instruccion*
    ;

declaracion:
	tipo ID
{
if namespaceTable.variableExists($ID.text, currentFunctionName):
    print("Error: linea", $ID.line, ": Variable", $ID.text, "ya fue declarada")
} '=' ss_expresion ';'
{
if $ss_expresion.type != $tipo.text:
    print("Error: linea", $ID.line, ": Variable", $ID.text, "es de tipo", $tipo.text)
else:
    namespaceTable.addVariable($ID.text, $tipo.text, currentFunctionName)
    cuadruplos.createMemoryRegister($ID.text, currentFunctionName)
}
	;

instruccion:
    (
        asignacion
        | mostrarMensaje
        | dormir
        | mientrasQue
        | cambioColor
        | posicion
        | condicional
        | llamadaFuncion
	) ';'
	;

asignacion:
	ID '=' ss_expresion
{
idType = namespaceTable.getVariableType($ID.text, currentFunctionName)
if not idType:
    print("Error: linea", $ID.line, ": Variable", $ID.text, "no ha sido declarada")
elif $ss_expresion.type != idType:
    print("Error: linea", $ID.line, ": Variable", $ID.text, "es de tipo", idType)
else:
    idcontent = cuadruplos.getMemoryRegister($ID.text, currentFunctionName)
    cuadruplos.addCuadruplo('=', $ss_expresion.valor,None,idcontent)
}
	;

tipo:
	MENSAJE
	| CONDICION
	| NUMERO
	;
	
mostrarMensaje:
	MOSTRAR (ID | STRING_CONSTANT) EN expresion ',' expresion
	;

dormir:
	DORMIR expresion
	;
	
mientrasQue:
	MIENTRAS QUE '(' ss_expresion ')' 
{
if $ss_expresion.type != CONDICION:
    print("Error: linea", $ss_expresion.start.line, ": el estatuto 'mientras que' necesita una condicion")
}
    '{' instruccion* '}'
	;

cambioColor:
	COLOR DE figura '=' color
	;

figura:
	NOMBRE_PROPIO ('[' expresion ']')?
	;

condicional:
	SI '(' ss_expresion ')'
{
if $ss_expresion.type != CONDICION:
    print("Error: linea", $ss_expresion.start.line, ": el estatuto 'si' necesita una condicion")
}
    '{' (instruccion)* '}' (SINO '{' (instruccion)* '}')?
	;

llamadaFuncion returns [type]:
	ID '(' (ss_exp1=ss_expresion
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
functionType = namespaceTable.getFunctionType($ID.text)
if functionType and namespaceTable.argumentsAgree($ID.text, currentArgumentList):
    $type = None if functionType == "nada" else functionType
else:
    print("Error: linea", $ID.line, ": llamada a funcion", $ID.text, "inexistente")
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
if $neg.text and $factor_aux.type != CONDICION:
    print("Error: linea", $neg.line, ": operador", $neg.text, "no puede ser aplicado a", $factor_aux.type)
    $type = None
else:
    if $neg.text:
        $valor = cuadruplos.addCuadruplo($neg.text,$factor_aux.valor,None)
    else:
        $valor = $factor_aux.valor
} |
    ('-'? NUMERIC_CONSTANT {$type = NUMERO}) |
    STRING_CONSTANT 
{
$type = MENSAJE
$valor = $STRING_CONSTANT.text
}
	;

factor_aux returns[type,valor]:
    ID
{
$type = namespaceTable.getVariableType($ID.text, currentFunctionName)

if $type:
    $valor = cuadruplos.getMemoryRegister($ID.text, currentFunctionName)
else:
    $valor = None

} | CONDITION_CONSTANT 
{
$type = CONDICION
$valor = $CONDITION_CONSTANT.text
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
	
funciones:
	FUNCIONES '{' func* '}'
	;
	
func:
	tipoFunc ID '(' (parametro (',' parametro)*)? ')' {
global currentFunctionName
global currentParameterList
currentFunctionName = $ID.text
if not namespaceTable.addFunction(currentFunctionName, $tipoFunc.text, currentParameterList):
    print("Error: linea", $ID.line, ": Funcion", $ID.text, "ya fue declarada")
else:
    cuadruplos.newFunction(currentFunctionName)
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
    print("Error: linea", $ID.line, ": Parametro", $ID.text, "ya fue declarado")
else:
    modificable = False
    if $MODIFICABLE.text:
        modificable = True
    currentParameterList.append(($ID.text, $tipo.text, modificable))
}
    ;
    
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newline

DIBUJO : 'dibujo' ;
MATERIALES : 'materiales' ;
LLAMADO : 'llamado' ;
DE : 'de' ;
OVALO : 'ovalo';
RECTANGULO: 'rectangulo' ;
TRIANGULO : 'triangulo' ;
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
ESCENARIO : 'escenario' ;
COLOR : 'color' ;
LIENZO : 'lienzo' ;
EQUALS : '=' ;
TAMANO : 'tamano' ;  
POR : 'por' ;
EN : 'en' ;
POSICION : 'posicion' ;
X : 'x' ;
Y : 'y' ;
ANIMACION : 'animacion' ;
DORMIR : 'dormir' ;
MIENTRAS : 'mientras' ;
QUE : 'que' ;
SI : 'si' ;
SINO : 'sino' ;
MENSAJE : 'mensaje' ;
CONDICION : 'condicion' ;
NUMERO : 'numero' ;
FUNCIONES : 'funciones' ;
MOSTRAR : 'mostrar' ;
NADA : 'nada' ;
CONDITION_CONSTANT : VERDADERO | FALSO ;
VERDADERO : 'verdadero' ;
FALSO : 'falso' ;
MODIFICABLE : 'modificable' ;
NUMERIC_CONSTANT : [0-9]+ ;
STRING_CONSTANT : '"' ~('"')* '"' ;
NOMBRE_PROPIO : [A-Z][A-Za-z]* ;
ID : [a-z][A-Za-z]* ;