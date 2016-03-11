# Generated from Lienzo.g4 by ANTLR 4.5.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LienzoParser import LienzoParser
else:
    from LienzoParser import LienzoParser

from namespace import NamespaceTable
import sys

namespaceTable = NamespaceTable()
currentFunctionName = ""


# This class defines a complete listener for a parse tree produced by LienzoParser.
class LienzoListener(ParseTreeListener):

    # Enter a parse tree produced by LienzoParser#program.
    def enterProgram(self, ctx:LienzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by LienzoParser#program.
    def exitProgram(self, ctx:LienzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by LienzoParser#materiales.
    def enterMateriales(self, ctx:LienzoParser.MaterialesContext):
        pass

    # Exit a parse tree produced by LienzoParser#materiales.
    def exitMateriales(self, ctx:LienzoParser.MaterialesContext):
        pass


    # Enter a parse tree produced by LienzoParser#material.
    def enterMaterial(self, ctx:LienzoParser.MaterialContext):
        pass

    # Exit a parse tree produced by LienzoParser#material.
    def exitMaterial(self, ctx:LienzoParser.MaterialContext):
        pass


    # Enter a parse tree produced by LienzoParser#tipoFigura.
    def enterTipoFigura(self, ctx:LienzoParser.TipoFiguraContext):
        pass

    # Exit a parse tree produced by LienzoParser#tipoFigura.
    def exitTipoFigura(self, ctx:LienzoParser.TipoFiguraContext):
        pass


    # Enter a parse tree produced by LienzoParser#color.
    def enterColor(self, ctx:LienzoParser.ColorContext):
        pass

    # Exit a parse tree produced by LienzoParser#color.
    def exitColor(self, ctx:LienzoParser.ColorContext):
        pass


    # Enter a parse tree produced by LienzoParser#escenario.
    def enterEscenario(self, ctx:LienzoParser.EscenarioContext):
        pass

    # Exit a parse tree produced by LienzoParser#escenario.
    def exitEscenario(self, ctx:LienzoParser.EscenarioContext):
        pass


    # Enter a parse tree produced by LienzoParser#colorLienzo.
    def enterColorLienzo(self, ctx:LienzoParser.ColorLienzoContext):
        pass

    # Exit a parse tree produced by LienzoParser#colorLienzo.
    def exitColorLienzo(self, ctx:LienzoParser.ColorLienzoContext):
        pass


    # Enter a parse tree produced by LienzoParser#tamanoLienzo.
    def enterTamanoLienzo(self, ctx:LienzoParser.TamanoLienzoContext):
        pass

    # Exit a parse tree produced by LienzoParser#tamanoLienzo.
    def exitTamanoLienzo(self, ctx:LienzoParser.TamanoLienzoContext):
        pass


    # Enter a parse tree produced by LienzoParser#posicion.
    def enterPosicion(self, ctx:LienzoParser.PosicionContext):
        pass

    # Exit a parse tree produced by LienzoParser#posicion.
    def exitPosicion(self, ctx:LienzoParser.PosicionContext):
        pass


    # Enter a parse tree produced by LienzoParser#coord.
    def enterCoord(self, ctx:LienzoParser.CoordContext):
        pass

    # Exit a parse tree produced by LienzoParser#coord.
    def exitCoord(self, ctx:LienzoParser.CoordContext):
        pass


    # Enter a parse tree produced by LienzoParser#animacion.
    def enterAnimacion(self, ctx:LienzoParser.AnimacionContext):
        pass

    # Exit a parse tree produced by LienzoParser#animacion.
    def exitAnimacion(self, ctx:LienzoParser.AnimacionContext):
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


    # Enter a parse tree produced by LienzoParser#instruccion.
    def enterInstruccion(self, ctx:LienzoParser.InstruccionContext):
        pass

    # Exit a parse tree produced by LienzoParser#instruccion.
    def exitInstruccion(self, ctx:LienzoParser.InstruccionContext):
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


    # Enter a parse tree produced by LienzoParser#mostrarMensaje.
    def enterMostrarMensaje(self, ctx:LienzoParser.MostrarMensajeContext):
        pass

    # Exit a parse tree produced by LienzoParser#mostrarMensaje.
    def exitMostrarMensaje(self, ctx:LienzoParser.MostrarMensajeContext):
        pass


    # Enter a parse tree produced by LienzoParser#dormir.
    def enterDormir(self, ctx:LienzoParser.DormirContext):
        pass

    # Exit a parse tree produced by LienzoParser#dormir.
    def exitDormir(self, ctx:LienzoParser.DormirContext):
        pass


    # Enter a parse tree produced by LienzoParser#mientrasQue.
    def enterMientrasQue(self, ctx:LienzoParser.MientrasQueContext):
        pass

    # Exit a parse tree produced by LienzoParser#mientrasQue.
    def exitMientrasQue(self, ctx:LienzoParser.MientrasQueContext):
        pass


    # Enter a parse tree produced by LienzoParser#cambioColor.
    def enterCambioColor(self, ctx:LienzoParser.CambioColorContext):
        pass

    # Exit a parse tree produced by LienzoParser#cambioColor.
    def exitCambioColor(self, ctx:LienzoParser.CambioColorContext):
        pass


    # Enter a parse tree produced by LienzoParser#figura.
    def enterFigura(self, ctx:LienzoParser.FiguraContext):
        pass

    # Exit a parse tree produced by LienzoParser#figura.
    def exitFigura(self, ctx:LienzoParser.FiguraContext):
        pass


    # Enter a parse tree produced by LienzoParser#condicional.
    def enterCondicional(self, ctx:LienzoParser.CondicionalContext):
        pass

    # Exit a parse tree produced by LienzoParser#condicional.
    def exitCondicional(self, ctx:LienzoParser.CondicionalContext):
        pass


    # Enter a parse tree produced by LienzoParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:LienzoParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by LienzoParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:LienzoParser.LlamadaFuncionContext):
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


    # Enter a parse tree produced by LienzoParser#sexpresion.
    def enterSexpresion(self, ctx:LienzoParser.SexpresionContext):
        pass

    # Exit a parse tree produced by LienzoParser#sexpresion.
    def exitSexpresion(self, ctx:LienzoParser.SexpresionContext):
        pass


    # Enter a parse tree produced by LienzoParser#ssexpresion.
    def enterSsexpresion(self, ctx:LienzoParser.SsexpresionContext):
        pass

    # Exit a parse tree produced by LienzoParser#ssexpresion.
    def exitSsexpresion(self, ctx:LienzoParser.SsexpresionContext):
        pass


    # Enter a parse tree produced by LienzoParser#funciones.
    def enterFunciones(self, ctx:LienzoParser.FuncionesContext):
        pass

    # Exit a parse tree produced by LienzoParser#funciones.
    def exitFunciones(self, ctx:LienzoParser.FuncionesContext):
        pass


    # Enter a parse tree produced by LienzoParser#func.
    def enterFunc(self, ctx:LienzoParser.FuncContext):
        pass

    # Exit a parse tree produced by LienzoParser#func.
    def exitFunc(self, ctx:LienzoParser.FuncContext):
        pass


    # Enter a parse tree produced by LienzoParser#tipoFunc.
    def enterTipoFunc(self, ctx:LienzoParser.TipoFuncContext):
        pass

    # Exit a parse tree produced by LienzoParser#tipoFunc.
    def exitTipoFunc(self, ctx:LienzoParser.TipoFuncContext):
        pass


    # Enter a parse tree produced by LienzoParser#parametros.
    def enterParametros(self, ctx:LienzoParser.ParametrosContext):
        pass

    # Exit a parse tree produced by LienzoParser#parametros.
    def exitParametros(self, ctx:LienzoParser.ParametrosContext):
        pass


    # Enter a parse tree produced by LienzoParser#parametro.
    def enterParametro(self, ctx:LienzoParser.ParametroContext):
        pass

    # Exit a parse tree produced by LienzoParser#parametro.
    def exitParametro(self, ctx:LienzoParser.ParametroContext):
        pass


