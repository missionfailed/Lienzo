# Generated from Lienzo.g4 by ANTLR 4.5.2
# encoding: utf-8
from antlr4 import *
from io import StringIO


from namespace import NamespaceTable
from collections import defaultdict
from MemoryRegister import MemoryRegisters
from cuadruplos import *
import VM

namespaceTable = NamespaceTable()
currentFunctionName = ""

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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3D")
        buf.write("\u017d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\7\2F\n\2\f\2\16\2I")
        buf.write("\13\2\3\2\3\2\3\2\5\2N\n\2\3\2\3\2\7\2R\n\2\f\2\16\2U")
        buf.write("\13\2\3\2\3\2\7\2Y\n\2\f\2\16\2\\\13\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0084\n\7\f\7\16\7\u0087")
        buf.write("\13\7\5\7\u0089\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0092")
        buf.write("\n\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u009a\n\b\3\t\3\t\5\t")
        buf.write("\u009e\n\t\3\t\3\t\3\t\3\n\7\n\u00a4\n\n\f\n\16\n\u00a7")
        buf.write("\13\n\3\n\7\n\u00aa\n\n\f\n\16\n\u00ad\13\n\3\13\3\13")
        buf.write("\3\13\7\13\u00b2\n\13\f\13\16\13\u00b5\13\13\3\13\5\13")
        buf.write("\u00b8\n\13\3\f\3\f\3\f\5\f\u00bd\n\f\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u00c3\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00cf\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u0111\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\7\34\u0125\n\34\f\34\16\34\u0128\13\34\5\34\u012a")
        buf.write("\n\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35")
        buf.write("\u0135\n\35\f\35\16\35\u0138\13\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\7\36\u0141\n\36\f\36\16\36\u0144\13\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u014d\n\37\f")
        buf.write("\37\16\37\u0150\13\37\3 \3 \3 \3 \3 \3 \7 \u0158\n \f")
        buf.write(" \16 \u015b\13 \3!\5!\u015e\n!\3!\3!\3!\3!\3!\5!\u0165")
        buf.write("\n!\3!\3!\3!\3!\3!\5!\u016c\n!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u017b\n\"\3\"\2\2#\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@B\2\b\3\2\30!\4\299;<\3\2\t\n\3\2\13\20\3\2\21")
        buf.write("\22\3\2\23\25\u0184\2G\3\2\2\2\4`\3\2\2\2\6h\3\2\2\2\b")
        buf.write("j\3\2\2\2\nt\3\2\2\2\f|\3\2\2\2\16\u0099\3\2\2\2\20\u009b")
        buf.write("\3\2\2\2\22\u00a5\3\2\2\2\24\u00b7\3\2\2\2\26\u00c2\3")
        buf.write("\2\2\2\30\u00ce\3\2\2\2\32\u00d0\3\2\2\2\34\u00d5\3\2")
        buf.write("\2\2\36\u00d9\3\2\2\2 \u00dd\3\2\2\2\"\u00e2\3\2\2\2$")
        buf.write("\u00e7\3\2\2\2&\u00ec\3\2\2\2(\u00f1\3\2\2\2*\u00f5\3")
        buf.write("\2\2\2,\u00f9\3\2\2\2.\u0100\3\2\2\2\60\u0105\3\2\2\2")
        buf.write("\62\u0107\3\2\2\2\64\u0112\3\2\2\2\66\u011a\3\2\2\28\u012e")
        buf.write("\3\2\2\2:\u0139\3\2\2\2<\u0145\3\2\2\2>\u0151\3\2\2\2")
        buf.write("@\u016b\3\2\2\2B\u017a\3\2\2\2DF\5\n\6\2ED\3\2\2\2FI\3")
        buf.write("\2\2\2GE\3\2\2\2GH\3\2\2\2HM\3\2\2\2IG\3\2\2\2JK\5\b\5")
        buf.write("\2KL\5\4\3\2LN\3\2\2\2MJ\3\2\2\2MN\3\2\2\2NO\3\2\2\2O")
        buf.write("S\b\2\1\2PR\5\f\7\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3")
        buf.write("\2\2\2TV\3\2\2\2US\3\2\2\2VZ\b\2\1\2WY\5\26\f\2XW\3\2")
        buf.write("\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[]\3\2\2\2\\Z\3\2\2")
        buf.write("\2]^\7\2\2\3^_\b\2\1\2_\3\3\2\2\2`a\7\"\2\2ab\7\'\2\2")
        buf.write("bc\7#\2\2cd\7$\2\2de\5\6\4\2ef\7\3\2\2fg\b\3\1\2g\5\3")
        buf.write("\2\2\2hi\t\2\2\2i\7\3\2\2\2jk\7%\2\2kl\7\'\2\2lm\7#\2")
        buf.write("\2mn\7$\2\2no\58\35\2op\7&\2\2pq\58\35\2qr\7\3\2\2rs\b")
        buf.write("\5\1\2s\t\3\2\2\2tu\5\60\31\2uv\7D\2\2vw\b\6\1\2wx\7$")
        buf.write("\2\2xy\58\35\2yz\7\3\2\2z{\b\6\1\2{\13\3\2\2\2|}\5\16")
        buf.write("\b\2}~\7D\2\2~\177\b\7\1\2\177\u0088\7\4\2\2\u0080\u0085")
        buf.write("\5\20\t\2\u0081\u0082\7\5\2\2\u0082\u0084\5\20\t\2\u0083")
        buf.write("\u0081\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2")
        buf.write("\u0085\u0086\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3")
        buf.write("\2\2\2\u0088\u0080\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a")
        buf.write("\3\2\2\2\u008a\u008b\7\6\2\2\u008b\u008c\7\7\2\2\u008c")
        buf.write("\u0091\5\22\n\2\u008d\u008e\7\65\2\2\u008e\u008f\58\35")
        buf.write("\2\u008f\u0090\7\3\2\2\u0090\u0092\3\2\2\2\u0091\u008d")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0094\b\7\1\2\u0094\u0095\7\b\2\2\u0095\u0096\b\7\1\2")
        buf.write("\u0096\r\3\2\2\2\u0097\u009a\5\60\31\2\u0098\u009a\7?")
        buf.write("\2\2\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2\2\u009a\17")
        buf.write("\3\2\2\2\u009b\u009d\5\60\31\2\u009c\u009e\7A\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u00a0\7D\2\2\u00a0\u00a1\b\t\1\2\u00a1\21\3\2\2")
        buf.write("\2\u00a2\u00a4\5\n\6\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7")
        buf.write("\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\u00ab\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00aa\5\26\f")
        buf.write("\2\u00a9\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\23\3\2\2\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ae\u00b8\5\26\f\2\u00af\u00b3\7\7\2\2\u00b0")
        buf.write("\u00b2\5\26\f\2\u00b1\u00b0\3\2\2\2\u00b2\u00b5\3\2\2")
        buf.write("\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6")
        buf.write("\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b8\7\b\2\2\u00b7")
        buf.write("\u00ae\3\2\2\2\u00b7\u00af\3\2\2\2\u00b8\25\3\2\2\2\u00b9")
        buf.write("\u00bd\5.\30\2\u00ba\u00bd\5\30\r\2\u00bb\u00bd\5\66\34")
        buf.write("\2\u00bc\u00b9\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\7\3\2\2\u00bf")
        buf.write("\u00c3\3\2\2\2\u00c0\u00c3\5\62\32\2\u00c1\u00c3\5\64")
        buf.write("\33\2\u00c2\u00bc\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3\27\3\2\2\2\u00c4\u00cf\5\32\16\2\u00c5")
        buf.write("\u00cf\5\34\17\2\u00c6\u00cf\5\36\20\2\u00c7\u00cf\5 ")
        buf.write("\21\2\u00c8\u00cf\5\"\22\2\u00c9\u00cf\5&\24\2\u00ca\u00cf")
        buf.write("\5$\23\2\u00cb\u00cf\5,\27\2\u00cc\u00cf\5(\25\2\u00cd")
        buf.write("\u00cf\5*\26\2\u00ce\u00c4\3\2\2\2\u00ce\u00c5\3\2\2\2")
        buf.write("\u00ce\u00c6\3\2\2\2\u00ce\u00c7\3\2\2\2\u00ce\u00c8\3")
        buf.write("\2\2\2\u00ce\u00c9\3\2\2\2\u00ce\u00ca\3\2\2\2\u00ce\u00cb")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write("\31\3\2\2\2\u00d0\u00d1\7:\2\2\u00d1\u00d2\58\35\2\u00d2")
        buf.write("\u00d3\7D\2\2\u00d3\u00d4\b\16\1\2\u00d4\33\3\2\2\2\u00d5")
        buf.write("\u00d6\7=\2\2\u00d6\u00d7\58\35\2\u00d7\u00d8\b\17\1\2")
        buf.write("\u00d8\35\3\2\2\2\u00d9\u00da\7>\2\2\u00da\u00db\58\35")
        buf.write("\2\u00db\u00dc\b\20\1\2\u00dc\37\3\2\2\2\u00dd\u00de\7")
        buf.write(")\2\2\u00de\u00df\7*\2\2\u00df\u00e0\58\35\2\u00e0\u00e1")
        buf.write("\b\21\1\2\u00e1!\3\2\2\2\u00e2\u00e3\7)\2\2\u00e3\u00e4")
        buf.write("\7+\2\2\u00e4\u00e5\58\35\2\u00e5\u00e6\b\22\1\2\u00e6")
        buf.write("#\3\2\2\2\u00e7\u00e8\7,\2\2\u00e8\u00e9\7-\2\2\u00e9")
        buf.write("\u00ea\58\35\2\u00ea\u00eb\b\23\1\2\u00eb%\3\2\2\2\u00ec")
        buf.write("\u00ed\7,\2\2\u00ed\u00ee\7.\2\2\u00ee\u00ef\58\35\2\u00ef")
        buf.write("\u00f0\b\24\1\2\u00f0\'\3\2\2\2\u00f1\u00f2\7/\2\2\u00f2")
        buf.write("\u00f3\7\61\2\2\u00f3\u00f4\b\25\1\2\u00f4)\3\2\2\2\u00f5")
        buf.write("\u00f6\7\60\2\2\u00f6\u00f7\7\61\2\2\u00f7\u00f8\b\26")
        buf.write("\1\2\u00f8+\3\2\2\2\u00f9\u00fa\7\"\2\2\u00fa\u00fb\7")
        buf.write("\'\2\2\u00fb\u00fc\7\61\2\2\u00fc\u00fd\7$\2\2\u00fd\u00fe")
        buf.write("\5\6\4\2\u00fe\u00ff\b\27\1\2\u00ff-\3\2\2\2\u0100\u0101")
        buf.write("\7D\2\2\u0101\u0102\7$\2\2\u0102\u0103\58\35\2\u0103\u0104")
        buf.write("\b\30\1\2\u0104/\3\2\2\2\u0105\u0106\t\3\2\2\u0106\61")
        buf.write("\3\2\2\2\u0107\u0108\7\67\2\2\u0108\u0109\58\35\2\u0109")
        buf.write("\u010a\b\32\1\2\u010a\u0110\5\24\13\2\u010b\u010c\78\2")
        buf.write("\2\u010c\u010d\b\32\1\2\u010d\u010e\5\24\13\2\u010e\u010f")
        buf.write("\b\32\1\2\u010f\u0111\3\2\2\2\u0110\u010b\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\63\3\2\2\2\u0112\u0113\7\64\2\2\u0113")
        buf.write("\u0114\7\66\2\2\u0114\u0115\b\33\1\2\u0115\u0116\58\35")
        buf.write("\2\u0116\u0117\b\33\1\2\u0117\u0118\5\24\13\2\u0118\u0119")
        buf.write("\b\33\1\2\u0119\65\3\2\2\2\u011a\u011b\7D\2\2\u011b\u011c")
        buf.write("\b\34\1\2\u011c\u011d\7\4\2\2\u011d\u0129\b\34\1\2\u011e")
        buf.write("\u011f\58\35\2\u011f\u0126\b\34\1\2\u0120\u0121\7\5\2")
        buf.write("\2\u0121\u0122\58\35\2\u0122\u0123\b\34\1\2\u0123\u0125")
        buf.write("\3\2\2\2\u0124\u0120\3\2\2\2\u0125\u0128\3\2\2\2\u0126")
        buf.write("\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u012a\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0129\u011e\3\2\2\2\u0129\u012a\3")
        buf.write("\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\7\6\2\2\u012c\u012d")
        buf.write("\b\34\1\2\u012d\67\3\2\2\2\u012e\u012f\5:\36\2\u012f\u0136")
        buf.write("\b\35\1\2\u0130\u0131\t\4\2\2\u0131\u0132\5:\36\2\u0132")
        buf.write("\u0133\b\35\1\2\u0133\u0135\3\2\2\2\u0134\u0130\3\2\2")
        buf.write("\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u01379\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013a")
        buf.write("\5<\37\2\u013a\u0142\b\36\1\2\u013b\u013c\t\5\2\2\u013c")
        buf.write("\u013d\5<\37\2\u013d\u013e\3\2\2\2\u013e\u013f\b\36\1")
        buf.write("\2\u013f\u0141\3\2\2\2\u0140\u013b\3\2\2\2\u0141\u0144")
        buf.write("\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143")
        buf.write(";\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0146\5> \2\u0146")
        buf.write("\u014e\b\37\1\2\u0147\u0148\t\6\2\2\u0148\u0149\5> \2")
        buf.write("\u0149\u014a\3\2\2\2\u014a\u014b\b\37\1\2\u014b\u014d")
        buf.write("\3\2\2\2\u014c\u0147\3\2\2\2\u014d\u0150\3\2\2\2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f=\3\2\2\2\u0150")
        buf.write("\u014e\3\2\2\2\u0151\u0152\5@!\2\u0152\u0159\b \1\2\u0153")
        buf.write("\u0154\t\7\2\2\u0154\u0155\5@!\2\u0155\u0156\b \1\2\u0156")
        buf.write("\u0158\3\2\2\2\u0157\u0153\3\2\2\2\u0158\u015b\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a?\3\2\2")
        buf.write("\2\u015b\u0159\3\2\2\2\u015c\u015e\7\26\2\2\u015d\u015c")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u0160\5B\"\2\u0160\u0161\3\2\2\2\u0161\u0162\b!\1\2\u0162")
        buf.write("\u016c\3\2\2\2\u0163\u0165\7\22\2\2\u0164\u0163\3\2\2")
        buf.write("\2\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167")
        buf.write("\7B\2\2\u0167\u0168\3\2\2\2\u0168\u016c\b!\1\2\u0169\u016a")
        buf.write("\7C\2\2\u016a\u016c\b!\1\2\u016b\u015d\3\2\2\2\u016b\u0164")
        buf.write("\3\2\2\2\u016b\u0169\3\2\2\2\u016cA\3\2\2\2\u016d\u016e")
        buf.write("\7D\2\2\u016e\u017b\b\"\1\2\u016f\u0170\7@\2\2\u0170\u017b")
        buf.write("\b\"\1\2\u0171\u0172\5\66\34\2\u0172\u0173\b\"\1\2\u0173")
        buf.write("\u017b\3\2\2\2\u0174\u0175\7\4\2\2\u0175\u0176\58\35\2")
        buf.write("\u0176\u0177\7\6\2\2\u0177\u0178\b\"\1\2\u0178\u017b\3")
        buf.write("\2\2\2\u0179\u017b\5\30\r\2\u017a\u016d\3\2\2\2\u017a")
        buf.write("\u016f\3\2\2\2\u017a\u0171\3\2\2\2\u017a\u0174\3\2\2\2")
        buf.write("\u017a\u0179\3\2\2\2\u017bC\3\2\2\2\35GMSZ\u0085\u0088")
        buf.write("\u0091\u0099\u009d\u00a5\u00ab\u00b3\u00b7\u00bc\u00c2")
        buf.write("\u00ce\u0110\u0126\u0129\u0136\u0142\u014e\u0159\u015d")
        buf.write("\u0164\u016b\u017a")
        return buf.getvalue()


class LienzoParser ( Parser ):

    grammarFileName = "Lienzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'", "'{'", "'}'", 
                     "'&'", "'|'", "'=='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "<INVALID>", 
                     "'rojo'", "'verde'", "'amarillo'", "'azul'", "'blanco'", 
                     "'negro'", "'morado'", "'naranja'", "'cafe'", "'gris'", 
                     "'color'", "'lienzo'", "'='", "'tamano'", "'por'", 
                     "'de'", "'en'", "'mover'", "'adelante'", "'atras'", 
                     "'girar'", "'derecha'", "'izquierda'", "'levantar'", 
                     "'bajar'", "'pluma'", "'dibujo'", "'dormir'", "'mientras'", 
                     "'regresar'", "'que'", "'si'", "'sino'", "'texto'", 
                     "'leer'", "'boleano'", "'numero'", "'escribir'", "'imprimir'", 
                     "'nada'", "<INVALID>", "'modificable'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "ROJO", "VERDE", "AMARILLO", "AZUL", 
                      "BLANCO", "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", 
                      "COLOR", "LIENZO", "EQUALS", "TAMANO", "POR", "DE", 
                      "EN", "MOVER", "ADELANTE", "ATRAS", "GIRAR", "DERECHA", 
                      "IZQUIERDA", "LEVANTAR", "BAJAR", "PLUMA", "DIBUJO", 
                      "DORMIR", "MIENTRAS", "REGRESAR", "QUE", "SI", "SINO", 
                      "TEXTO", "LEER", "BOLEANO", "NUMERO", "ESCRIBIR", 
                      "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", "MODIFICABLE", 
                      "NUMERIC_CONSTANT", "STRING_CONSTANT", "ID" ]

    RULE_program = 0
    RULE_colorLienzo = 1
    RULE_color = 2
    RULE_tamanoLienzo = 3
    RULE_declaracion = 4
    RULE_funcion = 5
    RULE_tipoFunc = 6
    RULE_parametro = 7
    RULE_cuerpo = 8
    RULE_bloque_instrucciones = 9
    RULE_instruccion_aux = 10
    RULE_llamadaFuncionPredefinida = 11
    RULE_lectura = 12
    RULE_escritura = 13
    RULE_imprimir = 14
    RULE_mover_adelante = 15
    RULE_mover_atras = 16
    RULE_girar_derecha = 17
    RULE_girar_izquierda = 18
    RULE_subir_pluma = 19
    RULE_bajar_pluma = 20
    RULE_cambio_color = 21
    RULE_asignacion = 22
    RULE_tipo = 23
    RULE_condicional = 24
    RULE_mientrasQue = 25
    RULE_llamadaFuncion = 26
    RULE_ss_expresion = 27
    RULE_s_expresion = 28
    RULE_expresion = 29
    RULE_termino = 30
    RULE_factor = 31
    RULE_factor_aux = 32

    ruleNames =  [ "program", "colorLienzo", "color", "tamanoLienzo", "declaracion", 
                   "funcion", "tipoFunc", "parametro", "cuerpo", "bloque_instrucciones", 
                   "instruccion_aux", "llamadaFuncionPredefinida", "lectura", 
                   "escritura", "imprimir", "mover_adelante", "mover_atras", 
                   "girar_derecha", "girar_izquierda", "subir_pluma", "bajar_pluma", 
                   "cambio_color", "asignacion", "tipo", "condicional", 
                   "mientrasQue", "llamadaFuncion", "ss_expresion", "s_expresion", 
                   "expresion", "termino", "factor", "factor_aux" ]

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
    ROJO=22
    VERDE=23
    AMARILLO=24
    AZUL=25
    BLANCO=26
    NEGRO=27
    MORADO=28
    NARANJA=29
    CAFE=30
    GRIS=31
    COLOR=32
    LIENZO=33
    EQUALS=34
    TAMANO=35
    POR=36
    DE=37
    EN=38
    MOVER=39
    ADELANTE=40
    ATRAS=41
    GIRAR=42
    DERECHA=43
    IZQUIERDA=44
    LEVANTAR=45
    BAJAR=46
    PLUMA=47
    DIBUJO=48
    DORMIR=49
    MIENTRAS=50
    REGRESAR=51
    QUE=52
    SI=53
    SINO=54
    TEXTO=55
    LEER=56
    BOLEANO=57
    NUMERO=58
    ESCRIBIR=59
    IMPRIMIR=60
    NADA=61
    BOOLEAN_CONSTANT=62
    MODIFICABLE=63
    NUMERIC_CONSTANT=64
    STRING_CONSTANT=65
    ID=66

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LienzoParser.EOF, 0)

        def declaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.DeclaracionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.DeclaracionContext,i)


        def tamanoLienzo(self):
            return self.getTypedRuleContext(LienzoParser.TamanoLienzoContext,0)


        def colorLienzo(self):
            return self.getTypedRuleContext(LienzoParser.ColorLienzoContext,0)


        def funcion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.FuncionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.FuncionContext,i)


        def instruccion_aux(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.Instruccion_auxContext)
            else:
                return self.getTypedRuleContext(LienzoParser.Instruccion_auxContext,i)


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
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    self.declaracion() 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 75
            _la = self._input.LA(1)
            if _la==LienzoParser.TAMANO:
                self.state = 72
                self.tamanoLienzo()
                self.state = 73
                self.colorLienzo()



            cuadruplos.addCuadruplo("", GOTO, None, None, None, False)
            cuadruplos.pushPilaSaltos(cuadruplos.last())

            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO) | (1 << LienzoParser.NADA))) != 0):
                self.state = 78
                self.funcion()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(), cuadruplos.current())

            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & ((1 << (LienzoParser.COLOR - 32)) | (1 << (LienzoParser.MOVER - 32)) | (1 << (LienzoParser.GIRAR - 32)) | (1 << (LienzoParser.LEVANTAR - 32)) | (1 << (LienzoParser.BAJAR - 32)) | (1 << (LienzoParser.MIENTRAS - 32)) | (1 << (LienzoParser.SI - 32)) | (1 << (LienzoParser.LEER - 32)) | (1 << (LienzoParser.ESCRIBIR - 32)) | (1 << (LienzoParser.IMPRIMIR - 32)) | (1 << (LienzoParser.ID - 32)))) != 0):
                self.state = 85
                self.instruccion_aux()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.match(LienzoParser.EOF)

            VM.executeVM(namespaceTable.getDirProc(), cuadruplos.getCuadruplos())

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
            self._color = None # ColorContext

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
        self.enterRule(localctx, 2, self.RULE_colorLienzo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(LienzoParser.COLOR)
            self.state = 95
            self.match(LienzoParser.DE)
            self.state = 96
            self.match(LienzoParser.LIENZO)
            self.state = 97
            self.match(LienzoParser.EQUALS)
            self.state = 98
            localctx._color = self.color()
            self.state = 99
            self.match(LienzoParser.T__0)

            cuadruplos.addCuadruplo("", CANVAS_COLOR, (None if localctx._color is None else localctx._color.start).text, None, None, False)

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
        self.enterRule(localctx, 4, self.RULE_color)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
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
        self.enterRule(localctx, 6, self.RULE_tamanoLienzo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(LienzoParser.TAMANO)
            self.state = 105
            self.match(LienzoParser.DE)
            self.state = 106
            self.match(LienzoParser.LIENZO)
            self.state = 107
            self.match(LienzoParser.EQUALS)
            self.state = 108
            localctx.largo = self.ss_expresion()
            self.state = 109
            self.match(LienzoParser.POR)
            self.state = 110
            localctx.ancho = self.ss_expresion()
            self.state = 111
            self.match(LienzoParser.T__0)

            if localctx.largo.type != NUMERO:
                error((None if localctx.largo is None else localctx.largo.start).line, "Largo del lienzo debe ser una expresion entera")
            elif localctx.ancho.type != NUMERO:
                error((None if localctx.ancho is None else localctx.ancho.start).line, "Ancho del lienzo debe ser una expresion entera")
            else:
                cuadruplos.addCuadruplo("", CANVAS_SIZE, localctx.largo.valor, localctx.ancho.valor, None, False)

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
        self.enterRule(localctx, 8, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            localctx._tipo = self.tipo()
            self.state = 115
            localctx._ID = self.match(LienzoParser.ID)

            if namespaceTable.idAlreadyTaken((None if localctx._ID is None else localctx._ID.text), currentFunctionName):
                error((0 if localctx._ID is None else localctx._ID.line), ": Identificador " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarado")

            self.state = 117
            self.match(LienzoParser.EQUALS)
            self.state = 118
            localctx._ss_expresion = self.ss_expresion()
            self.state = 119
            self.match(LienzoParser.T__0)

            if localctx._ss_expresion.type != (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))):
                error((0 if localctx._ID is None else localctx._ID.line), "Variable " + (None if localctx._ID is None else localctx._ID.text) + " es de tipo " + (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))))
            else:
                namespaceTable.addVariable((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))), currentFunctionName)
                idcontent = memoryregisters.createMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
                cuadruplos.addCuadruplo(currentFunctionName, '=', localctx._ss_expresion.valor, None, idcontent)

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
            self._REGRESAR = None # Token
            self._ss_expresion = None # Ss_expresionContext

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


        def REGRESAR(self):
            return self.getToken(LienzoParser.REGRESAR, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


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
        self.enterRule(localctx, 10, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            localctx._tipoFunc = self.tipoFunc()
            self.state = 123
            localctx._ID = self.match(LienzoParser.ID)

            global currentFunctionName
            currentFunctionName = (None if localctx._ID is None else localctx._ID.text)
            if not namespaceTable.addFunction(currentFunctionName, (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))), cuadruplos.current()):
                error((0 if localctx._ID is None else localctx._ID.line), "Funcion " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarada")
            else:
                memoryregisters.newFunction(currentFunctionName)

            self.state = 125
            self.match(LienzoParser.T__1)
            self.state = 134
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 126
                self.parametro()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__2:
                    self.state = 127
                    self.match(LienzoParser.T__2)
                    self.state = 128
                    self.parametro()
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 136
            self.match(LienzoParser.T__3)
            self.state = 137
            self.match(LienzoParser.T__4)
            self.state = 138
            self.cuerpo()
            self.state = 143
            _la = self._input.LA(1)
            if _la==LienzoParser.REGRESAR:
                self.state = 139
                localctx._REGRESAR = self.match(LienzoParser.REGRESAR)
                self.state = 140
                localctx._ss_expresion = self.ss_expresion()
                self.state = 141
                self.match(LienzoParser.T__0)



            if localctx._REGRESAR:
                if (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))) == "nada":
                    error((0 if localctx._ID is None else localctx._ID.line), "Funcion " + (None if localctx._ID is None else localctx._ID.text) + " no debe tener valor de retorno")
                elif localctx._ss_expresion.type != (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))):
                    error((0 if localctx._ID is None else localctx._ID.line), "Funcion " + (None if localctx._ID is None else localctx._ID.text) + " tiene valor de retorno de tipo incorrecto. Se esperaba un " + (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))))
                else:
                    cuadruplos.addCuadruplo(currentFunctionName, RETURN,localctx._ss_expresion.valor, None, None, False)
            else:
                if (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))) == "nada":
                    cuadruplos.addCuadruplo(currentFunctionName, RETURN,None,None,None,False)
                else:
                    error((0 if localctx._ID is None else localctx._ID.line), "Funcion " + (None if localctx._ID is None else localctx._ID.text) + " debe tener valor de retorno")

            self.state = 146
            self.match(LienzoParser.T__5)

            cuadruplos.addCuadruplo(currentFunctionName, RET, None, None, None, False)
            currentFunctionName = ""

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
        self.enterRule(localctx, 12, self.RULE_tipoFunc)
        try:
            self.state = 151
            token = self._input.LA(1)
            if token in [LienzoParser.TEXTO, LienzoParser.BOLEANO, LienzoParser.NUMERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.tipo()

            elif token in [LienzoParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
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
        self.enterRule(localctx, 14, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            localctx._tipo = self.tipo()
            self.state = 155
            _la = self._input.LA(1)
            if _la==LienzoParser.MODIFICABLE:
                self.state = 154
                localctx._MODIFICABLE = self.match(LienzoParser.MODIFICABLE)


            self.state = 157
            localctx._ID = self.match(LienzoParser.ID)

            modificable = False
            if (None if localctx._MODIFICABLE is None else localctx._MODIFICABLE.text):
                modificable = True
            if not namespaceTable.addParameter(currentFunctionName, (None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))), modificable):
                error((0 if localctx._ID is None else localctx._ID.line), "Parametro " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarado")
            else:
                memoryregisters.createMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)

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
        self.enterRule(localctx, 16, self.RULE_cuerpo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 160
                self.declaracion()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & ((1 << (LienzoParser.COLOR - 32)) | (1 << (LienzoParser.MOVER - 32)) | (1 << (LienzoParser.GIRAR - 32)) | (1 << (LienzoParser.LEVANTAR - 32)) | (1 << (LienzoParser.BAJAR - 32)) | (1 << (LienzoParser.MIENTRAS - 32)) | (1 << (LienzoParser.SI - 32)) | (1 << (LienzoParser.LEER - 32)) | (1 << (LienzoParser.ESCRIBIR - 32)) | (1 << (LienzoParser.IMPRIMIR - 32)) | (1 << (LienzoParser.ID - 32)))) != 0):
                self.state = 166
                self.instruccion_aux()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bloque_instruccionesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion_aux(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.Instruccion_auxContext)
            else:
                return self.getTypedRuleContext(LienzoParser.Instruccion_auxContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_bloque_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque_instrucciones" ):
                listener.enterBloque_instrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque_instrucciones" ):
                listener.exitBloque_instrucciones(self)




    def bloque_instrucciones(self):

        localctx = LienzoParser.Bloque_instruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bloque_instrucciones)
        self._la = 0 # Token type
        try:
            self.state = 181
            token = self._input.LA(1)
            if token in [LienzoParser.COLOR, LienzoParser.MOVER, LienzoParser.GIRAR, LienzoParser.LEVANTAR, LienzoParser.BAJAR, LienzoParser.MIENTRAS, LienzoParser.SI, LienzoParser.LEER, LienzoParser.ESCRIBIR, LienzoParser.IMPRIMIR, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.instruccion_aux()

            elif token in [LienzoParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(LienzoParser.T__4)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & ((1 << (LienzoParser.COLOR - 32)) | (1 << (LienzoParser.MOVER - 32)) | (1 << (LienzoParser.GIRAR - 32)) | (1 << (LienzoParser.LEVANTAR - 32)) | (1 << (LienzoParser.BAJAR - 32)) | (1 << (LienzoParser.MIENTRAS - 32)) | (1 << (LienzoParser.SI - 32)) | (1 << (LienzoParser.LEER - 32)) | (1 << (LienzoParser.ESCRIBIR - 32)) | (1 << (LienzoParser.IMPRIMIR - 32)) | (1 << (LienzoParser.ID - 32)))) != 0):
                    self.state = 174
                    self.instruccion_aux()
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 180
                self.match(LienzoParser.T__5)

            else:
                raise NoViableAltException(self)

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


        def llamadaFuncionPredefinida(self):
            return self.getTypedRuleContext(LienzoParser.LlamadaFuncionPredefinidaContext,0)


        def llamadaFuncion(self):
            return self.getTypedRuleContext(LienzoParser.LlamadaFuncionContext,0)


        def condicional(self):
            return self.getTypedRuleContext(LienzoParser.CondicionalContext,0)


        def mientrasQue(self):
            return self.getTypedRuleContext(LienzoParser.MientrasQueContext,0)


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
        self.enterRule(localctx, 20, self.RULE_instruccion_aux)
        try:
            self.state = 192
            token = self._input.LA(1)
            if token in [LienzoParser.COLOR, LienzoParser.MOVER, LienzoParser.GIRAR, LienzoParser.LEVANTAR, LienzoParser.BAJAR, LienzoParser.LEER, LienzoParser.ESCRIBIR, LienzoParser.IMPRIMIR, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self._errHandler.sync(self);
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 183
                    self.asignacion()
                    pass

                elif la_ == 2:
                    self.state = 184
                    self.llamadaFuncionPredefinida()
                    pass

                elif la_ == 3:
                    self.state = 185
                    self.llamadaFuncion()
                    pass


                self.state = 188
                self.match(LienzoParser.T__0)

            elif token in [LienzoParser.SI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.condicional()

            elif token in [LienzoParser.MIENTRAS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.mientrasQue()

            else:
                raise NoViableAltException(self)

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


        def mover_adelante(self):
            return self.getTypedRuleContext(LienzoParser.Mover_adelanteContext,0)


        def mover_atras(self):
            return self.getTypedRuleContext(LienzoParser.Mover_atrasContext,0)


        def girar_izquierda(self):
            return self.getTypedRuleContext(LienzoParser.Girar_izquierdaContext,0)


        def girar_derecha(self):
            return self.getTypedRuleContext(LienzoParser.Girar_derechaContext,0)


        def cambio_color(self):
            return self.getTypedRuleContext(LienzoParser.Cambio_colorContext,0)


        def subir_pluma(self):
            return self.getTypedRuleContext(LienzoParser.Subir_plumaContext,0)


        def bajar_pluma(self):
            return self.getTypedRuleContext(LienzoParser.Bajar_plumaContext,0)


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
        self.enterRule(localctx, 22, self.RULE_llamadaFuncionPredefinida)
        try:
            self.state = 204
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.lectura()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.escritura()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.imprimir()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 197
                self.mover_adelante()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 198
                self.mover_atras()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 199
                self.girar_izquierda()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 200
                self.girar_derecha()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 201
                self.cambio_color()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 202
                self.subir_pluma()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 203
                self.bajar_pluma()
                pass


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
            self._ss_expresion = None # Ss_expresionContext
            self._ID = None # Token

        def LEER(self):
            return self.getToken(LienzoParser.LEER, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


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
        self.enterRule(localctx, 24, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(LienzoParser.LEER)
            self.state = 207
            localctx._ss_expresion = self.ss_expresion()
            self.state = 208
            localctx._ID = self.match(LienzoParser.ID)

            idcontent=memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text),currentFunctionName)
            cuadruplos.addCuadruplo(currentFunctionName, READ, localctx._ss_expresion.valor, None, idcontent)

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
        self.enterRule(localctx, 26, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(LienzoParser.ESCRIBIR)
            self.state = 212
            localctx._ss_expresion = self.ss_expresion()

            cuadruplos.addCuadruplo(currentFunctionName, WRITE, localctx._ss_expresion.valor, None, None, False)

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
            self._ss_expresion = None # Ss_expresionContext

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
        self.enterRule(localctx, 28, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(LienzoParser.IMPRIMIR)
            self.state = 216
            localctx._ss_expresion = self.ss_expresion()

            cuadruplos.addCuadruplo(currentFunctionName, PRINT, localctx._ss_expresion.valor, None, None, False)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mover_adelanteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext

        def MOVER(self):
            return self.getToken(LienzoParser.MOVER, 0)

        def ADELANTE(self):
            return self.getToken(LienzoParser.ADELANTE, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_mover_adelante

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMover_adelante" ):
                listener.enterMover_adelante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMover_adelante" ):
                listener.exitMover_adelante(self)




    def mover_adelante(self):

        localctx = LienzoParser.Mover_adelanteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_mover_adelante)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(LienzoParser.MOVER)
            self.state = 220
            self.match(LienzoParser.ADELANTE)
            self.state = 221
            localctx._ss_expresion = self.ss_expresion()

            cuadruplos.addCuadruplo(currentFunctionName, FORWARD, localctx._ss_expresion.valor, None, None, False)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mover_atrasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext

        def MOVER(self):
            return self.getToken(LienzoParser.MOVER, 0)

        def ATRAS(self):
            return self.getToken(LienzoParser.ATRAS, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_mover_atras

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMover_atras" ):
                listener.enterMover_atras(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMover_atras" ):
                listener.exitMover_atras(self)




    def mover_atras(self):

        localctx = LienzoParser.Mover_atrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_mover_atras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(LienzoParser.MOVER)
            self.state = 225
            self.match(LienzoParser.ATRAS)
            self.state = 226
            localctx._ss_expresion = self.ss_expresion()

            cuadruplos.addCuadruplo(currentFunctionName, BACKWARD, localctx._ss_expresion.valor, None, None, False)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Girar_derechaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext

        def GIRAR(self):
            return self.getToken(LienzoParser.GIRAR, 0)

        def DERECHA(self):
            return self.getToken(LienzoParser.DERECHA, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_girar_derecha

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGirar_derecha" ):
                listener.enterGirar_derecha(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGirar_derecha" ):
                listener.exitGirar_derecha(self)




    def girar_derecha(self):

        localctx = LienzoParser.Girar_derechaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_girar_derecha)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(LienzoParser.GIRAR)
            self.state = 230
            self.match(LienzoParser.DERECHA)
            self.state = 231
            localctx._ss_expresion = self.ss_expresion()

            cuadruplos.addCuadruplo(currentFunctionName, RIGHT, localctx._ss_expresion.valor, None, None, False)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Girar_izquierdaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext

        def GIRAR(self):
            return self.getToken(LienzoParser.GIRAR, 0)

        def IZQUIERDA(self):
            return self.getToken(LienzoParser.IZQUIERDA, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_girar_izquierda

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGirar_izquierda" ):
                listener.enterGirar_izquierda(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGirar_izquierda" ):
                listener.exitGirar_izquierda(self)




    def girar_izquierda(self):

        localctx = LienzoParser.Girar_izquierdaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_girar_izquierda)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(LienzoParser.GIRAR)
            self.state = 235
            self.match(LienzoParser.IZQUIERDA)
            self.state = 236
            localctx._ss_expresion = self.ss_expresion()

            cuadruplos.addCuadruplo(currentFunctionName, LEFT, localctx._ss_expresion.valor, None, None, False)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Subir_plumaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEVANTAR(self):
            return self.getToken(LienzoParser.LEVANTAR, 0)

        def PLUMA(self):
            return self.getToken(LienzoParser.PLUMA, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_subir_pluma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubir_pluma" ):
                listener.enterSubir_pluma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubir_pluma" ):
                listener.exitSubir_pluma(self)




    def subir_pluma(self):

        localctx = LienzoParser.Subir_plumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_subir_pluma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(LienzoParser.LEVANTAR)
            self.state = 240
            self.match(LienzoParser.PLUMA)

            cuadruplos.addCuadruplo(currentFunctionName, PENUP, None, None, None, False)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bajar_plumaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BAJAR(self):
            return self.getToken(LienzoParser.BAJAR, 0)

        def PLUMA(self):
            return self.getToken(LienzoParser.PLUMA, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_bajar_pluma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBajar_pluma" ):
                listener.enterBajar_pluma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBajar_pluma" ):
                listener.exitBajar_pluma(self)




    def bajar_pluma(self):

        localctx = LienzoParser.Bajar_plumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_bajar_pluma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(LienzoParser.BAJAR)
            self.state = 244
            self.match(LienzoParser.PLUMA)

            cuadruplos.addCuadruplo(currentFunctionName, PENDOWN, None, None, None, False)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cambio_colorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._color = None # ColorContext

        def COLOR(self):
            return self.getToken(LienzoParser.COLOR, 0)

        def DE(self):
            return self.getToken(LienzoParser.DE, 0)

        def PLUMA(self):
            return self.getToken(LienzoParser.PLUMA, 0)

        def color(self):
            return self.getTypedRuleContext(LienzoParser.ColorContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_cambio_color

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCambio_color" ):
                listener.enterCambio_color(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCambio_color" ):
                listener.exitCambio_color(self)




    def cambio_color(self):

        localctx = LienzoParser.Cambio_colorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_cambio_color)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(LienzoParser.COLOR)
            self.state = 248
            self.match(LienzoParser.DE)
            self.state = 249
            self.match(LienzoParser.PLUMA)
            self.state = 250
            self.match(LienzoParser.EQUALS)
            self.state = 251
            localctx._color = self.color()

            cuadruplos.addCuadruplo(currentFunctionName, COLOR_CHANGE, (None if localctx._color is None else self._input.getText((localctx._color.start,localctx._color.stop))), None, None, False)

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
        self.enterRule(localctx, 44, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 255
            self.match(LienzoParser.EQUALS)
            self.state = 256
            localctx._ss_expresion = self.ss_expresion()

            idType = namespaceTable.getVariableType((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
            if not idType:
                error((0 if localctx._ID is None else localctx._ID.line), "Variable " + (None if localctx._ID is None else localctx._ID.text) + " no ha sido declarada")
            elif localctx._ss_expresion.type != idType:
                error((0 if localctx._ID is None else localctx._ID.line), "Variable " + (None if localctx._ID is None else localctx._ID.text) + " es de tipo " + idType)
            else:
                idcontent = memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
                cuadruplos.addCuadruplo(currentFunctionName, '=', localctx._ss_expresion.valor, None, idcontent)

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
        self.enterRule(localctx, 46, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
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

    class CondicionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext
            self._SINO = None # Token

        def SI(self):
            return self.getToken(LienzoParser.SI, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def bloque_instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.Bloque_instruccionesContext)
            else:
                return self.getTypedRuleContext(LienzoParser.Bloque_instruccionesContext,i)


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
        self.enterRule(localctx, 48, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(LienzoParser.SI)
            self.state = 262
            localctx._ss_expresion = self.ss_expresion()

            if localctx._ss_expresion.type != BOLEANO:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "el estatuto 'si' necesita una boleano")
            else:
                cuadruplos.addCuadruplo(currentFunctionName, GOTOF, localctx._ss_expresion.valor, None, None, False)
                cuadruplos.pushPilaSaltos(cuadruplos.last())

            self.state = 264
            self.bloque_instrucciones()
            self.state = 270
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 265
                localctx._SINO = self.match(LienzoParser.SINO)

                if localctx._SINO:
                    cuadruplos.addCuadruplo(currentFunctionName, GOTO,None,None,None,False)
                    cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(),cuadruplos.current())
                    cuadruplos.pushPilaSaltos(cuadruplos.last())

                self.state = 267
                self.bloque_instrucciones()

                cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(),cuadruplos.current())



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


        def bloque_instrucciones(self):
            return self.getTypedRuleContext(LienzoParser.Bloque_instruccionesContext,0)


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
        self.enterRule(localctx, 50, self.RULE_mientrasQue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(LienzoParser.MIENTRAS)
            self.state = 273
            self.match(LienzoParser.QUE)

            cuadruplos.pushPilaSaltos(cuadruplos.current())

            self.state = 275
            localctx._ss_expresion = self.ss_expresion()

            if localctx._ss_expresion.type != BOLEANO:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "el estatuto 'mientras que' necesita una boleano")
            else:
                cuadruplos.addCuadruplo(currentFunctionName, GOTOF,localctx._ss_expresion.valor,None,None,False)
                cuadruplos.pushPilaSaltos(cuadruplos.last())

            self.state = 277
            self.bloque_instrucciones()

            pop1 = cuadruplos.popPilaSaltos()
            pop2 = cuadruplos.popPilaSaltos()
            cuadruplos.addCuadruplo(currentFunctionName, GOTO,None,None,pop2,False)
            cuadruplos.editCuadruplo(pop1,cuadruplos.current())

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
            self.name = None
            self.type = None
            self._ID = None # Token
            self.ss_exp1 = None # Ss_expresionContext
            self.ss_exp2 = None # Ss_expresionContext
            self.paren = None # Token

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
        self.enterRule(localctx, 52, self.RULE_llamadaFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            localctx._ID = self.match(LienzoParser.ID)

            functionType = namespaceTable.getFunctionType((None if localctx._ID is None else localctx._ID.text))
            localctx.name = (None if localctx._ID is None else localctx._ID.text)
            if not functionType:
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": llamada a funcion", (None if localctx._ID is None else localctx._ID.text), "inexistente")
            else:
                localctx.type = None if functionType == "nada" else functionType
                cuadruplos.addCuadruplo(currentFunctionName, ERA, (None if localctx._ID is None else localctx._ID.text), None, None, False)

            self.state = 282
            self.match(LienzoParser.T__1)

            k = 0

            self.state = 295
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__1) | (1 << LienzoParser.T__15) | (1 << LienzoParser.T__19) | (1 << LienzoParser.COLOR) | (1 << LienzoParser.MOVER) | (1 << LienzoParser.GIRAR) | (1 << LienzoParser.LEVANTAR) | (1 << LienzoParser.BAJAR) | (1 << LienzoParser.LEER) | (1 << LienzoParser.ESCRIBIR) | (1 << LienzoParser.IMPRIMIR) | (1 << LienzoParser.BOOLEAN_CONSTANT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (LienzoParser.NUMERIC_CONSTANT - 64)) | (1 << (LienzoParser.STRING_CONSTANT - 64)) | (1 << (LienzoParser.ID - 64)))) != 0):
                self.state = 284
                localctx.ss_exp1 = self.ss_expresion()

                if namespaceTable.argumentAgree((None if localctx._ID is None else localctx._ID.text), k, (None if localctx.ss_exp1 is None else self._input.getText((localctx.ss_exp1.start,localctx.ss_exp1.stop))), localctx.ss_exp1.type):
                    cuadruplos.addCuadruplo(currentFunctionName, PARAM, localctx.ss_exp1.valor, None, "param" + str(k))
                else:
                    error((None if localctx.ss_exp1 is None else localctx.ss_exp1.start).line, ": argumento #" + k + "no concuerda con el parametro esperado")
                k += 1

                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__2:
                    self.state = 286
                    self.match(LienzoParser.T__2)
                    self.state = 287
                    localctx.ss_exp2 = self.ss_expresion()

                    if namespaceTable.argumentAgree((None if localctx._ID is None else localctx._ID.text), k, (None if localctx.ss_exp2 is None else self._input.getText((localctx.ss_exp2.start,localctx.ss_exp2.stop))), localctx.ss_exp2.type):
                        cuadruplos.addCuadruplo(currentFunctionName, PARAM, localctx.ss_exp2.valor, None, "param" + str(k))
                    else:
                        error((None if localctx.ss_exp1 is None else localctx.ss_exp1.start).line, ": argumento #" + k + "no concuerda con el parametro esperado")
                    k += 1

                    self.state = 294
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 297
            localctx.paren = self.match(LienzoParser.T__3)

            amountOfParameters = namespaceTable.getParameterAmount((None if localctx._ID is None else localctx._ID.text))
            if k != amountOfParameters:
                error((0 if localctx.paren is None else localctx.paren.line), "Se esperaban" + amountOfParameters + " parametros, se recibieron " + k)
            else:
                cuadruplos.addCuadruplo(currentFunctionName, GOSUB, (None if localctx._ID is None else localctx._ID.text), namespaceTable.getDireccionInicio((None if localctx._ID is None else localctx._ID.text)), None, False)

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
        self.enterRule(localctx, 54, self.RULE_ss_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            localctx.s_exp1 = self.s_expresion()

            localctx.type = localctx.s_exp1.type
            localctx.valor = localctx.s_exp1.valor

            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 302
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==LienzoParser.T__6 or _la==LienzoParser.T__7):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 303
                    localctx.s_exp2 = self.s_expresion()

                    tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.s_exp2.type]
                    if not tipo:
                        print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.s_exp2.type)
                    else:
                        namespaceTable.addTemporal(currentFunctionName, tipo)
                        localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text),localctx.valor,localctx.s_exp2.valor)
                    localctx.type = tipo
             
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 56, self.RULE_s_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            localctx.exp1 = self.expresion()

            localctx.type = localctx.exp1.type
            localctx.valor = localctx.exp1.valor

            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 313
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__8) | (1 << LienzoParser.T__9) | (1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12) | (1 << LienzoParser.T__13))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 314
                    localctx.exp2 = self.expresion()

                    tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.exp2.type]
                    if not tipo:
                        print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.exp2.type)
                    else:
                        localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text),localctx.valor,localctx.exp2.valor)
                        namespaceTable.addTemporal(currentFunctionName, tipo)
                    localctx.type = tipo
             
                self.state = 322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            localctx.term1 = self.termino()

            localctx.type = localctx.term1.type
            localctx.valor = localctx.term1.valor

            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 325
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==LienzoParser.T__14 or _la==LienzoParser.T__15):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 326
                    localctx.term2 = self.termino()

                    tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.term2.type]
                    if not tipo:
                        print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.term2.type)
                    else:
                        localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text),localctx.valor,localctx.term2.valor)
                        namespaceTable.addTemporal(currentFunctionName, tipo)
                    localctx.type = tipo
             
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 60, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            localctx.factor1 = self.factor()

            localctx.type = localctx.factor1.type
            localctx.valor = localctx.factor1.valor

            self.state = 343
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 337
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__16) | (1 << LienzoParser.T__17) | (1 << LienzoParser.T__18))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 338
                    localctx.factor2 = self.factor()

                    tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.factor2.type]
                    if not tipo:
                        print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.factor2.type)
                    else:
                        localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text),localctx.valor,localctx.factor2.valor)
                        namespaceTable.addTemporal(currentFunctionName, tipo)
                    localctx.type = tipo
             
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 62, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 361
            token = self._input.LA(1)
            if token in [LienzoParser.T__1, LienzoParser.T__19, LienzoParser.COLOR, LienzoParser.MOVER, LienzoParser.GIRAR, LienzoParser.LEVANTAR, LienzoParser.BAJAR, LienzoParser.LEER, LienzoParser.ESCRIBIR, LienzoParser.IMPRIMIR, LienzoParser.BOOLEAN_CONSTANT, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                _la = self._input.LA(1)
                if _la==LienzoParser.T__19:
                    self.state = 346
                    localctx.neg = self.match(LienzoParser.T__19)


                self.state = 349
                localctx._factor_aux = self.factor_aux()

                localctx.type = localctx._factor_aux.type
                if (None if localctx.neg is None else localctx.neg.text) and localctx._factor_aux.type != BOLEANO:
                    error((0 if localctx.neg is None else localctx.neg.line), "operador " + (None if localctx.neg is None else localctx.neg.text) + " no puede ser aplicado a " + localctx._factor_aux.type)
                    localctx.type = None
                else:
                    if (None if localctx.neg is None else localctx.neg.text):
                        localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.neg is None else localctx.neg.text), localctx._factor_aux.valor, None)
                        namespaceTable.addTemporal(currentFunctionName, localctx.type)
                    else:
                        localctx.valor = localctx._factor_aux.valor


            elif token in [LienzoParser.T__15, LienzoParser.NUMERIC_CONSTANT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                _la = self._input.LA(1)
                if _la==LienzoParser.T__15:
                    self.state = 353
                    localctx.neg = self.match(LienzoParser.T__15)


                self.state = 356
                localctx._NUMERIC_CONSTANT = self.match(LienzoParser.NUMERIC_CONSTANT)

                localctx.type = NUMERO

                if (None if localctx.neg is None else localctx.neg.text):
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.neg is None else localctx.neg.text), num((None if localctx._NUMERIC_CONSTANT is None else localctx._NUMERIC_CONSTANT.text)), None)
                    namespaceTable.addTemporal(currentFunctionName, localctx.type)
                else:
                    localctx.valor = num((None if localctx._NUMERIC_CONSTANT is None else localctx._NUMERIC_CONSTANT.text))


            elif token in [LienzoParser.STRING_CONSTANT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 359
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


        def llamadaFuncionPredefinida(self):
            return self.getTypedRuleContext(LienzoParser.LlamadaFuncionPredefinidaContext,0)


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
        self.enterRule(localctx, 64, self.RULE_factor_aux)
        try:
            self.state = 376
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                localctx._ID = self.match(LienzoParser.ID)

                localctx.type = namespaceTable.getVariableType((None if localctx._ID is None else localctx._ID.text), currentFunctionName)

                if localctx.type:
                    localctx.valor = memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
                    namespaceTable.addTemporal(currentFunctionName, localctx.type)
                else:
                    localctx.valor = None
                    error((0 if localctx._ID is None else localctx._ID.line), "variable " + (None if localctx._ID is None else localctx._ID.text) + " no ha sido declarada")

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                localctx._BOOLEAN_CONSTANT = self.match(LienzoParser.BOOLEAN_CONSTANT)

                localctx.type = BOLEANO
                localctx.valor = True if (None if localctx._BOOLEAN_CONSTANT is None else localctx._BOOLEAN_CONSTANT.text) == 'verdadero' else False

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 367
                localctx._llamadaFuncion = self.llamadaFuncion()

                functionType = localctx._llamadaFuncion.type
                localctx.type = functionType if functionType != "nada" else None
                if functionType:
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, '=', memoryregisters.getMemoryRegister(localctx._llamadaFuncion.name, ""), None)
                else:
                    localctx.valor = None

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 370
                self.match(LienzoParser.T__1)
                self.state = 371
                localctx._ss_expresion = self.ss_expresion()
                self.state = 372
                self.match(LienzoParser.T__3)

                localctx.type = localctx._ss_expresion.type
                if localctx.type:
                    localctx.valor = localctx._ss_expresion.valor
                else:
                    localctx.valor = None

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 375
                self.llamadaFuncionPredefinida()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





