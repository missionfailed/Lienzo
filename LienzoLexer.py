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
        buf.write("\u0231\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\u00ce\n\30\3\30\3\30\3\30\3\30\3\30\3\30\6\30\u00d6\n")
        buf.write("\30\r\30\16\30\u00d7\5\30\u00da\n\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,")
        buf.write("\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\38\38\39\39\39\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3")
        buf.write("<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3C\3C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3D\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\5D\u0204\nD\3E\3E\3E\3E\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3F\6F\u0213\nF\rF\16F\u0214\3G\6G\u0218\nG\rG")
        buf.write("\16G\u0219\3G\3G\6G\u021e\nG\rG\16G\u021f\3H\3H\7H\u0224")
        buf.write("\nH\fH\16H\u0227\13H\3H\3H\3I\3I\7I\u022d\nI\fI\16I\u0230")
        buf.write("\13I\2\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087")
        buf.write("E\u0089F\u008bG\u008dH\u008fI\u0091J\3\2\t\4\2\f\f\17")
        buf.write("\17\3\2,,\5\2\13\f\17\17\"\"\3\2\62;\3\2$$\4\2C\\c|\5")
        buf.write("\2\62;C\\c|\u023b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u0095")
        buf.write("\3\2\2\2\7\u0097\3\2\2\2\t\u0099\3\2\2\2\13\u009b\3\2")
        buf.write("\2\2\r\u009d\3\2\2\2\17\u009f\3\2\2\2\21\u00a1\3\2\2\2")
        buf.write("\23\u00a3\3\2\2\2\25\u00a5\3\2\2\2\27\u00a7\3\2\2\2\31")
        buf.write("\u00aa\3\2\2\2\33\u00ad\3\2\2\2\35\u00af\3\2\2\2\37\u00b1")
        buf.write("\3\2\2\2!\u00b4\3\2\2\2#\u00b7\3\2\2\2%\u00b9\3\2\2\2")
        buf.write("\'\u00bb\3\2\2\2)\u00bd\3\2\2\2+\u00bf\3\2\2\2-\u00c1")
        buf.write("\3\2\2\2/\u00d9\3\2\2\2\61\u00dd\3\2\2\2\63\u00e2\3\2")
        buf.write("\2\2\65\u00e8\3\2\2\2\67\u00f1\3\2\2\29\u00f6\3\2\2\2")
        buf.write(";\u00fd\3\2\2\2=\u0103\3\2\2\2?\u010a\3\2\2\2A\u0112\3")
        buf.write("\2\2\2C\u0117\3\2\2\2E\u011c\3\2\2\2G\u0122\3\2\2\2I\u012c")
        buf.write("\3\2\2\2K\u0133\3\2\2\2M\u0135\3\2\2\2O\u013c\3\2\2\2")
        buf.write("Q\u0140\3\2\2\2S\u0143\3\2\2\2U\u0146\3\2\2\2W\u014c\3")
        buf.write("\2\2\2Y\u0155\3\2\2\2[\u015b\3\2\2\2]\u0161\3\2\2\2_\u0169")
        buf.write("\3\2\2\2a\u0173\3\2\2\2c\u017c\3\2\2\2e\u0182\3\2\2\2")
        buf.write("g\u0188\3\2\2\2i\u0191\3\2\2\2k\u019a\3\2\2\2m\u019e\3")
        buf.write("\2\2\2o\u01a2\3\2\2\2q\u01a8\3\2\2\2s\u01ab\3\2\2\2u\u01b0")
        buf.write("\3\2\2\2w\u01b6\3\2\2\2y\u01bb\3\2\2\2{\u01c5\3\2\2\2")
        buf.write("}\u01cf\3\2\2\2\177\u01d7\3\2\2\2\u0081\u01de\3\2\2\2")
        buf.write("\u0083\u01e7\3\2\2\2\u0085\u01f0\3\2\2\2\u0087\u0203\3")
        buf.write("\2\2\2\u0089\u0205\3\2\2\2\u008b\u0212\3\2\2\2\u008d\u0217")
        buf.write("\3\2\2\2\u008f\u0221\3\2\2\2\u0091\u022a\3\2\2\2\u0093")
        buf.write("\u0094\7=\2\2\u0094\4\3\2\2\2\u0095\u0096\7]\2\2\u0096")
        buf.write("\6\3\2\2\2\u0097\u0098\7_\2\2\u0098\b\3\2\2\2\u0099\u009a")
        buf.write("\7*\2\2\u009a\n\3\2\2\2\u009b\u009c\7.\2\2\u009c\f\3\2")
        buf.write("\2\2\u009d\u009e\7+\2\2\u009e\16\3\2\2\2\u009f\u00a0\7")
        buf.write("}\2\2\u00a0\20\3\2\2\2\u00a1\u00a2\7\177\2\2\u00a2\22")
        buf.write("\3\2\2\2\u00a3\u00a4\7(\2\2\u00a4\24\3\2\2\2\u00a5\u00a6")
        buf.write("\7~\2\2\u00a6\26\3\2\2\2\u00a7\u00a8\7?\2\2\u00a8\u00a9")
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
        buf.write("\u00da\7\f\2\2\u00d0\u00d1\7\61\2\2\u00d1\u00d2\7,\2\2")
        buf.write("\u00d2\u00d3\n\3\2\2\u00d3\u00da\7\61\2\2\u00d4\u00d6")
        buf.write("\t\4\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da\3\2\2\2")
        buf.write("\u00d9\u00c3\3\2\2\2\u00d9\u00d0\3\2\2\2\u00d9\u00d5\3")
        buf.write("\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\b\30\2\2\u00dc")
        buf.write("\60\3\2\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7q\2\2\u00df")
        buf.write("\u00e0\7l\2\2\u00e0\u00e1\7q\2\2\u00e1\62\3\2\2\2\u00e2")
        buf.write("\u00e3\7x\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7t\2\2\u00e5")
        buf.write("\u00e6\7f\2\2\u00e6\u00e7\7g\2\2\u00e7\64\3\2\2\2\u00e8")
        buf.write("\u00e9\7c\2\2\u00e9\u00ea\7o\2\2\u00ea\u00eb\7c\2\2\u00eb")
        buf.write("\u00ec\7t\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7n\2\2\u00ee")
        buf.write("\u00ef\7n\2\2\u00ef\u00f0\7q\2\2\u00f0\66\3\2\2\2\u00f1")
        buf.write("\u00f2\7c\2\2\u00f2\u00f3\7|\2\2\u00f3\u00f4\7w\2\2\u00f4")
        buf.write("\u00f5\7n\2\2\u00f58\3\2\2\2\u00f6\u00f7\7d\2\2\u00f7")
        buf.write("\u00f8\7n\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa\7p\2\2\u00fa")
        buf.write("\u00fb\7e\2\2\u00fb\u00fc\7q\2\2\u00fc:\3\2\2\2\u00fd")
        buf.write("\u00fe\7p\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100\7i\2\2\u0100")
        buf.write("\u0101\7t\2\2\u0101\u0102\7q\2\2\u0102<\3\2\2\2\u0103")
        buf.write("\u0104\7o\2\2\u0104\u0105\7q\2\2\u0105\u0106\7t\2\2\u0106")
        buf.write("\u0107\7c\2\2\u0107\u0108\7f\2\2\u0108\u0109\7q\2\2\u0109")
        buf.write(">\3\2\2\2\u010a\u010b\7p\2\2\u010b\u010c\7c\2\2\u010c")
        buf.write("\u010d\7t\2\2\u010d\u010e\7c\2\2\u010e\u010f\7p\2\2\u010f")
        buf.write("\u0110\7l\2\2\u0110\u0111\7c\2\2\u0111@\3\2\2\2\u0112")
        buf.write("\u0113\7e\2\2\u0113\u0114\7c\2\2\u0114\u0115\7h\2\2\u0115")
        buf.write("\u0116\7g\2\2\u0116B\3\2\2\2\u0117\u0118\7i\2\2\u0118")
        buf.write("\u0119\7t\2\2\u0119\u011a\7k\2\2\u011a\u011b\7u\2\2\u011b")
        buf.write("D\3\2\2\2\u011c\u011d\7e\2\2\u011d\u011e\7q\2\2\u011e")
        buf.write("\u011f\7n\2\2\u011f\u0120\7q\2\2\u0120\u0121\7t\2\2\u0121")
        buf.write("F\3\2\2\2\u0122\u0123\7x\2\2\u0123\u0124\7g\2\2\u0124")
        buf.write("\u0125\7n\2\2\u0125\u0126\7q\2\2\u0126\u0127\7e\2\2\u0127")
        buf.write("\u0128\7k\2\2\u0128\u0129\7f\2\2\u0129\u012a\7c\2\2\u012a")
        buf.write("\u012b\7f\2\2\u012bH\3\2\2\2\u012c\u012d\7n\2\2\u012d")
        buf.write("\u012e\7k\2\2\u012e\u012f\7g\2\2\u012f\u0130\7p\2\2\u0130")
        buf.write("\u0131\7|\2\2\u0131\u0132\7q\2\2\u0132J\3\2\2\2\u0133")
        buf.write("\u0134\7?\2\2\u0134L\3\2\2\2\u0135\u0136\7v\2\2\u0136")
        buf.write("\u0137\7c\2\2\u0137\u0138\7o\2\2\u0138\u0139\7c\2\2\u0139")
        buf.write("\u013a\7p\2\2\u013a\u013b\7q\2\2\u013bN\3\2\2\2\u013c")
        buf.write("\u013d\7r\2\2\u013d\u013e\7q\2\2\u013e\u013f\7t\2\2\u013f")
        buf.write("P\3\2\2\2\u0140\u0141\7f\2\2\u0141\u0142\7g\2\2\u0142")
        buf.write("R\3\2\2\2\u0143\u0144\7g\2\2\u0144\u0145\7p\2\2\u0145")
        buf.write("T\3\2\2\2\u0146\u0147\7o\2\2\u0147\u0148\7q\2\2\u0148")
        buf.write("\u0149\7x\2\2\u0149\u014a\7g\2\2\u014a\u014b\7t\2\2\u014b")
        buf.write("V\3\2\2\2\u014c\u014d\7c\2\2\u014d\u014e\7f\2\2\u014e")
        buf.write("\u014f\7g\2\2\u014f\u0150\7n\2\2\u0150\u0151\7c\2\2\u0151")
        buf.write("\u0152\7p\2\2\u0152\u0153\7v\2\2\u0153\u0154\7g\2\2\u0154")
        buf.write("X\3\2\2\2\u0155\u0156\7c\2\2\u0156\u0157\7v\2\2\u0157")
        buf.write("\u0158\7t\2\2\u0158\u0159\7c\2\2\u0159\u015a\7u\2\2\u015a")
        buf.write("Z\3\2\2\2\u015b\u015c\7i\2\2\u015c\u015d\7k\2\2\u015d")
        buf.write("\u015e\7t\2\2\u015e\u015f\7c\2\2\u015f\u0160\7t\2\2\u0160")
        buf.write("\\\3\2\2\2\u0161\u0162\7f\2\2\u0162\u0163\7g\2\2\u0163")
        buf.write("\u0164\7t\2\2\u0164\u0165\7g\2\2\u0165\u0166\7e\2\2\u0166")
        buf.write("\u0167\7j\2\2\u0167\u0168\7c\2\2\u0168^\3\2\2\2\u0169")
        buf.write("\u016a\7k\2\2\u016a\u016b\7|\2\2\u016b\u016c\7s\2\2\u016c")
        buf.write("\u016d\7w\2\2\u016d\u016e\7k\2\2\u016e\u016f\7g\2\2\u016f")
        buf.write("\u0170\7t\2\2\u0170\u0171\7f\2\2\u0171\u0172\7c\2\2\u0172")
        buf.write("`\3\2\2\2\u0173\u0174\7n\2\2\u0174\u0175\7g\2\2\u0175")
        buf.write("\u0176\7x\2\2\u0176\u0177\7c\2\2\u0177\u0178\7p\2\2\u0178")
        buf.write("\u0179\7v\2\2\u0179\u017a\7c\2\2\u017a\u017b\7t\2\2\u017b")
        buf.write("b\3\2\2\2\u017c\u017d\7d\2\2\u017d\u017e\7c\2\2\u017e")
        buf.write("\u017f\7l\2\2\u017f\u0180\7c\2\2\u0180\u0181\7t\2\2\u0181")
        buf.write("d\3\2\2\2\u0182\u0183\7r\2\2\u0183\u0184\7n\2\2\u0184")
        buf.write("\u0185\7w\2\2\u0185\u0186\7o\2\2\u0186\u0187\7c\2\2\u0187")
        buf.write("f\3\2\2\2\u0188\u0189\7o\2\2\u0189\u018a\7k\2\2\u018a")
        buf.write("\u018b\7g\2\2\u018b\u018c\7p\2\2\u018c\u018d\7v\2\2\u018d")
        buf.write("\u018e\7t\2\2\u018e\u018f\7c\2\2\u018f\u0190\7u\2\2\u0190")
        buf.write("h\3\2\2\2\u0191\u0192\7t\2\2\u0192\u0193\7g\2\2\u0193")
        buf.write("\u0194\7i\2\2\u0194\u0195\7t\2\2\u0195\u0196\7g\2\2\u0196")
        buf.write("\u0197\7u\2\2\u0197\u0198\7c\2\2\u0198\u0199\7t\2\2\u0199")
        buf.write("j\3\2\2\2\u019a\u019b\7s\2\2\u019b\u019c\7w\2\2\u019c")
        buf.write("\u019d\7g\2\2\u019dl\3\2\2\2\u019e\u019f\7u\2\2\u019f")
        buf.write("\u01a0\7k\2\2\u01a0\u01a1\7p\2\2\u01a1n\3\2\2\2\u01a2")
        buf.write("\u01a3\7u\2\2\u01a3\u01a4\7c\2\2\u01a4\u01a5\7n\2\2\u01a5")
        buf.write("\u01a6\7v\2\2\u01a6\u01a7\7q\2\2\u01a7p\3\2\2\2\u01a8")
        buf.write("\u01a9\7u\2\2\u01a9\u01aa\7k\2\2\u01aar\3\2\2\2\u01ab")
        buf.write("\u01ac\7u\2\2\u01ac\u01ad\7k\2\2\u01ad\u01ae\7p\2\2\u01ae")
        buf.write("\u01af\7q\2\2\u01aft\3\2\2\2\u01b0\u01b1\7v\2\2\u01b1")
        buf.write("\u01b2\7g\2\2\u01b2\u01b3\7z\2\2\u01b3\u01b4\7v\2\2\u01b4")
        buf.write("\u01b5\7q\2\2\u01b5v\3\2\2\2\u01b6\u01b7\7n\2\2\u01b7")
        buf.write("\u01b8\7g\2\2\u01b8\u01b9\7g\2\2\u01b9\u01ba\7t\2\2\u01ba")
        buf.write("x\3\2\2\2\u01bb\u01bc\7r\2\2\u01bc\u01bd\7q\2\2\u01bd")
        buf.write("\u01be\7u\2\2\u01be\u01bf\7k\2\2\u01bf\u01c0\7e\2\2\u01c0")
        buf.write("\u01c1\7k\2\2\u01c1\u01c2\7q\2\2\u01c2\u01c3\7p\2\2\u01c3")
        buf.write("\u01c4\7Z\2\2\u01c4z\3\2\2\2\u01c5\u01c6\7r\2\2\u01c6")
        buf.write("\u01c7\7q\2\2\u01c7\u01c8\7u\2\2\u01c8\u01c9\7k\2\2\u01c9")
        buf.write("\u01ca\7e\2\2\u01ca\u01cb\7k\2\2\u01cb\u01cc\7q\2\2\u01cc")
        buf.write("\u01cd\7p\2\2\u01cd\u01ce\7[\2\2\u01ce|\3\2\2\2\u01cf")
        buf.write("\u01d0\7d\2\2\u01d0\u01d1\7q\2\2\u01d1\u01d2\7n\2\2\u01d2")
        buf.write("\u01d3\7g\2\2\u01d3\u01d4\7c\2\2\u01d4\u01d5\7p\2\2\u01d5")
        buf.write("\u01d6\7q\2\2\u01d6~\3\2\2\2\u01d7\u01d8\7p\2\2\u01d8")
        buf.write("\u01d9\7w\2\2\u01d9\u01da\7o\2\2\u01da\u01db\7g\2\2\u01db")
        buf.write("\u01dc\7t\2\2\u01dc\u01dd\7q\2\2\u01dd\u0080\3\2\2\2\u01de")
        buf.write("\u01df\7g\2\2\u01df\u01e0\7u\2\2\u01e0\u01e1\7e\2\2\u01e1")
        buf.write("\u01e2\7t\2\2\u01e2\u01e3\7k\2\2\u01e3\u01e4\7d\2\2\u01e4")
        buf.write("\u01e5\7k\2\2\u01e5\u01e6\7t\2\2\u01e6\u0082\3\2\2\2\u01e7")
        buf.write("\u01e8\7k\2\2\u01e8\u01e9\7o\2\2\u01e9\u01ea\7r\2\2\u01ea")
        buf.write("\u01eb\7t\2\2\u01eb\u01ec\7k\2\2\u01ec\u01ed\7o\2\2\u01ed")
        buf.write("\u01ee\7k\2\2\u01ee\u01ef\7t\2\2\u01ef\u0084\3\2\2\2\u01f0")
        buf.write("\u01f1\7p\2\2\u01f1\u01f2\7c\2\2\u01f2\u01f3\7f\2\2\u01f3")
        buf.write("\u01f4\7c\2\2\u01f4\u0086\3\2\2\2\u01f5\u01f6\7x\2\2\u01f6")
        buf.write("\u01f7\7g\2\2\u01f7\u01f8\7t\2\2\u01f8\u01f9\7f\2\2\u01f9")
        buf.write("\u01fa\7c\2\2\u01fa\u01fb\7f\2\2\u01fb\u01fc\7g\2\2\u01fc")
        buf.write("\u01fd\7t\2\2\u01fd\u0204\7q\2\2\u01fe\u01ff\7h\2\2\u01ff")
        buf.write("\u0200\7c\2\2\u0200\u0201\7n\2\2\u0201\u0202\7u\2\2\u0202")
        buf.write("\u0204\7q\2\2\u0203\u01f5\3\2\2\2\u0203\u01fe\3\2\2\2")
        buf.write("\u0204\u0088\3\2\2\2\u0205\u0206\7o\2\2\u0206\u0207\7")
        buf.write("q\2\2\u0207\u0208\7f\2\2\u0208\u0209\7k\2\2\u0209\u020a")
        buf.write("\7h\2\2\u020a\u020b\7k\2\2\u020b\u020c\7e\2\2\u020c\u020d")
        buf.write("\7c\2\2\u020d\u020e\7d\2\2\u020e\u020f\7n\2\2\u020f\u0210")
        buf.write("\7g\2\2\u0210\u008a\3\2\2\2\u0211\u0213\t\5\2\2\u0212")
        buf.write("\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0212\3\2\2\2")
        buf.write("\u0214\u0215\3\2\2\2\u0215\u008c\3\2\2\2\u0216\u0218\t")
        buf.write("\5\2\2\u0217\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u0217")
        buf.write("\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021b\3\2\2\2\u021b")
        buf.write("\u021d\7\60\2\2\u021c\u021e\t\5\2\2\u021d\u021c\3\2\2")
        buf.write("\2\u021e\u021f\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220")
        buf.write("\3\2\2\2\u0220\u008e\3\2\2\2\u0221\u0225\7$\2\2\u0222")
        buf.write("\u0224\n\6\2\2\u0223\u0222\3\2\2\2\u0224\u0227\3\2\2\2")
        buf.write("\u0225\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0228\3")
        buf.write("\2\2\2\u0227\u0225\3\2\2\2\u0228\u0229\7$\2\2\u0229\u0090")
        buf.write("\3\2\2\2\u022a\u022e\t\7\2\2\u022b\u022d\t\b\2\2\u022c")
        buf.write("\u022b\3\2\2\2\u022d\u0230\3\2\2\2\u022e\u022c\3\2\2\2")
        buf.write("\u022e\u022f\3\2\2\2\u022f\u0092\3\2\2\2\u0230\u022e\3")
        buf.write("\2\2\2\r\2\u00c9\u00cd\u00d7\u00d9\u0203\u0214\u0219\u021f")
        buf.write("\u0225\u022e\3\b\2\2")
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


