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


# This class defines a complete listener for a parse tree produced by LienzoParser.
class LienzoListener(ParseTreeListener):

    # Enter a parse tree produced by LienzoParser#program.
    def enterProgram(self, ctx:LienzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by LienzoParser#program.
    def exitProgram(self, ctx:LienzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by LienzoParser#lienzo.
    def enterLienzo(self, ctx:LienzoParser.LienzoContext):
        pass

    # Exit a parse tree produced by LienzoParser#lienzo.
    def exitLienzo(self, ctx:LienzoParser.LienzoContext):
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


    # Enter a parse tree produced by LienzoParser#declaracion_global.
    def enterDeclaracion_global(self, ctx:LienzoParser.Declaracion_globalContext):
        pass

    # Exit a parse tree produced by LienzoParser#declaracion_global.
    def exitDeclaracion_global(self, ctx:LienzoParser.Declaracion_globalContext):
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


    # Enter a parse tree produced by LienzoParser#declaracion.
    def enterDeclaracion(self, ctx:LienzoParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by LienzoParser#declaracion.
    def exitDeclaracion(self, ctx:LienzoParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by LienzoParser#instruccion_aux.
    def enterInstruccion_aux(self, ctx:LienzoParser.Instruccion_auxContext):
        pass

    # Exit a parse tree produced by LienzoParser#instruccion_aux.
    def exitInstruccion_aux(self, ctx:LienzoParser.Instruccion_auxContext):
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


    # Enter a parse tree produced by LienzoParser#imprimir.
    def enterImprimir(self, ctx:LienzoParser.ImprimirContext):
        pass

    # Exit a parse tree produced by LienzoParser#imprimir.
    def exitImprimir(self, ctx:LienzoParser.ImprimirContext):
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


    # Enter a parse tree produced by LienzoParser#dibujo.
    def enterDibujo(self, ctx:LienzoParser.DibujoContext):
        pass

    # Exit a parse tree produced by LienzoParser#dibujo.
    def exitDibujo(self, ctx:LienzoParser.DibujoContext):
        pass


