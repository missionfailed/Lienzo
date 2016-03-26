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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2;")
        buf.write("\u019b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\6\26\u00a3\n")
        buf.write("\26\r\26\16\26\u00a4\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\5\66\u0171\n\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\38\38\78\u0181\n8\f8\168\u0184")
        buf.write("\138\38\38\68\u0188\n8\r8\168\u0189\58\u018c\n8\39\39")
        buf.write("\79\u0190\n9\f9\169\u0193\139\39\39\3:\6:\u0198\n:\r:")
        buf.write("\16:\u0199\2\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;\3\2\7\5\2\13\f\17\17\"\"\3\2\63;\3\2")
        buf.write("\62;\3\2$$\4\2C\\c|\u01a1\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3u\3\2\2")
        buf.write("\2\5w\3\2\2\2\7y\3\2\2\2\t{\3\2\2\2\13}\3\2\2\2\r\177")
        buf.write("\3\2\2\2\17\u0081\3\2\2\2\21\u0083\3\2\2\2\23\u0085\3")
        buf.write("\2\2\2\25\u0088\3\2\2\2\27\u008b\3\2\2\2\31\u008d\3\2")
        buf.write("\2\2\33\u008f\3\2\2\2\35\u0092\3\2\2\2\37\u0095\3\2\2")
        buf.write("\2!\u0097\3\2\2\2#\u0099\3\2\2\2%\u009b\3\2\2\2\'\u009d")
        buf.write("\3\2\2\2)\u009f\3\2\2\2+\u00a2\3\2\2\2-\u00a8\3\2\2\2")
        buf.write("/\u00af\3\2\2\2\61\u00b4\3\2\2\2\63\u00ba\3\2\2\2\65\u00c3")
        buf.write("\3\2\2\2\67\u00c8\3\2\2\29\u00cf\3\2\2\2;\u00d5\3\2\2")
        buf.write("\2=\u00dc\3\2\2\2?\u00e4\3\2\2\2A\u00e9\3\2\2\2C\u00ee")
        buf.write("\3\2\2\2E\u00f4\3\2\2\2G\u00fb\3\2\2\2I\u00fd\3\2\2\2")
        buf.write("K\u0104\3\2\2\2M\u0108\3\2\2\2O\u010b\3\2\2\2Q\u010e\3")
        buf.write("\2\2\2S\u0115\3\2\2\2U\u011c\3\2\2\2W\u0125\3\2\2\2Y\u0129")
        buf.write("\3\2\2\2[\u012c\3\2\2\2]\u0131\3\2\2\2_\u0137\3\2\2\2")
        buf.write("a\u013c\3\2\2\2c\u0144\3\2\2\2e\u014b\3\2\2\2g\u0154\3")
        buf.write("\2\2\2i\u015d\3\2\2\2k\u0170\3\2\2\2m\u0172\3\2\2\2o\u017e")
        buf.write("\3\2\2\2q\u018d\3\2\2\2s\u0197\3\2\2\2uv\7}\2\2v\4\3\2")
        buf.write("\2\2wx\7=\2\2x\6\3\2\2\2yz\7\177\2\2z\b\3\2\2\2{|\7*\2")
        buf.write("\2|\n\3\2\2\2}~\7.\2\2~\f\3\2\2\2\177\u0080\7+\2\2\u0080")
        buf.write("\16\3\2\2\2\u0081\u0082\7(\2\2\u0082\20\3\2\2\2\u0083")
        buf.write("\u0084\7~\2\2\u0084\22\3\2\2\2\u0085\u0086\7?\2\2\u0086")
        buf.write("\u0087\7?\2\2\u0087\24\3\2\2\2\u0088\u0089\7#\2\2\u0089")
        buf.write("\u008a\7?\2\2\u008a\26\3\2\2\2\u008b\u008c\7@\2\2\u008c")
        buf.write("\30\3\2\2\2\u008d\u008e\7>\2\2\u008e\32\3\2\2\2\u008f")
        buf.write("\u0090\7@\2\2\u0090\u0091\7?\2\2\u0091\34\3\2\2\2\u0092")
        buf.write("\u0093\7>\2\2\u0093\u0094\7?\2\2\u0094\36\3\2\2\2\u0095")
        buf.write("\u0096\7-\2\2\u0096 \3\2\2\2\u0097\u0098\7/\2\2\u0098")
        buf.write("\"\3\2\2\2\u0099\u009a\7,\2\2\u009a$\3\2\2\2\u009b\u009c")
        buf.write("\7\61\2\2\u009c&\3\2\2\2\u009d\u009e\7\'\2\2\u009e(\3")
        buf.write("\2\2\2\u009f\u00a0\7#\2\2\u00a0*\3\2\2\2\u00a1\u00a3\t")
        buf.write("\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a2")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\u00a7\b\26\2\2\u00a7,\3\2\2\2\u00a8\u00a9\7i\2\2\u00a9")
        buf.write("\u00aa\7n\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7d\2\2\u00ac")
        buf.write("\u00ad\7c\2\2\u00ad\u00ae\7n\2\2\u00ae.\3\2\2\2\u00af")
        buf.write("\u00b0\7t\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7l\2\2\u00b2")
        buf.write("\u00b3\7q\2\2\u00b3\60\3\2\2\2\u00b4\u00b5\7x\2\2\u00b5")
        buf.write("\u00b6\7g\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7f\2\2\u00b8")
        buf.write("\u00b9\7g\2\2\u00b9\62\3\2\2\2\u00ba\u00bb\7c\2\2\u00bb")
        buf.write("\u00bc\7o\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7t\2\2\u00be")
        buf.write("\u00bf\7k\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1\7n\2\2\u00c1")
        buf.write("\u00c2\7q\2\2\u00c2\64\3\2\2\2\u00c3\u00c4\7c\2\2\u00c4")
        buf.write("\u00c5\7|\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7\7n\2\2\u00c7")
        buf.write("\66\3\2\2\2\u00c8\u00c9\7d\2\2\u00c9\u00ca\7n\2\2\u00ca")
        buf.write("\u00cb\7c\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7e\2\2\u00cd")
        buf.write("\u00ce\7q\2\2\u00ce8\3\2\2\2\u00cf\u00d0\7p\2\2\u00d0")
        buf.write("\u00d1\7g\2\2\u00d1\u00d2\7i\2\2\u00d2\u00d3\7t\2\2\u00d3")
        buf.write("\u00d4\7q\2\2\u00d4:\3\2\2\2\u00d5\u00d6\7o\2\2\u00d6")
        buf.write("\u00d7\7q\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9\7c\2\2\u00d9")
        buf.write("\u00da\7f\2\2\u00da\u00db\7q\2\2\u00db<\3\2\2\2\u00dc")
        buf.write("\u00dd\7p\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7t\2\2\u00df")
        buf.write("\u00e0\7c\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7l\2\2\u00e2")
        buf.write("\u00e3\7c\2\2\u00e3>\3\2\2\2\u00e4\u00e5\7e\2\2\u00e5")
        buf.write("\u00e6\7c\2\2\u00e6\u00e7\7h\2\2\u00e7\u00e8\7g\2\2\u00e8")
        buf.write("@\3\2\2\2\u00e9\u00ea\7i\2\2\u00ea\u00eb\7t\2\2\u00eb")
        buf.write("\u00ec\7k\2\2\u00ec\u00ed\7u\2\2\u00edB\3\2\2\2\u00ee")
        buf.write("\u00ef\7e\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1\7n\2\2\u00f1")
        buf.write("\u00f2\7q\2\2\u00f2\u00f3\7t\2\2\u00f3D\3\2\2\2\u00f4")
        buf.write("\u00f5\7n\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7g\2\2\u00f7")
        buf.write("\u00f8\7p\2\2\u00f8\u00f9\7|\2\2\u00f9\u00fa\7q\2\2\u00fa")
        buf.write("F\3\2\2\2\u00fb\u00fc\7?\2\2\u00fcH\3\2\2\2\u00fd\u00fe")
        buf.write("\7v\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7o\2\2\u0100\u0101")
        buf.write("\7c\2\2\u0101\u0102\7p\2\2\u0102\u0103\7q\2\2\u0103J\3")
        buf.write("\2\2\2\u0104\u0105\7r\2\2\u0105\u0106\7q\2\2\u0106\u0107")
        buf.write("\7t\2\2\u0107L\3\2\2\2\u0108\u0109\7f\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010aN\3\2\2\2\u010b\u010c\7g\2\2\u010c\u010d")
        buf.write("\7p\2\2\u010dP\3\2\2\2\u010e\u010f\7f\2\2\u010f\u0110")
        buf.write("\7k\2\2\u0110\u0111\7d\2\2\u0111\u0112\7w\2\2\u0112\u0113")
        buf.write("\7l\2\2\u0113\u0114\7q\2\2\u0114R\3\2\2\2\u0115\u0116")
        buf.write("\7f\2\2\u0116\u0117\7q\2\2\u0117\u0118\7t\2\2\u0118\u0119")
        buf.write("\7o\2\2\u0119\u011a\7k\2\2\u011a\u011b\7t\2\2\u011bT\3")
        buf.write("\2\2\2\u011c\u011d\7o\2\2\u011d\u011e\7k\2\2\u011e\u011f")
        buf.write("\7g\2\2\u011f\u0120\7p\2\2\u0120\u0121\7v\2\2\u0121\u0122")
        buf.write("\7t\2\2\u0122\u0123\7c\2\2\u0123\u0124\7u\2\2\u0124V\3")
        buf.write("\2\2\2\u0125\u0126\7s\2\2\u0126\u0127\7w\2\2\u0127\u0128")
        buf.write("\7g\2\2\u0128X\3\2\2\2\u0129\u012a\7u\2\2\u012a\u012b")
        buf.write("\7k\2\2\u012bZ\3\2\2\2\u012c\u012d\7u\2\2\u012d\u012e")
        buf.write("\7k\2\2\u012e\u012f\7p\2\2\u012f\u0130\7q\2\2\u0130\\")
        buf.write("\3\2\2\2\u0131\u0132\7v\2\2\u0132\u0133\7g\2\2\u0133\u0134")
        buf.write("\7z\2\2\u0134\u0135\7v\2\2\u0135\u0136\7q\2\2\u0136^\3")
        buf.write("\2\2\2\u0137\u0138\7n\2\2\u0138\u0139\7g\2\2\u0139\u013a")
        buf.write("\7g\2\2\u013a\u013b\7t\2\2\u013b`\3\2\2\2\u013c\u013d")
        buf.write("\7d\2\2\u013d\u013e\7q\2\2\u013e\u013f\7n\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140\u0141\7c\2\2\u0141\u0142\7p\2\2\u0142\u0143")
        buf.write("\7q\2\2\u0143b\3\2\2\2\u0144\u0145\7p\2\2\u0145\u0146")
        buf.write("\7w\2\2\u0146\u0147\7o\2\2\u0147\u0148\7g\2\2\u0148\u0149")
        buf.write("\7t\2\2\u0149\u014a\7q\2\2\u014ad\3\2\2\2\u014b\u014c")
        buf.write("\7g\2\2\u014c\u014d\7u\2\2\u014d\u014e\7e\2\2\u014e\u014f")
        buf.write("\7t\2\2\u014f\u0150\7k\2\2\u0150\u0151\7d\2\2\u0151\u0152")
        buf.write("\7k\2\2\u0152\u0153\7t\2\2\u0153f\3\2\2\2\u0154\u0155")
        buf.write("\7k\2\2\u0155\u0156\7o\2\2\u0156\u0157\7r\2\2\u0157\u0158")
        buf.write("\7t\2\2\u0158\u0159\7k\2\2\u0159\u015a\7o\2\2\u015a\u015b")
        buf.write("\7k\2\2\u015b\u015c\7t\2\2\u015ch\3\2\2\2\u015d\u015e")
        buf.write("\7p\2\2\u015e\u015f\7c\2\2\u015f\u0160\7f\2\2\u0160\u0161")
        buf.write("\7c\2\2\u0161j\3\2\2\2\u0162\u0163\7x\2\2\u0163\u0164")
        buf.write("\7g\2\2\u0164\u0165\7t\2\2\u0165\u0166\7f\2\2\u0166\u0167")
        buf.write("\7c\2\2\u0167\u0168\7f\2\2\u0168\u0169\7g\2\2\u0169\u016a")
        buf.write("\7t\2\2\u016a\u0171\7q\2\2\u016b\u016c\7h\2\2\u016c\u016d")
        buf.write("\7c\2\2\u016d\u016e\7n\2\2\u016e\u016f\7u\2\2\u016f\u0171")
        buf.write("\7q\2\2\u0170\u0162\3\2\2\2\u0170\u016b\3\2\2\2\u0171")
        buf.write("l\3\2\2\2\u0172\u0173\7o\2\2\u0173\u0174\7q\2\2\u0174")
        buf.write("\u0175\7f\2\2\u0175\u0176\7k\2\2\u0176\u0177\7h\2\2\u0177")
        buf.write("\u0178\7k\2\2\u0178\u0179\7e\2\2\u0179\u017a\7c\2\2\u017a")
        buf.write("\u017b\7d\2\2\u017b\u017c\7n\2\2\u017c\u017d\7g\2\2\u017d")
        buf.write("n\3\2\2\2\u017e\u0182\t\3\2\2\u017f\u0181\t\4\2\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u018b\3\2\2\2\u0184\u0182\3")
        buf.write("\2\2\2\u0185\u0187\7\60\2\2\u0186\u0188\t\4\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u0185\3")
        buf.write("\2\2\2\u018b\u018c\3\2\2\2\u018cp\3\2\2\2\u018d\u0191")
        buf.write("\7$\2\2\u018e\u0190\n\5\2\2\u018f\u018e\3\2\2\2\u0190")
        buf.write("\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0192\u0194\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195\7")
        buf.write("$\2\2\u0195r\3\2\2\2\u0196\u0198\t\6\2\2\u0197\u0196\3")
        buf.write("\2\2\2\u0198\u0199\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a")
        buf.write("\3\2\2\2\u019at\3\2\2\2\n\2\u00a4\u0170\u0182\u0189\u018b")
        buf.write("\u0191\u0199\3\b\2\2")
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
    DIBUJO = 40
    DORMIR = 41
    MIENTRAS = 42
    QUE = 43
    SI = 44
    SINO = 45
    TEXTO = 46
    LEER = 47
    BOLEANO = 48
    NUMERO = 49
    ESCRIBIR = 50
    IMPRIMIR = 51
    NADA = 52
    BOOLEAN_CONSTANT = 53
    MODIFICABLE = 54
    NUMERIC_CONSTANT = 55
    STRING_CONSTANT = 56
    ID = 57

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "';'", "'}'", "'('", "','", "')'", "'&'", "'|'", "'=='", 
            "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'global'", "'rojo'", "'verde'", "'amarillo'", 
            "'azul'", "'blanco'", "'negro'", "'morado'", "'naranja'", "'cafe'", 
            "'gris'", "'color'", "'lienzo'", "'='", "'tamano'", "'por'", 
            "'de'", "'en'", "'dibujo'", "'dormir'", "'mientras'", "'que'", 
            "'si'", "'sino'", "'texto'", "'leer'", "'boleano'", "'numero'", 
            "'escribir'", "'imprimir'", "'nada'", "'modificable'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "GLOBAL", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", 
            "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", "LIENZO", 
            "EQUALS", "TAMANO", "POR", "DE", "EN", "DIBUJO", "DORMIR", "MIENTRAS", 
            "QUE", "SI", "SINO", "TEXTO", "LEER", "BOLEANO", "NUMERO", "ESCRIBIR", 
            "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", "MODIFICABLE", "NUMERIC_CONSTANT", 
            "STRING_CONSTANT", "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "WS", "GLOBAL", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", 
                  "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", 
                  "LIENZO", "EQUALS", "TAMANO", "POR", "DE", "EN", "DIBUJO", 
                  "DORMIR", "MIENTRAS", "QUE", "SI", "SINO", "TEXTO", "LEER", 
                  "BOLEANO", "NUMERO", "ESCRIBIR", "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", 
                  "MODIFICABLE", "NUMERIC_CONSTANT", "STRING_CONSTANT", 
                  "ID" ]

    grammarFileName = "Lienzo.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


