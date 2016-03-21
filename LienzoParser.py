# Generated from Lienzo.g4 by ANTLR 4.5.2
# encoding: utf-8
from antlr4 import *
from io import StringIO


from namespace import NamespaceTable
from collections import defaultdict
from MemoryRegister import MemoryRegisters
from cuadruplos import Cuadruplos

namespaceTable = NamespaceTable()
currentFunctionName = ""
currentParameterList = []
currentArgumentList = []

memoryregisters = MemoryRegisters()
cuadruplos = Cuadruplos()

diccionario_ids = {}

CONDICION = "condicion"
MENSAJE = "mensaje"
NUMERO = "numero"

cubo = {}
cubo[CONDICION] = {}
cubo[MENSAJE] = {}
cubo[NUMERO] = {}

# Condiciones
cubo[CONDICION]['+'] = defaultdict(lambda: None, {})
cubo[CONDICION]['-'] = defaultdict(lambda: None, {})
cubo[CONDICION]['*'] = defaultdict(lambda: None, {})
cubo[CONDICION]['/'] = defaultdict(lambda: None, {})
cubo[CONDICION]['%'] = defaultdict(lambda: None, {})
cubo[CONDICION]['<'] = defaultdict(lambda: None, {})
cubo[CONDICION]['>'] = defaultdict(lambda: None, {})
cubo[CONDICION]['<='] = defaultdict(lambda: None, {})
cubo[CONDICION]['>='] = defaultdict(lambda: None, {})
cubo[CONDICION]['=='] = defaultdict(lambda: None, {CONDICION : CONDICION})
cubo[CONDICION]['!='] = defaultdict(lambda: None, {CONDICION : CONDICION})
cubo[CONDICION]['&'] = defaultdict(lambda: None, {CONDICION : CONDICION})
cubo[CONDICION]['|'] = defaultdict(lambda: None, {CONDICION : CONDICION})

# Mensajes
cubo[MENSAJE]['+'] = defaultdict(lambda: None, {MENSAJE : MENSAJE})
cubo[MENSAJE]['-'] = defaultdict(lambda: None, {})
cubo[MENSAJE]['*'] = defaultdict(lambda: None, {})
cubo[MENSAJE]['/'] = defaultdict(lambda: None, {})
cubo[MENSAJE]['%'] = defaultdict(lambda: None, {})
cubo[MENSAJE]['<'] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['>'] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['<='] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['>='] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['=='] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['!='] = defaultdict(lambda: None, {MENSAJE : CONDICION})
cubo[MENSAJE]['&'] = defaultdict(lambda: None, {})
cubo[MENSAJE]['|'] = defaultdict(lambda: None, {})

# Numero
cubo[NUMERO]['+'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['-'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['*'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['/'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['%'] = defaultdict(lambda: None, {NUMERO : NUMERO})
cubo[NUMERO]['<'] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['>'] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['<='] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['>='] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['=='] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['!='] = defaultdict(lambda: None, {NUMERO : CONDICION})
cubo[NUMERO]['&'] = defaultdict(lambda: None, {})
cubo[NUMERO]['|'] = defaultdict(lambda: None, {})

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3H")
        buf.write("\u017f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\7\3Q\n\3\f\3\16\3T\13\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7p\n\7")
        buf.write("\f\7\16\7s\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\7\r\u0095\n\r\f")
        buf.write("\r\16\r\u0098\13\r\3\r\7\r\u009b\n\r\f\r\16\r\u009e\13")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\5\17\u00b0\n\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\7\24\u00cd\n\24\f\24\16\24\u00d0\13\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00df\n\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\7\27\u00e8\n\27\f\27\16\27\u00eb\13\27\3\27\3")
        buf.write("\27\3\27\3\27\7\27\u00f1\n\27\f\27\16\27\u00f4\13\27\3")
        buf.write("\27\5\27\u00f7\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\7\30\u0101\n\30\f\30\16\30\u0104\13\30\5\30\u0106")
        buf.write("\n\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31")
        buf.write("\u0111\n\31\f\31\16\31\u0114\13\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\7\32\u011d\n\32\f\32\16\32\u0120\13\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0129\n\33\f")
        buf.write("\33\16\33\u012c\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7")
        buf.write("\34\u0134\n\34\f\34\16\34\u0137\13\34\3\35\5\35\u013a")
        buf.write("\n\35\3\35\3\35\3\35\3\35\3\35\5\35\u0141\n\35\3\35\3")
        buf.write("\35\3\35\3\35\5\35\u0147\n\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0155\n\36\3")
        buf.write("\37\3\37\3\37\7\37\u015a\n\37\f\37\16\37\u015d\13\37\3")
        buf.write("\37\3\37\3 \3 \3 \3 \3 \3 \7 \u0167\n \f \16 \u016a\13")
        buf.write(" \5 \u016c\n \3 \3 \3 \3 \3 \3 \3!\3!\5!\u0176\n!\3\"")
        buf.write("\3\"\5\"\u017a\n\"\3\"\3\"\3\"\3\"\2\2#\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@B\2")
        buf.write("\13\3\2\36 \3\2!*\3\2\63\64\3\2;=\4\2FFHH\3\2\13\f\3\2")
        buf.write("\r\22\3\2\23\24\3\2\25\27\u017f\2D\3\2\2\2\4M\3\2\2\2")
        buf.write("\6W\3\2\2\2\bb\3\2\2\2\nd\3\2\2\2\ff\3\2\2\2\16v\3\2\2")
        buf.write("\2\20|\3\2\2\2\22\u0084\3\2\2\2\24\u008b\3\2\2\2\26\u008d")
        buf.write("\3\2\2\2\30\u0096\3\2\2\2\32\u009f\3\2\2\2\34\u00af\3")
        buf.write("\2\2\2\36\u00b3\3\2\2\2 \u00b8\3\2\2\2\"\u00ba\3\2\2\2")
        buf.write("$\u00c1\3\2\2\2&\u00c4\3\2\2\2(\u00d3\3\2\2\2*\u00d9\3")
        buf.write("\2\2\2,\u00e0\3\2\2\2.\u00f8\3\2\2\2\60\u010a\3\2\2\2")
        buf.write("\62\u0115\3\2\2\2\64\u0121\3\2\2\2\66\u012d\3\2\2\28\u0146")
        buf.write("\3\2\2\2:\u0154\3\2\2\2<\u0156\3\2\2\2>\u0160\3\2\2\2")
        buf.write("@\u0175\3\2\2\2B\u0177\3\2\2\2DE\7\32\2\2EF\7\3\2\2FG")
        buf.write("\5\4\3\2GH\5\f\7\2HI\5<\37\2IJ\5\26\f\2JK\7\4\2\2KL\7")
        buf.write("\2\2\3L\3\3\2\2\2MN\7\33\2\2NR\7\3\2\2OQ\5\6\4\2PO\3\2")
        buf.write("\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2")
        buf.write("UV\7\4\2\2V\5\3\2\2\2WX\7E\2\2XY\5\b\5\2YZ\5\n\6\2Z[\7")
        buf.write("\34\2\2[\\\7G\2\2\\]\7\35\2\2]^\5\64\33\2^_\7\60\2\2_")
        buf.write("`\5\64\33\2`a\7\5\2\2a\7\3\2\2\2bc\t\2\2\2c\t\3\2\2\2")
        buf.write("de\t\3\2\2e\13\3\2\2\2fg\7+\2\2gh\7\3\2\2hi\5\16\b\2i")
        buf.write("j\7\5\2\2jk\5\20\t\2kq\7\5\2\2lm\5\22\n\2mn\7\5\2\2np")
        buf.write("\3\2\2\2ol\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt\3\2")
        buf.write("\2\2sq\3\2\2\2tu\7\4\2\2u\r\3\2\2\2vw\7,\2\2wx\7\35\2")
        buf.write("\2xy\7-\2\2yz\7.\2\2z{\5\n\6\2{\17\3\2\2\2|}\7/\2\2}~")
        buf.write("\7\35\2\2~\177\7-\2\2\177\u0080\7.\2\2\u0080\u0081\5\64")
        buf.write("\33\2\u0081\u0082\7\60\2\2\u0082\u0083\5\64\33\2\u0083")
        buf.write("\21\3\2\2\2\u0084\u0085\7\62\2\2\u0085\u0086\5\24\13\2")
        buf.write("\u0086\u0087\7\35\2\2\u0087\u0088\5*\26\2\u0088\u0089")
        buf.write("\7.\2\2\u0089\u008a\5\64\33\2\u008a\23\3\2\2\2\u008b\u008c")
        buf.write("\t\4\2\2\u008c\25\3\2\2\2\u008d\u008e\7\65\2\2\u008e\u008f")
        buf.write("\b\f\1\2\u008f\u0090\7\3\2\2\u0090\u0091\5\30\r\2\u0091")
        buf.write("\u0092\7\4\2\2\u0092\27\3\2\2\2\u0093\u0095\5\32\16\2")
        buf.write("\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3")
        buf.write("\2\2\2\u0096\u0097\3\2\2\2\u0097\u009c\3\2\2\2\u0098\u0096")
        buf.write("\3\2\2\2\u0099\u009b\5\34\17\2\u009a\u0099\3\2\2\2\u009b")
        buf.write("\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2")
        buf.write("\u009d\31\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\5 \21")
        buf.write("\2\u00a0\u00a1\7H\2\2\u00a1\u00a2\b\16\1\2\u00a2\u00a3")
        buf.write("\7.\2\2\u00a3\u00a4\5\60\31\2\u00a4\u00a5\7\5\2\2\u00a5")
        buf.write("\u00a6\b\16\1\2\u00a6\33\3\2\2\2\u00a7\u00b0\5\36\20\2")
        buf.write("\u00a8\u00b0\5\"\22\2\u00a9\u00b0\5$\23\2\u00aa\u00b0")
        buf.write("\5&\24\2\u00ab\u00b0\5(\25\2\u00ac\u00b0\5\22\n\2\u00ad")
        buf.write("\u00b0\5,\27\2\u00ae\u00b0\5.\30\2\u00af\u00a7\3\2\2\2")
        buf.write("\u00af\u00a8\3\2\2\2\u00af\u00a9\3\2\2\2\u00af\u00aa\3")
        buf.write("\2\2\2\u00af\u00ab\3\2\2\2\u00af\u00ac\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("\u00b2\7\5\2\2\u00b2\35\3\2\2\2\u00b3\u00b4\7H\2\2\u00b4")
        buf.write("\u00b5\7.\2\2\u00b5\u00b6\5\60\31\2\u00b6\u00b7\b\20\1")
        buf.write("\2\u00b7\37\3\2\2\2\u00b8\u00b9\t\5\2\2\u00b9!\3\2\2\2")
        buf.write("\u00ba\u00bb\7?\2\2\u00bb\u00bc\t\6\2\2\u00bc\u00bd\7")
        buf.write("\61\2\2\u00bd\u00be\5\64\33\2\u00be\u00bf\7\6\2\2\u00bf")
        buf.write("\u00c0\5\64\33\2\u00c0#\3\2\2\2\u00c1\u00c2\7\66\2\2\u00c2")
        buf.write("\u00c3\5\64\33\2\u00c3%\3\2\2\2\u00c4\u00c5\7\67\2\2\u00c5")
        buf.write("\u00c6\78\2\2\u00c6\u00c7\7\7\2\2\u00c7\u00c8\5\60\31")
        buf.write("\2\u00c8\u00c9\7\b\2\2\u00c9\u00ca\b\24\1\2\u00ca\u00ce")
        buf.write("\7\3\2\2\u00cb\u00cd\5\34\17\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d1\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d2\7")
        buf.write("\4\2\2\u00d2\'\3\2\2\2\u00d3\u00d4\7,\2\2\u00d4\u00d5")
        buf.write("\7\35\2\2\u00d5\u00d6\5*\26\2\u00d6\u00d7\7.\2\2\u00d7")
        buf.write("\u00d8\5\n\6\2\u00d8)\3\2\2\2\u00d9\u00de\7G\2\2\u00da")
        buf.write("\u00db\7\t\2\2\u00db\u00dc\5\64\33\2\u00dc\u00dd\7\n\2")
        buf.write("\2\u00dd\u00df\3\2\2\2\u00de\u00da\3\2\2\2\u00de\u00df")
        buf.write("\3\2\2\2\u00df+\3\2\2\2\u00e0\u00e1\79\2\2\u00e1\u00e2")
        buf.write("\7\7\2\2\u00e2\u00e3\5\60\31\2\u00e3\u00e4\7\b\2\2\u00e4")
        buf.write("\u00e5\b\27\1\2\u00e5\u00e9\7\3\2\2\u00e6\u00e8\5\34\17")
        buf.write("\2\u00e7\u00e6\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00ec\u00f6\7\4\2\2\u00ed\u00ee\7:\2\2")
        buf.write("\u00ee\u00f2\7\3\2\2\u00ef\u00f1\5\34\17\2\u00f0\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f5\u00f7\7\4\2\2\u00f6\u00ed\3\2\2\2\u00f6\u00f7\3")
        buf.write("\2\2\2\u00f7-\3\2\2\2\u00f8\u00f9\7H\2\2\u00f9\u0105\7")
        buf.write("\7\2\2\u00fa\u00fb\5\60\31\2\u00fb\u0102\b\30\1\2\u00fc")
        buf.write("\u00fd\7\6\2\2\u00fd\u00fe\5\60\31\2\u00fe\u00ff\b\30")
        buf.write("\1\2\u00ff\u0101\3\2\2\2\u0100\u00fc\3\2\2\2\u0101\u0104")
        buf.write("\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103")
        buf.write("\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u00fa\3\2\2\2")
        buf.write("\u0105\u0106\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\7")
        buf.write("\b\2\2\u0108\u0109\b\30\1\2\u0109/\3\2\2\2\u010a\u010b")
        buf.write("\5\62\32\2\u010b\u0112\b\31\1\2\u010c\u010d\t\7\2\2\u010d")
        buf.write("\u010e\5\62\32\2\u010e\u010f\b\31\1\2\u010f\u0111\3\2")
        buf.write("\2\2\u0110\u010c\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110")
        buf.write("\3\2\2\2\u0112\u0113\3\2\2\2\u0113\61\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0115\u0116\5\64\33\2\u0116\u011e\b\32\1\2\u0117")
        buf.write("\u0118\t\b\2\2\u0118\u0119\5\64\33\2\u0119\u011a\3\2\2")
        buf.write("\2\u011a\u011b\b\32\1\2\u011b\u011d\3\2\2\2\u011c\u0117")
        buf.write("\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2\2\u011e")
        buf.write("\u011f\3\2\2\2\u011f\63\3\2\2\2\u0120\u011e\3\2\2\2\u0121")
        buf.write("\u0122\5\66\34\2\u0122\u012a\b\33\1\2\u0123\u0124\t\t")
        buf.write("\2\2\u0124\u0125\5\66\34\2\u0125\u0126\3\2\2\2\u0126\u0127")
        buf.write("\b\33\1\2\u0127\u0129\3\2\2\2\u0128\u0123\3\2\2\2\u0129")
        buf.write("\u012c\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\65\3\2\2\2\u012c\u012a\3\2\2\2\u012d\u012e\58\35")
        buf.write("\2\u012e\u0135\b\34\1\2\u012f\u0130\t\n\2\2\u0130\u0131")
        buf.write("\58\35\2\u0131\u0132\b\34\1\2\u0132\u0134\3\2\2\2\u0133")
        buf.write("\u012f\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2")
        buf.write("\u0135\u0136\3\2\2\2\u0136\67\3\2\2\2\u0137\u0135\3\2")
        buf.write("\2\2\u0138\u013a\7\30\2\2\u0139\u0138\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\5:\36\2\u013c")
        buf.write("\u013d\3\2\2\2\u013d\u013e\b\35\1\2\u013e\u0147\3\2\2")
        buf.write("\2\u013f\u0141\7\24\2\2\u0140\u013f\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\7E\2\2\u0143")
        buf.write("\u0147\b\35\1\2\u0144\u0145\7F\2\2\u0145\u0147\b\35\1")
        buf.write("\2\u0146\u0139\3\2\2\2\u0146\u0140\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u01479\3\2\2\2\u0148\u0149\7H\2\2\u0149\u0155")
        buf.write("\b\36\1\2\u014a\u014b\7A\2\2\u014b\u0155\b\36\1\2\u014c")
        buf.write("\u014d\5.\30\2\u014d\u014e\b\36\1\2\u014e\u0155\3\2\2")
        buf.write("\2\u014f\u0150\7\7\2\2\u0150\u0151\5\60\31\2\u0151\u0152")
        buf.write("\7\b\2\2\u0152\u0153\b\36\1\2\u0153\u0155\3\2\2\2\u0154")
        buf.write("\u0148\3\2\2\2\u0154\u014a\3\2\2\2\u0154\u014c\3\2\2\2")
        buf.write("\u0154\u014f\3\2\2\2\u0155;\3\2\2\2\u0156\u0157\7>\2\2")
        buf.write("\u0157\u015b\7\3\2\2\u0158\u015a\5> \2\u0159\u0158\3\2")
        buf.write("\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015c\u015e\3\2\2\2\u015d\u015b\3\2\2\2\u015e")
        buf.write("\u015f\7\4\2\2\u015f=\3\2\2\2\u0160\u0161\5@!\2\u0161")
        buf.write("\u0162\7H\2\2\u0162\u016b\7\7\2\2\u0163\u0168\5B\"\2\u0164")
        buf.write("\u0165\7\6\2\2\u0165\u0167\5B\"\2\u0166\u0164\3\2\2\2")
        buf.write("\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3")
        buf.write("\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u0163")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016e\7\b\2\2\u016e\u016f\b \1\2\u016f\u0170\7\3\2\2")
        buf.write("\u0170\u0171\5\30\r\2\u0171\u0172\7\4\2\2\u0172?\3\2\2")
        buf.write("\2\u0173\u0176\5 \21\2\u0174\u0176\7@\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0175\u0174\3\2\2\2\u0176A\3\2\2\2\u0177\u0179")
        buf.write("\5 \21\2\u0178\u017a\7D\2\2\u0179\u0178\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\7H\2\2")
        buf.write("\u017c\u017d\b\"\1\2\u017dC\3\2\2\2\33Rq\u0096\u009c\u00af")
        buf.write("\u00ce\u00de\u00e9\u00f2\u00f6\u0102\u0105\u0112\u011e")
        buf.write("\u012a\u0135\u0139\u0140\u0146\u0154\u015b\u0168\u016b")
        buf.write("\u0175\u0179")
        return buf.getvalue()


class LienzoParser ( Parser ):

    grammarFileName = "Lienzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "','", "'('", "')'", 
                     "'['", "']'", "'&'", "'|'", "'=='", "'!='", "'>'", 
                     "'<'", "'>='", "'<='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "<INVALID>", "'dibujo'", "'materiales'", 
                     "'llamado'", "'de'", "'ovalo'", "'rectangulo'", "'triangulo'", 
                     "'rojo'", "'verde'", "'amarillo'", "'azul'", "'blanco'", 
                     "'negro'", "'morado'", "'naranja'", "'cafe'", "'gris'", 
                     "'escenario'", "'color'", "'lienzo'", "'='", "'tamano'", 
                     "'por'", "'en'", "'posicion'", "'x'", "'y'", "'animacion'", 
                     "'dormir'", "'mientras'", "'que'", "'si'", "'sino'", 
                     "'mensaje'", "'condicion'", "'numero'", "'funciones'", 
                     "'mostrar'", "'nada'", "<INVALID>", "'verdadero'", 
                     "'falso'", "'modificable'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "DIBUJO", 
                      "MATERIALES", "LLAMADO", "DE", "OVALO", "RECTANGULO", 
                      "TRIANGULO", "ROJO", "VERDE", "AMARILLO", "AZUL", 
                      "BLANCO", "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", 
                      "ESCENARIO", "COLOR", "LIENZO", "EQUALS", "TAMANO", 
                      "POR", "EN", "POSICION", "X", "Y", "ANIMACION", "DORMIR", 
                      "MIENTRAS", "QUE", "SI", "SINO", "MENSAJE", "CONDICION", 
                      "NUMERO", "FUNCIONES", "MOSTRAR", "NADA", "CONDITION_CONSTANT", 
                      "VERDADERO", "FALSO", "MODIFICABLE", "NUMERIC_CONSTANT", 
                      "STRING_CONSTANT", "NOMBRE_PROPIO", "ID" ]

    RULE_program = 0
    RULE_materiales = 1
    RULE_material = 2
    RULE_tipoFigura = 3
    RULE_color = 4
    RULE_escenario = 5
    RULE_colorLienzo = 6
    RULE_tamanoLienzo = 7
    RULE_posicion = 8
    RULE_coord = 9
    RULE_animacion = 10
    RULE_cuerpo = 11
    RULE_declaracion = 12
    RULE_instruccion = 13
    RULE_asignacion = 14
    RULE_tipo = 15
    RULE_mostrarMensaje = 16
    RULE_dormir = 17
    RULE_mientrasQue = 18
    RULE_cambioColor = 19
    RULE_figura = 20
    RULE_condicional = 21
    RULE_llamadaFuncion = 22
    RULE_ss_expresion = 23
    RULE_s_expresion = 24
    RULE_expresion = 25
    RULE_termino = 26
    RULE_factor = 27
    RULE_factor_aux = 28
    RULE_funciones = 29
    RULE_func = 30
    RULE_tipoFunc = 31
    RULE_parametro = 32

    ruleNames =  [ "program", "materiales", "material", "tipoFigura", "color", 
                   "escenario", "colorLienzo", "tamanoLienzo", "posicion", 
                   "coord", "animacion", "cuerpo", "declaracion", "instruccion", 
                   "asignacion", "tipo", "mostrarMensaje", "dormir", "mientrasQue", 
                   "cambioColor", "figura", "condicional", "llamadaFuncion", 
                   "ss_expresion", "s_expresion", "expresion", "termino", 
                   "factor", "factor_aux", "funciones", "func", "tipoFunc", 
                   "parametro" ]

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
    T__20=21
    T__21=22
    WS=23
    DIBUJO=24
    MATERIALES=25
    LLAMADO=26
    DE=27
    OVALO=28
    RECTANGULO=29
    TRIANGULO=30
    ROJO=31
    VERDE=32
    AMARILLO=33
    AZUL=34
    BLANCO=35
    NEGRO=36
    MORADO=37
    NARANJA=38
    CAFE=39
    GRIS=40
    ESCENARIO=41
    COLOR=42
    LIENZO=43
    EQUALS=44
    TAMANO=45
    POR=46
    EN=47
    POSICION=48
    X=49
    Y=50
    ANIMACION=51
    DORMIR=52
    MIENTRAS=53
    QUE=54
    SI=55
    SINO=56
    MENSAJE=57
    CONDICION=58
    NUMERO=59
    FUNCIONES=60
    MOSTRAR=61
    NADA=62
    CONDITION_CONSTANT=63
    VERDADERO=64
    FALSO=65
    MODIFICABLE=66
    NUMERIC_CONSTANT=67
    STRING_CONSTANT=68
    NOMBRE_PROPIO=69
    ID=70

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIBUJO(self):
            return self.getToken(LienzoParser.DIBUJO, 0)

        def materiales(self):
            return self.getTypedRuleContext(LienzoParser.MaterialesContext,0)


        def escenario(self):
            return self.getTypedRuleContext(LienzoParser.EscenarioContext,0)


        def funciones(self):
            return self.getTypedRuleContext(LienzoParser.FuncionesContext,0)


        def animacion(self):
            return self.getTypedRuleContext(LienzoParser.AnimacionContext,0)


        def EOF(self):
            return self.getToken(LienzoParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(LienzoParser.DIBUJO)
            self.state = 67
            self.match(LienzoParser.T__0)
            self.state = 68
            self.materiales()
            self.state = 69
            self.escenario()
            self.state = 70
            self.funciones()
            self.state = 71
            self.animacion()
            self.state = 72
            self.match(LienzoParser.T__1)
            self.state = 73
            self.match(LienzoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MaterialesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATERIALES(self):
            return self.getToken(LienzoParser.MATERIALES, 0)

        def material(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.MaterialContext)
            else:
                return self.getTypedRuleContext(LienzoParser.MaterialContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_materiales

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMateriales" ):
                listener.enterMateriales(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMateriales" ):
                listener.exitMateriales(self)




    def materiales(self):

        localctx = LienzoParser.MaterialesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_materiales)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(LienzoParser.MATERIALES)
            self.state = 76
            self.match(LienzoParser.T__0)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.NUMERIC_CONSTANT:
                self.state = 77
                self.material()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self.match(LienzoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MaterialContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERIC_CONSTANT(self):
            return self.getToken(LienzoParser.NUMERIC_CONSTANT, 0)

        def tipoFigura(self):
            return self.getTypedRuleContext(LienzoParser.TipoFiguraContext,0)


        def color(self):
            return self.getTypedRuleContext(LienzoParser.ColorContext,0)


        def LLAMADO(self):
            return self.getToken(LienzoParser.LLAMADO, 0)

        def NOMBRE_PROPIO(self):
            return self.getToken(LienzoParser.NOMBRE_PROPIO, 0)

        def DE(self):
            return self.getToken(LienzoParser.DE, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.ExpresionContext,i)


        def POR(self):
            return self.getToken(LienzoParser.POR, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_material

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaterial" ):
                listener.enterMaterial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaterial" ):
                listener.exitMaterial(self)




    def material(self):

        localctx = LienzoParser.MaterialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_material)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(LienzoParser.NUMERIC_CONSTANT)
            self.state = 86
            self.tipoFigura()
            self.state = 87
            self.color()
            self.state = 88
            self.match(LienzoParser.LLAMADO)
            self.state = 89
            self.match(LienzoParser.NOMBRE_PROPIO)
            self.state = 90
            self.match(LienzoParser.DE)
            self.state = 91
            self.expresion()
            self.state = 92
            self.match(LienzoParser.POR)
            self.state = 93
            self.expresion()
            self.state = 94
            self.match(LienzoParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TipoFiguraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OVALO(self):
            return self.getToken(LienzoParser.OVALO, 0)

        def RECTANGULO(self):
            return self.getToken(LienzoParser.RECTANGULO, 0)

        def TRIANGULO(self):
            return self.getToken(LienzoParser.TRIANGULO, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_tipoFigura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoFigura" ):
                listener.enterTipoFigura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoFigura" ):
                listener.exitTipoFigura(self)




    def tipoFigura(self):

        localctx = LienzoParser.TipoFiguraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipoFigura)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.OVALO) | (1 << LienzoParser.RECTANGULO) | (1 << LienzoParser.TRIANGULO))) != 0)):
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
        self.enterRule(localctx, 8, self.RULE_color)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
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

    class EscenarioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCENARIO(self):
            return self.getToken(LienzoParser.ESCENARIO, 0)

        def colorLienzo(self):
            return self.getTypedRuleContext(LienzoParser.ColorLienzoContext,0)


        def tamanoLienzo(self):
            return self.getTypedRuleContext(LienzoParser.TamanoLienzoContext,0)


        def posicion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.PosicionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.PosicionContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_escenario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscenario" ):
                listener.enterEscenario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscenario" ):
                listener.exitEscenario(self)




    def escenario(self):

        localctx = LienzoParser.EscenarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_escenario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(LienzoParser.ESCENARIO)
            self.state = 101
            self.match(LienzoParser.T__0)
            self.state = 102
            self.colorLienzo()
            self.state = 103
            self.match(LienzoParser.T__2)
            self.state = 104
            self.tamanoLienzo()
            self.state = 105
            self.match(LienzoParser.T__2)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.POSICION:
                self.state = 106
                self.posicion()
                self.state = 107
                self.match(LienzoParser.T__2)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(LienzoParser.T__1)
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
        self.enterRule(localctx, 12, self.RULE_colorLienzo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(LienzoParser.COLOR)
            self.state = 117
            self.match(LienzoParser.DE)
            self.state = 118
            self.match(LienzoParser.LIENZO)
            self.state = 119
            self.match(LienzoParser.EQUALS)
            self.state = 120
            self.color()
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

        def TAMANO(self):
            return self.getToken(LienzoParser.TAMANO, 0)

        def DE(self):
            return self.getToken(LienzoParser.DE, 0)

        def LIENZO(self):
            return self.getToken(LienzoParser.LIENZO, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.ExpresionContext,i)


        def POR(self):
            return self.getToken(LienzoParser.POR, 0)

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
        self.enterRule(localctx, 14, self.RULE_tamanoLienzo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(LienzoParser.TAMANO)
            self.state = 123
            self.match(LienzoParser.DE)
            self.state = 124
            self.match(LienzoParser.LIENZO)
            self.state = 125
            self.match(LienzoParser.EQUALS)
            self.state = 126
            self.expresion()
            self.state = 127
            self.match(LienzoParser.POR)
            self.state = 128
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PosicionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSICION(self):
            return self.getToken(LienzoParser.POSICION, 0)

        def coord(self):
            return self.getTypedRuleContext(LienzoParser.CoordContext,0)


        def DE(self):
            return self.getToken(LienzoParser.DE, 0)

        def figura(self):
            return self.getTypedRuleContext(LienzoParser.FiguraContext,0)


        def expresion(self):
            return self.getTypedRuleContext(LienzoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_posicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosicion" ):
                listener.enterPosicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosicion" ):
                listener.exitPosicion(self)




    def posicion(self):

        localctx = LienzoParser.PosicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_posicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(LienzoParser.POSICION)
            self.state = 131
            self.coord()
            self.state = 132
            self.match(LienzoParser.DE)
            self.state = 133
            self.figura()
            self.state = 134
            self.match(LienzoParser.EQUALS)
            self.state = 135
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CoordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def X(self):
            return self.getToken(LienzoParser.X, 0)

        def Y(self):
            return self.getToken(LienzoParser.Y, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_coord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoord" ):
                listener.enterCoord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoord" ):
                listener.exitCoord(self)




    def coord(self):

        localctx = LienzoParser.CoordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_coord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not(_la==LienzoParser.X or _la==LienzoParser.Y):
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

    class AnimacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANIMACION(self):
            return self.getToken(LienzoParser.ANIMACION, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(LienzoParser.CuerpoContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_animacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnimacion" ):
                listener.enterAnimacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnimacion" ):
                listener.exitAnimacion(self)




    def animacion(self):

        localctx = LienzoParser.AnimacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_animacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(LienzoParser.ANIMACION)

            global currentFunctionName
            currentFunctionName = "animacion"
            namespaceTable.addFunction(currentFunctionName, "nada", [])
            memoryregisters.newFunction(currentFunctionName)

            self.state = 141
            self.match(LienzoParser.T__0)
            self.state = 142
            self.cuerpo()
            self.state = 143
            self.match(LienzoParser.T__1)
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


        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.InstruccionContext,i)


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
        self.enterRule(localctx, 22, self.RULE_cuerpo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MENSAJE) | (1 << LienzoParser.CONDICION) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 145
                self.declaracion()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (LienzoParser.COLOR - 42)) | (1 << (LienzoParser.POSICION - 42)) | (1 << (LienzoParser.DORMIR - 42)) | (1 << (LienzoParser.MIENTRAS - 42)) | (1 << (LienzoParser.SI - 42)) | (1 << (LienzoParser.MOSTRAR - 42)) | (1 << (LienzoParser.ID - 42)))) != 0):
                self.state = 151
                self.instruccion()
                self.state = 156
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
        self.enterRule(localctx, 24, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            localctx._tipo = self.tipo()
            self.state = 158
            localctx._ID = self.match(LienzoParser.ID)

            if namespaceTable.variableExists((None if localctx._ID is None else localctx._ID.text), currentFunctionName):
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": Variable", (None if localctx._ID is None else localctx._ID.text), "ya fue declarada")

            self.state = 160
            self.match(LienzoParser.EQUALS)
            self.state = 161
            localctx._ss_expresion = self.ss_expresion()
            self.state = 162
            self.match(LienzoParser.T__2)

            if localctx._ss_expresion.type != (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))):
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": Variable", (None if localctx._ID is None else localctx._ID.text), "es de tipo", (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))))
            else:
                namespaceTable.addVariable((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))), currentFunctionName)
                memoryregisters.createMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstruccionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(LienzoParser.AsignacionContext,0)


        def mostrarMensaje(self):
            return self.getTypedRuleContext(LienzoParser.MostrarMensajeContext,0)


        def dormir(self):
            return self.getTypedRuleContext(LienzoParser.DormirContext,0)


        def mientrasQue(self):
            return self.getTypedRuleContext(LienzoParser.MientrasQueContext,0)


        def cambioColor(self):
            return self.getTypedRuleContext(LienzoParser.CambioColorContext,0)


        def posicion(self):
            return self.getTypedRuleContext(LienzoParser.PosicionContext,0)


        def condicional(self):
            return self.getTypedRuleContext(LienzoParser.CondicionalContext,0)


        def llamadaFuncion(self):
            return self.getTypedRuleContext(LienzoParser.LlamadaFuncionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)




    def instruccion(self):

        localctx = LienzoParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_instruccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 165
                self.asignacion()
                pass

            elif la_ == 2:
                self.state = 166
                self.mostrarMensaje()
                pass

            elif la_ == 3:
                self.state = 167
                self.dormir()
                pass

            elif la_ == 4:
                self.state = 168
                self.mientrasQue()
                pass

            elif la_ == 5:
                self.state = 169
                self.cambioColor()
                pass

            elif la_ == 6:
                self.state = 170
                self.posicion()
                pass

            elif la_ == 7:
                self.state = 171
                self.condicional()
                pass

            elif la_ == 8:
                self.state = 172
                self.llamadaFuncion()
                pass


            self.state = 175
            self.match(LienzoParser.T__2)
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
        self.enterRule(localctx, 28, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 178
            self.match(LienzoParser.EQUALS)
            self.state = 179
            localctx._ss_expresion = self.ss_expresion()

            idType = namespaceTable.getVariableType((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
            if not idType:
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": Variable", (None if localctx._ID is None else localctx._ID.text), "no ha sido declarada")
            elif localctx._ss_expresion.type != idType:
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": Variable", (None if localctx._ID is None else localctx._ID.text), "es de tipo", idType)
            else:
                idcontent = memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
                cuadruplos.addCuadruplo('=', localctx._ss_expresion.valor,None,idcontent)

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

        def MENSAJE(self):
            return self.getToken(LienzoParser.MENSAJE, 0)

        def CONDICION(self):
            return self.getToken(LienzoParser.CONDICION, 0)

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
        self.enterRule(localctx, 30, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MENSAJE) | (1 << LienzoParser.CONDICION) | (1 << LienzoParser.NUMERO))) != 0)):
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

    class MostrarMensajeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOSTRAR(self):
            return self.getToken(LienzoParser.MOSTRAR, 0)

        def EN(self):
            return self.getToken(LienzoParser.EN, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.ExpresionContext,i)


        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def STRING_CONSTANT(self):
            return self.getToken(LienzoParser.STRING_CONSTANT, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_mostrarMensaje

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMostrarMensaje" ):
                listener.enterMostrarMensaje(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMostrarMensaje" ):
                listener.exitMostrarMensaje(self)




    def mostrarMensaje(self):

        localctx = LienzoParser.MostrarMensajeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_mostrarMensaje)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(LienzoParser.MOSTRAR)
            self.state = 185
            _la = self._input.LA(1)
            if not(_la==LienzoParser.STRING_CONSTANT or _la==LienzoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 186
            self.match(LienzoParser.EN)
            self.state = 187
            self.expresion()
            self.state = 188
            self.match(LienzoParser.T__3)
            self.state = 189
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DormirContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DORMIR(self):
            return self.getToken(LienzoParser.DORMIR, 0)

        def expresion(self):
            return self.getTypedRuleContext(LienzoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_dormir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDormir" ):
                listener.enterDormir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDormir" ):
                listener.exitDormir(self)




    def dormir(self):

        localctx = LienzoParser.DormirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_dormir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(LienzoParser.DORMIR)
            self.state = 192
            self.expresion()
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


        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.InstruccionContext,i)


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
        self.enterRule(localctx, 36, self.RULE_mientrasQue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(LienzoParser.MIENTRAS)
            self.state = 195
            self.match(LienzoParser.QUE)
            self.state = 196
            self.match(LienzoParser.T__4)
            self.state = 197
            localctx._ss_expresion = self.ss_expresion()
            self.state = 198
            self.match(LienzoParser.T__5)

            if localctx._ss_expresion.type != CONDICION:
                print("Error: linea", (None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, ": el estatuto 'mientras que' necesita una condicion")

            self.state = 200
            self.match(LienzoParser.T__0)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (LienzoParser.COLOR - 42)) | (1 << (LienzoParser.POSICION - 42)) | (1 << (LienzoParser.DORMIR - 42)) | (1 << (LienzoParser.MIENTRAS - 42)) | (1 << (LienzoParser.SI - 42)) | (1 << (LienzoParser.MOSTRAR - 42)) | (1 << (LienzoParser.ID - 42)))) != 0):
                self.state = 201
                self.instruccion()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self.match(LienzoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CambioColorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLOR(self):
            return self.getToken(LienzoParser.COLOR, 0)

        def DE(self):
            return self.getToken(LienzoParser.DE, 0)

        def figura(self):
            return self.getTypedRuleContext(LienzoParser.FiguraContext,0)


        def color(self):
            return self.getTypedRuleContext(LienzoParser.ColorContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_cambioColor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCambioColor" ):
                listener.enterCambioColor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCambioColor" ):
                listener.exitCambioColor(self)




    def cambioColor(self):

        localctx = LienzoParser.CambioColorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_cambioColor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(LienzoParser.COLOR)
            self.state = 210
            self.match(LienzoParser.DE)
            self.state = 211
            self.figura()
            self.state = 212
            self.match(LienzoParser.EQUALS)
            self.state = 213
            self.color()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FiguraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOMBRE_PROPIO(self):
            return self.getToken(LienzoParser.NOMBRE_PROPIO, 0)

        def expresion(self):
            return self.getTypedRuleContext(LienzoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_figura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFigura" ):
                listener.enterFigura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFigura" ):
                listener.exitFigura(self)




    def figura(self):

        localctx = LienzoParser.FiguraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_figura)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(LienzoParser.NOMBRE_PROPIO)
            self.state = 220
            _la = self._input.LA(1)
            if _la==LienzoParser.T__6:
                self.state = 216
                self.match(LienzoParser.T__6)
                self.state = 217
                self.expresion()
                self.state = 218
                self.match(LienzoParser.T__7)


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


        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.InstruccionContext,i)


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
        self.enterRule(localctx, 42, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(LienzoParser.SI)
            self.state = 223
            self.match(LienzoParser.T__4)
            self.state = 224
            localctx._ss_expresion = self.ss_expresion()
            self.state = 225
            self.match(LienzoParser.T__5)

            if localctx._ss_expresion.type != CONDICION:
                print("Error: linea", (None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, ": el estatuto 'si' necesita una condicion")

            self.state = 227
            self.match(LienzoParser.T__0)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (LienzoParser.COLOR - 42)) | (1 << (LienzoParser.POSICION - 42)) | (1 << (LienzoParser.DORMIR - 42)) | (1 << (LienzoParser.MIENTRAS - 42)) | (1 << (LienzoParser.SI - 42)) | (1 << (LienzoParser.MOSTRAR - 42)) | (1 << (LienzoParser.ID - 42)))) != 0):
                self.state = 228
                self.instruccion()
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 234
            self.match(LienzoParser.T__1)
            self.state = 244
            _la = self._input.LA(1)
            if _la==LienzoParser.SINO:
                self.state = 235
                self.match(LienzoParser.SINO)
                self.state = 236
                self.match(LienzoParser.T__0)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (LienzoParser.COLOR - 42)) | (1 << (LienzoParser.POSICION - 42)) | (1 << (LienzoParser.DORMIR - 42)) | (1 << (LienzoParser.MIENTRAS - 42)) | (1 << (LienzoParser.SI - 42)) | (1 << (LienzoParser.MOSTRAR - 42)) | (1 << (LienzoParser.ID - 42)))) != 0):
                    self.state = 237
                    self.instruccion()
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 243
                self.match(LienzoParser.T__1)


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
        self.enterRule(localctx, 44, self.RULE_llamadaFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 247
            self.match(LienzoParser.T__4)
            self.state = 259
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__4) | (1 << LienzoParser.T__17) | (1 << LienzoParser.T__21) | (1 << LienzoParser.CONDITION_CONSTANT))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (LienzoParser.NUMERIC_CONSTANT - 67)) | (1 << (LienzoParser.STRING_CONSTANT - 67)) | (1 << (LienzoParser.ID - 67)))) != 0):
                self.state = 248
                localctx.ss_exp1 = self.ss_expresion()

                global currentArgumentList
                currentArgumentList.append(((None if localctx.ss_exp1 is None else self._input.getText((localctx.ss_exp1.start,localctx.ss_exp1.stop))), localctx.ss_exp1.type))

                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__3:
                    self.state = 250
                    self.match(LienzoParser.T__3)
                    self.state = 251
                    localctx.ss_exp2 = self.ss_expresion()

                    currentArgumentList.append(((None if localctx.ss_exp2 is None else self._input.getText((localctx.ss_exp2.start,localctx.ss_exp2.stop))), localctx.ss_exp2.type))

                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 261
            self.match(LienzoParser.T__5)

            functionType = namespaceTable.getFunctionType((None if localctx._ID is None else localctx._ID.text))
            if functionType and namespaceTable.argumentsAgree((None if localctx._ID is None else localctx._ID.text), currentArgumentList):
                localctx.type = None if functionType == "nada" else functionType
            else:
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": llamada a funcion", (None if localctx._ID is None else localctx._ID.text), "inexistente")

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
        self.enterRule(localctx, 46, self.RULE_ss_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            localctx.s_exp1 = self.s_expresion()

            localctx.type = localctx.s_exp1.type
            localctx.valor = localctx.s_exp1.valor

            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.T__8 or _la==LienzoParser.T__9:
                self.state = 266
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__8 or _la==LienzoParser.T__9):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 267
                localctx.s_exp2 = self.s_expresion()

                localctx.type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.s_exp2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.s_exp2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.s_exp2.valor)

                self.state = 274
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
        self.enterRule(localctx, 48, self.RULE_s_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            localctx.exp1 = self.expresion()

            localctx.type = localctx.exp1.type
            localctx.valor = localctx.exp1.valor

            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12) | (1 << LienzoParser.T__13) | (1 << LienzoParser.T__14) | (1 << LienzoParser.T__15))) != 0):
                self.state = 277
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12) | (1 << LienzoParser.T__13) | (1 << LienzoParser.T__14) | (1 << LienzoParser.T__15))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 278
                localctx.exp2 = self.expresion()

                localctx.type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.exp2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.exp2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.exp2.valor)

                self.state = 286
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
        self.enterRule(localctx, 50, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            localctx.term1 = self.termino()

            localctx.type = localctx.term1.type
            localctx.valor = localctx.term1.valor

            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.T__16 or _la==LienzoParser.T__17:
                self.state = 289
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__16 or _la==LienzoParser.T__17):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 290
                localctx.term2 = self.termino()

                type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.term2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.term2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.term2.valor)
                    

                self.state = 298
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
        self.enterRule(localctx, 52, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            localctx.factor1 = self.factor()

            localctx.type = localctx.factor1.type
            localctx.valor = localctx.factor1.valor

            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__18) | (1 << LienzoParser.T__19) | (1 << LienzoParser.T__20))) != 0):
                self.state = 301
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__18) | (1 << LienzoParser.T__19) | (1 << LienzoParser.T__20))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 302
                localctx.factor2 = self.factor()

                type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.factor2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.factor2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.factor2.valor)

                self.state = 309
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
        self.enterRule(localctx, 54, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 324
            token = self._input.LA(1)
            if token in [LienzoParser.T__4, LienzoParser.T__21, LienzoParser.CONDITION_CONSTANT, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                _la = self._input.LA(1)
                if _la==LienzoParser.T__21:
                    self.state = 310
                    localctx.neg = self.match(LienzoParser.T__21)


                self.state = 313
                localctx._factor_aux = self.factor_aux()

                localctx.type = localctx._factor_aux.type
                if (None if localctx.neg is None else localctx.neg.text) and localctx._factor_aux.type != CONDICION:
                    print("Error: linea", (0 if localctx.neg is None else localctx.neg.line), ": operador", (None if localctx.neg is None else localctx.neg.text), "no puede ser aplicado a", localctx._factor_aux.type)
                    localctx.type = None
                else:
                    if (None if localctx.neg is None else localctx.neg.text):
                        localctx.valor = cuadruplos.addCuadruplo((None if localctx.neg is None else localctx.neg.text),localctx._factor_aux.valor,None)
                    else:
                        localctx.valor = localctx._factor_aux.valor


            elif token in [LienzoParser.T__17, LienzoParser.NUMERIC_CONSTANT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                _la = self._input.LA(1)
                if _la==LienzoParser.T__17:
                    self.state = 317
                    self.match(LienzoParser.T__17)


                self.state = 320
                self.match(LienzoParser.NUMERIC_CONSTANT)
                localctx.type = NUMERO

            elif token in [LienzoParser.STRING_CONSTANT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                localctx._STRING_CONSTANT = self.match(LienzoParser.STRING_CONSTANT)

                localctx.type = MENSAJE
                localctx.valor = (None if localctx._STRING_CONSTANT is None else localctx._STRING_CONSTANT.text)


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
            self._CONDITION_CONSTANT = None # Token
            self._llamadaFuncion = None # LlamadaFuncionContext
            self._ss_expresion = None # Ss_expresionContext

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def CONDITION_CONSTANT(self):
            return self.getToken(LienzoParser.CONDITION_CONSTANT, 0)

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
        self.enterRule(localctx, 56, self.RULE_factor_aux)
        try:
            self.state = 338
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                localctx._ID = self.match(LienzoParser.ID)

                localctx.type = namespaceTable.getVariableType((None if localctx._ID is None else localctx._ID.text), currentFunctionName)

                if localctx.type:
                    localctx.valor = memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
                else:
                    localctx.valor = None


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                localctx._CONDITION_CONSTANT = self.match(LienzoParser.CONDITION_CONSTANT)

                localctx.type = CONDICION
                localctx.valor = (None if localctx._CONDITION_CONSTANT is None else localctx._CONDITION_CONSTANT.text)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 330
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
                self.state = 333
                self.match(LienzoParser.T__4)
                self.state = 334
                localctx._ss_expresion = self.ss_expresion()
                self.state = 335
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

    class FuncionesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCIONES(self):
            return self.getToken(LienzoParser.FUNCIONES, 0)

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.FuncContext)
            else:
                return self.getTypedRuleContext(LienzoParser.FuncContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_funciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunciones" ):
                listener.enterFunciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunciones" ):
                listener.exitFunciones(self)




    def funciones(self):

        localctx = LienzoParser.FuncionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_funciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(LienzoParser.FUNCIONES)
            self.state = 341
            self.match(LienzoParser.T__0)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MENSAJE) | (1 << LienzoParser.CONDICION) | (1 << LienzoParser.NUMERO) | (1 << LienzoParser.NADA))) != 0):
                self.state = 342
                self.func()
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 348
            self.match(LienzoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncContext(ParserRuleContext):

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
            return LienzoParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = LienzoParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            localctx._tipoFunc = self.tipoFunc()
            self.state = 351
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 352
            self.match(LienzoParser.T__4)
            self.state = 361
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MENSAJE) | (1 << LienzoParser.CONDICION) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 353
                self.parametro()
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__3:
                    self.state = 354
                    self.match(LienzoParser.T__3)
                    self.state = 355
                    self.parametro()
                    self.state = 360
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 363
            self.match(LienzoParser.T__5)

            global currentFunctionName
            global currentParameterList
            currentFunctionName = (None if localctx._ID is None else localctx._ID.text)
            if not namespaceTable.addFunction(currentFunctionName, (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))), currentParameterList):
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": Funcion", (None if localctx._ID is None else localctx._ID.text), "ya fue declarada")
            else:
                memoryregisters.newFunction(currentFunctionName)
            currentParameterList = []

            self.state = 365
            self.match(LienzoParser.T__0)
            self.state = 366
            self.cuerpo()
            self.state = 367
            self.match(LienzoParser.T__1)
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
        self.enterRule(localctx, 62, self.RULE_tipoFunc)
        try:
            self.state = 371
            token = self._input.LA(1)
            if token in [LienzoParser.MENSAJE, LienzoParser.CONDICION, LienzoParser.NUMERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.tipo()

            elif token in [LienzoParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
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
        self.enterRule(localctx, 64, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            localctx._tipo = self.tipo()
            self.state = 375
            _la = self._input.LA(1)
            if _la==LienzoParser.MODIFICABLE:
                self.state = 374
                localctx._MODIFICABLE = self.match(LienzoParser.MODIFICABLE)


            self.state = 377
            localctx._ID = self.match(LienzoParser.ID)

            global currentParameterList
            if (None if localctx._ID is None else localctx._ID.text) in [parameter[0] for parameter in currentParameterList]:
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": Parametro", (None if localctx._ID is None else localctx._ID.text), "ya fue declarado")
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





