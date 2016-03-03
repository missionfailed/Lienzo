grammar Lienzo;

start_rule: program;

program:
	DIBUJO '{' materiales escenario funciones animacion '}'
	;

materiales:
	MATERIALES '{' (INTEGER_VALUE tipoFigura color LLAMADO NOMBRE_PROPIO DE expresion POR expresion ';')* '}'
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
	ANIMACION '{' (instruccion)* '}'
	;

instruccion:
	(
	asignacion
	| declaracion
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
	;

declaracion:
	tipo asignacion
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
	MIENTRAS QUE '(' ssexpresion ')' '{' (instruccion)* '}'
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
	;
	
expresion:
	termino (('+'|'-') expresion)?
	;

termino:
	factor (('*'|'/'|'%') termino)?
	;

factor:
	('!')? (ID | INTEGER_VALUE | VERDADERO | FALSO | STRING_VALUE | '(' expresion ')')
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
	(tipo | NADA) ID '(' (tipo (MODIFICABLE)? ID (',' tipo (MODIFICABLE)? ID)*)? ')' '{' (instruccion)* '}'
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