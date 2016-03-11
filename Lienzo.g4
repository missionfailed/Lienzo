grammar Lienzo;

options {
    language=Python3;
}

@header {
from namespace import NamespaceTable

namespaceTable = NamespaceTable()
currentFunctionName = ""
currentParameterList = []
}

program:
	DIBUJO '{' materiales escenario funciones animacion '}' EOF
	;

materiales:
	MATERIALES '{' material* '}'
	;

material:
	(INTEGER_VALUE tipoFigura color LLAMADO NOMBRE_PROPIO DE expresion POR expresion ';')
{
# se anade material a la tabla de materiales, con figura como tipo
}
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
namespaceTable.addFunction("animacion", "nada", [])
} 
'{' cuerpo '}'
	;

cuerpo:
    declaracion* instruccion*
    ;

declaracion:
	tipo ID '=' ssexpresion ';' 
{
if not namespaceTable.addVariable($ID.text, $tipo.text, currentFunctionName):
    print("Error: linea", $ID.line, ": Variable", $ID.text, "ya fue declarada")
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
	ID '=' ssexpresion
{
if not namespaceTable.variableExists($ID.text, currentFunctionName):
    print("Error: linea", $ID.line, ": Variable", $ID.text, "no ha sido declarada")
}
	;

tipo:
	MENSAJE
	| CONDICION
	| NUMERO
	;
	
mostrarMensaje:
	MOSTRAR (ID | STRING_VALUE) EN expresion ',' expresion
	;

dormir:
	DORMIR expresion
	;
	
mientrasQue:
	MIENTRAS QUE '(' ssexpresion ')' '{' instruccion* '}'
	;

cambioColor:
	COLOR DE figura '=' color
	;

figura:
	NOMBRE_PROPIO ('[' expresion ']')?
	;

condicional:
	SI '(' ssexpresion ')' '{' (instruccion)* '}' (SINO '{' (instruccion)* '}')?
	;

llamadaFuncion:
	ID '(' (ssexpresion (',' ssexpresion)*)? ')'
{ 
if not namespaceTable.functionExists($ID.text):
    print("Error: linea", $ID.line, ": llamada a funcion", $ID.text, "inexistente")
}
	;
	
expresion:
	termino (('+'|'-') expresion)?
	;

termino:
	factor (('*'|'/'|'%') termino)?
	;

factor:
	('!')? (ID | llamadaFuncion | INTEGER_VALUE | VERDADERO | FALSO | STRING_VALUE | '(' expresion ')')
	;

sexpresion:
	expresion (('>' | '<' | '>=' | '<=' | '==' | '!=') sexpresion)?
	;

ssexpresion:
	 sexpresion (('&' | '|') ssexpresion)?
	 ;
	
funciones:
	FUNCIONES '{' (func)* '}'
	;
	
func:
	tipoFunc ID '(' (parametro (',' parametro)*)? ')' {
global currentFunctionName
global currentParameterList
currentFunctionName = $ID.text
if not namespaceTable.addFunction(currentFunctionName, $tipoFunc.text, currentParameterList):
    print("Error: linea", $ID.line, ": Funcion", $ID.text, "ya fue declarada")
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
VERDADERO : 'verdadero' ;
FALSO : 'falso' ;
MODIFICABLE : 'modificable' ;
INTEGER_VALUE : [0-9]+ ;
STRING_VALUE: '"' ~('"')* '"' ;
NOMBRE_PROPIO : [A-Z][A-Za-z]* ;
ID : [a-z][A-Za-z]*  ;