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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2G")
        buf.write("\u01fe\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\6\30\u00bf\n\30\r\30\16\30\u00c0")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(")
        buf.write("\3(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3;\3;\3;\3")
        buf.write(";\3;\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3@\3")
        buf.write("@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\5")
        buf.write("A\u01d1\nA\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3C\6C\u01e0")
        buf.write("\nC\rC\16C\u01e1\3D\6D\u01e5\nD\rD\16D\u01e6\3D\3D\6D")
        buf.write("\u01eb\nD\rD\16D\u01ec\3E\3E\7E\u01f1\nE\fE\16E\u01f4")
        buf.write("\13E\3E\3E\3F\3F\7F\u01fa\nF\fF\16F\u01fd\13F\2\2G\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w")
        buf.write("=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008b")
        buf.write("G\3\2\7\5\2\13\f\17\17\"\"\3\2\62;\3\2$$\4\2C\\c|\5\2")
        buf.write("\62;C\\c|\u0204\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
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
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2")
        buf.write("\2\5\u008f\3\2\2\2\7\u0091\3\2\2\2\t\u0093\3\2\2\2\13")
        buf.write("\u0095\3\2\2\2\r\u0097\3\2\2\2\17\u0099\3\2\2\2\21\u009b")
        buf.write("\3\2\2\2\23\u009d\3\2\2\2\25\u009f\3\2\2\2\27\u00a1\3")
        buf.write("\2\2\2\31\u00a4\3\2\2\2\33\u00a7\3\2\2\2\35\u00a9\3\2")
        buf.write("\2\2\37\u00ab\3\2\2\2!\u00ae\3\2\2\2#\u00b1\3\2\2\2%\u00b3")
        buf.write("\3\2\2\2\'\u00b5\3\2\2\2)\u00b7\3\2\2\2+\u00b9\3\2\2\2")
        buf.write("-\u00bb\3\2\2\2/\u00be\3\2\2\2\61\u00c4\3\2\2\2\63\u00c9")
        buf.write("\3\2\2\2\65\u00cf\3\2\2\2\67\u00d8\3\2\2\29\u00dd\3\2")
        buf.write("\2\2;\u00e4\3\2\2\2=\u00ea\3\2\2\2?\u00f1\3\2\2\2A\u00f9")
        buf.write("\3\2\2\2C\u00fe\3\2\2\2E\u0103\3\2\2\2G\u0109\3\2\2\2")
        buf.write("I\u0110\3\2\2\2K\u0112\3\2\2\2M\u0119\3\2\2\2O\u011d\3")
        buf.write("\2\2\2Q\u0120\3\2\2\2S\u0123\3\2\2\2U\u0129\3\2\2\2W\u0132")
        buf.write("\3\2\2\2Y\u0138\3\2\2\2[\u013e\3\2\2\2]\u0146\3\2\2\2")
        buf.write("_\u0150\3\2\2\2a\u0159\3\2\2\2c\u015f\3\2\2\2e\u0165\3")
        buf.write("\2\2\2g\u016c\3\2\2\2i\u0173\3\2\2\2k\u017c\3\2\2\2m\u0185")
        buf.write("\3\2\2\2o\u0189\3\2\2\2q\u018c\3\2\2\2s\u0191\3\2\2\2")
        buf.write("u\u0197\3\2\2\2w\u019c\3\2\2\2y\u01a4\3\2\2\2{\u01ab\3")
        buf.write("\2\2\2}\u01b4\3\2\2\2\177\u01bd\3\2\2\2\u0081\u01d0\3")
        buf.write("\2\2\2\u0083\u01d2\3\2\2\2\u0085\u01df\3\2\2\2\u0087\u01e4")
        buf.write("\3\2\2\2\u0089\u01ee\3\2\2\2\u008b\u01f7\3\2\2\2\u008d")
        buf.write("\u008e\7=\2\2\u008e\4\3\2\2\2\u008f\u0090\7]\2\2\u0090")
        buf.write("\6\3\2\2\2\u0091\u0092\7_\2\2\u0092\b\3\2\2\2\u0093\u0094")
        buf.write("\7*\2\2\u0094\n\3\2\2\2\u0095\u0096\7.\2\2\u0096\f\3\2")
        buf.write("\2\2\u0097\u0098\7+\2\2\u0098\16\3\2\2\2\u0099\u009a\7")
        buf.write("}\2\2\u009a\20\3\2\2\2\u009b\u009c\7\177\2\2\u009c\22")
        buf.write("\3\2\2\2\u009d\u009e\7(\2\2\u009e\24\3\2\2\2\u009f\u00a0")
        buf.write("\7~\2\2\u00a0\26\3\2\2\2\u00a1\u00a2\7?\2\2\u00a2\u00a3")
        buf.write("\7?\2\2\u00a3\30\3\2\2\2\u00a4\u00a5\7#\2\2\u00a5\u00a6")
        buf.write("\7?\2\2\u00a6\32\3\2\2\2\u00a7\u00a8\7@\2\2\u00a8\34\3")
        buf.write("\2\2\2\u00a9\u00aa\7>\2\2\u00aa\36\3\2\2\2\u00ab\u00ac")
        buf.write("\7@\2\2\u00ac\u00ad\7?\2\2\u00ad \3\2\2\2\u00ae\u00af")
        buf.write("\7>\2\2\u00af\u00b0\7?\2\2\u00b0\"\3\2\2\2\u00b1\u00b2")
        buf.write("\7-\2\2\u00b2$\3\2\2\2\u00b3\u00b4\7/\2\2\u00b4&\3\2\2")
        buf.write("\2\u00b5\u00b6\7,\2\2\u00b6(\3\2\2\2\u00b7\u00b8\7\61")
        buf.write("\2\2\u00b8*\3\2\2\2\u00b9\u00ba\7\'\2\2\u00ba,\3\2\2\2")
        buf.write("\u00bb\u00bc\7#\2\2\u00bc.\3\2\2\2\u00bd\u00bf\t\2\2\2")
        buf.write("\u00be\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00be\3")
        buf.write("\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3")
        buf.write("\b\30\2\2\u00c3\60\3\2\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6")
        buf.write("\7q\2\2\u00c6\u00c7\7l\2\2\u00c7\u00c8\7q\2\2\u00c8\62")
        buf.write("\3\2\2\2\u00c9\u00ca\7x\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc")
        buf.write("\7t\2\2\u00cc\u00cd\7f\2\2\u00cd\u00ce\7g\2\2\u00ce\64")
        buf.write("\3\2\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7o\2\2\u00d1\u00d2")
        buf.write("\7c\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5")
        buf.write("\7n\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7\7q\2\2\u00d7\66")
        buf.write("\3\2\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da\7|\2\2\u00da\u00db")
        buf.write("\7w\2\2\u00db\u00dc\7n\2\2\u00dc8\3\2\2\2\u00dd\u00de")
        buf.write("\7d\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1")
        buf.write("\7p\2\2\u00e1\u00e2\7e\2\2\u00e2\u00e3\7q\2\2\u00e3:\3")
        buf.write("\2\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7")
        buf.write("\7i\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7q\2\2\u00e9<\3")
        buf.write("\2\2\2\u00ea\u00eb\7o\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7f\2\2\u00ef\u00f0")
        buf.write("\7q\2\2\u00f0>\3\2\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f7\7l\2\2\u00f7\u00f8\7c\2\2\u00f8@\3")
        buf.write("\2\2\2\u00f9\u00fa\7e\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7h\2\2\u00fc\u00fd\7g\2\2\u00fdB\3\2\2\2\u00fe\u00ff")
        buf.write("\7i\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7k\2\2\u0101\u0102")
        buf.write("\7u\2\2\u0102D\3\2\2\2\u0103\u0104\7e\2\2\u0104\u0105")
        buf.write("\7q\2\2\u0105\u0106\7n\2\2\u0106\u0107\7q\2\2\u0107\u0108")
        buf.write("\7t\2\2\u0108F\3\2\2\2\u0109\u010a\7n\2\2\u010a\u010b")
        buf.write("\7k\2\2\u010b\u010c\7g\2\2\u010c\u010d\7p\2\2\u010d\u010e")
        buf.write("\7|\2\2\u010e\u010f\7q\2\2\u010fH\3\2\2\2\u0110\u0111")
        buf.write("\7?\2\2\u0111J\3\2\2\2\u0112\u0113\7v\2\2\u0113\u0114")
        buf.write("\7c\2\2\u0114\u0115\7o\2\2\u0115\u0116\7c\2\2\u0116\u0117")
        buf.write("\7p\2\2\u0117\u0118\7q\2\2\u0118L\3\2\2\2\u0119\u011a")
        buf.write("\7r\2\2\u011a\u011b\7q\2\2\u011b\u011c\7t\2\2\u011cN\3")
        buf.write("\2\2\2\u011d\u011e\7f\2\2\u011e\u011f\7g\2\2\u011fP\3")
        buf.write("\2\2\2\u0120\u0121\7g\2\2\u0121\u0122\7p\2\2\u0122R\3")
        buf.write("\2\2\2\u0123\u0124\7o\2\2\u0124\u0125\7q\2\2\u0125\u0126")
        buf.write("\7x\2\2\u0126\u0127\7g\2\2\u0127\u0128\7t\2\2\u0128T\3")
        buf.write("\2\2\2\u0129\u012a\7c\2\2\u012a\u012b\7f\2\2\u012b\u012c")
        buf.write("\7g\2\2\u012c\u012d\7n\2\2\u012d\u012e\7c\2\2\u012e\u012f")
        buf.write("\7p\2\2\u012f\u0130\7v\2\2\u0130\u0131\7g\2\2\u0131V\3")
        buf.write("\2\2\2\u0132\u0133\7c\2\2\u0133\u0134\7v\2\2\u0134\u0135")
        buf.write("\7t\2\2\u0135\u0136\7c\2\2\u0136\u0137\7u\2\2\u0137X\3")
        buf.write("\2\2\2\u0138\u0139\7i\2\2\u0139\u013a\7k\2\2\u013a\u013b")
        buf.write("\7t\2\2\u013b\u013c\7c\2\2\u013c\u013d\7t\2\2\u013dZ\3")
        buf.write("\2\2\2\u013e\u013f\7f\2\2\u013f\u0140\7g\2\2\u0140\u0141")
        buf.write("\7t\2\2\u0141\u0142\7g\2\2\u0142\u0143\7e\2\2\u0143\u0144")
        buf.write("\7j\2\2\u0144\u0145\7c\2\2\u0145\\\3\2\2\2\u0146\u0147")
        buf.write("\7k\2\2\u0147\u0148\7|\2\2\u0148\u0149\7s\2\2\u0149\u014a")
        buf.write("\7w\2\2\u014a\u014b\7k\2\2\u014b\u014c\7g\2\2\u014c\u014d")
        buf.write("\7t\2\2\u014d\u014e\7f\2\2\u014e\u014f\7c\2\2\u014f^\3")
        buf.write("\2\2\2\u0150\u0151\7n\2\2\u0151\u0152\7g\2\2\u0152\u0153")
        buf.write("\7x\2\2\u0153\u0154\7c\2\2\u0154\u0155\7p\2\2\u0155\u0156")
        buf.write("\7v\2\2\u0156\u0157\7c\2\2\u0157\u0158\7t\2\2\u0158`\3")
        buf.write("\2\2\2\u0159\u015a\7d\2\2\u015a\u015b\7c\2\2\u015b\u015c")
        buf.write("\7l\2\2\u015c\u015d\7c\2\2\u015d\u015e\7t\2\2\u015eb\3")
        buf.write("\2\2\2\u015f\u0160\7r\2\2\u0160\u0161\7n\2\2\u0161\u0162")
        buf.write("\7w\2\2\u0162\u0163\7o\2\2\u0163\u0164\7c\2\2\u0164d\3")
        buf.write("\2\2\2\u0165\u0166\7f\2\2\u0166\u0167\7k\2\2\u0167\u0168")
        buf.write("\7d\2\2\u0168\u0169\7w\2\2\u0169\u016a\7l\2\2\u016a\u016b")
        buf.write("\7q\2\2\u016bf\3\2\2\2\u016c\u016d\7f\2\2\u016d\u016e")
        buf.write("\7q\2\2\u016e\u016f\7t\2\2\u016f\u0170\7o\2\2\u0170\u0171")
        buf.write("\7k\2\2\u0171\u0172\7t\2\2\u0172h\3\2\2\2\u0173\u0174")
        buf.write("\7o\2\2\u0174\u0175\7k\2\2\u0175\u0176\7g\2\2\u0176\u0177")
        buf.write("\7p\2\2\u0177\u0178\7v\2\2\u0178\u0179\7t\2\2\u0179\u017a")
        buf.write("\7c\2\2\u017a\u017b\7u\2\2\u017bj\3\2\2\2\u017c\u017d")
        buf.write("\7t\2\2\u017d\u017e\7g\2\2\u017e\u017f\7i\2\2\u017f\u0180")
        buf.write("\7t\2\2\u0180\u0181\7g\2\2\u0181\u0182\7u\2\2\u0182\u0183")
        buf.write("\7c\2\2\u0183\u0184\7t\2\2\u0184l\3\2\2\2\u0185\u0186")
        buf.write("\7s\2\2\u0186\u0187\7w\2\2\u0187\u0188\7g\2\2\u0188n\3")
        buf.write("\2\2\2\u0189\u018a\7u\2\2\u018a\u018b\7k\2\2\u018bp\3")
        buf.write("\2\2\2\u018c\u018d\7u\2\2\u018d\u018e\7k\2\2\u018e\u018f")
        buf.write("\7p\2\2\u018f\u0190\7q\2\2\u0190r\3\2\2\2\u0191\u0192")
        buf.write("\7v\2\2\u0192\u0193\7g\2\2\u0193\u0194\7z\2\2\u0194\u0195")
        buf.write("\7v\2\2\u0195\u0196\7q\2\2\u0196t\3\2\2\2\u0197\u0198")
        buf.write("\7n\2\2\u0198\u0199\7g\2\2\u0199\u019a\7g\2\2\u019a\u019b")
        buf.write("\7t\2\2\u019bv\3\2\2\2\u019c\u019d\7d\2\2\u019d\u019e")
        buf.write("\7q\2\2\u019e\u019f\7n\2\2\u019f\u01a0\7g\2\2\u01a0\u01a1")
        buf.write("\7c\2\2\u01a1\u01a2\7p\2\2\u01a2\u01a3\7q\2\2\u01a3x\3")
        buf.write("\2\2\2\u01a4\u01a5\7p\2\2\u01a5\u01a6\7w\2\2\u01a6\u01a7")
        buf.write("\7o\2\2\u01a7\u01a8\7g\2\2\u01a8\u01a9\7t\2\2\u01a9\u01aa")
        buf.write("\7q\2\2\u01aaz\3\2\2\2\u01ab\u01ac\7g\2\2\u01ac\u01ad")
        buf.write("\7u\2\2\u01ad\u01ae\7e\2\2\u01ae\u01af\7t\2\2\u01af\u01b0")
        buf.write("\7k\2\2\u01b0\u01b1\7d\2\2\u01b1\u01b2\7k\2\2\u01b2\u01b3")
        buf.write("\7t\2\2\u01b3|\3\2\2\2\u01b4\u01b5\7k\2\2\u01b5\u01b6")
        buf.write("\7o\2\2\u01b6\u01b7\7r\2\2\u01b7\u01b8\7t\2\2\u01b8\u01b9")
        buf.write("\7k\2\2\u01b9\u01ba\7o\2\2\u01ba\u01bb\7k\2\2\u01bb\u01bc")
        buf.write("\7t\2\2\u01bc~\3\2\2\2\u01bd\u01be\7p\2\2\u01be\u01bf")
        buf.write("\7c\2\2\u01bf\u01c0\7f\2\2\u01c0\u01c1\7c\2\2\u01c1\u0080")
        buf.write("\3\2\2\2\u01c2\u01c3\7x\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5")
        buf.write("\7t\2\2\u01c5\u01c6\7f\2\2\u01c6\u01c7\7c\2\2\u01c7\u01c8")
        buf.write("\7f\2\2\u01c8\u01c9\7g\2\2\u01c9\u01ca\7t\2\2\u01ca\u01d1")
        buf.write("\7q\2\2\u01cb\u01cc\7h\2\2\u01cc\u01cd\7c\2\2\u01cd\u01ce")
        buf.write("\7n\2\2\u01ce\u01cf\7u\2\2\u01cf\u01d1\7q\2\2\u01d0\u01c2")
        buf.write("\3\2\2\2\u01d0\u01cb\3\2\2\2\u01d1\u0082\3\2\2\2\u01d2")
        buf.write("\u01d3\7o\2\2\u01d3\u01d4\7q\2\2\u01d4\u01d5\7f\2\2\u01d5")
        buf.write("\u01d6\7k\2\2\u01d6\u01d7\7h\2\2\u01d7\u01d8\7k\2\2\u01d8")
        buf.write("\u01d9\7e\2\2\u01d9\u01da\7c\2\2\u01da\u01db\7d\2\2\u01db")
        buf.write("\u01dc\7n\2\2\u01dc\u01dd\7g\2\2\u01dd\u0084\3\2\2\2\u01de")
        buf.write("\u01e0\t\3\2\2\u01df\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u0086\3")
        buf.write("\2\2\2\u01e3\u01e5\t\3\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e6")
        buf.write("\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("\u01e8\3\2\2\2\u01e8\u01ea\7\60\2\2\u01e9\u01eb\t\3\2")
        buf.write("\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ea")
        buf.write("\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u0088\3\2\2\2\u01ee")
        buf.write("\u01f2\7$\2\2\u01ef\u01f1\n\4\2\2\u01f0\u01ef\3\2\2\2")
        buf.write("\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3")
        buf.write("\2\2\2\u01f3\u01f5\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01f6")
        buf.write("\7$\2\2\u01f6\u008a\3\2\2\2\u01f7\u01fb\t\5\2\2\u01f8")
        buf.write("\u01fa\t\6\2\2\u01f9\u01f8\3\2\2\2\u01fa\u01fd\3\2\2\2")
        buf.write("\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u008c\3")
        buf.write("\2\2\2\u01fd\u01fb\3\2\2\2\n\2\u00c0\u01d0\u01e1\u01e6")
        buf.write("\u01ec\u01f2\u01fb\3\b\2\2")
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
    LIENZO = 35
    EQUALS = 36
    TAMANO = 37
    POR = 38
    DE = 39
    EN = 40
    MOVER = 41
    ADELANTE = 42
    ATRAS = 43
    GIRAR = 44
    DERECHA = 45
    IZQUIERDA = 46
    LEVANTAR = 47
    BAJAR = 48
    PLUMA = 49
    DIBUJO = 50
    DORMIR = 51
    MIENTRAS = 52
    REGRESAR = 53
    QUE = 54
    SI = 55
    SINO = 56
    TEXTO = 57
    LEER = 58
    BOLEANO = 59
    NUMERO = 60
    ESCRIBIR = 61
    IMPRIMIR = 62
    NADA = 63
    BOOLEAN_CONSTANT = 64
    MODIFICABLE = 65
    INTEGRAL_CONSTANT = 66
    NUMERIC_CONSTANT = 67
    STRING_CONSTANT = 68
    ID = 69

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'['", "']'", "'('", "','", "')'", "'{'", "'}'", "'&'", 
            "'|'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'rojo'", "'verde'", "'amarillo'", 
            "'azul'", "'blanco'", "'negro'", "'morado'", "'naranja'", "'cafe'", 
            "'gris'", "'color'", "'lienzo'", "'='", "'tamano'", "'por'", 
            "'de'", "'en'", "'mover'", "'adelante'", "'atras'", "'girar'", 
            "'derecha'", "'izquierda'", "'levantar'", "'bajar'", "'pluma'", 
            "'dibujo'", "'dormir'", "'mientras'", "'regresar'", "'que'", 
            "'si'", "'sino'", "'texto'", "'leer'", "'boleano'", "'numero'", 
            "'escribir'", "'imprimir'", "'nada'", "'modificable'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", "NEGRO", 
            "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", "LIENZO", "EQUALS", 
            "TAMANO", "POR", "DE", "EN", "MOVER", "ADELANTE", "ATRAS", "GIRAR", 
            "DERECHA", "IZQUIERDA", "LEVANTAR", "BAJAR", "PLUMA", "DIBUJO", 
            "DORMIR", "MIENTRAS", "REGRESAR", "QUE", "SI", "SINO", "TEXTO", 
            "LEER", "BOLEANO", "NUMERO", "ESCRIBIR", "IMPRIMIR", "NADA", 
            "BOOLEAN_CONSTANT", "MODIFICABLE", "INTEGRAL_CONSTANT", "NUMERIC_CONSTANT", 
            "STRING_CONSTANT", "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "WS", "ROJO", "VERDE", "AMARILLO", "AZUL", 
                  "BLANCO", "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", 
                  "COLOR", "LIENZO", "EQUALS", "TAMANO", "POR", "DE", "EN", 
                  "MOVER", "ADELANTE", "ATRAS", "GIRAR", "DERECHA", "IZQUIERDA", 
                  "LEVANTAR", "BAJAR", "PLUMA", "DIBUJO", "DORMIR", "MIENTRAS", 
                  "REGRESAR", "QUE", "SI", "SINO", "TEXTO", "LEER", "BOLEANO", 
                  "NUMERO", "ESCRIBIR", "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", 
                  "MODIFICABLE", "INTEGRAL_CONSTANT", "NUMERIC_CONSTANT", 
                  "STRING_CONSTANT", "ID" ]

    grammarFileName = "Lienzo.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


