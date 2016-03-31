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


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2D")
        buf.write("\u01ef\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38")
        buf.write("\38\38\38\38\38\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u01c5\n?\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3A\6A\u01d4\nA\rA\16A\u01d5\3A\3A")
        buf.write("\6A\u01da\nA\rA\16A\u01db\5A\u01de\nA\3B\3B\7B\u01e2\n")
        buf.write("B\fB\16B\u01e5\13B\3B\3B\3C\3C\7C\u01eb\nC\fC\16C\u01ee")
        buf.write("\13C\2\2D\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\3\2\7")
        buf.write("\5\2\13\f\17\17\"\"\3\2\62;\3\2$$\4\2C\\c|\5\2\62;C\\")
        buf.write("c|\u01f5\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
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
        buf.write("-\u00ba\3\2\2\2/\u00c1\3\2\2\2\61\u00c6\3\2\2\2\63\u00cc")
        buf.write("\3\2\2\2\65\u00d5\3\2\2\2\67\u00da\3\2\2\29\u00e1\3\2")
        buf.write("\2\2;\u00e7\3\2\2\2=\u00ee\3\2\2\2?\u00f6\3\2\2\2A\u00fb")
        buf.write("\3\2\2\2C\u0100\3\2\2\2E\u0106\3\2\2\2G\u010d\3\2\2\2")
        buf.write("I\u010f\3\2\2\2K\u0116\3\2\2\2M\u011a\3\2\2\2O\u011d\3")
        buf.write("\2\2\2Q\u0120\3\2\2\2S\u0126\3\2\2\2U\u012f\3\2\2\2W\u0135")
        buf.write("\3\2\2\2Y\u013b\3\2\2\2[\u0143\3\2\2\2]\u014d\3\2\2\2")
        buf.write("_\u0156\3\2\2\2a\u015c\3\2\2\2c\u0162\3\2\2\2e\u0169\3")
        buf.write("\2\2\2g\u0170\3\2\2\2i\u0179\3\2\2\2k\u017d\3\2\2\2m\u0180")
        buf.write("\3\2\2\2o\u0185\3\2\2\2q\u018b\3\2\2\2s\u0190\3\2\2\2")
        buf.write("u\u0198\3\2\2\2w\u019f\3\2\2\2y\u01a8\3\2\2\2{\u01b1\3")
        buf.write("\2\2\2}\u01c4\3\2\2\2\177\u01c6\3\2\2\2\u0081\u01d3\3")
        buf.write("\2\2\2\u0083\u01df\3\2\2\2\u0085\u01e8\3\2\2\2\u0087\u0088")
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
        buf.write(",\3\2\2\2\u00ba\u00bb\7i\2\2\u00bb\u00bc\7n\2\2\u00bc")
        buf.write("\u00bd\7q\2\2\u00bd\u00be\7d\2\2\u00be\u00bf\7c\2\2\u00bf")
        buf.write("\u00c0\7n\2\2\u00c0.\3\2\2\2\u00c1\u00c2\7t\2\2\u00c2")
        buf.write("\u00c3\7q\2\2\u00c3\u00c4\7l\2\2\u00c4\u00c5\7q\2\2\u00c5")
        buf.write("\60\3\2\2\2\u00c6\u00c7\7x\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write("\u00c9\7t\2\2\u00c9\u00ca\7f\2\2\u00ca\u00cb\7g\2\2\u00cb")
        buf.write("\62\3\2\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7o\2\2\u00ce")
        buf.write("\u00cf\7c\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1\7k\2\2\u00d1")
        buf.write("\u00d2\7n\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7q\2\2\u00d4")
        buf.write("\64\3\2\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7|\2\2\u00d7")
        buf.write("\u00d8\7w\2\2\u00d8\u00d9\7n\2\2\u00d9\66\3\2\2\2\u00da")
        buf.write("\u00db\7d\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7c\2\2\u00dd")
        buf.write("\u00de\7p\2\2\u00de\u00df\7e\2\2\u00df\u00e0\7q\2\2\u00e0")
        buf.write("8\3\2\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7g\2\2\u00e3")
        buf.write("\u00e4\7i\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7q\2\2\u00e6")
        buf.write(":\3\2\2\2\u00e7\u00e8\7o\2\2\u00e8\u00e9\7q\2\2\u00e9")
        buf.write("\u00ea\7t\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7f\2\2\u00ec")
        buf.write("\u00ed\7q\2\2\u00ed<\3\2\2\2\u00ee\u00ef\7p\2\2\u00ef")
        buf.write("\u00f0\7c\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7c\2\2\u00f2")
        buf.write("\u00f3\7p\2\2\u00f3\u00f4\7l\2\2\u00f4\u00f5\7c\2\2\u00f5")
        buf.write(">\3\2\2\2\u00f6\u00f7\7e\2\2\u00f7\u00f8\7c\2\2\u00f8")
        buf.write("\u00f9\7h\2\2\u00f9\u00fa\7g\2\2\u00fa@\3\2\2\2\u00fb")
        buf.write("\u00fc\7i\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7k\2\2\u00fe")
        buf.write("\u00ff\7u\2\2\u00ffB\3\2\2\2\u0100\u0101\7e\2\2\u0101")
        buf.write("\u0102\7q\2\2\u0102\u0103\7n\2\2\u0103\u0104\7q\2\2\u0104")
        buf.write("\u0105\7t\2\2\u0105D\3\2\2\2\u0106\u0107\7n\2\2\u0107")
        buf.write("\u0108\7k\2\2\u0108\u0109\7g\2\2\u0109\u010a\7p\2\2\u010a")
        buf.write("\u010b\7|\2\2\u010b\u010c\7q\2\2\u010cF\3\2\2\2\u010d")
        buf.write("\u010e\7?\2\2\u010eH\3\2\2\2\u010f\u0110\7v\2\2\u0110")
        buf.write("\u0111\7c\2\2\u0111\u0112\7o\2\2\u0112\u0113\7c\2\2\u0113")
        buf.write("\u0114\7p\2\2\u0114\u0115\7q\2\2\u0115J\3\2\2\2\u0116")
        buf.write("\u0117\7r\2\2\u0117\u0118\7q\2\2\u0118\u0119\7t\2\2\u0119")
        buf.write("L\3\2\2\2\u011a\u011b\7f\2\2\u011b\u011c\7g\2\2\u011c")
        buf.write("N\3\2\2\2\u011d\u011e\7g\2\2\u011e\u011f\7p\2\2\u011f")
        buf.write("P\3\2\2\2\u0120\u0121\7o\2\2\u0121\u0122\7q\2\2\u0122")
        buf.write("\u0123\7x\2\2\u0123\u0124\7g\2\2\u0124\u0125\7t\2\2\u0125")
        buf.write("R\3\2\2\2\u0126\u0127\7c\2\2\u0127\u0128\7f\2\2\u0128")
        buf.write("\u0129\7g\2\2\u0129\u012a\7n\2\2\u012a\u012b\7c\2\2\u012b")
        buf.write("\u012c\7p\2\2\u012c\u012d\7v\2\2\u012d\u012e\7g\2\2\u012e")
        buf.write("T\3\2\2\2\u012f\u0130\7c\2\2\u0130\u0131\7v\2\2\u0131")
        buf.write("\u0132\7t\2\2\u0132\u0133\7c\2\2\u0133\u0134\7u\2\2\u0134")
        buf.write("V\3\2\2\2\u0135\u0136\7i\2\2\u0136\u0137\7k\2\2\u0137")
        buf.write("\u0138\7t\2\2\u0138\u0139\7c\2\2\u0139\u013a\7t\2\2\u013a")
        buf.write("X\3\2\2\2\u013b\u013c\7f\2\2\u013c\u013d\7g\2\2\u013d")
        buf.write("\u013e\7t\2\2\u013e\u013f\7g\2\2\u013f\u0140\7e\2\2\u0140")
        buf.write("\u0141\7j\2\2\u0141\u0142\7c\2\2\u0142Z\3\2\2\2\u0143")
        buf.write("\u0144\7k\2\2\u0144\u0145\7|\2\2\u0145\u0146\7s\2\2\u0146")
        buf.write("\u0147\7w\2\2\u0147\u0148\7k\2\2\u0148\u0149\7g\2\2\u0149")
        buf.write("\u014a\7t\2\2\u014a\u014b\7f\2\2\u014b\u014c\7c\2\2\u014c")
        buf.write("\\\3\2\2\2\u014d\u014e\7n\2\2\u014e\u014f\7g\2\2\u014f")
        buf.write("\u0150\7x\2\2\u0150\u0151\7c\2\2\u0151\u0152\7p\2\2\u0152")
        buf.write("\u0153\7v\2\2\u0153\u0154\7c\2\2\u0154\u0155\7t\2\2\u0155")
        buf.write("^\3\2\2\2\u0156\u0157\7d\2\2\u0157\u0158\7c\2\2\u0158")
        buf.write("\u0159\7l\2\2\u0159\u015a\7c\2\2\u015a\u015b\7t\2\2\u015b")
        buf.write("`\3\2\2\2\u015c\u015d\7r\2\2\u015d\u015e\7n\2\2\u015e")
        buf.write("\u015f\7w\2\2\u015f\u0160\7o\2\2\u0160\u0161\7c\2\2\u0161")
        buf.write("b\3\2\2\2\u0162\u0163\7f\2\2\u0163\u0164\7k\2\2\u0164")
        buf.write("\u0165\7d\2\2\u0165\u0166\7w\2\2\u0166\u0167\7l\2\2\u0167")
        buf.write("\u0168\7q\2\2\u0168d\3\2\2\2\u0169\u016a\7f\2\2\u016a")
        buf.write("\u016b\7q\2\2\u016b\u016c\7t\2\2\u016c\u016d\7o\2\2\u016d")
        buf.write("\u016e\7k\2\2\u016e\u016f\7t\2\2\u016ff\3\2\2\2\u0170")
        buf.write("\u0171\7o\2\2\u0171\u0172\7k\2\2\u0172\u0173\7g\2\2\u0173")
        buf.write("\u0174\7p\2\2\u0174\u0175\7v\2\2\u0175\u0176\7t\2\2\u0176")
        buf.write("\u0177\7c\2\2\u0177\u0178\7u\2\2\u0178h\3\2\2\2\u0179")
        buf.write("\u017a\7s\2\2\u017a\u017b\7w\2\2\u017b\u017c\7g\2\2\u017c")
        buf.write("j\3\2\2\2\u017d\u017e\7u\2\2\u017e\u017f\7k\2\2\u017f")
        buf.write("l\3\2\2\2\u0180\u0181\7u\2\2\u0181\u0182\7k\2\2\u0182")
        buf.write("\u0183\7p\2\2\u0183\u0184\7q\2\2\u0184n\3\2\2\2\u0185")
        buf.write("\u0186\7v\2\2\u0186\u0187\7g\2\2\u0187\u0188\7z\2\2\u0188")
        buf.write("\u0189\7v\2\2\u0189\u018a\7q\2\2\u018ap\3\2\2\2\u018b")
        buf.write("\u018c\7n\2\2\u018c\u018d\7g\2\2\u018d\u018e\7g\2\2\u018e")
        buf.write("\u018f\7t\2\2\u018fr\3\2\2\2\u0190\u0191\7d\2\2\u0191")
        buf.write("\u0192\7q\2\2\u0192\u0193\7n\2\2\u0193\u0194\7g\2\2\u0194")
        buf.write("\u0195\7c\2\2\u0195\u0196\7p\2\2\u0196\u0197\7q\2\2\u0197")
        buf.write("t\3\2\2\2\u0198\u0199\7p\2\2\u0199\u019a\7w\2\2\u019a")
        buf.write("\u019b\7o\2\2\u019b\u019c\7g\2\2\u019c\u019d\7t\2\2\u019d")
        buf.write("\u019e\7q\2\2\u019ev\3\2\2\2\u019f\u01a0\7g\2\2\u01a0")
        buf.write("\u01a1\7u\2\2\u01a1\u01a2\7e\2\2\u01a2\u01a3\7t\2\2\u01a3")
        buf.write("\u01a4\7k\2\2\u01a4\u01a5\7d\2\2\u01a5\u01a6\7k\2\2\u01a6")
        buf.write("\u01a7\7t\2\2\u01a7x\3\2\2\2\u01a8\u01a9\7k\2\2\u01a9")
        buf.write("\u01aa\7o\2\2\u01aa\u01ab\7r\2\2\u01ab\u01ac\7t\2\2\u01ac")
        buf.write("\u01ad\7k\2\2\u01ad\u01ae\7o\2\2\u01ae\u01af\7k\2\2\u01af")
        buf.write("\u01b0\7t\2\2\u01b0z\3\2\2\2\u01b1\u01b2\7p\2\2\u01b2")
        buf.write("\u01b3\7c\2\2\u01b3\u01b4\7f\2\2\u01b4\u01b5\7c\2\2\u01b5")
        buf.write("|\3\2\2\2\u01b6\u01b7\7x\2\2\u01b7\u01b8\7g\2\2\u01b8")
        buf.write("\u01b9\7t\2\2\u01b9\u01ba\7f\2\2\u01ba\u01bb\7c\2\2\u01bb")
        buf.write("\u01bc\7f\2\2\u01bc\u01bd\7g\2\2\u01bd\u01be\7t\2\2\u01be")
        buf.write("\u01c5\7q\2\2\u01bf\u01c0\7h\2\2\u01c0\u01c1\7c\2\2\u01c1")
        buf.write("\u01c2\7n\2\2\u01c2\u01c3\7u\2\2\u01c3\u01c5\7q\2\2\u01c4")
        buf.write("\u01b6\3\2\2\2\u01c4\u01bf\3\2\2\2\u01c5~\3\2\2\2\u01c6")
        buf.write("\u01c7\7o\2\2\u01c7\u01c8\7q\2\2\u01c8\u01c9\7f\2\2\u01c9")
        buf.write("\u01ca\7k\2\2\u01ca\u01cb\7h\2\2\u01cb\u01cc\7k\2\2\u01cc")
        buf.write("\u01cd\7e\2\2\u01cd\u01ce\7c\2\2\u01ce\u01cf\7d\2\2\u01cf")
        buf.write("\u01d0\7n\2\2\u01d0\u01d1\7g\2\2\u01d1\u0080\3\2\2\2\u01d2")
        buf.write("\u01d4\t\3\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2")
        buf.write("\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01dd\3")
        buf.write("\2\2\2\u01d7\u01d9\7\60\2\2\u01d8\u01da\t\3\2\2\u01d9")
        buf.write("\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01d9\3\2\2\2")
        buf.write("\u01db\u01dc\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd\u01d7\3")
        buf.write("\2\2\2\u01dd\u01de\3\2\2\2\u01de\u0082\3\2\2\2\u01df\u01e3")
        buf.write("\7$\2\2\u01e0\u01e2\n\4\2\2\u01e1\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e4\u01e6\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e7\7")
        buf.write("$\2\2\u01e7\u0084\3\2\2\2\u01e8\u01ec\t\5\2\2\u01e9\u01eb")
        buf.write("\t\6\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec")
        buf.write("\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u0086\3\2\2\2")
        buf.write("\u01ee\u01ec\3\2\2\2\n\2\u00b6\u01c4\u01d5\u01db\u01dd")
        buf.write("\u01e3\u01ec\3\b\2\2")
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
    GLOBAL = 22
    ROJO = 23
    VERDE = 24
    AMARILLO = 25
    AZUL = 26
    BLANCO = 27
    NEGRO = 28
    MORADO = 29
    NARANJA = 30
    CAFE = 31
    GRIS = 32
    COLOR = 33
    LIENZO = 34
    EQUALS = 35
    TAMANO = 36
    POR = 37
    DE = 38
    EN = 39
    MOVER = 40
    ADELANTE = 41
    ATRAS = 42
    GIRAR = 43
    DERECHA = 44
    IZQUIERDA = 45
    LEVANTAR = 46
    BAJAR = 47
    PLUMA = 48
    DIBUJO = 49
    DORMIR = 50
    MIENTRAS = 51
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
            "'%'", "'!'", "'global'", "'rojo'", "'verde'", "'amarillo'", 
            "'azul'", "'blanco'", "'negro'", "'morado'", "'naranja'", "'cafe'", 
            "'gris'", "'color'", "'lienzo'", "'='", "'tamano'", "'por'", 
            "'de'", "'en'", "'mover'", "'adelante'", "'atras'", "'girar'", 
            "'derecha'", "'izquierda'", "'levantar'", "'bajar'", "'pluma'", 
            "'dibujo'", "'dormir'", "'mientras'", "'que'", "'si'", "'sino'", 
            "'texto'", "'leer'", "'boleano'", "'numero'", "'escribir'", 
            "'imprimir'", "'nada'", "'modificable'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "GLOBAL", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", 
            "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", "LIENZO", 
            "EQUALS", "TAMANO", "POR", "DE", "EN", "MOVER", "ADELANTE", 
            "ATRAS", "GIRAR", "DERECHA", "IZQUIERDA", "LEVANTAR", "BAJAR", 
            "PLUMA", "DIBUJO", "DORMIR", "MIENTRAS", "QUE", "SI", "SINO", 
            "TEXTO", "LEER", "BOLEANO", "NUMERO", "ESCRIBIR", "IMPRIMIR", 
            "NADA", "BOOLEAN_CONSTANT", "MODIFICABLE", "NUMERIC_CONSTANT", 
            "STRING_CONSTANT", "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "WS", "GLOBAL", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", 
                  "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", 
                  "LIENZO", "EQUALS", "TAMANO", "POR", "DE", "EN", "MOVER", 
                  "ADELANTE", "ATRAS", "GIRAR", "DERECHA", "IZQUIERDA", 
                  "LEVANTAR", "BAJAR", "PLUMA", "DIBUJO", "DORMIR", "MIENTRAS", 
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


