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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3:")
        buf.write("\u013f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\7\2;\n\2\f")
        buf.write("\2\16\2>\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\7\bc\n")
        buf.write("\b\f\b\16\bf\13\b\3\b\7\bi\n\b\f\b\16\bl\13\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n{\n\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\5\13\u0082\n\13\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\7\21\u00a1\n\21\f\21\16\21\u00a4\13\21\3\21")
        buf.write("\3\21\3\21\3\21\7\21\u00aa\n\21\f\21\16\21\u00ad\13\21")
        buf.write("\3\21\5\21\u00b0\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\7\22\u00ba\n\22\f\22\16\22\u00bd\13\22\3\22\3")
        buf.write("\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23")
        buf.write("\u00ca\n\23\f\23\16\23\u00cd\13\23\5\23\u00cf\n\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00da\n")
        buf.write("\24\f\24\16\24\u00dd\13\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\7\25\u00e6\n\25\f\25\16\25\u00e9\13\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\7\26\u00f2\n\26\f\26\16\26")
        buf.write("\u00f5\13\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00fd")
        buf.write("\n\27\f\27\16\27\u0100\13\27\3\30\5\30\u0103\n\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u010a\n\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\5\30\u0111\n\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u011f\n\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\7\32\u0127\n\32\f\32\16\32\u012a")
        buf.write("\13\32\5\32\u012c\n\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\33\3\33\5\33\u0136\n\33\3\34\3\34\5\34\u013a\n\34\3\34")
        buf.write("\3\34\3\34\3\34\2\2\35\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\66\2\b\3\2\30!\4\2//\61\62\3")
        buf.write("\2\t\n\3\2\13\20\3\2\21\22\3\2\23\25\u0141\28\3\2\2\2")
        buf.write("\4B\3\2\2\2\6J\3\2\2\2\bP\3\2\2\2\nR\3\2\2\2\f[\3\2\2")
        buf.write("\2\16d\3\2\2\2\20m\3\2\2\2\22z\3\2\2\2\24\u0081\3\2\2")
        buf.write("\2\26\u0083\3\2\2\2\30\u0087\3\2\2\2\32\u008f\3\2\2\2")
        buf.write("\34\u0094\3\2\2\2\36\u0096\3\2\2\2 \u0099\3\2\2\2\"\u00b1")
        buf.write("\3\2\2\2$\u00c0\3\2\2\2&\u00d3\3\2\2\2(\u00de\3\2\2\2")
        buf.write("*\u00ea\3\2\2\2,\u00f6\3\2\2\2.\u0110\3\2\2\2\60\u011e")
        buf.write("\3\2\2\2\62\u0120\3\2\2\2\64\u0135\3\2\2\2\66\u0137\3")
        buf.write("\2\2\28<\5\4\3\29;\5\62\32\2:9\3\2\2\2;>\3\2\2\2<:\3\2")
        buf.write("\2\2<=\3\2\2\2=?\3\2\2\2><\3\2\2\2?@\5\f\7\2@A\7\2\2\3")
        buf.write("A\3\3\2\2\2BC\7#\2\2CD\7\3\2\2DE\5\6\4\2EF\7\4\2\2FG\5")
        buf.write("\n\6\2GH\7\4\2\2HI\7\5\2\2I\5\3\2\2\2JK\7\"\2\2KL\7\'")
        buf.write("\2\2LM\7#\2\2MN\7$\2\2NO\5\b\5\2O\7\3\2\2\2PQ\t\2\2\2")
        buf.write("Q\t\3\2\2\2RS\7%\2\2ST\7\'\2\2TU\7#\2\2UV\7$\2\2VW\5&")
        buf.write("\24\2WX\7&\2\2XY\5&\24\2YZ\b\6\1\2Z\13\3\2\2\2[\\\7)\2")
        buf.write("\2\\]\b\7\1\2]^\7\3\2\2^_\5\16\b\2_`\7\5\2\2`\r\3\2\2")
        buf.write("\2ac\5\20\t\2ba\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2")
        buf.write("ej\3\2\2\2fd\3\2\2\2gi\5\22\n\2hg\3\2\2\2il\3\2\2\2jh")
        buf.write("\3\2\2\2jk\3\2\2\2k\17\3\2\2\2lj\3\2\2\2mn\5\34\17\2n")
        buf.write("o\7:\2\2op\b\t\1\2pq\7$\2\2qr\5&\24\2rs\7\4\2\2st\b\t")
        buf.write("\1\2t\21\3\2\2\2u{\5\32\16\2v{\5 \21\2w{\5\"\22\2x{\5")
        buf.write("\24\13\2y{\5$\23\2zu\3\2\2\2zv\3\2\2\2zw\3\2\2\2zx\3\2")
        buf.write("\2\2zy\3\2\2\2{|\3\2\2\2|}\7\4\2\2}\23\3\2\2\2~\u0082")
        buf.write("\5\26\f\2\177\u0082\5\30\r\2\u0080\u0082\5\36\20\2\u0081")
        buf.write("~\3\2\2\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082")
        buf.write("\25\3\2\2\2\u0083\u0084\7\60\2\2\u0084\u0085\7:\2\2\u0085")
        buf.write("\u0086\b\f\1\2\u0086\27\3\2\2\2\u0087\u0088\7\63\2\2\u0088")
        buf.write("\u0089\5&\24\2\u0089\u008a\7(\2\2\u008a\u008b\5*\26\2")
        buf.write("\u008b\u008c\7\6\2\2\u008c\u008d\5*\26\2\u008d\u008e\b")
        buf.write("\r\1\2\u008e\31\3\2\2\2\u008f\u0090\7:\2\2\u0090\u0091")
        buf.write("\7$\2\2\u0091\u0092\5&\24\2\u0092\u0093\b\16\1\2\u0093")
        buf.write("\33\3\2\2\2\u0094\u0095\t\3\2\2\u0095\35\3\2\2\2\u0096")
        buf.write("\u0097\7\64\2\2\u0097\u0098\5&\24\2\u0098\37\3\2\2\2\u0099")
        buf.write("\u009a\7-\2\2\u009a\u009b\7\7\2\2\u009b\u009c\5&\24\2")
        buf.write("\u009c\u009d\7\b\2\2\u009d\u009e\b\21\1\2\u009e\u00a2")
        buf.write("\7\3\2\2\u009f\u00a1\5\22\n\2\u00a0\u009f\3\2\2\2\u00a1")
        buf.write("\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00af\7")
        buf.write("\5\2\2\u00a6\u00a7\7.\2\2\u00a7\u00ab\7\3\2\2\u00a8\u00aa")
        buf.write("\5\22\n\2\u00a9\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2")
        buf.write("\u00ad\u00ab\3\2\2\2\u00ae\u00b0\7\5\2\2\u00af\u00a6\3")
        buf.write("\2\2\2\u00af\u00b0\3\2\2\2\u00b0!\3\2\2\2\u00b1\u00b2")
        buf.write("\7+\2\2\u00b2\u00b3\7,\2\2\u00b3\u00b4\7\7\2\2\u00b4\u00b5")
        buf.write("\5&\24\2\u00b5\u00b6\7\b\2\2\u00b6\u00b7\b\22\1\2\u00b7")
        buf.write("\u00bb\7\3\2\2\u00b8\u00ba\5\22\n\2\u00b9\u00b8\3\2\2")
        buf.write("\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc")
        buf.write("\3\2\2\2\u00bc\u00be\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be")
        buf.write("\u00bf\7\5\2\2\u00bf#\3\2\2\2\u00c0\u00c1\7:\2\2\u00c1")
        buf.write("\u00c2\b\23\1\2\u00c2\u00ce\7\7\2\2\u00c3\u00c4\5&\24")
        buf.write("\2\u00c4\u00cb\b\23\1\2\u00c5\u00c6\7\6\2\2\u00c6\u00c7")
        buf.write("\5&\24\2\u00c7\u00c8\b\23\1\2\u00c8\u00ca\3\2\2\2\u00c9")
        buf.write("\u00c5\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3")
        buf.write("\2\2\2\u00ce\u00c3\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d1\7\b\2\2\u00d1\u00d2\b\23\1\2\u00d2")
        buf.write("%\3\2\2\2\u00d3\u00d4\5(\25\2\u00d4\u00db\b\24\1\2\u00d5")
        buf.write("\u00d6\t\4\2\2\u00d6\u00d7\5(\25\2\u00d7\u00d8\b\24\1")
        buf.write("\2\u00d8\u00da\3\2\2\2\u00d9\u00d5\3\2\2\2\u00da\u00dd")
        buf.write("\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write("\'\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\5*\26\2\u00df")
        buf.write("\u00e7\b\25\1\2\u00e0\u00e1\t\5\2\2\u00e1\u00e2\5*\26")
        buf.write("\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\b\25\1\2\u00e4\u00e6")
        buf.write("\3\2\2\2\u00e5\u00e0\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8)\3\2\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00ea\u00eb\5,\27\2\u00eb\u00f3\b\26\1")
        buf.write("\2\u00ec\u00ed\t\6\2\2\u00ed\u00ee\5,\27\2\u00ee\u00ef")
        buf.write("\3\2\2\2\u00ef\u00f0\b\26\1\2\u00f0\u00f2\3\2\2\2\u00f1")
        buf.write("\u00ec\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2")
        buf.write("\u00f3\u00f4\3\2\2\2\u00f4+\3\2\2\2\u00f5\u00f3\3\2\2")
        buf.write("\2\u00f6\u00f7\5.\30\2\u00f7\u00fe\b\27\1\2\u00f8\u00f9")
        buf.write("\t\7\2\2\u00f9\u00fa\5.\30\2\u00fa\u00fb\b\27\1\2\u00fb")
        buf.write("\u00fd\3\2\2\2\u00fc\u00f8\3\2\2\2\u00fd\u0100\3\2\2\2")
        buf.write("\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff-\3\2\2")
        buf.write("\2\u0100\u00fe\3\2\2\2\u0101\u0103\7\26\2\2\u0102\u0101")
        buf.write("\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\3\2\2\2\u0104")
        buf.write("\u0105\5\60\31\2\u0105\u0106\3\2\2\2\u0106\u0107\b\30")
        buf.write("\1\2\u0107\u0111\3\2\2\2\u0108\u010a\7\22\2\2\u0109\u0108")
        buf.write("\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u010c\78\2\2\u010c\u010d\3\2\2\2\u010d\u0111\b\30\1\2")
        buf.write("\u010e\u010f\79\2\2\u010f\u0111\b\30\1\2\u0110\u0102\3")
        buf.write("\2\2\2\u0110\u0109\3\2\2\2\u0110\u010e\3\2\2\2\u0111/")
        buf.write("\3\2\2\2\u0112\u0113\7:\2\2\u0113\u011f\b\31\1\2\u0114")
        buf.write("\u0115\7\66\2\2\u0115\u011f\b\31\1\2\u0116\u0117\5$\23")
        buf.write("\2\u0117\u0118\b\31\1\2\u0118\u011f\3\2\2\2\u0119\u011a")
        buf.write("\7\7\2\2\u011a\u011b\5&\24\2\u011b\u011c\7\b\2\2\u011c")
        buf.write("\u011d\b\31\1\2\u011d\u011f\3\2\2\2\u011e\u0112\3\2\2")
        buf.write("\2\u011e\u0114\3\2\2\2\u011e\u0116\3\2\2\2\u011e\u0119")
        buf.write("\3\2\2\2\u011f\61\3\2\2\2\u0120\u0121\5\64\33\2\u0121")
        buf.write("\u0122\7:\2\2\u0122\u012b\7\7\2\2\u0123\u0128\5\66\34")
        buf.write("\2\u0124\u0125\7\6\2\2\u0125\u0127\5\66\34\2\u0126\u0124")
        buf.write("\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\u012c\3\2\2\2\u012a\u0128\3\2\2\2")
        buf.write("\u012b\u0123\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d\3")
        buf.write("\2\2\2\u012d\u012e\7\b\2\2\u012e\u012f\b\32\1\2\u012f")
        buf.write("\u0130\7\3\2\2\u0130\u0131\5\16\b\2\u0131\u0132\7\5\2")
        buf.write("\2\u0132\63\3\2\2\2\u0133\u0136\5\34\17\2\u0134\u0136")
        buf.write("\7\65\2\2\u0135\u0133\3\2\2\2\u0135\u0134\3\2\2\2\u0136")
        buf.write("\65\3\2\2\2\u0137\u0139\5\34\17\2\u0138\u013a\7\67\2\2")
        buf.write("\u0139\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\3")
        buf.write("\2\2\2\u013b\u013c\7:\2\2\u013c\u013d\b\34\1\2\u013d\67")
        buf.write("\3\2\2\2\31<djz\u0081\u00a2\u00ab\u00af\u00bb\u00cb\u00ce")
        buf.write("\u00db\u00e7\u00f3\u00fe\u0102\u0109\u0110\u011e\u0128")
        buf.write("\u012b\u0135\u0139")
        return buf.getvalue()


class LienzoParser ( Parser ):

    grammarFileName = "Lienzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "';'", "'}'", "','", "'('", "')'", 
                     "'&'", "'|'", "'=='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "<INVALID>", 
                     "'rojo'", "'verde'", "'amarillo'", "'azul'", "'blanco'", 
                     "'negro'", "'morado'", "'naranja'", "'cafe'", "'gris'", 
                     "'color'", "'lienzo'", "'='", "'tamano'", "'por'", 
                     "'de'", "'en'", "'dibujo'", "'dormir'", "'mientras'", 
                     "'que'", "'si'", "'sino'", "'texto'", "'leer'", "'boleano'", 
                     "'numero'", "'escribir'", "'imprimir'", "'nada'", "<INVALID>", 
                     "'modificable'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "ROJO", "VERDE", "AMARILLO", "AZUL", 
                      "BLANCO", "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", 
                      "COLOR", "LIENZO", "EQUALS", "TAMANO", "POR", "DE", 
                      "EN", "DIBUJO", "DORMIR", "MIENTRAS", "QUE", "SI", 
                      "SINO", "TEXTO", "LEER", "BOLEANO", "NUMERO", "ESCRIBIR", 
                      "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", "MODIFICABLE", 
                      "NUMERIC_CONSTANT", "STRING_CONSTANT", "ID" ]

    RULE_program = 0
    RULE_lienzo = 1
    RULE_colorLienzo = 2
    RULE_color = 3
    RULE_tamanoLienzo = 4
    RULE_dibujo = 5
    RULE_cuerpo = 6
    RULE_declaracion = 7
    RULE_instruccion_aux = 8
    RULE_llamadaFuncionPredefinida = 9
    RULE_lectura = 10
    RULE_escritura = 11
    RULE_asignacion = 12
    RULE_tipo = 13
    RULE_imprimir = 14
    RULE_condicional = 15
    RULE_mientrasQue = 16
    RULE_llamadaFuncion = 17
    RULE_ss_expresion = 18
    RULE_s_expresion = 19
    RULE_expresion = 20
    RULE_termino = 21
    RULE_factor = 22
    RULE_factor_aux = 23
    RULE_funcion = 24
    RULE_tipoFunc = 25
    RULE_parametro = 26

    ruleNames =  [ "program", "lienzo", "colorLienzo", "color", "tamanoLienzo", 
                   "dibujo", "cuerpo", "declaracion", "instruccion_aux", 
                   "llamadaFuncionPredefinida", "lectura", "escritura", 
                   "asignacion", "tipo", "imprimir", "condicional", "mientrasQue", 
                   "llamadaFuncion", "ss_expresion", "s_expresion", "expresion", 
                   "termino", "factor", "factor_aux", "funcion", "tipoFunc", 
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
    DIBUJO=39
    DORMIR=40
    MIENTRAS=41
    QUE=42
    SI=43
    SINO=44
    TEXTO=45
    LEER=46
    BOLEANO=47
    NUMERO=48
    ESCRIBIR=49
    IMPRIMIR=50
    NADA=51
    BOOLEAN_CONSTANT=52
    MODIFICABLE=53
    NUMERIC_CONSTANT=54
    STRING_CONSTANT=55
    ID=56

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
            self.state = 54
            self.lienzo()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO) | (1 << LienzoParser.NADA))) != 0):
                self.state = 55
                self.funcion()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.dibujo()
            self.state = 62
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
            self.state = 64
            self.match(LienzoParser.LIENZO)
            self.state = 65
            self.match(LienzoParser.T__0)
            self.state = 66
            self.colorLienzo()
            self.state = 67
            self.match(LienzoParser.T__1)
            self.state = 68
            self.tamanoLienzo()
            self.state = 69
            self.match(LienzoParser.T__1)
            self.state = 70
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
            self.state = 72
            self.match(LienzoParser.COLOR)
            self.state = 73
            self.match(LienzoParser.DE)
            self.state = 74
            self.match(LienzoParser.LIENZO)
            self.state = 75
            self.match(LienzoParser.EQUALS)
            self.state = 76
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
            self.state = 78
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
            self.state = 80
            self.match(LienzoParser.TAMANO)
            self.state = 81
            self.match(LienzoParser.DE)
            self.state = 82
            self.match(LienzoParser.LIENZO)
            self.state = 83
            self.match(LienzoParser.EQUALS)
            self.state = 84
            localctx.largo = self.ss_expresion()
            self.state = 85
            self.match(LienzoParser.POR)
            self.state = 86
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
        self.enterRule(localctx, 10, self.RULE_dibujo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            localctx._DIBUJO = self.match(LienzoParser.DIBUJO)

            global currentFunctionName
            currentFunctionName = (None if localctx._DIBUJO is None else localctx._DIBUJO.text)
            namespaceTable.addFunction(currentFunctionName, "nada", [])
            memoryregisters.newFunction(currentFunctionName)

            self.state = 91
            self.match(LienzoParser.T__0)
            self.state = 92
            self.cuerpo()
            self.state = 93
            self.match(LienzoParser.T__2)
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
        self.enterRule(localctx, 12, self.RULE_cuerpo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 95
                self.declaracion()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MIENTRAS) | (1 << LienzoParser.SI) | (1 << LienzoParser.LEER) | (1 << LienzoParser.ESCRIBIR) | (1 << LienzoParser.IMPRIMIR) | (1 << LienzoParser.ID))) != 0):
                self.state = 101
                self.instruccion_aux()
                self.state = 106
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
        self.enterRule(localctx, 14, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            localctx._tipo = self.tipo()
            self.state = 108
            localctx._ID = self.match(LienzoParser.ID)

            if namespaceTable.variableExists((None if localctx._ID is None else localctx._ID.text), currentFunctionName):
                error((0 if localctx._ID is None else localctx._ID.line), ": Variable " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarada")

            self.state = 110
            self.match(LienzoParser.EQUALS)
            self.state = 111
            localctx._ss_expresion = self.ss_expresion()
            self.state = 112
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
        self.enterRule(localctx, 16, self.RULE_instruccion_aux)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 115
                self.asignacion()
                pass

            elif la_ == 2:
                self.state = 116
                self.condicional()
                pass

            elif la_ == 3:
                self.state = 117
                self.mientrasQue()
                pass

            elif la_ == 4:
                self.state = 118
                self.llamadaFuncionPredefinida()
                pass

            elif la_ == 5:
                self.state = 119
                self.llamadaFuncion()
                pass


            self.state = 122
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
        self.enterRule(localctx, 18, self.RULE_llamadaFuncionPredefinida)
        try:
            self.state = 127
            token = self._input.LA(1)
            if token in [LienzoParser.LEER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.lectura()

            elif token in [LienzoParser.ESCRIBIR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.escritura()

            elif token in [LienzoParser.IMPRIMIR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
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
        self.enterRule(localctx, 20, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(LienzoParser.LEER)
            self.state = 130
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
        self.enterRule(localctx, 22, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(LienzoParser.ESCRIBIR)
            self.state = 134
            localctx._ss_expresion = self.ss_expresion()
            self.state = 135
            self.match(LienzoParser.EN)
            self.state = 136
            self.expresion()
            self.state = 137
            self.match(LienzoParser.T__3)
            self.state = 138
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
        self.enterRule(localctx, 24, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 142
            self.match(LienzoParser.EQUALS)
            self.state = 143
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
        self.enterRule(localctx, 26, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
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
        self.enterRule(localctx, 28, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(LienzoParser.IMPRIMIR)
            self.state = 149
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
        self.enterRule(localctx, 30, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(LienzoParser.SI)
            self.state = 152
            self.match(LienzoParser.T__4)
            self.state = 153
            localctx._ss_expresion = self.ss_expresion()
            self.state = 154
            self.match(LienzoParser.T__5)

            if localctx._ss_expresion.type != BOLEANO:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "el estatuto 'si' necesita una boleano")

            self.state = 156
            self.match(LienzoParser.T__0)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MIENTRAS) | (1 << LienzoParser.SI) | (1 << LienzoParser.LEER) | (1 << LienzoParser.ESCRIBIR) | (1 << LienzoParser.IMPRIMIR) | (1 << LienzoParser.ID))) != 0):
                self.state = 157
                self.instruccion_aux()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 163
            self.match(LienzoParser.T__2)
            self.state = 173
            _la = self._input.LA(1)
            if _la==LienzoParser.SINO:
                self.state = 164
                self.match(LienzoParser.SINO)
                self.state = 165
                self.match(LienzoParser.T__0)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MIENTRAS) | (1 << LienzoParser.SI) | (1 << LienzoParser.LEER) | (1 << LienzoParser.ESCRIBIR) | (1 << LienzoParser.IMPRIMIR) | (1 << LienzoParser.ID))) != 0):
                    self.state = 166
                    self.instruccion_aux()
                    self.state = 171
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 172
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
        self.enterRule(localctx, 32, self.RULE_mientrasQue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(LienzoParser.MIENTRAS)
            self.state = 176
            self.match(LienzoParser.QUE)
            self.state = 177
            self.match(LienzoParser.T__4)
            self.state = 178
            localctx._ss_expresion = self.ss_expresion()
            self.state = 179
            self.match(LienzoParser.T__5)

            if localctx._ss_expresion.type != BOLEANO:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "el estatuto 'mientras que' necesita una boleano")

            self.state = 181
            self.match(LienzoParser.T__0)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MIENTRAS) | (1 << LienzoParser.SI) | (1 << LienzoParser.LEER) | (1 << LienzoParser.ESCRIBIR) | (1 << LienzoParser.IMPRIMIR) | (1 << LienzoParser.ID))) != 0):
                self.state = 182
                self.instruccion_aux()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
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
        self.enterRule(localctx, 34, self.RULE_llamadaFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            localctx._ID = self.match(LienzoParser.ID)

            functionType = namespaceTable.getFunctionType((None if localctx._ID is None else localctx._ID.text))
            if not functionType:
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": llamada a funcion", (None if localctx._ID is None else localctx._ID.text), "inexistente")
            else:
                localctx.type = None if functionType == "nada" else functionType

            self.state = 192
            self.match(LienzoParser.T__4)
            self.state = 204
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__4) | (1 << LienzoParser.T__15) | (1 << LienzoParser.T__19) | (1 << LienzoParser.BOOLEAN_CONSTANT) | (1 << LienzoParser.NUMERIC_CONSTANT) | (1 << LienzoParser.STRING_CONSTANT) | (1 << LienzoParser.ID))) != 0):
                self.state = 193
                localctx.ss_exp1 = self.ss_expresion()

                global currentArgumentList
                currentArgumentList.append(((None if localctx.ss_exp1 is None else self._input.getText((localctx.ss_exp1.start,localctx.ss_exp1.stop))), localctx.ss_exp1.type))

                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__3:
                    self.state = 195
                    self.match(LienzoParser.T__3)
                    self.state = 196
                    localctx.ss_exp2 = self.ss_expresion()

                    currentArgumentList.append(((None if localctx.ss_exp2 is None else self._input.getText((localctx.ss_exp2.start,localctx.ss_exp2.stop))), localctx.ss_exp2.type))

                    self.state = 203
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 206
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
        self.enterRule(localctx, 36, self.RULE_ss_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            localctx.s_exp1 = self.s_expresion()

            localctx.type = localctx.s_exp1.type
            localctx.valor = localctx.s_exp1.valor

            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.T__6 or _la==LienzoParser.T__7:
                self.state = 211
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__6 or _la==LienzoParser.T__7):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 212
                localctx.s_exp2 = self.s_expresion()

                localctx.type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.s_exp2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.s_exp2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.s_exp2.valor)

                self.state = 219
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
        self.enterRule(localctx, 38, self.RULE_s_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            localctx.exp1 = self.expresion()

            localctx.type = localctx.exp1.type
            localctx.valor = localctx.exp1.valor

            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__8) | (1 << LienzoParser.T__9) | (1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12) | (1 << LienzoParser.T__13))) != 0):
                self.state = 222
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__8) | (1 << LienzoParser.T__9) | (1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12) | (1 << LienzoParser.T__13))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 223
                localctx.exp2 = self.expresion()

                localctx.type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.exp2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.exp2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.exp2.valor)

                self.state = 231
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
        self.enterRule(localctx, 40, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            localctx.term1 = self.termino()

            localctx.type = localctx.term1.type
            localctx.valor = localctx.term1.valor

            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.T__14 or _la==LienzoParser.T__15:
                self.state = 234
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__14 or _la==LienzoParser.T__15):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 235
                localctx.term2 = self.termino()

                type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.term2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.term2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.term2.valor)

                self.state = 243
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
        self.enterRule(localctx, 42, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            localctx.factor1 = self.factor()

            localctx.type = localctx.factor1.type
            localctx.valor = localctx.factor1.valor

            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__16) | (1 << LienzoParser.T__17) | (1 << LienzoParser.T__18))) != 0):
                self.state = 246
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__16) | (1 << LienzoParser.T__17) | (1 << LienzoParser.T__18))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 247
                localctx.factor2 = self.factor()

                type = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.factor2.type]
                if not type:
                    print("Error: linea", (0 if localctx.op is None else localctx.op.line), ": operador", (None if localctx.op is None else localctx.op.text), "no puede ser aplicado a", localctx.type, "y a", localctx.factor2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.op is None else localctx.op.text),localctx.valor,localctx.factor2.valor)

                self.state = 254
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
        self.enterRule(localctx, 44, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 270
            token = self._input.LA(1)
            if token in [LienzoParser.T__4, LienzoParser.T__19, LienzoParser.BOOLEAN_CONSTANT, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                _la = self._input.LA(1)
                if _la==LienzoParser.T__19:
                    self.state = 255
                    localctx.neg = self.match(LienzoParser.T__19)


                self.state = 258
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
                self.state = 263
                _la = self._input.LA(1)
                if _la==LienzoParser.T__15:
                    self.state = 262
                    localctx.neg = self.match(LienzoParser.T__15)


                self.state = 265
                localctx._NUMERIC_CONSTANT = self.match(LienzoParser.NUMERIC_CONSTANT)

                localctx.type = NUMERO

                if (None if localctx.neg is None else localctx.neg.text):
                    localctx.valor = cuadruplos.addCuadruplo((None if localctx.neg is None else localctx.neg.text),num((None if localctx._NUMERIC_CONSTANT is None else localctx._NUMERIC_CONSTANT.text)),None)
                else:
                    localctx.valor = num((None if localctx._NUMERIC_CONSTANT is None else localctx._NUMERIC_CONSTANT.text))


            elif token in [LienzoParser.STRING_CONSTANT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
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
        self.enterRule(localctx, 46, self.RULE_factor_aux)
        try:
            self.state = 284
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
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
                self.state = 274
                localctx._BOOLEAN_CONSTANT = self.match(LienzoParser.BOOLEAN_CONSTANT)

                localctx.type = BOLEANO
                localctx.valor = True if (None if localctx._BOOLEAN_CONSTANT is None else localctx._BOOLEAN_CONSTANT.text) == 'verdadero' else False

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
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
                self.state = 279
                self.match(LienzoParser.T__4)
                self.state = 280
                localctx._ss_expresion = self.ss_expresion()
                self.state = 281
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
        self.enterRule(localctx, 48, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            localctx._tipoFunc = self.tipoFunc()
            self.state = 287
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 288
            self.match(LienzoParser.T__4)
            self.state = 297
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 289
                self.parametro()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__3:
                    self.state = 290
                    self.match(LienzoParser.T__3)
                    self.state = 291
                    self.parametro()
                    self.state = 296
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 299
            self.match(LienzoParser.T__5)

            global currentFunctionName
            global currentParameterList
            currentFunctionName = (None if localctx._ID is None else localctx._ID.text)
            if not namespaceTable.addFunction(currentFunctionName, (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))), currentParameterList):
                error((0 if localctx._ID is None else localctx._ID.line), "Funcion " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarada")
            else:
                memoryregisters.newFunction(currentFunctionName)
            currentParameterList = []

            self.state = 301
            self.match(LienzoParser.T__0)
            self.state = 302
            self.cuerpo()
            self.state = 303
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
        self.enterRule(localctx, 50, self.RULE_tipoFunc)
        try:
            self.state = 307
            token = self._input.LA(1)
            if token in [LienzoParser.TEXTO, LienzoParser.BOLEANO, LienzoParser.NUMERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.tipo()

            elif token in [LienzoParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
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
        self.enterRule(localctx, 52, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            localctx._tipo = self.tipo()
            self.state = 311
            _la = self._input.LA(1)
            if _la==LienzoParser.MODIFICABLE:
                self.state = 310
                localctx._MODIFICABLE = self.match(LienzoParser.MODIFICABLE)


            self.state = 313
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





