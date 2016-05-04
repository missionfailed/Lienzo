# Generated from Lienzo.g4 by ANTLR 4.5.2
from antlr4 import *
from io import StringIO


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


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2J")
        buf.write("\u0238\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\7\30\u00c8\n\30\f\30\16\30\u00cb\13\30\3\30\5\30")
        buf.write("\u00ce\n\30\3\30\3\30\3\30\3\30\3\30\7\30\u00d5\n\30\f")
        buf.write("\30\16\30\u00d8\13\30\3\30\3\30\3\30\6\30\u00dd\n\30\r")
        buf.write("\30\16\30\u00de\5\30\u00e1\n\30\3\30\3\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%")
        buf.write("\3%\3%\3%\3%\3%\3%\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\38\38\38")
        buf.write("\39\39\39\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3<\3<\3<\3")
        buf.write("<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3C\3C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3")
        buf.write("D\3D\5D\u020b\nD\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3")
        buf.write("F\6F\u021a\nF\rF\16F\u021b\3G\6G\u021f\nG\rG\16G\u0220")
        buf.write("\3G\3G\6G\u0225\nG\rG\16G\u0226\3H\3H\7H\u022b\nH\fH\16")
        buf.write("H\u022e\13H\3H\3H\3I\3I\7I\u0234\nI\fI\16I\u0237\13I\3")
        buf.write("\u00d6\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087")
        buf.write("E\u0089F\u008bG\u008dH\u008fI\u0091J\3\2\b\4\2\f\f\17")
        buf.write("\17\5\2\13\f\17\17\"\"\3\2\62;\3\2$$\4\2C\\c|\5\2\62;")
        buf.write("C\\c|\u0243\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u0095\3\2\2")
        buf.write("\2\7\u0097\3\2\2\2\t\u0099\3\2\2\2\13\u009b\3\2\2\2\r")
        buf.write("\u009d\3\2\2\2\17\u009f\3\2\2\2\21\u00a1\3\2\2\2\23\u00a3")
        buf.write("\3\2\2\2\25\u00a5\3\2\2\2\27\u00a7\3\2\2\2\31\u00aa\3")
        buf.write("\2\2\2\33\u00ad\3\2\2\2\35\u00af\3\2\2\2\37\u00b1\3\2")
        buf.write("\2\2!\u00b4\3\2\2\2#\u00b7\3\2\2\2%\u00b9\3\2\2\2\'\u00bb")
        buf.write("\3\2\2\2)\u00bd\3\2\2\2+\u00bf\3\2\2\2-\u00c1\3\2\2\2")
        buf.write("/\u00e0\3\2\2\2\61\u00e4\3\2\2\2\63\u00e9\3\2\2\2\65\u00ef")
        buf.write("\3\2\2\2\67\u00f8\3\2\2\29\u00fd\3\2\2\2;\u0104\3\2\2")
        buf.write("\2=\u010a\3\2\2\2?\u0111\3\2\2\2A\u0119\3\2\2\2C\u011e")
        buf.write("\3\2\2\2E\u0123\3\2\2\2G\u0129\3\2\2\2I\u0133\3\2\2\2")
        buf.write("K\u013a\3\2\2\2M\u013c\3\2\2\2O\u0143\3\2\2\2Q\u0147\3")
        buf.write("\2\2\2S\u014a\3\2\2\2U\u014d\3\2\2\2W\u0153\3\2\2\2Y\u015c")
        buf.write("\3\2\2\2[\u0162\3\2\2\2]\u0168\3\2\2\2_\u0170\3\2\2\2")
        buf.write("a\u017a\3\2\2\2c\u0183\3\2\2\2e\u0189\3\2\2\2g\u018f\3")
        buf.write("\2\2\2i\u0198\3\2\2\2k\u01a1\3\2\2\2m\u01a5\3\2\2\2o\u01a9")
        buf.write("\3\2\2\2q\u01af\3\2\2\2s\u01b2\3\2\2\2u\u01b7\3\2\2\2")
        buf.write("w\u01bd\3\2\2\2y\u01c2\3\2\2\2{\u01cc\3\2\2\2}\u01d6\3")
        buf.write("\2\2\2\177\u01de\3\2\2\2\u0081\u01e5\3\2\2\2\u0083\u01ee")
        buf.write("\3\2\2\2\u0085\u01f7\3\2\2\2\u0087\u020a\3\2\2\2\u0089")
        buf.write("\u020c\3\2\2\2\u008b\u0219\3\2\2\2\u008d\u021e\3\2\2\2")
        buf.write("\u008f\u0228\3\2\2\2\u0091\u0231\3\2\2\2\u0093\u0094\7")
        buf.write("=\2\2\u0094\4\3\2\2\2\u0095\u0096\7]\2\2\u0096\6\3\2\2")
        buf.write("\2\u0097\u0098\7_\2\2\u0098\b\3\2\2\2\u0099\u009a\7*\2")
        buf.write("\2\u009a\n\3\2\2\2\u009b\u009c\7.\2\2\u009c\f\3\2\2\2")
        buf.write("\u009d\u009e\7+\2\2\u009e\16\3\2\2\2\u009f\u00a0\7}\2")
        buf.write("\2\u00a0\20\3\2\2\2\u00a1\u00a2\7\177\2\2\u00a2\22\3\2")
        buf.write("\2\2\u00a3\u00a4\7(\2\2\u00a4\24\3\2\2\2\u00a5\u00a6\7")
        buf.write("~\2\2\u00a6\26\3\2\2\2\u00a7\u00a8\7?\2\2\u00a8\u00a9")
        buf.write("\7?\2\2\u00a9\30\3\2\2\2\u00aa\u00ab\7#\2\2\u00ab\u00ac")
        buf.write("\7?\2\2\u00ac\32\3\2\2\2\u00ad\u00ae\7@\2\2\u00ae\34\3")
        buf.write("\2\2\2\u00af\u00b0\7>\2\2\u00b0\36\3\2\2\2\u00b1\u00b2")
        buf.write("\7@\2\2\u00b2\u00b3\7?\2\2\u00b3 \3\2\2\2\u00b4\u00b5")
        buf.write("\7>\2\2\u00b5\u00b6\7?\2\2\u00b6\"\3\2\2\2\u00b7\u00b8")
        buf.write("\7-\2\2\u00b8$\3\2\2\2\u00b9\u00ba\7/\2\2\u00ba&\3\2\2")
        buf.write("\2\u00bb\u00bc\7,\2\2\u00bc(\3\2\2\2\u00bd\u00be\7\61")
        buf.write("\2\2\u00be*\3\2\2\2\u00bf\u00c0\7\'\2\2\u00c0,\3\2\2\2")
        buf.write("\u00c1\u00c2\7#\2\2\u00c2.\3\2\2\2\u00c3\u00c4\7\61\2")
        buf.write("\2\u00c4\u00c5\7\61\2\2\u00c5\u00c9\3\2\2\2\u00c6\u00c8")
        buf.write("\n\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cd\3\2\2\2")
        buf.write("\u00cb\u00c9\3\2\2\2\u00cc\u00ce\7\17\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00e1\7\f\2\2\u00d0\u00d1\7\61\2\2\u00d1\u00d2\7,\2\2")
        buf.write("\u00d2\u00d6\3\2\2\2\u00d3\u00d5\13\2\2\2\u00d4\u00d3")
        buf.write("\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00d6\3\2\2\2")
        buf.write("\u00d9\u00da\7,\2\2\u00da\u00e1\7\61\2\2\u00db\u00dd\t")
        buf.write("\3\2\2\u00dc\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0")
        buf.write("\u00c3\3\2\2\2\u00e0\u00d0\3\2\2\2\u00e0\u00dc\3\2\2\2")
        buf.write("\u00e1\u00e2\3\2\2\2\u00e2\u00e3\b\30\2\2\u00e3\60\3\2")
        buf.write("\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7")
        buf.write("\7l\2\2\u00e7\u00e8\7q\2\2\u00e8\62\3\2\2\2\u00e9\u00ea")
        buf.write("\7x\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed")
        buf.write("\7f\2\2\u00ed\u00ee\7g\2\2\u00ee\64\3\2\2\2\u00ef\u00f0")
        buf.write("\7c\2\2\u00f0\u00f1\7o\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7n\2\2\u00f5\u00f6")
        buf.write("\7n\2\2\u00f6\u00f7\7q\2\2\u00f7\66\3\2\2\2\u00f8\u00f9")
        buf.write("\7c\2\2\u00f9\u00fa\7|\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc")
        buf.write("\7n\2\2\u00fc8\3\2\2\2\u00fd\u00fe\7d\2\2\u00fe\u00ff")
        buf.write("\7n\2\2\u00ff\u0100\7c\2\2\u0100\u0101\7p\2\2\u0101\u0102")
        buf.write("\7e\2\2\u0102\u0103\7q\2\2\u0103:\3\2\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105\u0106\7g\2\2\u0106\u0107\7i\2\2\u0107\u0108")
        buf.write("\7t\2\2\u0108\u0109\7q\2\2\u0109<\3\2\2\2\u010a\u010b")
        buf.write("\7o\2\2\u010b\u010c\7q\2\2\u010c\u010d\7t\2\2\u010d\u010e")
        buf.write("\7c\2\2\u010e\u010f\7f\2\2\u010f\u0110\7q\2\2\u0110>\3")
        buf.write("\2\2\2\u0111\u0112\7p\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7t\2\2\u0114\u0115\7c\2\2\u0115\u0116\7p\2\2\u0116\u0117")
        buf.write("\7l\2\2\u0117\u0118\7c\2\2\u0118@\3\2\2\2\u0119\u011a")
        buf.write("\7e\2\2\u011a\u011b\7c\2\2\u011b\u011c\7h\2\2\u011c\u011d")
        buf.write("\7g\2\2\u011dB\3\2\2\2\u011e\u011f\7i\2\2\u011f\u0120")
        buf.write("\7t\2\2\u0120\u0121\7k\2\2\u0121\u0122\7u\2\2\u0122D\3")
        buf.write("\2\2\2\u0123\u0124\7e\2\2\u0124\u0125\7q\2\2\u0125\u0126")
        buf.write("\7n\2\2\u0126\u0127\7q\2\2\u0127\u0128\7t\2\2\u0128F\3")
        buf.write("\2\2\2\u0129\u012a\7x\2\2\u012a\u012b\7g\2\2\u012b\u012c")
        buf.write("\7n\2\2\u012c\u012d\7q\2\2\u012d\u012e\7e\2\2\u012e\u012f")
        buf.write("\7k\2\2\u012f\u0130\7f\2\2\u0130\u0131\7c\2\2\u0131\u0132")
        buf.write("\7f\2\2\u0132H\3\2\2\2\u0133\u0134\7n\2\2\u0134\u0135")
        buf.write("\7k\2\2\u0135\u0136\7g\2\2\u0136\u0137\7p\2\2\u0137\u0138")
        buf.write("\7|\2\2\u0138\u0139\7q\2\2\u0139J\3\2\2\2\u013a\u013b")
        buf.write("\7?\2\2\u013bL\3\2\2\2\u013c\u013d\7v\2\2\u013d\u013e")
        buf.write("\7c\2\2\u013e\u013f\7o\2\2\u013f\u0140\7c\2\2\u0140\u0141")
        buf.write("\7p\2\2\u0141\u0142\7q\2\2\u0142N\3\2\2\2\u0143\u0144")
        buf.write("\7r\2\2\u0144\u0145\7q\2\2\u0145\u0146\7t\2\2\u0146P\3")
        buf.write("\2\2\2\u0147\u0148\7f\2\2\u0148\u0149\7g\2\2\u0149R\3")
        buf.write("\2\2\2\u014a\u014b\7g\2\2\u014b\u014c\7p\2\2\u014cT\3")
        buf.write("\2\2\2\u014d\u014e\7o\2\2\u014e\u014f\7q\2\2\u014f\u0150")
        buf.write("\7x\2\2\u0150\u0151\7g\2\2\u0151\u0152\7t\2\2\u0152V\3")
        buf.write("\2\2\2\u0153\u0154\7c\2\2\u0154\u0155\7f\2\2\u0155\u0156")
        buf.write("\7g\2\2\u0156\u0157\7n\2\2\u0157\u0158\7c\2\2\u0158\u0159")
        buf.write("\7p\2\2\u0159\u015a\7v\2\2\u015a\u015b\7g\2\2\u015bX\3")
        buf.write("\2\2\2\u015c\u015d\7c\2\2\u015d\u015e\7v\2\2\u015e\u015f")
        buf.write("\7t\2\2\u015f\u0160\7c\2\2\u0160\u0161\7u\2\2\u0161Z\3")
        buf.write("\2\2\2\u0162\u0163\7i\2\2\u0163\u0164\7k\2\2\u0164\u0165")
        buf.write("\7t\2\2\u0165\u0166\7c\2\2\u0166\u0167\7t\2\2\u0167\\")
        buf.write("\3\2\2\2\u0168\u0169\7f\2\2\u0169\u016a\7g\2\2\u016a\u016b")
        buf.write("\7t\2\2\u016b\u016c\7g\2\2\u016c\u016d\7e\2\2\u016d\u016e")
        buf.write("\7j\2\2\u016e\u016f\7c\2\2\u016f^\3\2\2\2\u0170\u0171")
        buf.write("\7k\2\2\u0171\u0172\7|\2\2\u0172\u0173\7s\2\2\u0173\u0174")
        buf.write("\7w\2\2\u0174\u0175\7k\2\2\u0175\u0176\7g\2\2\u0176\u0177")
        buf.write("\7t\2\2\u0177\u0178\7f\2\2\u0178\u0179\7c\2\2\u0179`\3")
        buf.write("\2\2\2\u017a\u017b\7n\2\2\u017b\u017c\7g\2\2\u017c\u017d")
        buf.write("\7x\2\2\u017d\u017e\7c\2\2\u017e\u017f\7p\2\2\u017f\u0180")
        buf.write("\7v\2\2\u0180\u0181\7c\2\2\u0181\u0182\7t\2\2\u0182b\3")
        buf.write("\2\2\2\u0183\u0184\7d\2\2\u0184\u0185\7c\2\2\u0185\u0186")
        buf.write("\7l\2\2\u0186\u0187\7c\2\2\u0187\u0188\7t\2\2\u0188d\3")
        buf.write("\2\2\2\u0189\u018a\7r\2\2\u018a\u018b\7n\2\2\u018b\u018c")
        buf.write("\7w\2\2\u018c\u018d\7o\2\2\u018d\u018e\7c\2\2\u018ef\3")
        buf.write("\2\2\2\u018f\u0190\7o\2\2\u0190\u0191\7k\2\2\u0191\u0192")
        buf.write("\7g\2\2\u0192\u0193\7p\2\2\u0193\u0194\7v\2\2\u0194\u0195")
        buf.write("\7t\2\2\u0195\u0196\7c\2\2\u0196\u0197\7u\2\2\u0197h\3")
        buf.write("\2\2\2\u0198\u0199\7t\2\2\u0199\u019a\7g\2\2\u019a\u019b")
        buf.write("\7i\2\2\u019b\u019c\7t\2\2\u019c\u019d\7g\2\2\u019d\u019e")
        buf.write("\7u\2\2\u019e\u019f\7c\2\2\u019f\u01a0\7t\2\2\u01a0j\3")
        buf.write("\2\2\2\u01a1\u01a2\7s\2\2\u01a2\u01a3\7w\2\2\u01a3\u01a4")
        buf.write("\7g\2\2\u01a4l\3\2\2\2\u01a5\u01a6\7u\2\2\u01a6\u01a7")
        buf.write("\7k\2\2\u01a7\u01a8\7p\2\2\u01a8n\3\2\2\2\u01a9\u01aa")
        buf.write("\7u\2\2\u01aa\u01ab\7c\2\2\u01ab\u01ac\7n\2\2\u01ac\u01ad")
        buf.write("\7v\2\2\u01ad\u01ae\7q\2\2\u01aep\3\2\2\2\u01af\u01b0")
        buf.write("\7u\2\2\u01b0\u01b1\7k\2\2\u01b1r\3\2\2\2\u01b2\u01b3")
        buf.write("\7u\2\2\u01b3\u01b4\7k\2\2\u01b4\u01b5\7p\2\2\u01b5\u01b6")
        buf.write("\7q\2\2\u01b6t\3\2\2\2\u01b7\u01b8\7v\2\2\u01b8\u01b9")
        buf.write("\7g\2\2\u01b9\u01ba\7z\2\2\u01ba\u01bb\7v\2\2\u01bb\u01bc")
        buf.write("\7q\2\2\u01bcv\3\2\2\2\u01bd\u01be\7n\2\2\u01be\u01bf")
        buf.write("\7g\2\2\u01bf\u01c0\7g\2\2\u01c0\u01c1\7t\2\2\u01c1x\3")
        buf.write("\2\2\2\u01c2\u01c3\7r\2\2\u01c3\u01c4\7q\2\2\u01c4\u01c5")
        buf.write("\7u\2\2\u01c5\u01c6\7k\2\2\u01c6\u01c7\7e\2\2\u01c7\u01c8")
        buf.write("\7k\2\2\u01c8\u01c9\7q\2\2\u01c9\u01ca\7p\2\2\u01ca\u01cb")
        buf.write("\7Z\2\2\u01cbz\3\2\2\2\u01cc\u01cd\7r\2\2\u01cd\u01ce")
        buf.write("\7q\2\2\u01ce\u01cf\7u\2\2\u01cf\u01d0\7k\2\2\u01d0\u01d1")
        buf.write("\7e\2\2\u01d1\u01d2\7k\2\2\u01d2\u01d3\7q\2\2\u01d3\u01d4")
        buf.write("\7p\2\2\u01d4\u01d5\7[\2\2\u01d5|\3\2\2\2\u01d6\u01d7")
        buf.write("\7d\2\2\u01d7\u01d8\7q\2\2\u01d8\u01d9\7n\2\2\u01d9\u01da")
        buf.write("\7g\2\2\u01da\u01db\7c\2\2\u01db\u01dc\7p\2\2\u01dc\u01dd")
        buf.write("\7q\2\2\u01dd~\3\2\2\2\u01de\u01df\7p\2\2\u01df\u01e0")
        buf.write("\7w\2\2\u01e0\u01e1\7o\2\2\u01e1\u01e2\7g\2\2\u01e2\u01e3")
        buf.write("\7t\2\2\u01e3\u01e4\7q\2\2\u01e4\u0080\3\2\2\2\u01e5\u01e6")
        buf.write("\7g\2\2\u01e6\u01e7\7u\2\2\u01e7\u01e8\7e\2\2\u01e8\u01e9")
        buf.write("\7t\2\2\u01e9\u01ea\7k\2\2\u01ea\u01eb\7d\2\2\u01eb\u01ec")
        buf.write("\7k\2\2\u01ec\u01ed\7t\2\2\u01ed\u0082\3\2\2\2\u01ee\u01ef")
        buf.write("\7k\2\2\u01ef\u01f0\7o\2\2\u01f0\u01f1\7r\2\2\u01f1\u01f2")
        buf.write("\7t\2\2\u01f2\u01f3\7k\2\2\u01f3\u01f4\7o\2\2\u01f4\u01f5")
        buf.write("\7k\2\2\u01f5\u01f6\7t\2\2\u01f6\u0084\3\2\2\2\u01f7\u01f8")
        buf.write("\7p\2\2\u01f8\u01f9\7c\2\2\u01f9\u01fa\7f\2\2\u01fa\u01fb")
        buf.write("\7c\2\2\u01fb\u0086\3\2\2\2\u01fc\u01fd\7x\2\2\u01fd\u01fe")
        buf.write("\7g\2\2\u01fe\u01ff\7t\2\2\u01ff\u0200\7f\2\2\u0200\u0201")
        buf.write("\7c\2\2\u0201\u0202\7f\2\2\u0202\u0203\7g\2\2\u0203\u0204")
        buf.write("\7t\2\2\u0204\u020b\7q\2\2\u0205\u0206\7h\2\2\u0206\u0207")
        buf.write("\7c\2\2\u0207\u0208\7n\2\2\u0208\u0209\7u\2\2\u0209\u020b")
        buf.write("\7q\2\2\u020a\u01fc\3\2\2\2\u020a\u0205\3\2\2\2\u020b")
        buf.write("\u0088\3\2\2\2\u020c\u020d\7o\2\2\u020d\u020e\7q\2\2\u020e")
        buf.write("\u020f\7f\2\2\u020f\u0210\7k\2\2\u0210\u0211\7h\2\2\u0211")
        buf.write("\u0212\7k\2\2\u0212\u0213\7e\2\2\u0213\u0214\7c\2\2\u0214")
        buf.write("\u0215\7d\2\2\u0215\u0216\7n\2\2\u0216\u0217\7g\2\2\u0217")
        buf.write("\u008a\3\2\2\2\u0218\u021a\t\4\2\2\u0219\u0218\3\2\2\2")
        buf.write("\u021a\u021b\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3")
        buf.write("\2\2\2\u021c\u008c\3\2\2\2\u021d\u021f\t\4\2\2\u021e\u021d")
        buf.write("\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u021e\3\2\2\2\u0220")
        buf.write("\u0221\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0224\7\60\2")
        buf.write("\2\u0223\u0225\t\4\2\2\u0224\u0223\3\2\2\2\u0225\u0226")
        buf.write("\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write("\u008e\3\2\2\2\u0228\u022c\7$\2\2\u0229\u022b\n\5\2\2")
        buf.write("\u022a\u0229\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a\3")
        buf.write("\2\2\2\u022c\u022d\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u022c")
        buf.write("\3\2\2\2\u022f\u0230\7$\2\2\u0230\u0090\3\2\2\2\u0231")
        buf.write("\u0235\t\6\2\2\u0232\u0234\t\7\2\2\u0233\u0232\3\2\2\2")
        buf.write("\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0236\3")
        buf.write("\2\2\2\u0236\u0092\3\2\2\2\u0237\u0235\3\2\2\2\16\2\u00c9")
        buf.write("\u00cd\u00d6\u00de\u00e0\u020a\u021b\u0220\u0226\u022c")
        buf.write("\u0235\3\b\2\2")
        return buf.getvalue()


class LienzoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    WS = 23
    ROJO = 24
    VERDE = 25
    AMARILLO = 26
    AZUL = 27
    BLANCO = 28
    NEGRO = 29
    MORADO = 30
    NARANJA = 31
    CAFE = 32
    GRIS = 33
    COLOR = 34
    VELOCIDAD = 35
    LIENZO = 36
    EQUALS = 37
    TAMANO = 38
    POR = 39
    DE = 40
    EN = 41
    MOVER = 42
    ADELANTE = 43
    ATRAS = 44
    GIRAR = 45
    DERECHA = 46
    IZQUIERDA = 47
    LEVANTAR = 48
    BAJAR = 49
    PLUMA = 50
    MIENTRAS = 51
    REGRESAR = 52
    QUE = 53
    SIN = 54
    SALTO = 55
    SI = 56
    SINO = 57
    TEXTO = 58
    LEER = 59
    POSICION_X = 60
    POSICION_Y = 61
    BOLEANO = 62
    NUMERO = 63
    ESCRIBIR = 64
    IMPRIMIR = 65
    NADA = 66
    BOOLEAN_CONSTANT = 67
    MODIFICABLE = 68
    INTEGRAL_CONSTANT = 69
    NUMERIC_CONSTANT = 70
    STRING_CONSTANT = 71
    ID = 72

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'['", "']'", "'('", "','", "')'", "'{'", "'}'", "'&'", 
            "'|'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'rojo'", "'verde'", "'amarillo'", 
            "'azul'", "'blanco'", "'negro'", "'morado'", "'naranja'", "'cafe'", 
            "'gris'", "'color'", "'velocidad'", "'lienzo'", "'='", "'tamano'", 
            "'por'", "'de'", "'en'", "'mover'", "'adelante'", "'atras'", 
            "'girar'", "'derecha'", "'izquierda'", "'levantar'", "'bajar'", 
            "'pluma'", "'mientras'", "'regresar'", "'que'", "'sin'", "'salto'", 
            "'si'", "'sino'", "'texto'", "'leer'", "'posicionX'", "'posicionY'", 
            "'boleano'", "'numero'", "'escribir'", "'imprimir'", "'nada'", 
            "'modificable'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", "NEGRO", 
            "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", "VELOCIDAD", "LIENZO", 
            "EQUALS", "TAMANO", "POR", "DE", "EN", "MOVER", "ADELANTE", 
            "ATRAS", "GIRAR", "DERECHA", "IZQUIERDA", "LEVANTAR", "BAJAR", 
            "PLUMA", "MIENTRAS", "REGRESAR", "QUE", "SIN", "SALTO", "SI", 
            "SINO", "TEXTO", "LEER", "POSICION_X", "POSICION_Y", "BOLEANO", 
            "NUMERO", "ESCRIBIR", "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", 
            "MODIFICABLE", "INTEGRAL_CONSTANT", "NUMERIC_CONSTANT", "STRING_CONSTANT", 
            "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "WS", "ROJO", "VERDE", "AMARILLO", "AZUL", 
                  "BLANCO", "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", 
                  "COLOR", "VELOCIDAD", "LIENZO", "EQUALS", "TAMANO", "POR", 
                  "DE", "EN", "MOVER", "ADELANTE", "ATRAS", "GIRAR", "DERECHA", 
                  "IZQUIERDA", "LEVANTAR", "BAJAR", "PLUMA", "MIENTRAS", 
                  "REGRESAR", "QUE", "SIN", "SALTO", "SI", "SINO", "TEXTO", 
                  "LEER", "POSICION_X", "POSICION_Y", "BOLEANO", "NUMERO", 
                  "ESCRIBIR", "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", "MODIFICABLE", 
                  "INTEGRAL_CONSTANT", "NUMERIC_CONSTANT", "STRING_CONSTANT", 
                  "ID" ]

    grammarFileName = "Lienzo.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


