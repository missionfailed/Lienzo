# Generated from Lienzo.g4 by ANTLR 4.5.2
from antlr4 import *
from io import StringIO


from namespace import NamespaceTable
from collections import defaultdict
from MemoryRegister import MemoryRegisters
from cuadruplos import *

namespaceTable = NamespaceTable()
currentFunctionName = ""
currentParameterList = []

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


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2D")
        buf.write("\u01f1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3")
        buf.write("\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\6\26\u00b5")
        buf.write("\n\26\r\26\16\26\u00b6\3\26\3\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\38\38\38\38\38\38\39\39\39\39\39\3:\3:\3:\3:\3:")
        buf.write("\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3")
        buf.write("<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u01c7\n?\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3A\6A\u01d6\nA\rA\16A\u01d7")
        buf.write("\3A\3A\6A\u01dc\nA\rA\16A\u01dd\5A\u01e0\nA\3B\3B\7B\u01e4")
        buf.write("\nB\fB\16B\u01e7\13B\3B\3B\3C\3C\7C\u01ed\nC\fC\16C\u01f0")
        buf.write("\13C\2\2D\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\3\2\7")
        buf.write("\5\2\13\f\17\17\"\"\3\2\62;\3\2$$\4\2C\\c|\5\2\62;C\\")
        buf.write("c|\u01f7\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\3\u0087\3\2\2")
        buf.write("\2\5\u0089\3\2\2\2\7\u008b\3\2\2\2\t\u008d\3\2\2\2\13")
        buf.write("\u008f\3\2\2\2\r\u0091\3\2\2\2\17\u0093\3\2\2\2\21\u0095")
        buf.write("\3\2\2\2\23\u0097\3\2\2\2\25\u009a\3\2\2\2\27\u009d\3")
        buf.write("\2\2\2\31\u009f\3\2\2\2\33\u00a1\3\2\2\2\35\u00a4\3\2")
        buf.write("\2\2\37\u00a7\3\2\2\2!\u00a9\3\2\2\2#\u00ab\3\2\2\2%\u00ad")
        buf.write("\3\2\2\2\'\u00af\3\2\2\2)\u00b1\3\2\2\2+\u00b4\3\2\2\2")
        buf.write("-\u00ba\3\2\2\2/\u00bf\3\2\2\2\61\u00c5\3\2\2\2\63\u00ce")
        buf.write("\3\2\2\2\65\u00d3\3\2\2\2\67\u00da\3\2\2\29\u00e0\3\2")
        buf.write("\2\2;\u00e7\3\2\2\2=\u00ef\3\2\2\2?\u00f4\3\2\2\2A\u00f9")
        buf.write("\3\2\2\2C\u00ff\3\2\2\2E\u0106\3\2\2\2G\u0108\3\2\2\2")
        buf.write("I\u010f\3\2\2\2K\u0113\3\2\2\2M\u0116\3\2\2\2O\u0119\3")
        buf.write("\2\2\2Q\u011f\3\2\2\2S\u0128\3\2\2\2U\u012e\3\2\2\2W\u0134")
        buf.write("\3\2\2\2Y\u013c\3\2\2\2[\u0146\3\2\2\2]\u014f\3\2\2\2")
        buf.write("_\u0155\3\2\2\2a\u015b\3\2\2\2c\u0162\3\2\2\2e\u0169\3")
        buf.write("\2\2\2g\u0172\3\2\2\2i\u017b\3\2\2\2k\u017f\3\2\2\2m\u0182")
        buf.write("\3\2\2\2o\u0187\3\2\2\2q\u018d\3\2\2\2s\u0192\3\2\2\2")
        buf.write("u\u019a\3\2\2\2w\u01a1\3\2\2\2y\u01aa\3\2\2\2{\u01b3\3")
        buf.write("\2\2\2}\u01c6\3\2\2\2\177\u01c8\3\2\2\2\u0081\u01d5\3")
        buf.write("\2\2\2\u0083\u01e1\3\2\2\2\u0085\u01ea\3\2\2\2\u0087\u0088")
        buf.write("\7=\2\2\u0088\4\3\2\2\2\u0089\u008a\7*\2\2\u008a\6\3\2")
        buf.write("\2\2\u008b\u008c\7.\2\2\u008c\b\3\2\2\2\u008d\u008e\7")
        buf.write("+\2\2\u008e\n\3\2\2\2\u008f\u0090\7}\2\2\u0090\f\3\2\2")
        buf.write("\2\u0091\u0092\7\177\2\2\u0092\16\3\2\2\2\u0093\u0094")
        buf.write("\7(\2\2\u0094\20\3\2\2\2\u0095\u0096\7~\2\2\u0096\22\3")
        buf.write("\2\2\2\u0097\u0098\7?\2\2\u0098\u0099\7?\2\2\u0099\24")
        buf.write("\3\2\2\2\u009a\u009b\7#\2\2\u009b\u009c\7?\2\2\u009c\26")
        buf.write("\3\2\2\2\u009d\u009e\7@\2\2\u009e\30\3\2\2\2\u009f\u00a0")
        buf.write("\7>\2\2\u00a0\32\3\2\2\2\u00a1\u00a2\7@\2\2\u00a2\u00a3")
        buf.write("\7?\2\2\u00a3\34\3\2\2\2\u00a4\u00a5\7>\2\2\u00a5\u00a6")
        buf.write("\7?\2\2\u00a6\36\3\2\2\2\u00a7\u00a8\7-\2\2\u00a8 \3\2")
        buf.write("\2\2\u00a9\u00aa\7/\2\2\u00aa\"\3\2\2\2\u00ab\u00ac\7")
        buf.write(",\2\2\u00ac$\3\2\2\2\u00ad\u00ae\7\61\2\2\u00ae&\3\2\2")
        buf.write("\2\u00af\u00b0\7\'\2\2\u00b0(\3\2\2\2\u00b1\u00b2\7#\2")
        buf.write("\2\u00b2*\3\2\2\2\u00b3\u00b5\t\2\2\2\u00b4\u00b3\3\2")
        buf.write("\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\b\26\2\2\u00b9")
        buf.write(",\3\2\2\2\u00ba\u00bb\7t\2\2\u00bb\u00bc\7q\2\2\u00bc")
        buf.write("\u00bd\7l\2\2\u00bd\u00be\7q\2\2\u00be.\3\2\2\2\u00bf")
        buf.write("\u00c0\7x\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7t\2\2\u00c2")
        buf.write("\u00c3\7f\2\2\u00c3\u00c4\7g\2\2\u00c4\60\3\2\2\2\u00c5")
        buf.write("\u00c6\7c\2\2\u00c6\u00c7\7o\2\2\u00c7\u00c8\7c\2\2\u00c8")
        buf.write("\u00c9\7t\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7n\2\2\u00cb")
        buf.write("\u00cc\7n\2\2\u00cc\u00cd\7q\2\2\u00cd\62\3\2\2\2\u00ce")
        buf.write("\u00cf\7c\2\2\u00cf\u00d0\7|\2\2\u00d0\u00d1\7w\2\2\u00d1")
        buf.write("\u00d2\7n\2\2\u00d2\64\3\2\2\2\u00d3\u00d4\7d\2\2\u00d4")
        buf.write("\u00d5\7n\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7p\2\2\u00d7")
        buf.write("\u00d8\7e\2\2\u00d8\u00d9\7q\2\2\u00d9\66\3\2\2\2\u00da")
        buf.write("\u00db\7p\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd\7i\2\2\u00dd")
        buf.write("\u00de\7t\2\2\u00de\u00df\7q\2\2\u00df8\3\2\2\2\u00e0")
        buf.write("\u00e1\7o\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7t\2\2\u00e3")
        buf.write("\u00e4\7c\2\2\u00e4\u00e5\7f\2\2\u00e5\u00e6\7q\2\2\u00e6")
        buf.write(":\3\2\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7c\2\2\u00e9")
        buf.write("\u00ea\7t\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7p\2\2\u00ec")
        buf.write("\u00ed\7l\2\2\u00ed\u00ee\7c\2\2\u00ee<\3\2\2\2\u00ef")
        buf.write("\u00f0\7e\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7h\2\2\u00f2")
        buf.write("\u00f3\7g\2\2\u00f3>\3\2\2\2\u00f4\u00f5\7i\2\2\u00f5")
        buf.write("\u00f6\7t\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7u\2\2\u00f8")
        buf.write("@\3\2\2\2\u00f9\u00fa\7e\2\2\u00fa\u00fb\7q\2\2\u00fb")
        buf.write("\u00fc\7n\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7t\2\2\u00fe")
        buf.write("B\3\2\2\2\u00ff\u0100\7n\2\2\u0100\u0101\7k\2\2\u0101")
        buf.write("\u0102\7g\2\2\u0102\u0103\7p\2\2\u0103\u0104\7|\2\2\u0104")
        buf.write("\u0105\7q\2\2\u0105D\3\2\2\2\u0106\u0107\7?\2\2\u0107")
        buf.write("F\3\2\2\2\u0108\u0109\7v\2\2\u0109\u010a\7c\2\2\u010a")
        buf.write("\u010b\7o\2\2\u010b\u010c\7c\2\2\u010c\u010d\7p\2\2\u010d")
        buf.write("\u010e\7q\2\2\u010eH\3\2\2\2\u010f\u0110\7r\2\2\u0110")
        buf.write("\u0111\7q\2\2\u0111\u0112\7t\2\2\u0112J\3\2\2\2\u0113")
        buf.write("\u0114\7f\2\2\u0114\u0115\7g\2\2\u0115L\3\2\2\2\u0116")
        buf.write("\u0117\7g\2\2\u0117\u0118\7p\2\2\u0118N\3\2\2\2\u0119")
        buf.write("\u011a\7o\2\2\u011a\u011b\7q\2\2\u011b\u011c\7x\2\2\u011c")
        buf.write("\u011d\7g\2\2\u011d\u011e\7t\2\2\u011eP\3\2\2\2\u011f")
        buf.write("\u0120\7c\2\2\u0120\u0121\7f\2\2\u0121\u0122\7g\2\2\u0122")
        buf.write("\u0123\7n\2\2\u0123\u0124\7c\2\2\u0124\u0125\7p\2\2\u0125")
        buf.write("\u0126\7v\2\2\u0126\u0127\7g\2\2\u0127R\3\2\2\2\u0128")
        buf.write("\u0129\7c\2\2\u0129\u012a\7v\2\2\u012a\u012b\7t\2\2\u012b")
        buf.write("\u012c\7c\2\2\u012c\u012d\7u\2\2\u012dT\3\2\2\2\u012e")
        buf.write("\u012f\7i\2\2\u012f\u0130\7k\2\2\u0130\u0131\7t\2\2\u0131")
        buf.write("\u0132\7c\2\2\u0132\u0133\7t\2\2\u0133V\3\2\2\2\u0134")
        buf.write("\u0135\7f\2\2\u0135\u0136\7g\2\2\u0136\u0137\7t\2\2\u0137")
        buf.write("\u0138\7g\2\2\u0138\u0139\7e\2\2\u0139\u013a\7j\2\2\u013a")
        buf.write("\u013b\7c\2\2\u013bX\3\2\2\2\u013c\u013d\7k\2\2\u013d")
        buf.write("\u013e\7|\2\2\u013e\u013f\7s\2\2\u013f\u0140\7w\2\2\u0140")
        buf.write("\u0141\7k\2\2\u0141\u0142\7g\2\2\u0142\u0143\7t\2\2\u0143")
        buf.write("\u0144\7f\2\2\u0144\u0145\7c\2\2\u0145Z\3\2\2\2\u0146")
        buf.write("\u0147\7n\2\2\u0147\u0148\7g\2\2\u0148\u0149\7x\2\2\u0149")
        buf.write("\u014a\7c\2\2\u014a\u014b\7p\2\2\u014b\u014c\7v\2\2\u014c")
        buf.write("\u014d\7c\2\2\u014d\u014e\7t\2\2\u014e\\\3\2\2\2\u014f")
        buf.write("\u0150\7d\2\2\u0150\u0151\7c\2\2\u0151\u0152\7l\2\2\u0152")
        buf.write("\u0153\7c\2\2\u0153\u0154\7t\2\2\u0154^\3\2\2\2\u0155")
        buf.write("\u0156\7r\2\2\u0156\u0157\7n\2\2\u0157\u0158\7w\2\2\u0158")
        buf.write("\u0159\7o\2\2\u0159\u015a\7c\2\2\u015a`\3\2\2\2\u015b")
        buf.write("\u015c\7f\2\2\u015c\u015d\7k\2\2\u015d\u015e\7d\2\2\u015e")
        buf.write("\u015f\7w\2\2\u015f\u0160\7l\2\2\u0160\u0161\7q\2\2\u0161")
        buf.write("b\3\2\2\2\u0162\u0163\7f\2\2\u0163\u0164\7q\2\2\u0164")
        buf.write("\u0165\7t\2\2\u0165\u0166\7o\2\2\u0166\u0167\7k\2\2\u0167")
        buf.write("\u0168\7t\2\2\u0168d\3\2\2\2\u0169\u016a\7o\2\2\u016a")
        buf.write("\u016b\7k\2\2\u016b\u016c\7g\2\2\u016c\u016d\7p\2\2\u016d")
        buf.write("\u016e\7v\2\2\u016e\u016f\7t\2\2\u016f\u0170\7c\2\2\u0170")
        buf.write("\u0171\7u\2\2\u0171f\3\2\2\2\u0172\u0173\7t\2\2\u0173")
        buf.write("\u0174\7g\2\2\u0174\u0175\7i\2\2\u0175\u0176\7t\2\2\u0176")
        buf.write("\u0177\7g\2\2\u0177\u0178\7u\2\2\u0178\u0179\7c\2\2\u0179")
        buf.write("\u017a\7t\2\2\u017ah\3\2\2\2\u017b\u017c\7s\2\2\u017c")
        buf.write("\u017d\7w\2\2\u017d\u017e\7g\2\2\u017ej\3\2\2\2\u017f")
        buf.write("\u0180\7u\2\2\u0180\u0181\7k\2\2\u0181l\3\2\2\2\u0182")
        buf.write("\u0183\7u\2\2\u0183\u0184\7k\2\2\u0184\u0185\7p\2\2\u0185")
        buf.write("\u0186\7q\2\2\u0186n\3\2\2\2\u0187\u0188\7v\2\2\u0188")
        buf.write("\u0189\7g\2\2\u0189\u018a\7z\2\2\u018a\u018b\7v\2\2\u018b")
        buf.write("\u018c\7q\2\2\u018cp\3\2\2\2\u018d\u018e\7n\2\2\u018e")
        buf.write("\u018f\7g\2\2\u018f\u0190\7g\2\2\u0190\u0191\7t\2\2\u0191")
        buf.write("r\3\2\2\2\u0192\u0193\7d\2\2\u0193\u0194\7q\2\2\u0194")
        buf.write("\u0195\7n\2\2\u0195\u0196\7g\2\2\u0196\u0197\7c\2\2\u0197")
        buf.write("\u0198\7p\2\2\u0198\u0199\7q\2\2\u0199t\3\2\2\2\u019a")
        buf.write("\u019b\7p\2\2\u019b\u019c\7w\2\2\u019c\u019d\7o\2\2\u019d")
        buf.write("\u019e\7g\2\2\u019e\u019f\7t\2\2\u019f\u01a0\7q\2\2\u01a0")
        buf.write("v\3\2\2\2\u01a1\u01a2\7g\2\2\u01a2\u01a3\7u\2\2\u01a3")
        buf.write("\u01a4\7e\2\2\u01a4\u01a5\7t\2\2\u01a5\u01a6\7k\2\2\u01a6")
        buf.write("\u01a7\7d\2\2\u01a7\u01a8\7k\2\2\u01a8\u01a9\7t\2\2\u01a9")
        buf.write("x\3\2\2\2\u01aa\u01ab\7k\2\2\u01ab\u01ac\7o\2\2\u01ac")
        buf.write("\u01ad\7r\2\2\u01ad\u01ae\7t\2\2\u01ae\u01af\7k\2\2\u01af")
        buf.write("\u01b0\7o\2\2\u01b0\u01b1\7k\2\2\u01b1\u01b2\7t\2\2\u01b2")
        buf.write("z\3\2\2\2\u01b3\u01b4\7p\2\2\u01b4\u01b5\7c\2\2\u01b5")
        buf.write("\u01b6\7f\2\2\u01b6\u01b7\7c\2\2\u01b7|\3\2\2\2\u01b8")
        buf.write("\u01b9\7x\2\2\u01b9\u01ba\7g\2\2\u01ba\u01bb\7t\2\2\u01bb")
        buf.write("\u01bc\7f\2\2\u01bc\u01bd\7c\2\2\u01bd\u01be\7f\2\2\u01be")
        buf.write("\u01bf\7g\2\2\u01bf\u01c0\7t\2\2\u01c0\u01c7\7q\2\2\u01c1")
        buf.write("\u01c2\7h\2\2\u01c2\u01c3\7c\2\2\u01c3\u01c4\7n\2\2\u01c4")
        buf.write("\u01c5\7u\2\2\u01c5\u01c7\7q\2\2\u01c6\u01b8\3\2\2\2\u01c6")
        buf.write("\u01c1\3\2\2\2\u01c7~\3\2\2\2\u01c8\u01c9\7o\2\2\u01c9")
        buf.write("\u01ca\7q\2\2\u01ca\u01cb\7f\2\2\u01cb\u01cc\7k\2\2\u01cc")
        buf.write("\u01cd\7h\2\2\u01cd\u01ce\7k\2\2\u01ce\u01cf\7e\2\2\u01cf")
        buf.write("\u01d0\7c\2\2\u01d0\u01d1\7d\2\2\u01d1\u01d2\7n\2\2\u01d2")
        buf.write("\u01d3\7g\2\2\u01d3\u0080\3\2\2\2\u01d4\u01d6\t\3\2\2")
        buf.write("\u01d5\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d5\3")
        buf.write("\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01df\3\2\2\2\u01d9\u01db")
        buf.write("\7\60\2\2\u01da\u01dc\t\3\2\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u01e0\3\2\2\2\u01df\u01d9\3\2\2\2\u01df\u01e0\3")
        buf.write("\2\2\2\u01e0\u0082\3\2\2\2\u01e1\u01e5\7$\2\2\u01e2\u01e4")
        buf.write("\n\4\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5")
        buf.write("\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e8\3\2\2\2")
        buf.write("\u01e7\u01e5\3\2\2\2\u01e8\u01e9\7$\2\2\u01e9\u0084\3")
        buf.write("\2\2\2\u01ea\u01ee\t\5\2\2\u01eb\u01ed\t\6\2\2\u01ec\u01eb")
        buf.write("\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u0086\3\2\2\2\u01f0\u01ee\3\2\2\2")
        buf.write("\n\2\u00b6\u01c6\u01d7\u01dd\u01df\u01e5\u01ee\3\b\2\2")
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
    WS = 21
    ROJO = 22
    VERDE = 23
    AMARILLO = 24
    AZUL = 25
    BLANCO = 26
    NEGRO = 27
    MORADO = 28
    NARANJA = 29
    CAFE = 30
    GRIS = 31
    COLOR = 32
    LIENZO = 33
    EQUALS = 34
    TAMANO = 35
    POR = 36
    DE = 37
    EN = 38
    MOVER = 39
    ADELANTE = 40
    ATRAS = 41
    GIRAR = 42
    DERECHA = 43
    IZQUIERDA = 44
    LEVANTAR = 45
    BAJAR = 46
    PLUMA = 47
    DIBUJO = 48
    DORMIR = 49
    MIENTRAS = 50
    REGRESAR = 51
    QUE = 52
    SI = 53
    SINO = 54
    TEXTO = 55
    LEER = 56
    BOLEANO = 57
    NUMERO = 58
    ESCRIBIR = 59
    IMPRIMIR = 60
    NADA = 61
    BOOLEAN_CONSTANT = 62
    MODIFICABLE = 63
    NUMERIC_CONSTANT = 64
    STRING_CONSTANT = 65
    ID = 66

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'('", "','", "')'", "'{'", "'}'", "'&'", "'|'", "'=='", 
            "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'rojo'", "'verde'", "'amarillo'", "'azul'", "'blanco'", 
            "'negro'", "'morado'", "'naranja'", "'cafe'", "'gris'", "'color'", 
            "'lienzo'", "'='", "'tamano'", "'por'", "'de'", "'en'", "'mover'", 
            "'adelante'", "'atras'", "'girar'", "'derecha'", "'izquierda'", 
            "'levantar'", "'bajar'", "'pluma'", "'dibujo'", "'dormir'", 
            "'mientras'", "'regresar'", "'que'", "'si'", "'sino'", "'texto'", 
            "'leer'", "'boleano'", "'numero'", "'escribir'", "'imprimir'", 
            "'nada'", "'modificable'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", "NEGRO", 
            "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", "LIENZO", "EQUALS", 
            "TAMANO", "POR", "DE", "EN", "MOVER", "ADELANTE", "ATRAS", "GIRAR", 
            "DERECHA", "IZQUIERDA", "LEVANTAR", "BAJAR", "PLUMA", "DIBUJO", 
            "DORMIR", "MIENTRAS", "REGRESAR", "QUE", "SI", "SINO", "TEXTO", 
            "LEER", "BOLEANO", "NUMERO", "ESCRIBIR", "IMPRIMIR", "NADA", 
            "BOOLEAN_CONSTANT", "MODIFICABLE", "NUMERIC_CONSTANT", "STRING_CONSTANT", 
            "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "WS", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", "NEGRO", 
                  "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", "LIENZO", 
                  "EQUALS", "TAMANO", "POR", "DE", "EN", "MOVER", "ADELANTE", 
                  "ATRAS", "GIRAR", "DERECHA", "IZQUIERDA", "LEVANTAR", 
                  "BAJAR", "PLUMA", "DIBUJO", "DORMIR", "MIENTRAS", "REGRESAR", 
                  "QUE", "SI", "SINO", "TEXTO", "LEER", "BOLEANO", "NUMERO", 
                  "ESCRIBIR", "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", "MODIFICABLE", 
                  "NUMERIC_CONSTANT", "STRING_CONSTANT", "ID" ]

    grammarFileName = "Lienzo.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


