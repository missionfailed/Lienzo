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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2:")
        buf.write("\u0192\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\6\26\u00a1\n\26\r")
        buf.write("\26\16\26\u00a2\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#")
        buf.write("\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3-\3")
        buf.write(".\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\5\65\u0168\n\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\7\67\u0178\n\67\f\67\16\67\u017b\13\67\3\67\3\67\6\67")
        buf.write("\u017f\n\67\r\67\16\67\u0180\5\67\u0183\n\67\38\38\78")
        buf.write("\u0187\n8\f8\168\u018a\138\38\38\39\69\u018f\n9\r9\16")
        buf.write("9\u0190\2\2:\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66")
        buf.write("k\67m8o9q:\3\2\7\5\2\13\f\17\17\"\"\3\2\63;\3\2\62;\3")
        buf.write("\2$$\4\2C\\c|\u0198\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\3s\3\2\2\2\5u\3\2\2\2\7w\3")
        buf.write("\2\2\2\ty\3\2\2\2\13{\3\2\2\2\r}\3\2\2\2\17\177\3\2\2")
        buf.write("\2\21\u0081\3\2\2\2\23\u0083\3\2\2\2\25\u0086\3\2\2\2")
        buf.write("\27\u0089\3\2\2\2\31\u008b\3\2\2\2\33\u008d\3\2\2\2\35")
        buf.write("\u0090\3\2\2\2\37\u0093\3\2\2\2!\u0095\3\2\2\2#\u0097")
        buf.write("\3\2\2\2%\u0099\3\2\2\2\'\u009b\3\2\2\2)\u009d\3\2\2\2")
        buf.write("+\u00a0\3\2\2\2-\u00a6\3\2\2\2/\u00ab\3\2\2\2\61\u00b1")
        buf.write("\3\2\2\2\63\u00ba\3\2\2\2\65\u00bf\3\2\2\2\67\u00c6\3")
        buf.write("\2\2\29\u00cc\3\2\2\2;\u00d3\3\2\2\2=\u00db\3\2\2\2?\u00e0")
        buf.write("\3\2\2\2A\u00e5\3\2\2\2C\u00eb\3\2\2\2E\u00f2\3\2\2\2")
        buf.write("G\u00f4\3\2\2\2I\u00fb\3\2\2\2K\u00ff\3\2\2\2M\u0102\3")
        buf.write("\2\2\2O\u0105\3\2\2\2Q\u010c\3\2\2\2S\u0113\3\2\2\2U\u011c")
        buf.write("\3\2\2\2W\u0120\3\2\2\2Y\u0123\3\2\2\2[\u0128\3\2\2\2")
        buf.write("]\u012e\3\2\2\2_\u0133\3\2\2\2a\u013b\3\2\2\2c\u0142\3")
        buf.write("\2\2\2e\u014b\3\2\2\2g\u0154\3\2\2\2i\u0167\3\2\2\2k\u0169")
        buf.write("\3\2\2\2m\u0175\3\2\2\2o\u0184\3\2\2\2q\u018e\3\2\2\2")
        buf.write("st\7}\2\2t\4\3\2\2\2uv\7=\2\2v\6\3\2\2\2wx\7\177\2\2x")
        buf.write("\b\3\2\2\2yz\7.\2\2z\n\3\2\2\2{|\7*\2\2|\f\3\2\2\2}~\7")
        buf.write("+\2\2~\16\3\2\2\2\177\u0080\7(\2\2\u0080\20\3\2\2\2\u0081")
        buf.write("\u0082\7~\2\2\u0082\22\3\2\2\2\u0083\u0084\7?\2\2\u0084")
        buf.write("\u0085\7?\2\2\u0085\24\3\2\2\2\u0086\u0087\7#\2\2\u0087")
        buf.write("\u0088\7?\2\2\u0088\26\3\2\2\2\u0089\u008a\7@\2\2\u008a")
        buf.write("\30\3\2\2\2\u008b\u008c\7>\2\2\u008c\32\3\2\2\2\u008d")
        buf.write("\u008e\7@\2\2\u008e\u008f\7?\2\2\u008f\34\3\2\2\2\u0090")
        buf.write("\u0091\7>\2\2\u0091\u0092\7?\2\2\u0092\36\3\2\2\2\u0093")
        buf.write("\u0094\7-\2\2\u0094 \3\2\2\2\u0095\u0096\7/\2\2\u0096")
        buf.write("\"\3\2\2\2\u0097\u0098\7,\2\2\u0098$\3\2\2\2\u0099\u009a")
        buf.write("\7\61\2\2\u009a&\3\2\2\2\u009b\u009c\7\'\2\2\u009c(\3")
        buf.write("\2\2\2\u009d\u009e\7#\2\2\u009e*\3\2\2\2\u009f\u00a1\t")
        buf.write("\2\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a5\b\26\2\2\u00a5,\3\2\2\2\u00a6\u00a7\7t\2\2\u00a7")
        buf.write("\u00a8\7q\2\2\u00a8\u00a9\7l\2\2\u00a9\u00aa\7q\2\2\u00aa")
        buf.write(".\3\2\2\2\u00ab\u00ac\7x\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write("\u00ae\7t\2\2\u00ae\u00af\7f\2\2\u00af\u00b0\7g\2\2\u00b0")
        buf.write("\60\3\2\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3\7o\2\2\u00b3")
        buf.write("\u00b4\7c\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6\7k\2\2\u00b6")
        buf.write("\u00b7\7n\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7q\2\2\u00b9")
        buf.write("\62\3\2\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7|\2\2\u00bc")
        buf.write("\u00bd\7w\2\2\u00bd\u00be\7n\2\2\u00be\64\3\2\2\2\u00bf")
        buf.write("\u00c0\7d\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2\7c\2\2\u00c2")
        buf.write("\u00c3\7p\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7q\2\2\u00c5")
        buf.write("\66\3\2\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write("\u00c9\7i\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7q\2\2\u00cb")
        buf.write("8\3\2\2\2\u00cc\u00cd\7o\2\2\u00cd\u00ce\7q\2\2\u00ce")
        buf.write("\u00cf\7t\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7f\2\2\u00d1")
        buf.write("\u00d2\7q\2\2\u00d2:\3\2\2\2\u00d3\u00d4\7p\2\2\u00d4")
        buf.write("\u00d5\7c\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7c\2\2\u00d7")
        buf.write("\u00d8\7p\2\2\u00d8\u00d9\7l\2\2\u00d9\u00da\7c\2\2\u00da")
        buf.write("<\3\2\2\2\u00db\u00dc\7e\2\2\u00dc\u00dd\7c\2\2\u00dd")
        buf.write("\u00de\7h\2\2\u00de\u00df\7g\2\2\u00df>\3\2\2\2\u00e0")
        buf.write("\u00e1\7i\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7k\2\2\u00e3")
        buf.write("\u00e4\7u\2\2\u00e4@\3\2\2\2\u00e5\u00e6\7e\2\2\u00e6")
        buf.write("\u00e7\7q\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9\7q\2\2\u00e9")
        buf.write("\u00ea\7t\2\2\u00eaB\3\2\2\2\u00eb\u00ec\7n\2\2\u00ec")
        buf.write("\u00ed\7k\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7p\2\2\u00ef")
        buf.write("\u00f0\7|\2\2\u00f0\u00f1\7q\2\2\u00f1D\3\2\2\2\u00f2")
        buf.write("\u00f3\7?\2\2\u00f3F\3\2\2\2\u00f4\u00f5\7v\2\2\u00f5")
        buf.write("\u00f6\7c\2\2\u00f6\u00f7\7o\2\2\u00f7\u00f8\7c\2\2\u00f8")
        buf.write("\u00f9\7p\2\2\u00f9\u00fa\7q\2\2\u00faH\3\2\2\2\u00fb")
        buf.write("\u00fc\7r\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7t\2\2\u00fe")
        buf.write("J\3\2\2\2\u00ff\u0100\7f\2\2\u0100\u0101\7g\2\2\u0101")
        buf.write("L\3\2\2\2\u0102\u0103\7g\2\2\u0103\u0104\7p\2\2\u0104")
        buf.write("N\3\2\2\2\u0105\u0106\7f\2\2\u0106\u0107\7k\2\2\u0107")
        buf.write("\u0108\7d\2\2\u0108\u0109\7w\2\2\u0109\u010a\7l\2\2\u010a")
        buf.write("\u010b\7q\2\2\u010bP\3\2\2\2\u010c\u010d\7f\2\2\u010d")
        buf.write("\u010e\7q\2\2\u010e\u010f\7t\2\2\u010f\u0110\7o\2\2\u0110")
        buf.write("\u0111\7k\2\2\u0111\u0112\7t\2\2\u0112R\3\2\2\2\u0113")
        buf.write("\u0114\7o\2\2\u0114\u0115\7k\2\2\u0115\u0116\7g\2\2\u0116")
        buf.write("\u0117\7p\2\2\u0117\u0118\7v\2\2\u0118\u0119\7t\2\2\u0119")
        buf.write("\u011a\7c\2\2\u011a\u011b\7u\2\2\u011bT\3\2\2\2\u011c")
        buf.write("\u011d\7s\2\2\u011d\u011e\7w\2\2\u011e\u011f\7g\2\2\u011f")
        buf.write("V\3\2\2\2\u0120\u0121\7u\2\2\u0121\u0122\7k\2\2\u0122")
        buf.write("X\3\2\2\2\u0123\u0124\7u\2\2\u0124\u0125\7k\2\2\u0125")
        buf.write("\u0126\7p\2\2\u0126\u0127\7q\2\2\u0127Z\3\2\2\2\u0128")
        buf.write("\u0129\7v\2\2\u0129\u012a\7g\2\2\u012a\u012b\7z\2\2\u012b")
        buf.write("\u012c\7v\2\2\u012c\u012d\7q\2\2\u012d\\\3\2\2\2\u012e")
        buf.write("\u012f\7n\2\2\u012f\u0130\7g\2\2\u0130\u0131\7g\2\2\u0131")
        buf.write("\u0132\7t\2\2\u0132^\3\2\2\2\u0133\u0134\7d\2\2\u0134")
        buf.write("\u0135\7q\2\2\u0135\u0136\7n\2\2\u0136\u0137\7g\2\2\u0137")
        buf.write("\u0138\7c\2\2\u0138\u0139\7p\2\2\u0139\u013a\7q\2\2\u013a")
        buf.write("`\3\2\2\2\u013b\u013c\7p\2\2\u013c\u013d\7w\2\2\u013d")
        buf.write("\u013e\7o\2\2\u013e\u013f\7g\2\2\u013f\u0140\7t\2\2\u0140")
        buf.write("\u0141\7q\2\2\u0141b\3\2\2\2\u0142\u0143\7g\2\2\u0143")
        buf.write("\u0144\7u\2\2\u0144\u0145\7e\2\2\u0145\u0146\7t\2\2\u0146")
        buf.write("\u0147\7k\2\2\u0147\u0148\7d\2\2\u0148\u0149\7k\2\2\u0149")
        buf.write("\u014a\7t\2\2\u014ad\3\2\2\2\u014b\u014c\7k\2\2\u014c")
        buf.write("\u014d\7o\2\2\u014d\u014e\7r\2\2\u014e\u014f\7t\2\2\u014f")
        buf.write("\u0150\7k\2\2\u0150\u0151\7o\2\2\u0151\u0152\7k\2\2\u0152")
        buf.write("\u0153\7t\2\2\u0153f\3\2\2\2\u0154\u0155\7p\2\2\u0155")
        buf.write("\u0156\7c\2\2\u0156\u0157\7f\2\2\u0157\u0158\7c\2\2\u0158")
        buf.write("h\3\2\2\2\u0159\u015a\7x\2\2\u015a\u015b\7g\2\2\u015b")
        buf.write("\u015c\7t\2\2\u015c\u015d\7f\2\2\u015d\u015e\7c\2\2\u015e")
        buf.write("\u015f\7f\2\2\u015f\u0160\7g\2\2\u0160\u0161\7t\2\2\u0161")
        buf.write("\u0168\7q\2\2\u0162\u0163\7h\2\2\u0163\u0164\7c\2\2\u0164")
        buf.write("\u0165\7n\2\2\u0165\u0166\7u\2\2\u0166\u0168\7q\2\2\u0167")
        buf.write("\u0159\3\2\2\2\u0167\u0162\3\2\2\2\u0168j\3\2\2\2\u0169")
        buf.write("\u016a\7o\2\2\u016a\u016b\7q\2\2\u016b\u016c\7f\2\2\u016c")
        buf.write("\u016d\7k\2\2\u016d\u016e\7h\2\2\u016e\u016f\7k\2\2\u016f")
        buf.write("\u0170\7e\2\2\u0170\u0171\7c\2\2\u0171\u0172\7d\2\2\u0172")
        buf.write("\u0173\7n\2\2\u0173\u0174\7g\2\2\u0174l\3\2\2\2\u0175")
        buf.write("\u0179\t\3\2\2\u0176\u0178\t\4\2\2\u0177\u0176\3\2\2\2")
        buf.write("\u0178\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3")
        buf.write("\2\2\2\u017a\u0182\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017e")
        buf.write("\7\60\2\2\u017d\u017f\t\4\2\2\u017e\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u0183\3\2\2\2\u0182\u017c\3\2\2\2\u0182\u0183\3")
        buf.write("\2\2\2\u0183n\3\2\2\2\u0184\u0188\7$\2\2\u0185\u0187\n")
        buf.write("\5\2\2\u0186\u0185\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018b\3\2\2\2\u018a")
        buf.write("\u0188\3\2\2\2\u018b\u018c\7$\2\2\u018cp\3\2\2\2\u018d")
        buf.write("\u018f\t\6\2\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2")
        buf.write("\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191r\3\2\2")
        buf.write("\2\n\2\u00a2\u0167\u0179\u0180\u0182\u0188\u0190\3\b\2")
        buf.write("\2")
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
    DIBUJO = 39
    DORMIR = 40
    MIENTRAS = 41
    QUE = 42
    SI = 43
    SINO = 44
    TEXTO = 45
    LEER = 46
    BOLEANO = 47
    NUMERO = 48
    ESCRIBIR = 49
    IMPRIMIR = 50
    NADA = 51
    BOOLEAN_CONSTANT = 52
    MODIFICABLE = 53
    NUMERIC_CONSTANT = 54
    STRING_CONSTANT = 55
    ID = 56

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "';'", "'}'", "','", "'('", "')'", "'&'", "'|'", "'=='", 
            "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'rojo'", "'verde'", "'amarillo'", "'azul'", "'blanco'", 
            "'negro'", "'morado'", "'naranja'", "'cafe'", "'gris'", "'color'", 
            "'lienzo'", "'='", "'tamano'", "'por'", "'de'", "'en'", "'dibujo'", 
            "'dormir'", "'mientras'", "'que'", "'si'", "'sino'", "'texto'", 
            "'leer'", "'boleano'", "'numero'", "'escribir'", "'imprimir'", 
            "'nada'", "'modificable'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", "NEGRO", 
            "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", "LIENZO", "EQUALS", 
            "TAMANO", "POR", "DE", "EN", "DIBUJO", "DORMIR", "MIENTRAS", 
            "QUE", "SI", "SINO", "TEXTO", "LEER", "BOLEANO", "NUMERO", "ESCRIBIR", 
            "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", "MODIFICABLE", "NUMERIC_CONSTANT", 
            "STRING_CONSTANT", "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "WS", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", "NEGRO", 
                  "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", "LIENZO", 
                  "EQUALS", "TAMANO", "POR", "DE", "EN", "DIBUJO", "DORMIR", 
                  "MIENTRAS", "QUE", "SI", "SINO", "TEXTO", "LEER", "BOLEANO", 
                  "NUMERO", "ESCRIBIR", "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", 
                  "MODIFICABLE", "NUMERIC_CONSTANT", "STRING_CONSTANT", 
                  "ID" ]

    grammarFileName = "Lienzo.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


