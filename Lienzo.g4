grammar Lienzo;

start_rule: dibujo;

dibujo:
	DIBUJO '{' materiales escenario funciones animacion '}'
	;

materiales:
	MATERIALES '{' (INTEGER_VALUE figura color LLAMADO NOMBRE_PROPIO DE expresion POR expresion ';')* '}'
	;

figura:
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
	POSICION coord DE ID '=' expresion
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
	) ';'
	;

asignacion:
	ID EQUALS expresion
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
	MOSTRAR ID EN expresion ',' expresion
	;

dormir:
	DORMIR expresion
	;
	
mientrasQue:
	MIENTRAS QUE '(' expresion ')' '{' (instruccion)* '}'
	;

cambioColor:
	COLOR DE NOMBRE_PROPIO '=' color
	;

condicional:
	SI '(' expresion ')' '{' (instruccion)* '}' (SINO '{' (instruccion)* '}')?
	;

expresion:
	termino (('+'|'-') expresion)?
	;

termino:
	factor (('*'|'/'|'%') termino)?
	;

factor:
	('!')? (ID | CONSTANTE | '(' expresion ')')
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
	(tipo | NADA) ID '(' (tipo (MODIFICABLE)? ID)* ')' '{' instruccion '}'
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
CONSTANTE_BOOLEANA : VERDADERO | FALSO ;
CONSTANTE : INTEGER_VALUE | CONSTANTE_BOOLEANA ;
MODIFICABLE : 'modificable' ;
INTEGER_VALUE: [0-9]+ ;
NOMBRE_PROPIO : [A-Z][A-Za-z]* ;
ID : [a-z][A-Za-z]+ ;