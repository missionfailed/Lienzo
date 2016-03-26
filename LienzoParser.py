# Generated from Lienzo.g4 by ANTLR 4.5.2
# encoding: utf-8
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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3;")
        buf.write("\u0150\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2")
        buf.write("\7\2=\n\2\f\2\16\2@\13\2\3\2\7\2C\n\2\f\2\16\2F\13\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\7\bs\n\b\f\b\16\bv\13\b\5\bx\n\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\5\t\u0082\n\t\3\n\3\n\5\n\u0086\n")
        buf.write("\n\3\n\3\n\3\n\3\13\7\13\u008c\n\13\f\13\16\13\u008f\13")
        buf.write("\13\3\13\7\13\u0092\n\13\f\13\16\13\u0095\13\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r\u00a4")
        buf.write("\n\r\3\r\3\r\3\16\3\16\3\16\5\16\u00ab\n\16\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\7\24\u00ca\n\24\f\24\16\24\u00cd")
        buf.write("\13\24\3\24\3\24\3\24\3\24\7\24\u00d3\n\24\f\24\16\24")
        buf.write("\u00d6\13\24\3\24\5\24\u00d9\n\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\7\25\u00e3\n\25\f\25\16\25\u00e6")
        buf.write("\13\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\7\26\u00f3\n\26\f\26\16\26\u00f6\13\26\5\26\u00f8")
        buf.write("\n\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27")
        buf.write("\u0103\n\27\f\27\16\27\u0106\13\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\7\30\u010f\n\30\f\30\16\30\u0112\13\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u011b\n\31\f")
        buf.write("\31\16\31\u011e\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7")
        buf.write("\32\u0126\n\32\f\32\16\32\u0129\13\32\3\33\5\33\u012c")
        buf.write("\n\33\3\33\3\33\3\33\3\33\3\33\5\33\u0133\n\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u013a\n\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0148\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\2\2\36\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write("\2\b\3\2\31\"\4\2\60\60\62\63\3\2\t\n\3\2\13\20\3\2\21")
        buf.write("\22\3\2\23\25\u0152\2:\3\2\2\2\4J\3\2\2\2\6R\3\2\2\2\b")
        buf.write("X\3\2\2\2\nZ\3\2\2\2\fc\3\2\2\2\16l\3\2\2\2\20\u0081\3")
        buf.write("\2\2\2\22\u0083\3\2\2\2\24\u008d\3\2\2\2\26\u0096\3\2")
        buf.write("\2\2\30\u00a3\3\2\2\2\32\u00aa\3\2\2\2\34\u00ac\3\2\2")
        buf.write("\2\36\u00b0\3\2\2\2 \u00b8\3\2\2\2\"\u00bd\3\2\2\2$\u00bf")
        buf.write("\3\2\2\2&\u00c2\3\2\2\2(\u00da\3\2\2\2*\u00e9\3\2\2\2")
        buf.write(",\u00fc\3\2\2\2.\u0107\3\2\2\2\60\u0113\3\2\2\2\62\u011f")
        buf.write("\3\2\2\2\64\u0139\3\2\2\2\66\u0147\3\2\2\28\u0149\3\2")
        buf.write("\2\2:>\5\4\3\2;=\5\f\7\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2")
        buf.write(">?\3\2\2\2?D\3\2\2\2@>\3\2\2\2AC\5\16\b\2BA\3\2\2\2CF")
        buf.write("\3\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2FD\3\2\2\2GH\58")
        buf.write("\35\2HI\7\2\2\3I\3\3\2\2\2JK\7$\2\2KL\7\3\2\2LM\5\6\4")
        buf.write("\2MN\7\4\2\2NO\5\n\6\2OP\7\4\2\2PQ\7\5\2\2Q\5\3\2\2\2")
        buf.write("RS\7#\2\2ST\7(\2\2TU\7$\2\2UV\7%\2\2VW\5\b\5\2W\7\3\2")
        buf.write("\2\2XY\t\2\2\2Y\t\3\2\2\2Z[\7&\2\2[\\\7(\2\2\\]\7$\2\2")
        buf.write("]^\7%\2\2^_\5,\27\2_`\7\'\2\2`a\5,\27\2ab\b\6\1\2b\13")
        buf.write("\3\2\2\2cd\5\"\22\2de\7\30\2\2ef\7;\2\2fg\b\7\1\2gh\7")
        buf.write("%\2\2hi\5,\27\2ij\7\4\2\2jk\b\7\1\2k\r\3\2\2\2lm\5\20")
        buf.write("\t\2mn\7;\2\2nw\7\6\2\2ot\5\22\n\2pq\7\7\2\2qs\5\22\n")
        buf.write("\2rp\3\2\2\2sv\3\2\2\2tr\3\2\2\2tu\3\2\2\2ux\3\2\2\2v")
        buf.write("t\3\2\2\2wo\3\2\2\2wx\3\2\2\2xy\3\2\2\2yz\7\b\2\2z{\b")
        buf.write("\b\1\2{|\7\3\2\2|}\5\24\13\2}~\7\5\2\2~\17\3\2\2\2\177")
        buf.write("\u0082\5\"\22\2\u0080\u0082\7\66\2\2\u0081\177\3\2\2\2")
        buf.write("\u0081\u0080\3\2\2\2\u0082\21\3\2\2\2\u0083\u0085\5\"")
        buf.write("\22\2\u0084\u0086\78\2\2\u0085\u0084\3\2\2\2\u0085\u0086")
        buf.write("\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\7;\2\2\u0088")
        buf.write("\u0089\b\n\1\2\u0089\23\3\2\2\2\u008a\u008c\5\26\f\2\u008b")
        buf.write("\u008a\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\u0093\3\2\2\2\u008f\u008d\3")
        buf.write("\2\2\2\u0090\u0092\5\30\r\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\25\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097\5\"")
        buf.write("\22\2\u0097\u0098\7;\2\2\u0098\u0099\b\f\1\2\u0099\u009a")
        buf.write("\7%\2\2\u009a\u009b\5,\27\2\u009b\u009c\7\4\2\2\u009c")
        buf.write("\u009d\b\f\1\2\u009d\27\3\2\2\2\u009e\u00a4\5 \21\2\u009f")
        buf.write("\u00a4\5&\24\2\u00a0\u00a4\5(\25\2\u00a1\u00a4\5\32\16")
        buf.write("\2\u00a2\u00a4\5*\26\2\u00a3\u009e\3\2\2\2\u00a3\u009f")
        buf.write("\3\2\2\2\u00a3\u00a0\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\7\4\2\2")
        buf.write("\u00a6\31\3\2\2\2\u00a7\u00ab\5\34\17\2\u00a8\u00ab\5")
        buf.write("\36\20\2\u00a9\u00ab\5$\23\2\u00aa\u00a7\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\33\3\2\2\2\u00ac")
        buf.write("\u00ad\7\61\2\2\u00ad\u00ae\7;\2\2\u00ae\u00af\b\17\1")
        buf.write("\2\u00af\35\3\2\2\2\u00b0\u00b1\7\64\2\2\u00b1\u00b2\5")
        buf.write(",\27\2\u00b2\u00b3\7)\2\2\u00b3\u00b4\5\60\31\2\u00b4")
        buf.write("\u00b5\7\7\2\2\u00b5\u00b6\5\60\31\2\u00b6\u00b7\b\20")
        buf.write("\1\2\u00b7\37\3\2\2\2\u00b8\u00b9\7;\2\2\u00b9\u00ba\7")
        buf.write("%\2\2\u00ba\u00bb\5,\27\2\u00bb\u00bc\b\21\1\2\u00bc!")
        buf.write("\3\2\2\2\u00bd\u00be\t\3\2\2\u00be#\3\2\2\2\u00bf\u00c0")
        buf.write("\7\65\2\2\u00c0\u00c1\5,\27\2\u00c1%\3\2\2\2\u00c2\u00c3")
        buf.write("\7.\2\2\u00c3\u00c4\7\6\2\2\u00c4\u00c5\5,\27\2\u00c5")
        buf.write("\u00c6\7\b\2\2\u00c6\u00c7\b\24\1\2\u00c7\u00cb\7\3\2")
        buf.write("\2\u00c8\u00ca\5\30\r\2\u00c9\u00c8\3\2\2\2\u00ca\u00cd")
        buf.write("\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc")
        buf.write("\u00ce\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00d8\7\5\2\2")
        buf.write("\u00cf\u00d0\7/\2\2\u00d0\u00d4\7\3\2\2\u00d1\u00d3\5")
        buf.write("\30\r\2\u00d2\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d7\3\2\2\2")
        buf.write("\u00d6\u00d4\3\2\2\2\u00d7\u00d9\7\5\2\2\u00d8\u00cf\3")
        buf.write("\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\'\3\2\2\2\u00da\u00db")
        buf.write("\7,\2\2\u00db\u00dc\7-\2\2\u00dc\u00dd\7\6\2\2\u00dd\u00de")
        buf.write("\5,\27\2\u00de\u00df\7\b\2\2\u00df\u00e0\b\25\1\2\u00e0")
        buf.write("\u00e4\7\3\2\2\u00e1\u00e3\5\30\r\2\u00e2\u00e1\3\2\2")
        buf.write("\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7")
        buf.write("\u00e8\7\5\2\2\u00e8)\3\2\2\2\u00e9\u00ea\7;\2\2\u00ea")
        buf.write("\u00eb\b\26\1\2\u00eb\u00f7\7\6\2\2\u00ec\u00ed\5,\27")
        buf.write("\2\u00ed\u00f4\b\26\1\2\u00ee\u00ef\7\7\2\2\u00ef\u00f0")
        buf.write("\5,\27\2\u00f0\u00f1\b\26\1\2\u00f1\u00f3\3\2\2\2\u00f2")
        buf.write("\u00ee\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f5\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3")
        buf.write("\2\2\2\u00f7\u00ec\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9")
        buf.write("\3\2\2\2\u00f9\u00fa\7\b\2\2\u00fa\u00fb\b\26\1\2\u00fb")
        buf.write("+\3\2\2\2\u00fc\u00fd\5.\30\2\u00fd\u0104\b\27\1\2\u00fe")
        buf.write("\u00ff\t\4\2\2\u00ff\u0100\5.\30\2\u0100\u0101\b\27\1")
        buf.write("\2\u0101\u0103\3\2\2\2\u0102\u00fe\3\2\2\2\u0103\u0106")
        buf.write("\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105")
        buf.write("-\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\5\60\31\2\u0108")
        buf.write("\u0110\b\30\1\2\u0109\u010a\t\5\2\2\u010a\u010b\5\60\31")
        buf.write("\2\u010b\u010c\3\2\2\2\u010c\u010d\b\30\1\2\u010d\u010f")
        buf.write("\3\2\2\2\u010e\u0109\3\2\2\2\u010f\u0112\3\2\2\2\u0110")
        buf.write("\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111/\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0113\u0114\5\62\32\2\u0114\u011c\b\31")
        buf.write("\1\2\u0115\u0116\t\6\2\2\u0116\u0117\5\62\32\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118\u0119\b\31\1\2\u0119\u011b\3\2\2\2\u011a")
        buf.write("\u0115\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2")
        buf.write("\u011c\u011d\3\2\2\2\u011d\61\3\2\2\2\u011e\u011c\3\2")
        buf.write("\2\2\u011f\u0120\5\64\33\2\u0120\u0127\b\32\1\2\u0121")
        buf.write("\u0122\t\7\2\2\u0122\u0123\5\64\33\2\u0123\u0124\b\32")
        buf.write("\1\2\u0124\u0126\3\2\2\2\u0125\u0121\3\2\2\2\u0126\u0129")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\63\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012c\7\26\2\2\u012b")
        buf.write("\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d\3\2\2\2")
        buf.write("\u012d\u012e\5\66\34\2\u012e\u012f\3\2\2\2\u012f\u0130")
        buf.write("\b\33\1\2\u0130\u013a\3\2\2\2\u0131\u0133\7\22\2\2\u0132")
        buf.write("\u0131\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0134\3\2\2\2")
        buf.write("\u0134\u0135\79\2\2\u0135\u0136\3\2\2\2\u0136\u013a\b")
        buf.write("\33\1\2\u0137\u0138\7:\2\2\u0138\u013a\b\33\1\2\u0139")
        buf.write("\u012b\3\2\2\2\u0139\u0132\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u013a\65\3\2\2\2\u013b\u013c\7;\2\2\u013c\u0148\b\34")
        buf.write("\1\2\u013d\u013e\7\67\2\2\u013e\u0148\b\34\1\2\u013f\u0140")
        buf.write("\5*\26\2\u0140\u0141\b\34\1\2\u0141\u0148\3\2\2\2\u0142")
        buf.write("\u0143\7\6\2\2\u0143\u0144\5,\27\2\u0144\u0145\7\b\2\2")
        buf.write("\u0145\u0146\b\34\1\2\u0146\u0148\3\2\2\2\u0147\u013b")
        buf.write("\3\2\2\2\u0147\u013d\3\2\2\2\u0147\u013f\3\2\2\2\u0147")
        buf.write("\u0142\3\2\2\2\u0148\67\3\2\2\2\u0149\u014a\7*\2\2\u014a")
        buf.write("\u014b\b\35\1\2\u014b\u014c\7\3\2\2\u014c\u014d\5\24\13")
        buf.write("\2\u014d\u014e\7\5\2\2\u014e9\3\2\2\2\32>Dtw\u0081\u0085")
        buf.write("\u008d\u0093\u00a3\u00aa\u00cb\u00d4\u00d8\u00e4\u00f4")
        buf.write("\u00f7\u0104\u0110\u011c\u0127\u012b\u0132\u0139\u0147")
        return buf.getvalue()


class LienzoParser ( Parser ):

    grammarFileName = "Lienzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "';'", "'}'", "'('", "','", "')'", 
                     "'&'", "'|'", "'=='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "<INVALID>", 
                     "'global'", "'rojo'", "'verde'", "'amarillo'", "'azul'", 
                     "'blanco'", "'negro'", "'morado'", "'naranja'", "'cafe'", 
                     "'gris'", "'color'", "'lienzo'", "'='", "'tamano'", 
                     "'por'", "'de'", "'en'", "'dibujo'", "'dormir'", "'mientras'", 
                     "'que'", "'si'", "'sino'", "'texto'", "'leer'", "'boleano'", 
                     "'numero'", "'escribir'", "'imprimir'", "'nada'", "<INVALID>", 
                     "'modificable'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "GLOBAL", "ROJO", "VERDE", "AMARILLO", 
                      "AZUL", "BLANCO", "NEGRO", "MORADO", "NARANJA", "CAFE", 
                      "GRIS", "COLOR", "LIENZO", "EQUALS", "TAMANO", "POR", 
                      "DE", "EN", "DIBUJO", "DORMIR", "MIENTRAS", "QUE", 
                      "SI", "SINO", "TEXTO", "LEER", "BOLEANO", "NUMERO", 
                      "ESCRIBIR", "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", 
                      "MODIFICABLE", "NUMERIC_CONSTANT", "STRING_CONSTANT", 
                      "ID" ]

    RULE_program = 0
    RULE_lienzo = 1
    RULE_colorLienzo = 2
    RULE_color = 3
    RULE_tamanoLienzo = 4
    RULE_declaracion_global = 5
    RULE_funcion = 6
    RULE_tipoFunc = 7
    RULE_parametro = 8
    RULE_cuerpo = 9
    RULE_declaracion = 10
    RULE_instruccion_aux = 11
    RULE_llamadaFuncionPredefinida = 12
    RULE_lectura = 13
    RULE_escritura = 14
    RULE_asignacion = 15
    RULE_tipo = 16
    RULE_imprimir = 17
    RULE_condicional = 18
    RULE_mientrasQue = 19
    RULE_llamadaFuncion = 20
    RULE_ss_expresion = 21
    RULE_s_expresion = 22
    RULE_expresion = 23
    RULE_termino = 24
    RULE_factor = 25
    RULE_factor_aux = 26
    RULE_dibujo = 27

    ruleNames =  [ "program", "lienzo", "colorLienzo", "color", "tamanoLienzo", 
                   "declaracion_global", "funcion", "tipoFunc", "parametro", 
                   "cuerpo", "declaracion", "instruccion_aux", "llamadaFuncionPredefinida", 
                   "lectura", "escritura", "asignacion", "tipo", "imprimir", 
                   "condicional", "mientrasQue", "llamadaFuncion", "ss_expresion", 
                   "s_expresion", "expresion", "termino", "factor", "factor_aux", 
                   "dibujo" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    WS=21
    GLOBAL=22
    ROJO=23
    VERDE=24
    AMARILLO=25
    AZUL=26
    BLANCO=27
    NEGRO=28
    MORADO=29
    NARANJA=30
    CAFE=31
    GRIS=32
    COLOR=33
    LIENZO=34
    EQUALS=35
    TAMANO=36
    POR=37
    DE=38
    EN=39
    DIBUJO=40
    DORMIR=41
    MIENTRAS=42
    QUE=43
    SI=44
    SINO=45
    TEXTO=46
    LEER=47
    BOLEANO=48
    NUMERO=49
    ESCRIBIR=50
    IMPRIMIR=51
    NADA=52
    BOOLEAN_CONSTANT=53
    MODIFICABLE=54
    NUMERIC_CONSTANT=55
    STRING_CONSTANT=56
    ID=57

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lienzo(self):
            return self.getTypedRuleContext(LienzoParser.LienzoContext,0)


        def dibujo(self):
            return self.getTypedRuleContext(LienzoParser.DibujoContext,0)


        def EOF(self):
            return self.getToken(LienzoParser.EOF, 0)

        def declaracion_global(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.Declaracion_globalContext)
            else:
                return self.getTypedRuleContext(LienzoParser.Declaracion_globalContext,i)


        def funcion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.FuncionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.FuncionContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = LienzoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.lienzo()
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    self.declaracion_global() 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO) | (1 << LienzoParser.NADA))) != 0):
                self.state = 63
                self.funcion()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.dibujo()
            self.state = 70
            self.match(LienzoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LienzoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIENZO(self):
            return self.getToken(LienzoParser.LIENZO, 0)

        def colorLienzo(self):
            return self.getTypedRuleContext(LienzoParser.ColorLienzoContext,0)


        def tamanoLienzo(self):
            return self.getTypedRuleContext(LienzoParser.TamanoLienzoContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_lienzo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLienzo" ):
                listener.enterLienzo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLienzo" ):
                listener.exitLienzo(self)




    def lienzo(self):

        localctx = LienzoParser.LienzoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_lienzo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(LienzoParser.LIENZO)
            self.state = 73
            self.match(LienzoParser.T__0)
            self.state = 74
            self.colorLienzo()
            self.state = 75
            self.match(LienzoParser.T__1)
            self.state = 76
            self.tamanoLienzo()
            self.state = 77
            self.match(LienzoParser.T__1)
            self.state = 78
            self.match(LienzoParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColorLienzoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLOR(self):
            return self.getToken(LienzoParser.COLOR, 0)

        def DE(self):
            return self.getToken(LienzoParser.DE, 0)

        def LIENZO(self):
            return self.getToken(LienzoParser.LIENZO, 0)

        def color(self):
            return self.getTypedRuleContext(LienzoParser.ColorContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_colorLienzo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColorLienzo" ):
                listener.enterColorLienzo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColorLienzo" ):
                listener.exitColorLienzo(self)




    def colorLienzo(self):

        localctx = LienzoParser.ColorLienzoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_colorLienzo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(LienzoParser.COLOR)
            self.state = 81
            self.match(LienzoParser.DE)
            self.state = 82
            self.match(LienzoParser.LIENZO)
            self.state = 83
            self.match(LienzoParser.EQUALS)
            self.state = 84
            self.color()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROJO(self):
            return self.getToken(LienzoParser.ROJO, 0)

        def VERDE(self):
            return self.getToken(LienzoParser.VERDE, 0)

        def AMARILLO(self):
            return self.getToken(LienzoParser.AMARILLO, 0)

        def AZUL(self):
            return self.getToken(LienzoParser.AZUL, 0)

        def BLANCO(self):
            return self.getToken(LienzoParser.BLANCO, 0)

        def NEGRO(self):
            return self.getToken(LienzoParser.NEGRO, 0)

        def MORADO(self):
            return self.getToken(LienzoParser.MORADO, 0)

        def NARANJA(self):
            return self.getToken(LienzoParser.NARANJA, 0)

        def CAFE(self):
            return self.getToken(LienzoParser.CAFE, 0)

        def GRIS(self):
            return self.getToken(LienzoParser.GRIS, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_color

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColor" ):
                listener.enterColor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColor" ):
                listener.exitColor(self)




    def color(self):

        localctx = LienzoParser.ColorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_color)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.ROJO) | (1 << LienzoParser.VERDE) | (1 << LienzoParser.AMARILLO) | (1 << LienzoParser.AZUL) | (1 << LienzoParser.BLANCO) | (1 << LienzoParser.NEGRO) | (1 << LienzoParser.MORADO) | (1 << LienzoParser.NARANJA) | (1 << LienzoParser.CAFE) | (1 << LienzoParser.GRIS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TamanoLienzoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.largo = None # Ss_expresionContext
            self.ancho = None # Ss_expresionContext

        def TAMANO(self):
            return self.getToken(LienzoParser.TAMANO, 0)

        def DE(self):
            return self.getToken(LienzoParser.DE, 0)

        def LIENZO(self):
            return self.getToken(LienzoParser.LIENZO, 0)

        def POR(self):
            return self.getToken(LienzoParser.POR, 0)

        def ss_expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.Ss_expresionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_tamanoLienzo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTamanoLienzo" ):
                listener.enterTamanoLienzo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTamanoLienzo" ):
                listener.exitTamanoLienzo(self)




    def tamanoLienzo(self):

        localctx = LienzoParser.TamanoLienzoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tamanoLienzo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(LienzoParser.TAMANO)
            self.state = 89
            self.match(LienzoParser.DE)
            self.state = 90
            self.match(LienzoParser.LIENZO)
            self.state = 91
            self.match(LienzoParser.EQUALS)
            self.state = 92
            localctx.largo = self.ss_expresion()
            self.state = 93
            self.match(LienzoParser.POR)
            self.state = 94
            localctx.ancho = self.ss_expresion()

            if localctx.largo.type != NUMERO:
                error((None if localctx.largo is None else localctx.largo.start).line, "Largo del lienzo debe ser una expresion entera")
            elif localctx.ancho.type != NUMERO:
                error((None if localctx.ancho is None else localctx.ancho.start).line, "Ancho del lienzo debe ser una expresion entera")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaracion_globalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext
            self._ID = None # Token
            self._ss_expresion = None # Ss_expresionContext

        def tipo(self):
            return self.getTypedRuleContext(LienzoParser.TipoContext,0)


        def GLOBAL(self):
            return self.getToken(LienzoParser.GLOBAL, 0)

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_declaracion_global

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_global" ):
                listener.enterDeclaracion_global(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_global" ):
                listener.exitDeclaracion_global(self)




    def declaracion_global(self):

        localctx = LienzoParser.Declaracion_globalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracion_global)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            localctx._tipo = self.tipo()
            self.state = 98
            self.match(LienzoParser.GLOBAL)
            self.state = 99
            localctx._ID = self.match(LienzoParser.ID)

            if namespaceTable.idAlreadyTaken((None if localctx._ID is None else localctx._ID.text), "global"):
                error((0 if localctx._ID is None else localctx._ID.line), ": Identificador " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarado")

            self.state = 101
            self.match(LienzoParser.EQUALS)
            self.state = 102
            localctx._ss_expresion = self.ss_expresion()
            self.state = 103
            self.match(LienzoParser.T__1)

            if localctx._ss_expresion.type != (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))):
                error((0 if localctx._ID is None else localctx._ID.line), "Variable " + (None if localctx._ID is None else localctx._ID.text) + " es de tipo " + (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))))
            else:
                namespaceTable.addVariable((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))), "global")
                idcontent= memoryregisters.createMemoryRegister((None if localctx._ID is None else localctx._ID.text), "global")
                cuadruplos.addCuadruplo('=', localctx._ss_expresion.valor,None,idcontent)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipoFunc = None # TipoFuncContext
            self._ID = None # Token

        def tipoFunc(self):
            return self.getTypedRuleContext(LienzoParser.TipoFuncContext,0)


        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(LienzoParser.CuerpoContext,0)


        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.ParametroContext)
            else:
                return self.getTypedRuleContext(LienzoParser.ParametroContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)




    def funcion(self):

        localctx = LienzoParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            localctx._tipoFunc = self.tipoFunc()
            self.state = 107
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 108
            self.match(LienzoParser.T__3)
            self.state = 117
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 109
                self.parametro()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__4:
                    self.state = 110
                    self.match(LienzoParser.T__4)
                    self.state = 111
                    self.parametro()
                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 119
            self.match(LienzoParser.T__5)

            global currentFunctionName
            global currentParameterList
            currentFunctionName = (None if localctx._ID is None else localctx._ID.text)
            if not namespaceTable.addFunction(currentFunctionName, (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))), currentParameterList):
                error((0 if localctx._ID is None else localctx._ID.line), "Funcion " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarada")
            else:
                memoryregisters.newFunction(currentFunctionName)
            currentParameterList = []

            self.state = 121
            self.match(LienzoParser.T__0)
            self.state = 122
            self.cuerpo()
            self.state = 123
            self.match(LienzoParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TipoFuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(LienzoParser.TipoContext,0)


        def NADA(self):
            return self.getToken(LienzoParser.NADA, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_tipoFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoFunc" ):
                listener.enterTipoFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoFunc" ):
                listener.exitTipoFunc(self)




    def tipoFunc(self):

        localctx = LienzoParser.TipoFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tipoFunc)
        try:
            self.state = 127
            token = self._input.LA(1)
            if token in [LienzoParser.TEXTO, LienzoParser.BOLEANO, LienzoParser.NUMERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.tipo()

            elif token in [LienzoParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(LienzoParser.NADA)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametroContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext
            self._MODIFICABLE = None # Token
            self._ID = None # Token

        def tipo(self):
            return self.getTypedRuleContext(LienzoParser.TipoContext,0)


        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def MODIFICABLE(self):
            return self.getToken(LienzoParser.MODIFICABLE, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)




    def parametro(self):

        localctx = LienzoParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            localctx._tipo = self.tipo()
            self.state = 131
            _la = self._input.LA(1)
            if _la==LienzoParser.MODIFICABLE:
                self.state = 130
                localctx._MODIFICABLE = self.match(LienzoParser.MODIFICABLE)


            self.state = 133
            localctx._ID = self.match(LienzoParser.ID)

            global currentParameterList
            if (None if localctx._ID is None else localctx._ID.text) in [parameter[0] for parameter in currentParameterList]:
                error((0 if localctx._ID is None else localctx._ID.line), "Parametro " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarado")
            else:
                modificable = False
                if (None if localctx._MODIFICABLE is None else localctx._MODIFICABLE.text):
                    modificable = True
                currentParameterList.append(((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))), modificable))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CuerpoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.DeclaracionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.DeclaracionContext,i)


        def instruccion_aux(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.Instruccion_auxContext)
            else:
                return self.getTypedRuleContext(LienzoParser.Instruccion_auxContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_cuerpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo" ):
                listener.enterCuerpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo" ):
                listener.exitCuerpo(self)




    def cuerpo(self):

        localctx = LienzoParser.CuerpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cuerpo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 136
                self.declaracion()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MIENTRAS) | (1 << LienzoParser.SI) | (1 << LienzoParser.LEER) | (1 << LienzoParser.ESCRIBIR) | (1 << LienzoParser.IMPRIMIR) | (1 << LienzoParser.ID))) != 0):
                self.state = 142
                self.instruccion_aux()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext
            self._ID = None # Token
            self._ss_expresion = None # Ss_expresionContext

        def tipo(self):
            return self.getTypedRuleContext(LienzoParser.TipoContext,0)


        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)




    def declaracion(self):

        localctx = LienzoParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            localctx._tipo = self.tipo()
            self.state = 149
            localctx._ID = self.match(LienzoParser.ID)

            if namespaceTable.idAlreadyTaken((None if localctx._ID is None else localctx._ID.text), currentFunctionName):
                error((0 if localctx._ID is None else localctx._ID.line), ": Identificador " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarado")

            self.state = 151
            self.match(LienzoParser.EQUALS)
            self.state = 152
            localctx._ss_expresion = self.ss_expresion()
            self.state = 153
            self.match(LienzoParser.T__1)

            if localctx._ss_expresion.type != (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))):
                error((0 if localctx._ID is None else localctx._ID.line), "Variable " + (None if localctx._ID is None else localctx._ID.text) + " es de tipo " + (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))))
            else:
                namespaceTable.addVariable((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))), currentFunctionName)
                idcontent= memoryregisters.createMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
                cuadruplos.addCuadruplo('=', localctx._ss_expresion.valor,None,idcontent)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instruccion_auxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(LienzoParser.AsignacionContext,0)


        def condicional(self):
            return self.getTypedRuleContext(LienzoParser.CondicionalContext,0)


        def mientrasQue(self):
            return self.getTypedRuleContext(LienzoParser.MientrasQueContext,0)


        def llamadaFuncionPredefinida(self):
            return self.getTypedRuleContext(LienzoParser.LlamadaFuncionPredefinidaContext,0)


        def llamadaFuncion(self):
            return self.getTypedRuleContext(LienzoParser.LlamadaFuncionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_instruccion_aux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion_aux" ):
                listener.enterInstruccion_aux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion_aux" ):
                listener.exitInstruccion_aux(self)




    def instruccion_aux(self):

        localctx = LienzoParser.Instruccion_auxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_instruccion_aux)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 156
                self.asignacion()
                pass

            elif la_ == 2:
                self.state = 157
                self.condicional()
                pass

            elif la_ == 3:
                self.state = 158
                self.mientrasQue()
                pass

            elif la_ == 4:
                self.state = 159
                self.llamadaFuncionPredefinida()
                pass

            elif la_ == 5:
                self.state = 160
                self.llamadaFuncion()
                pass


            self.state = 163
            self.match(LienzoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LlamadaFuncionPredefinidaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lectura(self):
            return self.getTypedRuleContext(LienzoParser.LecturaContext,0)


        def escritura(self):
            return self.getTypedRuleContext(LienzoParser.EscrituraContext,0)


        def imprimir(self):
            return self.getTypedRuleContext(LienzoParser.ImprimirContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_llamadaFuncionPredefinida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaFuncionPredefinida" ):
                listener.enterLlamadaFuncionPredefinida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaFuncionPredefinida" ):
                listener.exitLlamadaFuncionPredefinida(self)




    def llamadaFuncionPredefinida(self):

        localctx = LienzoParser.LlamadaFuncionPredefinidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_llamadaFuncionPredefinida)
        try:
            self.state = 168
            token = self._input.LA(1)
            if token in [LienzoParser.LEER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.lectura()

            elif token in [LienzoParser.ESCRIBIR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.escritura()

            elif token in [LienzoParser.IMPRIMIR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.imprimir()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LecturaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def LEER(self):
            return self.getToken(LienzoParser.LEER, 0)

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_lectura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLectura" ):
                listener.enterLectura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLectura" ):
                listener.exitLectura(self)




    def lectura(self):

        localctx = LienzoParser.LecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(LienzoParser.LEER)
            self.state = 171
            localctx._ID = self.match(LienzoParser.ID)

            idcontent=memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text),currentFunctionName)
            cuadruplos.addCuadruplo(READ,None,None,idcontent)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EscrituraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext

        def ESCRIBIR(self):
            return self.getToken(LienzoParser.ESCRIBIR, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def EN(self):
            return self.getToken(LienzoParser.EN, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.ExpresionContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_escritura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscritura" ):
                listener.enterEscritura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscritura" ):
                listener.exitEscritura(self)




    def escritura(self):

        localctx = LienzoParser.EscrituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(LienzoParser.ESCRIBIR)
            self.state = 175
            localctx._ss_expresion = self.ss_expresion()
            self.state = 176
            self.match(LienzoParser.EN)
            self.state = 177
            self.expresion()
            self.state = 178
            self.match(LienzoParser.T__4)
            self.state = 179
            self.expresion()

            if localctx._ss_expresion.type == TEXTO:
                cuadruplos.addCuadruplo(PRINT, localctx._ss_expresion.valor, None)
            else:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "solo se pueden imprimir texto")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsignacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._ss_expresion = None # Ss_expresionContext

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = LienzoParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 183
            self.match(LienzoParser.EQUALS)
            self.state = 184
            localctx._ss_expresion = self.ss_expresion()

            idType = namespaceTable.getVariableType((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
            if not idType:
                error((0 if localctx._ID is None else localctx._ID.line), "Variable " + (None if localctx._ID is None else localctx._ID.text) + " no ha sido declarada")
            elif localctx._ss_expresion.type != idType:
               error((0 if localctx._ID is None else localctx._ID.line), "Variable " + (None if localctx._ID is None else localctx._ID.text) + " es de tipo " + idType)
            else:
                idcontent = memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
                cuadruplos.addCuadruplo('=', localctx._ss_expresion.valor, None, idcontent)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TipoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXTO(self):
            return self.getToken(LienzoParser.TEXTO, 0)

        def BOLEANO(self):
            return self.getToken(LienzoParser.BOLEANO, 0)

        def NUMERO(self):
            return self.getToken(LienzoParser.NUMERO, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = LienzoParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImprimirContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPRIMIR(self):
            return self.getToken(LienzoParser.IMPRIMIR, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_imprimir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimir" ):
                listener.enterImprimir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimir" ):
                listener.exitImprimir(self)




    def imprimir(self):

        localctx = LienzoParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(LienzoParser.IMPRIMIR)
            self.state = 190
            self.ss_expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondicionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext

        def SI(self):
            return self.getToken(LienzoParser.SI, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def instruccion_aux(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.Instruccion_auxContext)
            else:
                return self.getTypedRuleContext(LienzoParser.Instruccion_auxContext,i)


        def SINO(self):
            return self.getToken(LienzoParser.SINO, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)




    def condicional(self):

        localctx = LienzoParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(LienzoParser.SI)
            self.state = 193
            self.match(LienzoParser.T__3)
            self.state = 194
            localctx._ss_expresion = self.ss_expresion()
            self.state = 195
            self.match(LienzoParser.T__5)

            if localctx._ss_expresion.type != BOLEANO:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "el estatuto 'si' necesita una boleano")

            self.state = 197
            self.match(LienzoParser.T__0)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MIENTRAS) | (1 << LienzoParser.SI) | (1 << LienzoParser.LEER) | (1 << LienzoParser.ESCRIBIR) | (1 << LienzoParser.IMPRIMIR) | (1 << LienzoParser.ID))) != 0):
                self.state = 198
                self.instruccion_aux()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self.match(LienzoParser.T__2)
            self.state = 214
            _la = self._input.LA(1)
            if _la==LienzoParser.SINO:
                self.state = 205
                self.match(LienzoParser.SINO)
                self.state = 206
                self.match(LienzoParser.T__0)
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MIENTRAS) | (1 << LienzoParser.SI) | (1 << LienzoParser.LEER) | (1 << LienzoParser.ESCRIBIR) | (1 << LienzoParser.IMPRIMIR) | (1 << LienzoParser.ID))) != 0):
                    self.state = 207
                    self.instruccion_aux()
                    self.state = 212
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 213
                self.match(LienzoParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MientrasQueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext

        def MIENTRAS(self):
            return self.getToken(LienzoParser.MIENTRAS, 0)

        def QUE(self):
            return self.getToken(LienzoParser.QUE, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def instruccion_aux(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.Instruccion_auxContext)
            else:
                return self.getTypedRuleContext(LienzoParser.Instruccion_auxContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_mientrasQue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMientrasQue" ):
                listener.enterMientrasQue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMientrasQue" ):
                listener.exitMientrasQue(self)




    def mientrasQue(self):

        localctx = LienzoParser.MientrasQueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_mientrasQue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(LienzoParser.MIENTRAS)
            self.state = 217
            self.match(LienzoParser.QUE)
            self.state = 218
            self.match(LienzoParser.T__3)
            self.state = 219
            localctx._ss_expresion = self.ss_expresion()
            self.state = 220
            self.match(LienzoParser.T__5)

            if localctx._ss_expresion.type != BOLEANO:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "el estatuto 'mientras que' necesita una boleano")

            self.state = 222
            self.match(LienzoParser.T__0)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MIENTRAS) | (1 << LienzoParser.SI) | (1 << LienzoParser.LEER) | (1 << LienzoParser.ESCRIBIR) | (1 << LienzoParser.IMPRIMIR) | (1 << LienzoParser.ID))) != 0):
                self.state = 223
                self.instruccion_aux()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
            self.match(LienzoParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LlamadaFuncionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self._ID = None # Token
            self.ss_exp1 = None # Ss_expresionContext
            self.ss_exp2 = None # Ss_expresionContext

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def ss_expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.Ss_expresionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_llamadaFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaFuncion" ):
                listener.enterLlamadaFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaFuncion" ):
                listener.exitLlamadaFuncion(self)




    def llamadaFuncion(self):

        localctx = LienzoParser.LlamadaFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_llamadaFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            localctx._ID = self.match(LienzoParser.ID)

            functionType = namespaceTable.getFunctionType((None if localctx._ID is None else localctx._ID.text))
            if not functionType:
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": llamada a funcion", (None if localctx._ID is None else localctx._ID.text), "inexistente")
            else:
                localctx.type = None if functionType == "nada" else functionType

            self.state = 233
            self.match(LienzoParser.T__3)
            self.state = 245
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__3) | (1 << LienzoParser.T__15) | (1 << LienzoParser.T__19) | (1 << LienzoParser.BOOLEAN_CONSTANT) | (1 << LienzoParser.NUMERIC_CONSTANT) | (1 << LienzoParser.STRING_CONSTANT) | (1 << LienzoParser.ID))) != 0):
                self.state = 234
                localctx.ss_exp1 = self.ss_expresion()

                global currentArgumentList
                currentArgumentList.append(((None if localctx.ss_exp1 is None else self._input.getText((localctx.ss_exp1.start,localctx.ss_exp1.stop))), localctx.ss_exp1.type))

                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__4:
                    self.state = 236
                    self.match(LienzoParser.T__4)
                    self.state = 237
                    localctx.ss_exp2 = self.ss_expresion()

                    currentArgumentList.append(((None if localctx.ss_exp2 is None else self._input.getText((localctx.ss_exp2.start,localctx.ss_exp2.stop))), localctx.ss_exp2.type))

                    self.state = 244
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 247
            self.match(LienzoParser.T__5)

            if not namespaceTable.argumentsAgree((None if localctx._ID is None else localctx._ID.text), currentArgumentList):
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": llamada a funcion", (None if localctx._ID is None else localctx._ID.text), ": argumentos incorrectos")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ss_expresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.valor = None
            self.s_exp1 = None # S_expresionContext
            self.op = None # Token
            self.s_exp2 = None # S_expresionContext

        def s_expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.S_expresionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.S_expresionContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_ss_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSs_expresion" ):
                listener.enterSs_expresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSs_expresion" ):
                listener.exitSs_expresion(self)




    def ss_expresion(self):

        localctx = LienzoParser.Ss_expresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ss_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            localctx.s_exp1 = self.s_expresion()

            localctx.type = localctx.s_exp1.type
            localctx.valor = localctx.s_exp1.valor

            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.T__6 or _la==LienzoParser.T__7:
                self.state = 252
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__6 or _la==LienzoParser.T__7):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 253
                localctx.s_exp2 = self.s_expresion()

                localctx.type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.s_exp2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.s_exp2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.s_exp2.valor)

                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class S_expresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.valor = None
            self.exp1 = None # ExpresionContext
            self.op = None # Token
            self.exp2 = None # ExpresionContext

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.ExpresionContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_s_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS_expresion" ):
                listener.enterS_expresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS_expresion" ):
                listener.exitS_expresion(self)




    def s_expresion(self):

        localctx = LienzoParser.S_expresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_s_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            localctx.exp1 = self.expresion()

            localctx.type = localctx.exp1.type
            localctx.valor = localctx.exp1.valor

            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__8) | (1 << LienzoParser.T__9) | (1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12) | (1 << LienzoParser.T__13))) != 0):
                self.state = 263
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__8) | (1 << LienzoParser.T__9) | (1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12) | (1 << LienzoParser.T__13))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 264
                localctx.exp2 = self.expresion()

                localctx.type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.exp2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.exp2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.exp2.valor)

                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.valor = None
            self.term1 = None # TerminoContext
            self.op = None # Token
            self.term2 = None # TerminoContext

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.TerminoContext)
            else:
                return self.getTypedRuleContext(LienzoParser.TerminoContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = LienzoParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            localctx.term1 = self.termino()

            localctx.type = localctx.term1.type
            localctx.valor = localctx.term1.valor

            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.T__14 or _la==LienzoParser.T__15:
                self.state = 275
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__14 or _la==LienzoParser.T__15):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 276
                localctx.term2 = self.termino()

                type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.term2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.term2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.term2.valor)

                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TerminoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.valor = None
            self.factor1 = None # FactorContext
            self.op = None # Token
            self.factor2 = None # FactorContext

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.FactorContext)
            else:
                return self.getTypedRuleContext(LienzoParser.FactorContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = LienzoParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            localctx.factor1 = self.factor()

            localctx.type = localctx.factor1.type
            localctx.valor = localctx.factor1.valor

            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__16) | (1 << LienzoParser.T__17) | (1 << LienzoParser.T__18))) != 0):
                self.state = 287
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__16) | (1 << LienzoParser.T__17) | (1 << LienzoParser.T__18))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 288
                localctx.factor2 = self.factor()

                type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.factor2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.factor2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.factor2.valor)

                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.valor = None
            self.neg = None # Token
            self._factor_aux = None # Factor_auxContext
            self._NUMERIC_CONSTANT = None # Token
            self._STRING_CONSTANT = None # Token

        def factor_aux(self):
            return self.getTypedRuleContext(LienzoParser.Factor_auxContext,0)


        def NUMERIC_CONSTANT(self):
            return self.getToken(LienzoParser.NUMERIC_CONSTANT, 0)

        def STRING_CONSTANT(self):
            return self.getToken(LienzoParser.STRING_CONSTANT, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = LienzoParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 311
            token = self._input.LA(1)
            if token in [LienzoParser.T__3, LienzoParser.T__19, LienzoParser.BOOLEAN_CONSTANT, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                _la = self._input.LA(1)
                if _la==LienzoParser.T__19:
                    self.state = 296
                    localctx.neg = self.match(LienzoParser.T__19)


                self.state = 299
                localctx._factor_aux = self.factor_aux()

                localctx.type = localctx._factor_aux.type
                if (None if localctx.neg is None else localctx.neg.text) and localctx._factor_aux.type != BOLEANO:
                    error((0 if localctx.neg is None else localctx.neg.line), "operador " + (None if localctx.neg is None else localctx.neg.text) + " no puede ser aplicado a " + localctx._factor_aux.type)
                    localctx.type = None
                else:
                    if (None if localctx.neg is None else localctx.neg.text):
                        localctx.valor = cuadruplos.addCuadruplo((None if localctx.neg is None else localctx.neg.text), localctx._factor_aux.valor, None)
                    else:
                        localctx.valor = localctx._factor_aux.valor


            elif token in [LienzoParser.T__15, LienzoParser.NUMERIC_CONSTANT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                _la = self._input.LA(1)
                if _la==LienzoParser.T__15:
                    self.state = 303
                    localctx.neg = self.match(LienzoParser.T__15)


                self.state = 306
                localctx._NUMERIC_CONSTANT = self.match(LienzoParser.NUMERIC_CONSTANT)

                localctx.type = NUMERO

                if (None if localctx.neg is None else localctx.neg.text):
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.neg is None else localctx.neg.text),num((None if localctx._NUMERIC_CONSTANT is None else localctx._NUMERIC_CONSTANT.text)),None)
                else:
                    localctx.valor = num((None if localctx._NUMERIC_CONSTANT is None else localctx._NUMERIC_CONSTANT.text))


            elif token in [LienzoParser.STRING_CONSTANT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                localctx._STRING_CONSTANT = self.match(LienzoParser.STRING_CONSTANT)

                localctx.type = TEXTO
                localctx.valor = (None if localctx._STRING_CONSTANT is None else localctx._STRING_CONSTANT.text)[1:-1]


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Factor_auxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.valor = None
            self._ID = None # Token
            self._BOOLEAN_CONSTANT = None # Token
            self._llamadaFuncion = None # LlamadaFuncionContext
            self._ss_expresion = None # Ss_expresionContext

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def BOOLEAN_CONSTANT(self):
            return self.getToken(LienzoParser.BOOLEAN_CONSTANT, 0)

        def llamadaFuncion(self):
            return self.getTypedRuleContext(LienzoParser.LlamadaFuncionContext,0)


        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_factor_aux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_aux" ):
                listener.enterFactor_aux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_aux" ):
                listener.exitFactor_aux(self)




    def factor_aux(self):

        localctx = LienzoParser.Factor_auxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_factor_aux)
        try:
            self.state = 325
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                localctx._ID = self.match(LienzoParser.ID)

                localctx.type = namespaceTable.getVariableType((None if localctx._ID is None else localctx._ID.text), currentFunctionName)

                if localctx.type:
                    localctx.valor = memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
                else:
                    localctx.valor = None
                    errir((0 if localctx._ID is None else localctx._ID.line), "variable " + (None if localctx._ID is None else localctx._ID.text) + " no ha sido declarada")


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                localctx._BOOLEAN_CONSTANT = self.match(LienzoParser.BOOLEAN_CONSTANT)

                localctx.type = BOLEANO
                localctx.valor = True if (None if localctx._BOOLEAN_CONSTANT is None else localctx._BOOLEAN_CONSTANT.text) == 'verdadero' else False

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
                localctx._llamadaFuncion = self.llamadaFuncion()

                functionType = localctx._llamadaFuncion.type
                localctx.type = functionType if functionType != "nada" else None
                if functionType:
                    pass
                else:
                    localctx.valor = None

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 320
                self.match(LienzoParser.T__3)
                self.state = 321
                localctx._ss_expresion = self.ss_expresion()
                self.state = 322
                self.match(LienzoParser.T__5)

                localctx.type = localctx._ss_expresion.type
                if localctx.type:
                    localctx.valor = localctx._ss_expresion.valor
                else:
                    localctx.valor = None

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DibujoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._DIBUJO = None # Token

        def DIBUJO(self):
            return self.getToken(LienzoParser.DIBUJO, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(LienzoParser.CuerpoContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_dibujo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDibujo" ):
                listener.enterDibujo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDibujo" ):
                listener.exitDibujo(self)




    def dibujo(self):

        localctx = LienzoParser.DibujoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_dibujo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            localctx._DIBUJO = self.match(LienzoParser.DIBUJO)

            global currentFunctionName
            currentFunctionName = (None if localctx._DIBUJO is None else localctx._DIBUJO.text)
            namespaceTable.addFunction(currentFunctionName, "nada", [])
            memoryregisters.newFunction(currentFunctionName)

            self.state = 329
            self.match(LienzoParser.T__0)
            self.state = 330
            self.cuerpo()
            self.state = 331
            self.match(LienzoParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





