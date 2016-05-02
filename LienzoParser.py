# Generated from Lienzo.g4 by ANTLR 4.5.2
# encoding: utf-8
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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3G")
        buf.write("\u0197\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\7")
        buf.write("\2L\n\2\f\2\16\2O\13\2\3\2\3\2\3\2\5\2T\n\2\3\2\3\2\7")
        buf.write("\2X\n\2\f\2\16\2[\13\2\3\2\3\2\7\2_\n\2\f\2\16\2b\13\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6}\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u0096\n\t")
        buf.write("\f\t\16\t\u0099\13\t\5\t\u009b\n\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\5\n\u00a5\n\n\3\13\3\13\5\13\u00a9\n\13\3")
        buf.write("\13\3\13\3\13\3\f\7\f\u00af\n\f\f\f\16\f\u00b2\13\f\3")
        buf.write("\f\7\f\u00b5\n\f\f\f\16\f\u00b8\13\f\3\r\3\r\3\r\7\r\u00bd")
        buf.write("\n\r\f\r\16\r\u00c0\13\r\3\r\5\r\u00c3\n\r\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00c9\n\16\3\16\3\16\3\16\3\16\5\16\u00cf")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\5\20\u00df\n\20\3\21\3\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u0115\n\33\3\33\3\33\3")
        buf.write("\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u0124\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\7\37\u013a\n\37\f\37\16\37\u013d\13\37\5\37")
        buf.write("\u013f\n\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \7 \u014a")
        buf.write("\n \f \16 \u014d\13 \3!\3!\3!\3!\3!\3!\3!\7!\u0156\n!")
        buf.write("\f!\16!\u0159\13!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0162")
        buf.write("\n\"\f\"\16\"\u0165\13\"\3#\3#\3#\3#\3#\3#\7#\u016d\n")
        buf.write("#\f#\16#\u0170\13#\3$\5$\u0173\n$\3$\3$\3$\3$\3$\5$\u017a")
        buf.write("\n$\3$\3$\3$\3$\3$\5$\u0181\n$\3%\3%\3%\3%\3%\5%\u0188")
        buf.write("\n%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0195\n%\3%\2")
        buf.write("\2&\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFH\2\t\3\2\32#\4\2;;=>\3\2\13\f\3\2\r")
        buf.write("\22\3\2\23\24\3\2\25\27\3\2DE\u019d\2M\3\2\2\2\4f\3\2")
        buf.write("\2\2\6n\3\2\2\2\bp\3\2\2\2\n|\3\2\2\2\f~\3\2\2\2\16\u0086")
        buf.write("\3\2\2\2\20\u008e\3\2\2\2\22\u00a4\3\2\2\2\24\u00a6\3")
        buf.write("\2\2\2\26\u00b0\3\2\2\2\30\u00c2\3\2\2\2\32\u00ce\3\2")
        buf.write("\2\2\34\u00d0\3\2\2\2\36\u00de\3\2\2\2 \u00e0\3\2\2\2")
        buf.write("\"\u00e4\3\2\2\2$\u00e8\3\2\2\2&\u00ec\3\2\2\2(\u00f1")
        buf.write("\3\2\2\2*\u00f6\3\2\2\2,\u00fb\3\2\2\2.\u0100\3\2\2\2")
        buf.write("\60\u0104\3\2\2\2\62\u0108\3\2\2\2\64\u010f\3\2\2\2\66")
        buf.write("\u011a\3\2\2\28\u011c\3\2\2\2:\u0127\3\2\2\2<\u012f\3")
        buf.write("\2\2\2>\u0143\3\2\2\2@\u014e\3\2\2\2B\u015a\3\2\2\2D\u0166")
        buf.write("\3\2\2\2F\u0180\3\2\2\2H\u0194\3\2\2\2JL\5\n\6\2KJ\3\2")
        buf.write("\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2NS\3\2\2\2OM\3\2\2\2")
        buf.write("PQ\5\b\5\2QR\5\4\3\2RT\3\2\2\2SP\3\2\2\2ST\3\2\2\2TU\3")
        buf.write("\2\2\2UY\b\2\1\2VX\5\20\t\2WV\3\2\2\2X[\3\2\2\2YW\3\2")
        buf.write("\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\`\b\2\1\2]_\5\32")
        buf.write("\16\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2ac\3\2\2")
        buf.write("\2b`\3\2\2\2cd\7\2\2\3de\b\2\1\2e\3\3\2\2\2fg\7$\2\2g")
        buf.write("h\7)\2\2hi\7%\2\2ij\7&\2\2jk\5\6\4\2kl\7\3\2\2lm\b\3\1")
        buf.write("\2m\5\3\2\2\2no\t\2\2\2o\7\3\2\2\2pq\7\'\2\2qr\7)\2\2")
        buf.write("rs\7%\2\2st\7&\2\2tu\5> \2uv\7(\2\2vw\5> \2wx\7\3\2\2")
        buf.write("xy\b\5\1\2y\t\3\2\2\2z}\5\f\7\2{}\5\16\b\2|z\3\2\2\2|")
        buf.write("{\3\2\2\2}\13\3\2\2\2~\177\5\66\34\2\177\u0080\7G\2\2")
        buf.write("\u0080\u0081\b\7\1\2\u0081\u0082\7&\2\2\u0082\u0083\5")
        buf.write("> \2\u0083\u0084\7\3\2\2\u0084\u0085\b\7\1\2\u0085\r\3")
        buf.write("\2\2\2\u0086\u0087\5\66\34\2\u0087\u0088\7\4\2\2\u0088")
        buf.write("\u0089\7D\2\2\u0089\u008a\7\5\2\2\u008a\u008b\7G\2\2\u008b")
        buf.write("\u008c\7\3\2\2\u008c\u008d\b\b\1\2\u008d\17\3\2\2\2\u008e")
        buf.write("\u008f\5\22\n\2\u008f\u0090\7G\2\2\u0090\u0091\b\t\1\2")
        buf.write("\u0091\u009a\7\6\2\2\u0092\u0097\5\24\13\2\u0093\u0094")
        buf.write("\7\7\2\2\u0094\u0096\5\24\13\2\u0095\u0093\3\2\2\2\u0096")
        buf.write("\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u0092\3")
        buf.write("\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d")
        buf.write("\7\b\2\2\u009d\u009e\7\t\2\2\u009e\u009f\5\26\f\2\u009f")
        buf.write("\u00a0\7\n\2\2\u00a0\u00a1\b\t\1\2\u00a1\21\3\2\2\2\u00a2")
        buf.write("\u00a5\5\66\34\2\u00a3\u00a5\7A\2\2\u00a4\u00a2\3\2\2")
        buf.write("\2\u00a4\u00a3\3\2\2\2\u00a5\23\3\2\2\2\u00a6\u00a8\5")
        buf.write("\66\34\2\u00a7\u00a9\7C\2\2\u00a8\u00a7\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\7G\2\2")
        buf.write("\u00ab\u00ac\b\13\1\2\u00ac\25\3\2\2\2\u00ad\u00af\5\n")
        buf.write("\6\2\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae")
        buf.write("\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b6\3\2\2\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b3\u00b5\5\32\16\2\u00b4\u00b3\3\2\2")
        buf.write("\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7")
        buf.write("\3\2\2\2\u00b7\27\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00c3")
        buf.write("\5\32\16\2\u00ba\u00be\7\t\2\2\u00bb\u00bd\5\32\16\2\u00bc")
        buf.write("\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00be\3")
        buf.write("\2\2\2\u00c1\u00c3\7\n\2\2\u00c2\u00b9\3\2\2\2\u00c2\u00ba")
        buf.write("\3\2\2\2\u00c3\31\3\2\2\2\u00c4\u00c9\5\64\33\2\u00c5")
        buf.write("\u00c9\5\36\20\2\u00c6\u00c9\5<\37\2\u00c7\u00c9\5\34")
        buf.write("\17\2\u00c8\u00c4\3\2\2\2\u00c8\u00c5\3\2\2\2\u00c8\u00c6")
        buf.write("\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\u00cb\7\3\2\2\u00cb\u00cf\3\2\2\2\u00cc\u00cf\58\35\2")
        buf.write("\u00cd\u00cf\5:\36\2\u00ce\u00c8\3\2\2\2\u00ce\u00cc\3")
        buf.write("\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\33\3\2\2\2\u00d0\u00d1")
        buf.write("\7\67\2\2\u00d1\u00d2\5> \2\u00d2\u00d3\b\17\1\2\u00d3")
        buf.write("\35\3\2\2\2\u00d4\u00df\5 \21\2\u00d5\u00df\5\"\22\2\u00d6")
        buf.write("\u00df\5$\23\2\u00d7\u00df\5&\24\2\u00d8\u00df\5(\25\2")
        buf.write("\u00d9\u00df\5,\27\2\u00da\u00df\5*\26\2\u00db\u00df\5")
        buf.write("\62\32\2\u00dc\u00df\5.\30\2\u00dd\u00df\5\60\31\2\u00de")
        buf.write("\u00d4\3\2\2\2\u00de\u00d5\3\2\2\2\u00de\u00d6\3\2\2\2")
        buf.write("\u00de\u00d7\3\2\2\2\u00de\u00d8\3\2\2\2\u00de\u00d9\3")
        buf.write("\2\2\2\u00de\u00da\3\2\2\2\u00de\u00db\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\37\3\2\2\2\u00e0\u00e1")
        buf.write("\7<\2\2\u00e1\u00e2\7G\2\2\u00e2\u00e3\b\21\1\2\u00e3")
        buf.write("!\3\2\2\2\u00e4\u00e5\7?\2\2\u00e5\u00e6\5> \2\u00e6\u00e7")
        buf.write("\b\22\1\2\u00e7#\3\2\2\2\u00e8\u00e9\7@\2\2\u00e9\u00ea")
        buf.write("\5> \2\u00ea\u00eb\b\23\1\2\u00eb%\3\2\2\2\u00ec\u00ed")
        buf.write("\7+\2\2\u00ed\u00ee\7,\2\2\u00ee\u00ef\5> \2\u00ef\u00f0")
        buf.write("\b\24\1\2\u00f0\'\3\2\2\2\u00f1\u00f2\7+\2\2\u00f2\u00f3")
        buf.write("\7-\2\2\u00f3\u00f4\5> \2\u00f4\u00f5\b\25\1\2\u00f5)")
        buf.write("\3\2\2\2\u00f6\u00f7\7.\2\2\u00f7\u00f8\7/\2\2\u00f8\u00f9")
        buf.write("\5> \2\u00f9\u00fa\b\26\1\2\u00fa+\3\2\2\2\u00fb\u00fc")
        buf.write("\7.\2\2\u00fc\u00fd\7\60\2\2\u00fd\u00fe\5> \2\u00fe\u00ff")
        buf.write("\b\27\1\2\u00ff-\3\2\2\2\u0100\u0101\7\61\2\2\u0101\u0102")
        buf.write("\7\63\2\2\u0102\u0103\b\30\1\2\u0103/\3\2\2\2\u0104\u0105")
        buf.write("\7\62\2\2\u0105\u0106\7\63\2\2\u0106\u0107\b\31\1\2\u0107")
        buf.write("\61\3\2\2\2\u0108\u0109\7$\2\2\u0109\u010a\7)\2\2\u010a")
        buf.write("\u010b\7\63\2\2\u010b\u010c\7&\2\2\u010c\u010d\5\6\4\2")
        buf.write("\u010d\u010e\b\32\1\2\u010e\63\3\2\2\2\u010f\u0114\7G")
        buf.write("\2\2\u0110\u0111\7\4\2\2\u0111\u0112\5> \2\u0112\u0113")
        buf.write("\7\5\2\2\u0113\u0115\3\2\2\2\u0114\u0110\3\2\2\2\u0114")
        buf.write("\u0115\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\7&\2\2")
        buf.write("\u0117\u0118\5> \2\u0118\u0119\b\33\1\2\u0119\65\3\2\2")
        buf.write("\2\u011a\u011b\t\3\2\2\u011b\67\3\2\2\2\u011c\u011d\7")
        buf.write("9\2\2\u011d\u011e\5> \2\u011e\u011f\b\35\1\2\u011f\u0123")
        buf.write("\5\30\r\2\u0120\u0121\7:\2\2\u0121\u0122\b\35\1\2\u0122")
        buf.write("\u0124\5\30\r\2\u0123\u0120\3\2\2\2\u0123\u0124\3\2\2")
        buf.write("\2\u0124\u0125\3\2\2\2\u0125\u0126\b\35\1\2\u01269\3\2")
        buf.write("\2\2\u0127\u0128\7\66\2\2\u0128\u0129\78\2\2\u0129\u012a")
        buf.write("\b\36\1\2\u012a\u012b\5> \2\u012b\u012c\b\36\1\2\u012c")
        buf.write("\u012d\5\30\r\2\u012d\u012e\b\36\1\2\u012e;\3\2\2\2\u012f")
        buf.write("\u0130\7G\2\2\u0130\u0131\b\37\1\2\u0131\u0132\7\6\2\2")
        buf.write("\u0132\u013e\b\37\1\2\u0133\u0134\5> \2\u0134\u013b\b")
        buf.write("\37\1\2\u0135\u0136\7\7\2\2\u0136\u0137\5> \2\u0137\u0138")
        buf.write("\b\37\1\2\u0138\u013a\3\2\2\2\u0139\u0135\3\2\2\2\u013a")
        buf.write("\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u0133\3")
        buf.write("\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141")
        buf.write("\7\b\2\2\u0141\u0142\b\37\1\2\u0142=\3\2\2\2\u0143\u0144")
        buf.write("\5@!\2\u0144\u014b\b \1\2\u0145\u0146\t\4\2\2\u0146\u0147")
        buf.write("\5@!\2\u0147\u0148\b \1\2\u0148\u014a\3\2\2\2\u0149\u0145")
        buf.write("\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c?\3\2\2\2\u014d\u014b\3\2\2\2\u014e")
        buf.write("\u014f\5B\"\2\u014f\u0157\b!\1\2\u0150\u0151\t\5\2\2\u0151")
        buf.write("\u0152\5B\"\2\u0152\u0153\3\2\2\2\u0153\u0154\b!\1\2\u0154")
        buf.write("\u0156\3\2\2\2\u0155\u0150\3\2\2\2\u0156\u0159\3\2\2\2")
        buf.write("\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158A\3\2\2")
        buf.write("\2\u0159\u0157\3\2\2\2\u015a\u015b\5D#\2\u015b\u0163\b")
        buf.write("\"\1\2\u015c\u015d\t\6\2\2\u015d\u015e\5D#\2\u015e\u015f")
        buf.write("\3\2\2\2\u015f\u0160\b\"\1\2\u0160\u0162\3\2\2\2\u0161")
        buf.write("\u015c\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0163\u0164\3\2\2\2\u0164C\3\2\2\2\u0165\u0163\3\2\2")
        buf.write("\2\u0166\u0167\5F$\2\u0167\u016e\b#\1\2\u0168\u0169\t")
        buf.write("\7\2\2\u0169\u016a\5F$\2\u016a\u016b\b#\1\2\u016b\u016d")
        buf.write("\3\2\2\2\u016c\u0168\3\2\2\2\u016d\u0170\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016fE\3\2\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0171\u0173\7\30\2\2\u0172\u0171\3\2\2")
        buf.write("\2\u0172\u0173\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175")
        buf.write("\5H%\2\u0175\u0176\3\2\2\2\u0176\u0177\b$\1\2\u0177\u0181")
        buf.write("\3\2\2\2\u0178\u017a\7\24\2\2\u0179\u0178\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\t\b\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u0181\b$\1\2\u017e\u017f\7")
        buf.write("F\2\2\u017f\u0181\b$\1\2\u0180\u0172\3\2\2\2\u0180\u0179")
        buf.write("\3\2\2\2\u0180\u017e\3\2\2\2\u0181G\3\2\2\2\u0182\u0187")
        buf.write("\7G\2\2\u0183\u0184\7\4\2\2\u0184\u0185\5> \2\u0185\u0186")
        buf.write("\7\5\2\2\u0186\u0188\3\2\2\2\u0187\u0183\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0195\b%\1\2")
        buf.write("\u018a\u018b\7B\2\2\u018b\u0195\b%\1\2\u018c\u018d\5<")
        buf.write("\37\2\u018d\u018e\b%\1\2\u018e\u0195\3\2\2\2\u018f\u0190")
        buf.write("\7\6\2\2\u0190\u0191\5> \2\u0191\u0192\7\b\2\2\u0192\u0193")
        buf.write("\b%\1\2\u0193\u0195\3\2\2\2\u0194\u0182\3\2\2\2\u0194")
        buf.write("\u018a\3\2\2\2\u0194\u018c\3\2\2\2\u0194\u018f\3\2\2\2")
        buf.write("\u0195I\3\2\2\2\37MSY`|\u0097\u009a\u00a4\u00a8\u00b0")
        buf.write("\u00b6\u00be\u00c2\u00c8\u00ce\u00de\u0114\u0123\u013b")
        buf.write("\u013e\u014b\u0157\u0163\u016e\u0172\u0179\u0180\u0187")
        buf.write("\u0194")
        return buf.getvalue()


class LienzoParser ( Parser ):

    grammarFileName = "Lienzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'['", "']'", "'('", "','", "')'", 
                     "'{'", "'}'", "'&'", "'|'", "'=='", "'!='", "'>'", 
                     "'<'", "'>='", "'<='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "<INVALID>", "'rojo'", "'verde'", "'amarillo'", 
                     "'azul'", "'blanco'", "'negro'", "'morado'", "'naranja'", 
                     "'cafe'", "'gris'", "'color'", "'lienzo'", "'='", "'tamano'", 
                     "'por'", "'de'", "'en'", "'mover'", "'adelante'", "'atras'", 
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
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ROJO", 
                      "VERDE", "AMARILLO", "AZUL", "BLANCO", "NEGRO", "MORADO", 
                      "NARANJA", "CAFE", "GRIS", "COLOR", "LIENZO", "EQUALS", 
                      "TAMANO", "POR", "DE", "EN", "MOVER", "ADELANTE", 
                      "ATRAS", "GIRAR", "DERECHA", "IZQUIERDA", "LEVANTAR", 
                      "BAJAR", "PLUMA", "DIBUJO", "DORMIR", "MIENTRAS", 
                      "REGRESAR", "QUE", "SI", "SINO", "TEXTO", "LEER", 
                      "BOLEANO", "NUMERO", "ESCRIBIR", "IMPRIMIR", "NADA", 
                      "BOOLEAN_CONSTANT", "MODIFICABLE", "INTEGRAL_CONSTANT", 
                      "NUMERIC_CONSTANT", "STRING_CONSTANT", "ID" ]

    RULE_program = 0
    RULE_colorLienzo = 1
    RULE_color = 2
    RULE_tamanoLienzo = 3
    RULE_declaracion = 4
    RULE_declaracion_variable = 5
    RULE_declaracion_arreglo = 6
    RULE_funcion = 7
    RULE_tipoFunc = 8
    RULE_parametro = 9
    RULE_cuerpo = 10
    RULE_bloque_instrucciones = 11
    RULE_instruccion_aux = 12
    RULE_regresar = 13
    RULE_llamadaFuncionPredefinida = 14
    RULE_lectura = 15
    RULE_escritura = 16
    RULE_imprimir = 17
    RULE_mover_adelante = 18
    RULE_mover_atras = 19
    RULE_girar_derecha = 20
    RULE_girar_izquierda = 21
    RULE_subir_pluma = 22
    RULE_bajar_pluma = 23
    RULE_cambio_color = 24
    RULE_asignacion = 25
    RULE_tipo = 26
    RULE_condicional = 27
    RULE_mientrasQue = 28
    RULE_llamadaFuncion = 29
    RULE_ss_expresion = 30
    RULE_s_expresion = 31
    RULE_expresion = 32
    RULE_termino = 33
    RULE_factor = 34
    RULE_factor_aux = 35

    ruleNames =  [ "program", "colorLienzo", "color", "tamanoLienzo", "declaracion", 
                   "declaracion_variable", "declaracion_arreglo", "funcion", 
                   "tipoFunc", "parametro", "cuerpo", "bloque_instrucciones", 
                   "instruccion_aux", "regresar", "llamadaFuncionPredefinida", 
                   "lectura", "escritura", "imprimir", "mover_adelante", 
                   "mover_atras", "girar_derecha", "girar_izquierda", "subir_pluma", 
                   "bajar_pluma", "cambio_color", "asignacion", "tipo", 
                   "condicional", "mientrasQue", "llamadaFuncion", "ss_expresion", 
                   "s_expresion", "expresion", "termino", "factor", "factor_aux" ]

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
    ROJO=24
    VERDE=25
    AMARILLO=26
    AZUL=27
    BLANCO=28
    NEGRO=29
    MORADO=30
    NARANJA=31
    CAFE=32
    GRIS=33
    COLOR=34
    LIENZO=35
    EQUALS=36
    TAMANO=37
    POR=38
    DE=39
    EN=40
    MOVER=41
    ADELANTE=42
    ATRAS=43
    GIRAR=44
    DERECHA=45
    IZQUIERDA=46
    LEVANTAR=47
    BAJAR=48
    PLUMA=49
    DIBUJO=50
    DORMIR=51
    MIENTRAS=52
    REGRESAR=53
    QUE=54
    SI=55
    SINO=56
    TEXTO=57
    LEER=58
    BOLEANO=59
    NUMERO=60
    ESCRIBIR=61
    IMPRIMIR=62
    NADA=63
    BOOLEAN_CONSTANT=64
    MODIFICABLE=65
    INTEGRAL_CONSTANT=66
    NUMERIC_CONSTANT=67
    STRING_CONSTANT=68
    ID=69

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
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 72
                    self.declaracion() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 81
            _la = self._input.LA(1)
            if _la==LienzoParser.TAMANO:
                self.state = 78
                self.tamanoLienzo()
                self.state = 79
                self.colorLienzo()



            cuadruplos.addCuadruplo("", GOTO, None, None, None, False)
            cuadruplos.pushPilaSaltos(cuadruplos.last())

            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO) | (1 << LienzoParser.NADA))) != 0):
                self.state = 84
                self.funcion()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(), cuadruplos.current())

            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & ((1 << (LienzoParser.COLOR - 34)) | (1 << (LienzoParser.MOVER - 34)) | (1 << (LienzoParser.GIRAR - 34)) | (1 << (LienzoParser.LEVANTAR - 34)) | (1 << (LienzoParser.BAJAR - 34)) | (1 << (LienzoParser.MIENTRAS - 34)) | (1 << (LienzoParser.REGRESAR - 34)) | (1 << (LienzoParser.SI - 34)) | (1 << (LienzoParser.LEER - 34)) | (1 << (LienzoParser.ESCRIBIR - 34)) | (1 << (LienzoParser.IMPRIMIR - 34)) | (1 << (LienzoParser.ID - 34)))) != 0):
                self.state = 91
                self.instruccion_aux()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(LienzoParser.EOF)

            cuadruplos.addCuadruplo("", END, None, None, None, False)
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
            self.state = 100
            self.match(LienzoParser.COLOR)
            self.state = 101
            self.match(LienzoParser.DE)
            self.state = 102
            self.match(LienzoParser.LIENZO)
            self.state = 103
            self.match(LienzoParser.EQUALS)
            self.state = 104
            localctx._color = self.color()
            self.state = 105
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
            self.state = 108
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
            self.state = 110
            self.match(LienzoParser.TAMANO)
            self.state = 111
            self.match(LienzoParser.DE)
            self.state = 112
            self.match(LienzoParser.LIENZO)
            self.state = 113
            self.match(LienzoParser.EQUALS)
            self.state = 114
            localctx.largo = self.ss_expresion()
            self.state = 115
            self.match(LienzoParser.POR)
            self.state = 116
            localctx.ancho = self.ss_expresion()
            self.state = 117
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

        def declaracion_variable(self):
            return self.getTypedRuleContext(LienzoParser.Declaracion_variableContext,0)


        def declaracion_arreglo(self):
            return self.getTypedRuleContext(LienzoParser.Declaracion_arregloContext,0)


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
            self.state = 122
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.declaracion_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.declaracion_arreglo()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaracion_variableContext(ParserRuleContext):

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
            return LienzoParser.RULE_declaracion_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_variable" ):
                listener.enterDeclaracion_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_variable" ):
                listener.exitDeclaracion_variable(self)




    def declaracion_variable(self):

        localctx = LienzoParser.Declaracion_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracion_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            localctx._tipo = self.tipo()
            self.state = 125
            localctx._ID = self.match(LienzoParser.ID)

            if namespaceTable.idAlreadyTaken((None if localctx._ID is None else localctx._ID.text), currentFunctionName):
                error((0 if localctx._ID is None else localctx._ID.line), ": Identificador " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarado")

            self.state = 127
            self.match(LienzoParser.EQUALS)
            self.state = 128
            localctx._ss_expresion = self.ss_expresion()
            self.state = 129
            self.match(LienzoParser.T__0)

            if localctx._ss_expresion.type != (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))):
                error((0 if localctx._ID is None else localctx._ID.line), "Variable " + (None if localctx._ID is None else localctx._ID.text) + " es de tipo " + (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))))
            else:
                namespaceTable.addVariable((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))), currentFunctionName)
                idcontent = memoryregisters.createMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName, (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))))
                cuadruplos.addCuadruplo(currentFunctionName, ASSIGN, localctx._ss_expresion.valor, None, idcontent, False)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaracion_arregloContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext
            self._INTEGRAL_CONSTANT = None # Token
            self._ID = None # Token

        def tipo(self):
            return self.getTypedRuleContext(LienzoParser.TipoContext,0)


        def INTEGRAL_CONSTANT(self):
            return self.getToken(LienzoParser.INTEGRAL_CONSTANT, 0)

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def getRuleIndex(self):
            return LienzoParser.RULE_declaracion_arreglo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_arreglo" ):
                listener.enterDeclaracion_arreglo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_arreglo" ):
                listener.exitDeclaracion_arreglo(self)




    def declaracion_arreglo(self):

        localctx = LienzoParser.Declaracion_arregloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaracion_arreglo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            localctx._tipo = self.tipo()
            self.state = 133
            self.match(LienzoParser.T__1)
            self.state = 134
            localctx._INTEGRAL_CONSTANT = self.match(LienzoParser.INTEGRAL_CONSTANT)
            self.state = 135
            self.match(LienzoParser.T__2)
            self.state = 136
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 137
            self.match(LienzoParser.T__0)

            if namespaceTable.idAlreadyTaken((None if localctx._ID is None else localctx._ID.text), currentFunctionName):
                error((0 if localctx._ID is None else localctx._ID.line), ": Identificador " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarado")
            else:
                length = num((None if localctx._INTEGRAL_CONSTANT is None else localctx._INTEGRAL_CONSTANT.text))
                if length == 0:
                    error((0 if localctx._ID is None else localctx._ID.line), ": La longitud del arreglo " + (None if localctx._ID is None else localctx._ID.text) + " debe ser mayor a 0")
                else:
                    namespaceTable.addArray((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))), length, currentFunctionName)
                    idcontents = memoryregisters.createMemoryRegisterForArray((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))), length, currentFunctionName)
                    valorInicial = 0
                    if (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))) == BOLEANO:
                        valorInicial = False
                    elif (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))) == TEXTO:
                        valorInicial = ""
                    for i in idcontents:
                        cuadruplos.addCuadruplo(currentFunctionName, ASSIGN, valorInicial, None, i, False)

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
        self.enterRule(localctx, 14, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            localctx._tipoFunc = self.tipoFunc()
            self.state = 141
            localctx._ID = self.match(LienzoParser.ID)

            global currentFunctionName
            global currentTipoFunc
            currentFunctionName = (None if localctx._ID is None else localctx._ID.text)
            currentTipoFunc = (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop)))
            if not namespaceTable.addFunction(currentFunctionName, (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))), cuadruplos.current()):
                error((0 if localctx._ID is None else localctx._ID.line), "Funcion " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarada")
            else:
                mr = memoryregisters.newFunction(currentFunctionName, (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))))
                valorInicial = 0
                if (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))) == BOLEANO:
                    valorInicial = False
                elif (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop))) == TEXTO:
                    valorInicial = ""
                cuadruplos.addCuadruplo("", ASSIGNFUNC, valorInicial, None, mr, False)

            self.state = 143
            self.match(LienzoParser.T__3)
            self.state = 152
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 144
                self.parametro()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__4:
                    self.state = 145
                    self.match(LienzoParser.T__4)
                    self.state = 146
                    self.parametro()
                    self.state = 151
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 154
            self.match(LienzoParser.T__5)
            self.state = 155
            self.match(LienzoParser.T__6)
            self.state = 156
            self.cuerpo()
            self.state = 157
            self.match(LienzoParser.T__7)

            global hasReturn
            if currentTipoFunc != "nada" and not hasReturn:
                error((0 if localctx._ID is None else localctx._ID.line), "Funcion " + (None if localctx._ID is None else localctx._ID.text) + " debe tener valor de retorno")
            else:
                hasReturn = False
            cuadruplos.addCuadruplo(currentFunctionName, RET, None, None, None, False)
            currentFunctionName = ""
            currentTipoFunc = ""

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
        self.enterRule(localctx, 16, self.RULE_tipoFunc)
        try:
            self.state = 162
            token = self._input.LA(1)
            if token in [LienzoParser.TEXTO, LienzoParser.BOLEANO, LienzoParser.NUMERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.tipo()

            elif token in [LienzoParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
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
        self.enterRule(localctx, 18, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            localctx._tipo = self.tipo()
            self.state = 166
            _la = self._input.LA(1)
            if _la==LienzoParser.MODIFICABLE:
                self.state = 165
                localctx._MODIFICABLE = self.match(LienzoParser.MODIFICABLE)


            self.state = 168
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
        self.enterRule(localctx, 20, self.RULE_cuerpo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 171
                self.declaracion()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & ((1 << (LienzoParser.COLOR - 34)) | (1 << (LienzoParser.MOVER - 34)) | (1 << (LienzoParser.GIRAR - 34)) | (1 << (LienzoParser.LEVANTAR - 34)) | (1 << (LienzoParser.BAJAR - 34)) | (1 << (LienzoParser.MIENTRAS - 34)) | (1 << (LienzoParser.REGRESAR - 34)) | (1 << (LienzoParser.SI - 34)) | (1 << (LienzoParser.LEER - 34)) | (1 << (LienzoParser.ESCRIBIR - 34)) | (1 << (LienzoParser.IMPRIMIR - 34)) | (1 << (LienzoParser.ID - 34)))) != 0):
                self.state = 177
                self.instruccion_aux()
                self.state = 182
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
        self.enterRule(localctx, 22, self.RULE_bloque_instrucciones)
        self._la = 0 # Token type
        try:
            self.state = 192
            token = self._input.LA(1)
            if token in [LienzoParser.COLOR, LienzoParser.MOVER, LienzoParser.GIRAR, LienzoParser.LEVANTAR, LienzoParser.BAJAR, LienzoParser.MIENTRAS, LienzoParser.REGRESAR, LienzoParser.SI, LienzoParser.LEER, LienzoParser.ESCRIBIR, LienzoParser.IMPRIMIR, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.instruccion_aux()

            elif token in [LienzoParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(LienzoParser.T__6)
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & ((1 << (LienzoParser.COLOR - 34)) | (1 << (LienzoParser.MOVER - 34)) | (1 << (LienzoParser.GIRAR - 34)) | (1 << (LienzoParser.LEVANTAR - 34)) | (1 << (LienzoParser.BAJAR - 34)) | (1 << (LienzoParser.MIENTRAS - 34)) | (1 << (LienzoParser.REGRESAR - 34)) | (1 << (LienzoParser.SI - 34)) | (1 << (LienzoParser.LEER - 34)) | (1 << (LienzoParser.ESCRIBIR - 34)) | (1 << (LienzoParser.IMPRIMIR - 34)) | (1 << (LienzoParser.ID - 34)))) != 0):
                    self.state = 185
                    self.instruccion_aux()
                    self.state = 190
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 191
                self.match(LienzoParser.T__7)

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


        def regresar(self):
            return self.getTypedRuleContext(LienzoParser.RegresarContext,0)


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
        self.enterRule(localctx, 24, self.RULE_instruccion_aux)
        try:
            self.state = 204
            token = self._input.LA(1)
            if token in [LienzoParser.COLOR, LienzoParser.MOVER, LienzoParser.GIRAR, LienzoParser.LEVANTAR, LienzoParser.BAJAR, LienzoParser.REGRESAR, LienzoParser.LEER, LienzoParser.ESCRIBIR, LienzoParser.IMPRIMIR, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self._errHandler.sync(self);
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 194
                    self.asignacion()
                    pass

                elif la_ == 2:
                    self.state = 195
                    self.llamadaFuncionPredefinida()
                    pass

                elif la_ == 3:
                    self.state = 196
                    self.llamadaFuncion()
                    pass

                elif la_ == 4:
                    self.state = 197
                    self.regresar()
                    pass


                self.state = 200
                self.match(LienzoParser.T__0)

            elif token in [LienzoParser.SI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.condicional()

            elif token in [LienzoParser.MIENTRAS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
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

    class RegresarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._REGRESAR = None # Token
            self._ss_expresion = None # Ss_expresionContext

        def REGRESAR(self):
            return self.getToken(LienzoParser.REGRESAR, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_regresar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegresar" ):
                listener.enterRegresar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegresar" ):
                listener.exitRegresar(self)




    def regresar(self):

        localctx = LienzoParser.RegresarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_regresar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            localctx._REGRESAR = self.match(LienzoParser.REGRESAR)
            self.state = 207
            localctx._ss_expresion = self.ss_expresion()

            global hasReturn
            hasReturn = True    
            if currentTipoFunc == "nada":
                error((0 if localctx._REGRESAR is None else localctx._REGRESAR.line), "Funcion " + currentFunctionName + " no debe tener valor de retorno")
            elif localctx._ss_expresion.type != currentTipoFunc:
                error((0 if localctx._REGRESAR is None else localctx._REGRESAR.line), "Funcion " + currentFunctionName + " tiene valor de retorno de tipo incorrecto. Se esperaba un " + currentTipoFunc)
            else:
                cuadruplos.addCuadruplo(currentFunctionName, RETURN, localctx._ss_expresion.valor, None, None, False)
                cuadruplos.addCuadruplo(currentFunctionName, RET, None, None, None, False)

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
        self.enterRule(localctx, 28, self.RULE_llamadaFuncionPredefinida)
        try:
            self.state = 220
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.lectura()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.escritura()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self.imprimir()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 213
                self.mover_adelante()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 214
                self.mover_atras()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 215
                self.girar_izquierda()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 216
                self.girar_derecha()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 217
                self.cambio_color()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 218
                self.subir_pluma()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 219
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
        self.enterRule(localctx, 30, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(LienzoParser.LEER)
            self.state = 223
            localctx._ID = self.match(LienzoParser.ID)

            idcontent = memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
            cuadruplos.addCuadruplo(currentFunctionName, READ, None, None, idcontent)

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
        self.enterRule(localctx, 32, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(LienzoParser.ESCRIBIR)
            self.state = 227
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
        self.enterRule(localctx, 34, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(LienzoParser.IMPRIMIR)
            self.state = 231
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
        self.enterRule(localctx, 36, self.RULE_mover_adelante)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(LienzoParser.MOVER)
            self.state = 235
            self.match(LienzoParser.ADELANTE)
            self.state = 236
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
        self.enterRule(localctx, 38, self.RULE_mover_atras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(LienzoParser.MOVER)
            self.state = 240
            self.match(LienzoParser.ATRAS)
            self.state = 241
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
        self.enterRule(localctx, 40, self.RULE_girar_derecha)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(LienzoParser.GIRAR)
            self.state = 245
            self.match(LienzoParser.DERECHA)
            self.state = 246
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
        self.enterRule(localctx, 42, self.RULE_girar_izquierda)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(LienzoParser.GIRAR)
            self.state = 250
            self.match(LienzoParser.IZQUIERDA)
            self.state = 251
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
        self.enterRule(localctx, 44, self.RULE_subir_pluma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(LienzoParser.LEVANTAR)
            self.state = 255
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
        self.enterRule(localctx, 46, self.RULE_bajar_pluma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(LienzoParser.BAJAR)
            self.state = 259
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
        self.enterRule(localctx, 48, self.RULE_cambio_color)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(LienzoParser.COLOR)
            self.state = 263
            self.match(LienzoParser.DE)
            self.state = 264
            self.match(LienzoParser.PLUMA)
            self.state = 265
            self.match(LienzoParser.EQUALS)
            self.state = 266
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
            self.arr = None # Token
            self.indice = None # Ss_expresionContext
            self.lhs = None # Ss_expresionContext

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def ss_expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.Ss_expresionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,i)


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
        self.enterRule(localctx, 50, self.RULE_asignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 274
            _la = self._input.LA(1)
            if _la==LienzoParser.T__1:
                self.state = 270
                localctx.arr = self.match(LienzoParser.T__1)
                self.state = 271
                localctx.indice = self.ss_expresion()
                self.state = 272
                self.match(LienzoParser.T__2)


            self.state = 276
            self.match(LienzoParser.EQUALS)
            self.state = 277
            localctx.lhs = self.ss_expresion()

            # regresa el tipo, no importa si es arreglo o variable
            idType = namespaceTable.getVariableType((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
            if not localctx.arr:
                if not idType:
                    error((0 if localctx._ID is None else localctx._ID.line), "Variable " + (None if localctx._ID is None else localctx._ID.text) + " no ha sido declarada")
                elif localctx.lhs.type != idType:
                    error((0 if localctx._ID is None else localctx._ID.line), "Variable " + (None if localctx._ID is None else localctx._ID.text) + " es de tipo " + idType)
                else:
                    idcontent = memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
                    cuadruplos.addCuadruplo(currentFunctionName, ASSIGN, localctx.lhs.valor, None, idcontent)
            else:
                if not idType:
                    error((0 if localctx._ID is None else localctx._ID.line), "Arreglo " + (None if localctx._ID is None else localctx._ID.text) + " no ha sido declarado")
                elif localctx.lhs.type != idType:
                    error((0 if localctx._ID is None else localctx._ID.line), "Arreglo " + (None if localctx._ID is None else localctx._ID.text) + " es de tipo " + idType)
                else:
                    cuadruplos.addCuadruplo(currentFunctionName, CHECK_BOUNDS, localctx.indice.valor, namespaceTable.getArrayLength((None if localctx._ID is None else localctx._ID.text), currentFunctionName), None, False)
                    idcontent = memoryregisters.getArrayMemoryRegister((None if localctx._ID is None else localctx._ID.text), localctx.indice.valor, currentFunctionName)
                    cuadruplos.addCuadruplo(currentFunctionName, ASSIGN, localctx.lhs.valor, None, idcontent)

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
        self.enterRule(localctx, 52, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
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
        self.enterRule(localctx, 54, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(LienzoParser.SI)
            self.state = 283
            localctx._ss_expresion = self.ss_expresion()

            if localctx._ss_expresion.type != BOLEANO:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "el estatuto 'si' necesita una boleano")
            else:
                cuadruplos.addCuadruplo(currentFunctionName, GOTOF, localctx._ss_expresion.valor, None, None, False)
                cuadruplos.pushPilaSaltos(cuadruplos.last())

            self.state = 285
            self.bloque_instrucciones()
            self.state = 289
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 286
                self.match(LienzoParser.SINO)

                cuadruplos.addCuadruplo(currentFunctionName, GOTO,None,None,None,False)
                cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(),cuadruplos.current())
                cuadruplos.pushPilaSaltos(cuadruplos.last())

                self.state = 288
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
        self.enterRule(localctx, 56, self.RULE_mientrasQue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(LienzoParser.MIENTRAS)
            self.state = 294
            self.match(LienzoParser.QUE)

            cuadruplos.pushPilaSaltos(cuadruplos.current())

            self.state = 296
            localctx._ss_expresion = self.ss_expresion()

            if localctx._ss_expresion.type != BOLEANO:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "el estatuto 'mientras que' necesita una boleano")
            else:
                cuadruplos.addCuadruplo(currentFunctionName, GOTOF,localctx._ss_expresion.valor,None,None,False)
                cuadruplos.pushPilaSaltos(cuadruplos.last())

            self.state = 298
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
            self.valor = None
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
        self.enterRule(localctx, 58, self.RULE_llamadaFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            localctx._ID = self.match(LienzoParser.ID)

            functionType = namespaceTable.getFunctionType((None if localctx._ID is None else localctx._ID.text))
            if not functionType:
                error((0 if localctx._ID is None else localctx._ID.line), ": llamada a funcion " + (None if localctx._ID is None else localctx._ID.text) + " inexistente")
                localctx.valor = None
            else:
                localctx.type = None if functionType == "nada" else functionType
                cuadruplos.addCuadruplo(currentFunctionName, ERA, (None if localctx._ID is None else localctx._ID.text), None, None, False)
                localctx.valor = memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text), "")

            self.state = 303
            self.match(LienzoParser.T__3)

            k = 0

            self.state = 316
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__3) | (1 << LienzoParser.T__17) | (1 << LienzoParser.T__21))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (LienzoParser.BOOLEAN_CONSTANT - 64)) | (1 << (LienzoParser.INTEGRAL_CONSTANT - 64)) | (1 << (LienzoParser.NUMERIC_CONSTANT - 64)) | (1 << (LienzoParser.STRING_CONSTANT - 64)) | (1 << (LienzoParser.ID - 64)))) != 0):
                self.state = 305
                localctx.ss_exp1 = self.ss_expresion()

                if namespaceTable.argumentAgree((None if localctx._ID is None else localctx._ID.text), k, (None if localctx.ss_exp1 is None else self._input.getText((localctx.ss_exp1.start,localctx.ss_exp1.stop))), localctx.ss_exp1.type):
                    cuadruplos.addCuadruplo(currentFunctionName, PARAM, localctx.ss_exp1.valor, namespaceTable.parameterReference((None if localctx._ID is None else localctx._ID.text), k), None, False)
                else:
                    error((None if localctx.ss_exp1 is None else localctx.ss_exp1.start).line, ": argumento #" + k + "no concuerda con el parametro esperado")
                k += 1

                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__4:
                    self.state = 307
                    self.match(LienzoParser.T__4)
                    self.state = 308
                    localctx.ss_exp2 = self.ss_expresion()

                    if namespaceTable.argumentAgree((None if localctx._ID is None else localctx._ID.text), k, (None if localctx.ss_exp2 is None else self._input.getText((localctx.ss_exp2.start,localctx.ss_exp2.stop))), localctx.ss_exp2.type):
                        cuadruplos.addCuadruplo(currentFunctionName, PARAM, localctx.ss_exp2.valor, namespaceTable.parameterReference((None if localctx._ID is None else localctx._ID.text), k), None, False)
                    else:
                        error((None if localctx.ss_exp1 is None else localctx.ss_exp1.start).line, ": argumento #" + k + "no concuerda con el parametro esperado")
                    k += 1

                    self.state = 315
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 318
            localctx.paren = self.match(LienzoParser.T__5)

            amountOfParameters = namespaceTable.getParameterAmount((None if localctx._ID is None else localctx._ID.text))
            if k != amountOfParameters:
                error((0 if localctx.paren is None else localctx.paren.line), "Se esperaban" + amountOfParameters + " parametros, se recibieron " + k)
            else:
                cuadruplos.addCuadruplo(currentFunctionName, GOSUB, namespaceTable.getDireccionInicio((None if localctx._ID is None else localctx._ID.text)), None, None, False)

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
        self.enterRule(localctx, 60, self.RULE_ss_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            localctx.s_exp1 = self.s_expresion()

            localctx.type = localctx.s_exp1.type
            localctx.valor = localctx.s_exp1.valor

            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.T__8 or _la==LienzoParser.T__9:
                self.state = 323
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__8 or _la==LienzoParser.T__9):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 324
                localctx.s_exp2 = self.s_expresion()

                tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.s_exp2.type]
                if not tipo:
                    error(op.line, ": operador " + (None if localctx.op is None else localctx.op.text) + " no puede ser aplicado a " + localctx.type +" y a " + localctx.s_exp2.type)
                else:
                    namespaceTable.addTemporal(currentFunctionName, tipo)
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text),localctx.valor,localctx.s_exp2.valor)
                localctx.type = tipo

                self.state = 331
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
        self.enterRule(localctx, 62, self.RULE_s_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            localctx.exp1 = self.expresion()

            localctx.type = localctx.exp1.type
            localctx.valor = localctx.exp1.valor

            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12) | (1 << LienzoParser.T__13) | (1 << LienzoParser.T__14) | (1 << LienzoParser.T__15))) != 0):
                self.state = 334
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12) | (1 << LienzoParser.T__13) | (1 << LienzoParser.T__14) | (1 << LienzoParser.T__15))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 335
                localctx.exp2 = self.expresion()

                tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.exp2.type]
                if not tipo:
                    error((0 if localctx.op is None else localctx.op.line), ": operador " + (None if localctx.op is None else localctx.op.text) + " no puede ser aplicado a " + localctx.type + " y a " + localctx.exp2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text),localctx.valor,localctx.exp2.valor)
                    namespaceTable.addTemporal(currentFunctionName, tipo)
                localctx.type = tipo

                self.state = 343
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
        self.enterRule(localctx, 64, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            localctx.term1 = self.termino()

            localctx.type = localctx.term1.type
            localctx.valor = localctx.term1.valor

            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.T__16 or _la==LienzoParser.T__17:
                self.state = 346
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__16 or _la==LienzoParser.T__17):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 347
                localctx.term2 = self.termino()

                tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.term2.type]
                if not tipo:
                    error((0 if localctx.op is None else localctx.op.line), ": operador " + (None if localctx.op is None else localctx.op.text) + " no puede ser aplicado a " + localctx.type + " y a " + localctx.term2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text),localctx.valor,localctx.term2.valor)
                    namespaceTable.addTemporal(currentFunctionName, tipo)
                localctx.type = tipo

                self.state = 355
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
        self.enterRule(localctx, 66, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            localctx.factor1 = self.factor()

            localctx.type = localctx.factor1.type
            localctx.valor = localctx.factor1.valor

            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__18) | (1 << LienzoParser.T__19) | (1 << LienzoParser.T__20))) != 0):
                self.state = 358
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__18) | (1 << LienzoParser.T__19) | (1 << LienzoParser.T__20))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 359
                localctx.factor2 = self.factor()

                tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.factor2.type]
                if not tipo:
                    error((0 if localctx.op is None else localctx.op.line), ": operador " + (None if localctx.op is None else localctx.op.text) + " no puede ser aplicado a " + localctx.type + " y a " + localctx.factor2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text),localctx.valor,localctx.factor2.valor)
                    namespaceTable.addTemporal(currentFunctionName, tipo)
                localctx.type = tipo

                self.state = 366
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
            self.n = None # Token
            self._STRING_CONSTANT = None # Token

        def factor_aux(self):
            return self.getTypedRuleContext(LienzoParser.Factor_auxContext,0)


        def NUMERIC_CONSTANT(self):
            return self.getToken(LienzoParser.NUMERIC_CONSTANT, 0)

        def INTEGRAL_CONSTANT(self):
            return self.getToken(LienzoParser.INTEGRAL_CONSTANT, 0)

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
        self.enterRule(localctx, 68, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 382
            token = self._input.LA(1)
            if token in [LienzoParser.T__3, LienzoParser.T__21, LienzoParser.BOOLEAN_CONSTANT, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                _la = self._input.LA(1)
                if _la==LienzoParser.T__21:
                    self.state = 367
                    localctx.neg = self.match(LienzoParser.T__21)


                self.state = 370
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


            elif token in [LienzoParser.T__17, LienzoParser.INTEGRAL_CONSTANT, LienzoParser.NUMERIC_CONSTANT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                _la = self._input.LA(1)
                if _la==LienzoParser.T__17:
                    self.state = 374
                    localctx.neg = self.match(LienzoParser.T__17)


                self.state = 377
                localctx.n = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.INTEGRAL_CONSTANT or _la==LienzoParser.NUMERIC_CONSTANT):
                    localctx.n = self._errHandler.recoverInline(self)
                else:
                    self.consume()

                localctx.type = NUMERO

                if (None if localctx.neg is None else localctx.neg.text):
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.neg is None else localctx.neg.text), num((None if localctx.n is None else localctx.n.text)), None)
                    namespaceTable.addTemporal(currentFunctionName, localctx.type)
                else:
                    localctx.valor = num((None if localctx.n is None else localctx.n.text))


            elif token in [LienzoParser.STRING_CONSTANT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 380
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
            self.arr = None # Token
            self._ss_expresion = None # Ss_expresionContext
            self._BOOLEAN_CONSTANT = None # Token
            self.lf = None # LlamadaFuncionContext
            self._llamadaFuncion = None # LlamadaFuncionContext

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def BOOLEAN_CONSTANT(self):
            return self.getToken(LienzoParser.BOOLEAN_CONSTANT, 0)

        def llamadaFuncion(self):
            return self.getTypedRuleContext(LienzoParser.LlamadaFuncionContext,0)


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
        self.enterRule(localctx, 70, self.RULE_factor_aux)
        self._la = 0 # Token type
        try:
            self.state = 402
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                localctx._ID = self.match(LienzoParser.ID)
                self.state = 389
                _la = self._input.LA(1)
                if _la==LienzoParser.T__1:
                    self.state = 385
                    localctx.arr = self.match(LienzoParser.T__1)
                    self.state = 386
                    localctx._ss_expresion = self.ss_expresion()
                    self.state = 387
                    self.match(LienzoParser.T__2)



                # no importa si es arreglo o variable, regresa el tipo correcto
                localctx.type = namespaceTable.getVariableType((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
                if not localctx.arr:
                    if localctx.type:
                        localctx.valor = memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text), currentFunctionName)
                    else:
                        localctx.valor = None
                        error((0 if localctx._ID is None else localctx._ID.line), "variable " + (None if localctx._ID is None else localctx._ID.text) + " no ha sido declarada")
                else:
                    if localctx.type:
                        cuadruplos.addCuadruplo(currentFunctionName, CHECK_BOUNDS, localctx._ss_expresion.valor, namespaceTable.getArrayLength((None if localctx._ID is None else localctx._ID.text), currentFunctionName), None, False)
                        localctx.valor = memoryregisters.getArrayMemoryRegister((None if localctx._ID is None else localctx._ID.text), localctx._ss_expresion.valor, currentFunctionName)
                    else:
                        localctx.valor = None
                        error((0 if localctx._ID is None else localctx._ID.line), "Arreglo " + (None if localctx._ID is None else localctx._ID.text) + " no ha sido declarado")  

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                localctx._BOOLEAN_CONSTANT = self.match(LienzoParser.BOOLEAN_CONSTANT)

                localctx.type = BOLEANO
                localctx.valor = True if (None if localctx._BOOLEAN_CONSTANT is None else localctx._BOOLEAN_CONSTANT.text) == 'verdadero' else False

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 394
                localctx.lf = localctx._llamadaFuncion = self.llamadaFuncion()

                functionType = localctx._llamadaFuncion.type
                localctx.type = functionType if functionType != "nada" else None
                localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, ASSIGN, localctx.lf.valor, None)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 397
                self.match(LienzoParser.T__3)
                self.state = 398
                localctx._ss_expresion = self.ss_expresion()
                self.state = 399
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





