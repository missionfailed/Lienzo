# Generated from Lienzo.g4 by ANTLR 4.5.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LienzoParser import LienzoParser
else:
    from LienzoParser import LienzoParser

from namespace import NamespaceTable
from collections import defaultdict
from MemoryRegister import MemoryRegisters
from cuadruplos import *
import sys
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
    sys.exit(0)


# This class defines a complete listener for a parse tree produced by LienzoParser.
class LienzoListener(ParseTreeListener):

    # Enter a parse tree produced by LienzoParser#program.
    def enterProgram(self, ctx:LienzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by LienzoParser#program.
    def exitProgram(self, ctx:LienzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by LienzoParser#colorLienzo.
    def enterColorLienzo(self, ctx:LienzoParser.ColorLienzoContext):
        pass

    # Exit a parse tree produced by LienzoParser#colorLienzo.
    def exitColorLienzo(self, ctx:LienzoParser.ColorLienzoContext):
        pass


    # Enter a parse tree produced by LienzoParser#color.
    def enterColor(self, ctx:LienzoParser.ColorContext):
        pass

    # Exit a parse tree produced by LienzoParser#color.
    def exitColor(self, ctx:LienzoParser.ColorContext):
        pass


    # Enter a parse tree produced by LienzoParser#tamanoLienzo.
    def enterTamanoLienzo(self, ctx:LienzoParser.TamanoLienzoContext):
        pass

    # Exit a parse tree produced by LienzoParser#tamanoLienzo.
    def exitTamanoLienzo(self, ctx:LienzoParser.TamanoLienzoContext):
        pass


    # Enter a parse tree produced by LienzoParser#declaracion.
    def enterDeclaracion(self, ctx:LienzoParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by LienzoParser#declaracion.
    def exitDeclaracion(self, ctx:LienzoParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by LienzoParser#declaracion_variable.
    def enterDeclaracion_variable(self, ctx:LienzoParser.Declaracion_variableContext):
        pass

    # Exit a parse tree produced by LienzoParser#declaracion_variable.
    def exitDeclaracion_variable(self, ctx:LienzoParser.Declaracion_variableContext):
        pass


    # Enter a parse tree produced by LienzoParser#declaracion_arreglo.
    def enterDeclaracion_arreglo(self, ctx:LienzoParser.Declaracion_arregloContext):
        pass

    # Exit a parse tree produced by LienzoParser#declaracion_arreglo.
    def exitDeclaracion_arreglo(self, ctx:LienzoParser.Declaracion_arregloContext):
        pass


    # Enter a parse tree produced by LienzoParser#funcion.
    def enterFuncion(self, ctx:LienzoParser.FuncionContext):
        pass

    # Exit a parse tree produced by LienzoParser#funcion.
    def exitFuncion(self, ctx:LienzoParser.FuncionContext):
        pass


    # Enter a parse tree produced by LienzoParser#tipoFunc.
    def enterTipoFunc(self, ctx:LienzoParser.TipoFuncContext):
        pass

    # Exit a parse tree produced by LienzoParser#tipoFunc.
    def exitTipoFunc(self, ctx:LienzoParser.TipoFuncContext):
        pass


    # Enter a parse tree produced by LienzoParser#parametro.
    def enterParametro(self, ctx:LienzoParser.ParametroContext):
        pass

    # Exit a parse tree produced by LienzoParser#parametro.
    def exitParametro(self, ctx:LienzoParser.ParametroContext):
        pass


    # Enter a parse tree produced by LienzoParser#cuerpo.
    def enterCuerpo(self, ctx:LienzoParser.CuerpoContext):
        pass

    # Exit a parse tree produced by LienzoParser#cuerpo.
    def exitCuerpo(self, ctx:LienzoParser.CuerpoContext):
        pass


    # Enter a parse tree produced by LienzoParser#bloque_instrucciones.
    def enterBloque_instrucciones(self, ctx:LienzoParser.Bloque_instruccionesContext):
        pass

    # Exit a parse tree produced by LienzoParser#bloque_instrucciones.
    def exitBloque_instrucciones(self, ctx:LienzoParser.Bloque_instruccionesContext):
        pass


    # Enter a parse tree produced by LienzoParser#instruccion_aux.
    def enterInstruccion_aux(self, ctx:LienzoParser.Instruccion_auxContext):
        pass

    # Exit a parse tree produced by LienzoParser#instruccion_aux.
    def exitInstruccion_aux(self, ctx:LienzoParser.Instruccion_auxContext):
        pass


    # Enter a parse tree produced by LienzoParser#regresar.
    def enterRegresar(self, ctx:LienzoParser.RegresarContext):
        pass

    # Exit a parse tree produced by LienzoParser#regresar.
    def exitRegresar(self, ctx:LienzoParser.RegresarContext):
        pass


    # Enter a parse tree produced by LienzoParser#llamadaFuncionPredefinida.
    def enterLlamadaFuncionPredefinida(self, ctx:LienzoParser.LlamadaFuncionPredefinidaContext):
        pass

    # Exit a parse tree produced by LienzoParser#llamadaFuncionPredefinida.
    def exitLlamadaFuncionPredefinida(self, ctx:LienzoParser.LlamadaFuncionPredefinidaContext):
        pass


    # Enter a parse tree produced by LienzoParser#lectura.
    def enterLectura(self, ctx:LienzoParser.LecturaContext):
        pass

    # Exit a parse tree produced by LienzoParser#lectura.
    def exitLectura(self, ctx:LienzoParser.LecturaContext):
        pass


    # Enter a parse tree produced by LienzoParser#escritura.
    def enterEscritura(self, ctx:LienzoParser.EscrituraContext):
        pass

    # Exit a parse tree produced by LienzoParser#escritura.
    def exitEscritura(self, ctx:LienzoParser.EscrituraContext):
        pass


    # Enter a parse tree produced by LienzoParser#imprimir_no_ln.
    def enterImprimir_no_ln(self, ctx:LienzoParser.Imprimir_no_lnContext):
        pass

    # Exit a parse tree produced by LienzoParser#imprimir_no_ln.
    def exitImprimir_no_ln(self, ctx:LienzoParser.Imprimir_no_lnContext):
        pass


    # Enter a parse tree produced by LienzoParser#imprimir.
    def enterImprimir(self, ctx:LienzoParser.ImprimirContext):
        pass

    # Exit a parse tree produced by LienzoParser#imprimir.
    def exitImprimir(self, ctx:LienzoParser.ImprimirContext):
        pass


    # Enter a parse tree produced by LienzoParser#mover_adelante.
    def enterMover_adelante(self, ctx:LienzoParser.Mover_adelanteContext):
        pass

    # Exit a parse tree produced by LienzoParser#mover_adelante.
    def exitMover_adelante(self, ctx:LienzoParser.Mover_adelanteContext):
        pass


    # Enter a parse tree produced by LienzoParser#mover_atras.
    def enterMover_atras(self, ctx:LienzoParser.Mover_atrasContext):
        pass

    # Exit a parse tree produced by LienzoParser#mover_atras.
    def exitMover_atras(self, ctx:LienzoParser.Mover_atrasContext):
        pass


    # Enter a parse tree produced by LienzoParser#girar_derecha.
    def enterGirar_derecha(self, ctx:LienzoParser.Girar_derechaContext):
        pass

    # Exit a parse tree produced by LienzoParser#girar_derecha.
    def exitGirar_derecha(self, ctx:LienzoParser.Girar_derechaContext):
        pass


    # Enter a parse tree produced by LienzoParser#girar_izquierda.
    def enterGirar_izquierda(self, ctx:LienzoParser.Girar_izquierdaContext):
        pass

    # Exit a parse tree produced by LienzoParser#girar_izquierda.
    def exitGirar_izquierda(self, ctx:LienzoParser.Girar_izquierdaContext):
        pass


    # Enter a parse tree produced by LienzoParser#subir_pluma.
    def enterSubir_pluma(self, ctx:LienzoParser.Subir_plumaContext):
        pass

    # Exit a parse tree produced by LienzoParser#subir_pluma.
    def exitSubir_pluma(self, ctx:LienzoParser.Subir_plumaContext):
        pass


    # Enter a parse tree produced by LienzoParser#bajar_pluma.
    def enterBajar_pluma(self, ctx:LienzoParser.Bajar_plumaContext):
        pass

    # Exit a parse tree produced by LienzoParser#bajar_pluma.
    def exitBajar_pluma(self, ctx:LienzoParser.Bajar_plumaContext):
        pass


    # Enter a parse tree produced by LienzoParser#cambio_color.
    def enterCambio_color(self, ctx:LienzoParser.Cambio_colorContext):
        pass

    # Exit a parse tree produced by LienzoParser#cambio_color.
    def exitCambio_color(self, ctx:LienzoParser.Cambio_colorContext):
        pass


    # Enter a parse tree produced by LienzoParser#velocidad_pluma.
    def enterVelocidad_pluma(self, ctx:LienzoParser.Velocidad_plumaContext):
        pass

    # Exit a parse tree produced by LienzoParser#velocidad_pluma.
    def exitVelocidad_pluma(self, ctx:LienzoParser.Velocidad_plumaContext):
        pass


    # Enter a parse tree produced by LienzoParser#posicion_x_pluma.
    def enterPosicion_x_pluma(self, ctx:LienzoParser.Posicion_x_plumaContext):
        pass

    # Exit a parse tree produced by LienzoParser#posicion_x_pluma.
    def exitPosicion_x_pluma(self, ctx:LienzoParser.Posicion_x_plumaContext):
        pass


    # Enter a parse tree produced by LienzoParser#posicion_y_pluma.
    def enterPosicion_y_pluma(self, ctx:LienzoParser.Posicion_y_plumaContext):
        pass

    # Exit a parse tree produced by LienzoParser#posicion_y_pluma.
    def exitPosicion_y_pluma(self, ctx:LienzoParser.Posicion_y_plumaContext):
        pass


    # Enter a parse tree produced by LienzoParser#asignacion.
    def enterAsignacion(self, ctx:LienzoParser.AsignacionContext):
        pass

    # Exit a parse tree produced by LienzoParser#asignacion.
    def exitAsignacion(self, ctx:LienzoParser.AsignacionContext):
        pass


    # Enter a parse tree produced by LienzoParser#tipo.
    def enterTipo(self, ctx:LienzoParser.TipoContext):
        pass

    # Exit a parse tree produced by LienzoParser#tipo.
    def exitTipo(self, ctx:LienzoParser.TipoContext):
        pass


    # Enter a parse tree produced by LienzoParser#condicional.
    def enterCondicional(self, ctx:LienzoParser.CondicionalContext):
        pass

    # Exit a parse tree produced by LienzoParser#condicional.
    def exitCondicional(self, ctx:LienzoParser.CondicionalContext):
        pass


    # Enter a parse tree produced by LienzoParser#mientrasQue.
    def enterMientrasQue(self, ctx:LienzoParser.MientrasQueContext):
        pass

    # Exit a parse tree produced by LienzoParser#mientrasQue.
    def exitMientrasQue(self, ctx:LienzoParser.MientrasQueContext):
        pass


    # Enter a parse tree produced by LienzoParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:LienzoParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by LienzoParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:LienzoParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by LienzoParser#ss_expresion.
    def enterSs_expresion(self, ctx:LienzoParser.Ss_expresionContext):
        pass

    # Exit a parse tree produced by LienzoParser#ss_expresion.
    def exitSs_expresion(self, ctx:LienzoParser.Ss_expresionContext):
        pass


    # Enter a parse tree produced by LienzoParser#s_expresion.
    def enterS_expresion(self, ctx:LienzoParser.S_expresionContext):
        pass

    # Exit a parse tree produced by LienzoParser#s_expresion.
    def exitS_expresion(self, ctx:LienzoParser.S_expresionContext):
        pass


    # Enter a parse tree produced by LienzoParser#expresion.
    def enterExpresion(self, ctx:LienzoParser.ExpresionContext):
        pass

    # Exit a parse tree produced by LienzoParser#expresion.
    def exitExpresion(self, ctx:LienzoParser.ExpresionContext):
        pass


    # Enter a parse tree produced by LienzoParser#termino.
    def enterTermino(self, ctx:LienzoParser.TerminoContext):
        pass

    # Exit a parse tree produced by LienzoParser#termino.
    def exitTermino(self, ctx:LienzoParser.TerminoContext):
        pass


    # Enter a parse tree produced by LienzoParser#factor.
    def enterFactor(self, ctx:LienzoParser.FactorContext):
        pass

    # Exit a parse tree produced by LienzoParser#factor.
    def exitFactor(self, ctx:LienzoParser.FactorContext):
        pass


    # Enter a parse tree produced by LienzoParser#factor_aux.
    def enterFactor_aux(self, ctx:LienzoParser.Factor_auxContext):
        pass

    # Exit a parse tree produced by LienzoParser#factor_aux.
    def exitFactor_aux(self, ctx:LienzoParser.Factor_auxContext):
        pass


