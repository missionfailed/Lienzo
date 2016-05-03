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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3J")
        buf.write("\u01c7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\3\2\7\2T\n\2\f\2\16\2W\13\2\3\2")
        buf.write("\5\2Z\n\2\3\2\5\2]\n\2\3\2\5\2`\n\2\3\2\5\2c\n\2\5\2e")
        buf.write("\n\2\3\2\3\2\7\2i\n\2\f\2\16\2l\13\2\3\2\3\2\7\2p\n\2")
        buf.write("\f\2\16\2s\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\5\6\u008e\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\7\t\u00a7\n\t\f\t\16\t\u00aa\13\t\5\t\u00ac\n\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\5\n\u00b6\n\n\3\13\3")
        buf.write("\13\5\13\u00ba\n\13\3\13\3\13\3\13\3\f\7\f\u00c0\n\f\f")
        buf.write("\f\16\f\u00c3\13\f\3\f\7\f\u00c6\n\f\f\f\16\f\u00c9\13")
        buf.write("\f\3\r\3\r\3\r\7\r\u00ce\n\r\f\r\16\r\u00d1\13\r\3\r\5")
        buf.write("\r\u00d4\n\r\3\16\3\16\3\16\3\16\5\16\u00da\n\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00e0\n\16\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00f4\n\20\3\21\3\21\3\21\3\21\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37\u0145")
        buf.write("\n\37\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3!\3!\3!\3!\3!\5")
        buf.write("!\u0154\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\7#\u016a\n#\f#\16#\u016d\13")
        buf.write("#\5#\u016f\n#\3#\3#\3#\3$\3$\3$\3$\3$\3$\7$\u017a\n$\f")
        buf.write("$\16$\u017d\13$\3%\3%\3%\3%\3%\3%\3%\7%\u0186\n%\f%\16")
        buf.write("%\u0189\13%\3&\3&\3&\3&\3&\3&\3&\7&\u0192\n&\f&\16&\u0195")
        buf.write("\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u019d\n\'\f\'\16\'\u01a0")
        buf.write("\13\'\3(\5(\u01a3\n(\3(\3(\3(\3(\3(\5(\u01aa\n(\3(\3(")
        buf.write("\3(\3(\3(\5(\u01b1\n(\3)\3)\3)\3)\3)\5)\u01b8\n)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01c5\n)\3)\2\2*\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNP\2\t\3\2\32#\4\2<<@A\3\2\13\f\3\2\r\22\3")
        buf.write("\2\23\24\3\2\25\27\3\2GH\u01d1\2U\3\2\2\2\4w\3\2\2\2\6")
        buf.write("\177\3\2\2\2\b\u0081\3\2\2\2\n\u008d\3\2\2\2\f\u008f\3")
        buf.write("\2\2\2\16\u0097\3\2\2\2\20\u009f\3\2\2\2\22\u00b5\3\2")
        buf.write("\2\2\24\u00b7\3\2\2\2\26\u00c1\3\2\2\2\30\u00d3\3\2\2")
        buf.write("\2\32\u00df\3\2\2\2\34\u00e1\3\2\2\2\36\u00f3\3\2\2\2")
        buf.write(" \u00f5\3\2\2\2\"\u00f9\3\2\2\2$\u00fd\3\2\2\2&\u0103")
        buf.write("\3\2\2\2(\u0107\3\2\2\2*\u010c\3\2\2\2,\u0111\3\2\2\2")
        buf.write(".\u0116\3\2\2\2\60\u011b\3\2\2\2\62\u011f\3\2\2\2\64\u0123")
        buf.write("\3\2\2\2\66\u012a\3\2\2\28\u0131\3\2\2\2:\u0138\3\2\2")
        buf.write("\2<\u013f\3\2\2\2>\u014a\3\2\2\2@\u014c\3\2\2\2B\u0157")
        buf.write("\3\2\2\2D\u015f\3\2\2\2F\u0173\3\2\2\2H\u017e\3\2\2\2")
        buf.write("J\u018a\3\2\2\2L\u0196\3\2\2\2N\u01b0\3\2\2\2P\u01c4\3")
        buf.write("\2\2\2RT\5\n\6\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2")
        buf.write("\2Vd\3\2\2\2WU\3\2\2\2XZ\5\b\5\2YX\3\2\2\2YZ\3\2\2\2Z")
        buf.write("\\\3\2\2\2[]\5\4\3\2\\[\3\2\2\2\\]\3\2\2\2]e\3\2\2\2^")
        buf.write("`\5\4\3\2_^\3\2\2\2_`\3\2\2\2`b\3\2\2\2ac\5\b\5\2ba\3")
        buf.write("\2\2\2bc\3\2\2\2ce\3\2\2\2dY\3\2\2\2d_\3\2\2\2ef\3\2\2")
        buf.write("\2fj\b\2\1\2gi\5\20\t\2hg\3\2\2\2il\3\2\2\2jh\3\2\2\2")
        buf.write("jk\3\2\2\2km\3\2\2\2lj\3\2\2\2mq\b\2\1\2np\5\32\16\2o")
        buf.write("n\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt\3\2\2\2sq\3")
        buf.write("\2\2\2tu\7\2\2\3uv\b\2\1\2v\3\3\2\2\2wx\7$\2\2xy\7*\2")
        buf.write("\2yz\7&\2\2z{\7\'\2\2{|\5\6\4\2|}\7\3\2\2}~\b\3\1\2~\5")
        buf.write("\3\2\2\2\177\u0080\t\2\2\2\u0080\7\3\2\2\2\u0081\u0082")
        buf.write("\7(\2\2\u0082\u0083\7*\2\2\u0083\u0084\7&\2\2\u0084\u0085")
        buf.write("\7\'\2\2\u0085\u0086\5F$\2\u0086\u0087\7)\2\2\u0087\u0088")
        buf.write("\5F$\2\u0088\u0089\7\3\2\2\u0089\u008a\b\5\1\2\u008a\t")
        buf.write("\3\2\2\2\u008b\u008e\5\f\7\2\u008c\u008e\5\16\b\2\u008d")
        buf.write("\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e\13\3\2\2\2\u008f")
        buf.write("\u0090\5> \2\u0090\u0091\7J\2\2\u0091\u0092\b\7\1\2\u0092")
        buf.write("\u0093\7\'\2\2\u0093\u0094\5F$\2\u0094\u0095\7\3\2\2\u0095")
        buf.write("\u0096\b\7\1\2\u0096\r\3\2\2\2\u0097\u0098\5> \2\u0098")
        buf.write("\u0099\7\4\2\2\u0099\u009a\7G\2\2\u009a\u009b\7\5\2\2")
        buf.write("\u009b\u009c\7J\2\2\u009c\u009d\7\3\2\2\u009d\u009e\b")
        buf.write("\b\1\2\u009e\17\3\2\2\2\u009f\u00a0\5\22\n\2\u00a0\u00a1")
        buf.write("\7J\2\2\u00a1\u00a2\b\t\1\2\u00a2\u00ab\7\6\2\2\u00a3")
        buf.write("\u00a8\5\24\13\2\u00a4\u00a5\7\7\2\2\u00a5\u00a7\5\24")
        buf.write("\13\2\u00a6\u00a4\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00ab\u00a3\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\u00ae\7\b\2\2\u00ae\u00af\7")
        buf.write("\t\2\2\u00af\u00b0\5\26\f\2\u00b0\u00b1\7\n\2\2\u00b1")
        buf.write("\u00b2\b\t\1\2\u00b2\21\3\2\2\2\u00b3\u00b6\5> \2\u00b4")
        buf.write("\u00b6\7D\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b6\23\3\2\2\2\u00b7\u00b9\5> \2\u00b8\u00ba\7F\2\2")
        buf.write("\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3")
        buf.write("\2\2\2\u00bb\u00bc\7J\2\2\u00bc\u00bd\b\13\1\2\u00bd\25")
        buf.write("\3\2\2\2\u00be\u00c0\5\n\6\2\u00bf\u00be\3\2\2\2\u00c0")
        buf.write("\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\u00c7\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c6\5")
        buf.write("\32\16\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\27\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00ca\u00d4\5\32\16\2\u00cb\u00cf\7\t\2")
        buf.write("\2\u00cc\u00ce\5\32\16\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00d2\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d4\7\n\2\2")
        buf.write("\u00d3\u00ca\3\2\2\2\u00d3\u00cb\3\2\2\2\u00d4\31\3\2")
        buf.write("\2\2\u00d5\u00da\5<\37\2\u00d6\u00da\5\36\20\2\u00d7\u00da")
        buf.write("\5D#\2\u00d8\u00da\5\34\17\2\u00d9\u00d5\3\2\2\2\u00d9")
        buf.write("\u00d6\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2")
        buf.write("\u00da\u00db\3\2\2\2\u00db\u00dc\7\3\2\2\u00dc\u00e0\3")
        buf.write("\2\2\2\u00dd\u00e0\5@!\2\u00de\u00e0\5B\"\2\u00df\u00d9")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2\u00e0")
        buf.write("\33\3\2\2\2\u00e1\u00e2\7\66\2\2\u00e2\u00e3\5F$\2\u00e3")
        buf.write("\u00e4\b\17\1\2\u00e4\35\3\2\2\2\u00e5\u00f4\5 \21\2\u00e6")
        buf.write("\u00f4\5\"\22\2\u00e7\u00f4\5&\24\2\u00e8\u00f4\5$\23")
        buf.write("\2\u00e9\u00f4\5(\25\2\u00ea\u00f4\5*\26\2\u00eb\u00f4")
        buf.write("\5.\30\2\u00ec\u00f4\5,\27\2\u00ed\u00f4\5\64\33\2\u00ee")
        buf.write("\u00f4\5\60\31\2\u00ef\u00f4\5\62\32\2\u00f0\u00f4\5\66")
        buf.write("\34\2\u00f1\u00f4\58\35\2\u00f2\u00f4\5:\36\2\u00f3\u00e5")
        buf.write("\3\2\2\2\u00f3\u00e6\3\2\2\2\u00f3\u00e7\3\2\2\2\u00f3")
        buf.write("\u00e8\3\2\2\2\u00f3\u00e9\3\2\2\2\u00f3\u00ea\3\2\2\2")
        buf.write("\u00f3\u00eb\3\2\2\2\u00f3\u00ec\3\2\2\2\u00f3\u00ed\3")
        buf.write("\2\2\2\u00f3\u00ee\3\2\2\2\u00f3\u00ef\3\2\2\2\u00f3\u00f0")
        buf.write("\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4")
        buf.write("\37\3\2\2\2\u00f5\u00f6\7=\2\2\u00f6\u00f7\7J\2\2\u00f7")
        buf.write("\u00f8\b\21\1\2\u00f8!\3\2\2\2\u00f9\u00fa\7B\2\2\u00fa")
        buf.write("\u00fb\5F$\2\u00fb\u00fc\b\22\1\2\u00fc#\3\2\2\2\u00fd")
        buf.write("\u00fe\7C\2\2\u00fe\u00ff\78\2\2\u00ff\u0100\79\2\2\u0100")
        buf.write("\u0101\5F$\2\u0101\u0102\b\23\1\2\u0102%\3\2\2\2\u0103")
        buf.write("\u0104\7C\2\2\u0104\u0105\5F$\2\u0105\u0106\b\24\1\2\u0106")
        buf.write("\'\3\2\2\2\u0107\u0108\7,\2\2\u0108\u0109\7-\2\2\u0109")
        buf.write("\u010a\5F$\2\u010a\u010b\b\25\1\2\u010b)\3\2\2\2\u010c")
        buf.write("\u010d\7,\2\2\u010d\u010e\7.\2\2\u010e\u010f\5F$\2\u010f")
        buf.write("\u0110\b\26\1\2\u0110+\3\2\2\2\u0111\u0112\7/\2\2\u0112")
        buf.write("\u0113\7\60\2\2\u0113\u0114\5F$\2\u0114\u0115\b\27\1\2")
        buf.write("\u0115-\3\2\2\2\u0116\u0117\7/\2\2\u0117\u0118\7\61\2")
        buf.write("\2\u0118\u0119\5F$\2\u0119\u011a\b\30\1\2\u011a/\3\2\2")
        buf.write("\2\u011b\u011c\7\62\2\2\u011c\u011d\7\64\2\2\u011d\u011e")
        buf.write("\b\31\1\2\u011e\61\3\2\2\2\u011f\u0120\7\63\2\2\u0120")
        buf.write("\u0121\7\64\2\2\u0121\u0122\b\32\1\2\u0122\63\3\2\2\2")
        buf.write("\u0123\u0124\7$\2\2\u0124\u0125\7*\2\2\u0125\u0126\7\64")
        buf.write("\2\2\u0126\u0127\7\'\2\2\u0127\u0128\5\6\4\2\u0128\u0129")
        buf.write("\b\33\1\2\u0129\65\3\2\2\2\u012a\u012b\7%\2\2\u012b\u012c")
        buf.write("\7*\2\2\u012c\u012d\7\64\2\2\u012d\u012e\7\'\2\2\u012e")
        buf.write("\u012f\5F$\2\u012f\u0130\b\34\1\2\u0130\67\3\2\2\2\u0131")
        buf.write("\u0132\7>\2\2\u0132\u0133\7*\2\2\u0133\u0134\7\64\2\2")
        buf.write("\u0134\u0135\7\'\2\2\u0135\u0136\5F$\2\u0136\u0137\b\35")
        buf.write("\1\2\u01379\3\2\2\2\u0138\u0139\7?\2\2\u0139\u013a\7*")
        buf.write("\2\2\u013a\u013b\7\64\2\2\u013b\u013c\7\'\2\2\u013c\u013d")
        buf.write("\5F$\2\u013d\u013e\b\36\1\2\u013e;\3\2\2\2\u013f\u0144")
        buf.write("\7J\2\2\u0140\u0141\7\4\2\2\u0141\u0142\5F$\2\u0142\u0143")
        buf.write("\7\5\2\2\u0143\u0145\3\2\2\2\u0144\u0140\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147\7\'\2\2")
        buf.write("\u0147\u0148\5F$\2\u0148\u0149\b\37\1\2\u0149=\3\2\2\2")
        buf.write("\u014a\u014b\t\3\2\2\u014b?\3\2\2\2\u014c\u014d\7:\2\2")
        buf.write("\u014d\u014e\5F$\2\u014e\u014f\b!\1\2\u014f\u0153\5\30")
        buf.write("\r\2\u0150\u0151\7;\2\2\u0151\u0152\b!\1\2\u0152\u0154")
        buf.write("\5\30\r\2\u0153\u0150\3\2\2\2\u0153\u0154\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155\u0156\b!\1\2\u0156A\3\2\2\2\u0157")
        buf.write("\u0158\7\65\2\2\u0158\u0159\7\67\2\2\u0159\u015a\b\"\1")
        buf.write("\2\u015a\u015b\5F$\2\u015b\u015c\b\"\1\2\u015c\u015d\5")
        buf.write("\30\r\2\u015d\u015e\b\"\1\2\u015eC\3\2\2\2\u015f\u0160")
        buf.write("\7J\2\2\u0160\u0161\b#\1\2\u0161\u0162\7\6\2\2\u0162\u016e")
        buf.write("\b#\1\2\u0163\u0164\5F$\2\u0164\u016b\b#\1\2\u0165\u0166")
        buf.write("\7\7\2\2\u0166\u0167\5F$\2\u0167\u0168\b#\1\2\u0168\u016a")
        buf.write("\3\2\2\2\u0169\u0165\3\2\2\2\u016a\u016d\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016f\3\2\2\2")
        buf.write("\u016d\u016b\3\2\2\2\u016e\u0163\3\2\2\2\u016e\u016f\3")
        buf.write("\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171\7\b\2\2\u0171\u0172")
        buf.write("\b#\1\2\u0172E\3\2\2\2\u0173\u0174\5H%\2\u0174\u017b\b")
        buf.write("$\1\2\u0175\u0176\t\4\2\2\u0176\u0177\5H%\2\u0177\u0178")
        buf.write("\b$\1\2\u0178\u017a\3\2\2\2\u0179\u0175\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017cG\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\5J&\2")
        buf.write("\u017f\u0187\b%\1\2\u0180\u0181\t\5\2\2\u0181\u0182\5")
        buf.write("J&\2\u0182\u0183\3\2\2\2\u0183\u0184\b%\1\2\u0184\u0186")
        buf.write("\3\2\2\2\u0185\u0180\3\2\2\2\u0186\u0189\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188I\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u018a\u018b\5L\'\2\u018b\u0193\b&\1\2\u018c")
        buf.write("\u018d\t\6\2\2\u018d\u018e\5L\'\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f\u0190\b&\1\2\u0190\u0192\3\2\2\2\u0191\u018c\3")
        buf.write("\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194")
        buf.write("\3\2\2\2\u0194K\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u0197")
        buf.write("\5N(\2\u0197\u019e\b\'\1\2\u0198\u0199\t\7\2\2\u0199\u019a")
        buf.write("\5N(\2\u019a\u019b\b\'\1\2\u019b\u019d\3\2\2\2\u019c\u0198")
        buf.write("\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019fM\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1")
        buf.write("\u01a3\7\30\2\2\u01a2\u01a1\3\2\2\2\u01a2\u01a3\3\2\2")
        buf.write("\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\5P)\2\u01a5\u01a6\3")
        buf.write("\2\2\2\u01a6\u01a7\b(\1\2\u01a7\u01b1\3\2\2\2\u01a8\u01aa")
        buf.write("\7\24\2\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01ab\u01ac\t\b\2\2\u01ac\u01ad\3\2\2\2")
        buf.write("\u01ad\u01b1\b(\1\2\u01ae\u01af\7I\2\2\u01af\u01b1\b(")
        buf.write("\1\2\u01b0\u01a2\3\2\2\2\u01b0\u01a9\3\2\2\2\u01b0\u01ae")
        buf.write("\3\2\2\2\u01b1O\3\2\2\2\u01b2\u01b7\7J\2\2\u01b3\u01b4")
        buf.write("\7\4\2\2\u01b4\u01b5\5F$\2\u01b5\u01b6\7\5\2\2\u01b6\u01b8")
        buf.write("\3\2\2\2\u01b7\u01b3\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01c5\b)\1\2\u01ba\u01bb\7E\2\2\u01bb")
        buf.write("\u01c5\b)\1\2\u01bc\u01bd\5D#\2\u01bd\u01be\b)\1\2\u01be")
        buf.write("\u01c5\3\2\2\2\u01bf\u01c0\7\6\2\2\u01c0\u01c1\5F$\2\u01c1")
        buf.write("\u01c2\7\b\2\2\u01c2\u01c3\b)\1\2\u01c3\u01c5\3\2\2\2")
        buf.write("\u01c4\u01b2\3\2\2\2\u01c4\u01ba\3\2\2\2\u01c4\u01bc\3")
        buf.write("\2\2\2\u01c4\u01bf\3\2\2\2\u01c5Q\3\2\2\2#UY\\_bdjq\u008d")
        buf.write("\u00a8\u00ab\u00b5\u00b9\u00c1\u00c7\u00cf\u00d3\u00d9")
        buf.write("\u00df\u00f3\u0144\u0153\u016b\u016e\u017b\u0187\u0193")
        buf.write("\u019e\u01a2\u01a9\u01b0\u01b7\u01c4")
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
                     "'cafe'", "'gris'", "'color'", "'velocidad'", "'lienzo'", 
                     "'='", "'tamano'", "'por'", "'de'", "'en'", "'mover'", 
                     "'adelante'", "'atras'", "'girar'", "'derecha'", "'izquierda'", 
                     "'levantar'", "'bajar'", "'pluma'", "'mientras'", "'regresar'", 
                     "'que'", "'sin'", "'salto'", "'si'", "'sino'", "'texto'", 
                     "'leer'", "'posicionX'", "'posicionY'", "'boleano'", 
                     "'numero'", "'escribir'", "'imprimir'", "'nada'", "<INVALID>", 
                     "'modificable'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ROJO", 
                      "VERDE", "AMARILLO", "AZUL", "BLANCO", "NEGRO", "MORADO", 
                      "NARANJA", "CAFE", "GRIS", "COLOR", "VELOCIDAD", "LIENZO", 
                      "EQUALS", "TAMANO", "POR", "DE", "EN", "MOVER", "ADELANTE", 
                      "ATRAS", "GIRAR", "DERECHA", "IZQUIERDA", "LEVANTAR", 
                      "BAJAR", "PLUMA", "MIENTRAS", "REGRESAR", "QUE", "SIN", 
                      "SALTO", "SI", "SINO", "TEXTO", "LEER", "POSICION_X", 
                      "POSICION_Y", "BOLEANO", "NUMERO", "ESCRIBIR", "IMPRIMIR", 
                      "NADA", "BOOLEAN_CONSTANT", "MODIFICABLE", "INTEGRAL_CONSTANT", 
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
    RULE_imprimir_no_ln = 17
    RULE_imprimir = 18
    RULE_mover_adelante = 19
    RULE_mover_atras = 20
    RULE_girar_derecha = 21
    RULE_girar_izquierda = 22
    RULE_subir_pluma = 23
    RULE_bajar_pluma = 24
    RULE_cambio_color = 25
    RULE_velocidad_pluma = 26
    RULE_posicion_x_pluma = 27
    RULE_posicion_y_pluma = 28
    RULE_asignacion = 29
    RULE_tipo = 30
    RULE_condicional = 31
    RULE_mientrasQue = 32
    RULE_llamadaFuncion = 33
    RULE_ss_expresion = 34
    RULE_s_expresion = 35
    RULE_expresion = 36
    RULE_termino = 37
    RULE_factor = 38
    RULE_factor_aux = 39

    ruleNames =  [ "program", "colorLienzo", "color", "tamanoLienzo", "declaracion", 
                   "declaracion_variable", "declaracion_arreglo", "funcion", 
                   "tipoFunc", "parametro", "cuerpo", "bloque_instrucciones", 
                   "instruccion_aux", "regresar", "llamadaFuncionPredefinida", 
                   "lectura", "escritura", "imprimir_no_ln", "imprimir", 
                   "mover_adelante", "mover_atras", "girar_derecha", "girar_izquierda", 
                   "subir_pluma", "bajar_pluma", "cambio_color", "velocidad_pluma", 
                   "posicion_x_pluma", "posicion_y_pluma", "asignacion", 
                   "tipo", "condicional", "mientrasQue", "llamadaFuncion", 
                   "ss_expresion", "s_expresion", "expresion", "termino", 
                   "factor", "factor_aux" ]

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
    VELOCIDAD=35
    LIENZO=36
    EQUALS=37
    TAMANO=38
    POR=39
    DE=40
    EN=41
    MOVER=42
    ADELANTE=43
    ATRAS=44
    GIRAR=45
    DERECHA=46
    IZQUIERDA=47
    LEVANTAR=48
    BAJAR=49
    PLUMA=50
    MIENTRAS=51
    REGRESAR=52
    QUE=53
    SIN=54
    SALTO=55
    SI=56
    SINO=57
    TEXTO=58
    LEER=59
    POSICION_X=60
    POSICION_Y=61
    BOLEANO=62
    NUMERO=63
    ESCRIBIR=64
    IMPRIMIR=65
    NADA=66
    BOOLEAN_CONSTANT=67
    MODIFICABLE=68
    INTEGRAL_CONSTANT=69
    NUMERIC_CONSTANT=70
    STRING_CONSTANT=71
    ID=72

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


        def tamanoLienzo(self):
            return self.getTypedRuleContext(LienzoParser.TamanoLienzoContext,0)


        def colorLienzo(self):
            return self.getTypedRuleContext(LienzoParser.ColorLienzoContext,0)


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
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 80
                    self.declaracion() 
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 98
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 87
                _la = self._input.LA(1)
                if _la==LienzoParser.TAMANO:
                    self.state = 86
                    self.tamanoLienzo()


                self.state = 90
                self._errHandler.sync(self);
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 89
                    self.colorLienzo()


                pass

            elif la_ == 2:
                self.state = 93
                self._errHandler.sync(self);
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 92
                    self.colorLienzo()


                self.state = 96
                _la = self._input.LA(1)
                if _la==LienzoParser.TAMANO:
                    self.state = 95
                    self.tamanoLienzo()


                pass



            cuadruplos.addCuadruplo("", GOTO, None, None, None, False)
            cuadruplos.pushPilaSaltos(cuadruplos.last())

            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 58)) & ~0x3f) == 0 and ((1 << (_la - 58)) & ((1 << (LienzoParser.TEXTO - 58)) | (1 << (LienzoParser.BOLEANO - 58)) | (1 << (LienzoParser.NUMERO - 58)) | (1 << (LienzoParser.NADA - 58)))) != 0):
                self.state = 101
                self.funcion()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(), cuadruplos.current())

            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & ((1 << (LienzoParser.COLOR - 34)) | (1 << (LienzoParser.VELOCIDAD - 34)) | (1 << (LienzoParser.MOVER - 34)) | (1 << (LienzoParser.GIRAR - 34)) | (1 << (LienzoParser.LEVANTAR - 34)) | (1 << (LienzoParser.BAJAR - 34)) | (1 << (LienzoParser.MIENTRAS - 34)) | (1 << (LienzoParser.REGRESAR - 34)) | (1 << (LienzoParser.SI - 34)) | (1 << (LienzoParser.LEER - 34)) | (1 << (LienzoParser.POSICION_X - 34)) | (1 << (LienzoParser.POSICION_Y - 34)) | (1 << (LienzoParser.ESCRIBIR - 34)) | (1 << (LienzoParser.IMPRIMIR - 34)) | (1 << (LienzoParser.ID - 34)))) != 0):
                self.state = 108
                self.instruccion_aux()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
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
            self.state = 117
            self.match(LienzoParser.COLOR)
            self.state = 118
            self.match(LienzoParser.DE)
            self.state = 119
            self.match(LienzoParser.LIENZO)
            self.state = 120
            self.match(LienzoParser.EQUALS)
            self.state = 121
            localctx._color = self.color()
            self.state = 122
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
            self.state = 125
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
            self.state = 127
            self.match(LienzoParser.TAMANO)
            self.state = 128
            self.match(LienzoParser.DE)
            self.state = 129
            self.match(LienzoParser.LIENZO)
            self.state = 130
            self.match(LienzoParser.EQUALS)
            self.state = 131
            localctx.largo = self.ss_expresion()
            self.state = 132
            self.match(LienzoParser.POR)
            self.state = 133
            localctx.ancho = self.ss_expresion()
            self.state = 134
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
            self.state = 139
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.declaracion_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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
            self.state = 141
            localctx._tipo = self.tipo()
            self.state = 142
            localctx._ID = self.match(LienzoParser.ID)

            if namespaceTable.idAlreadyTaken((None if localctx._ID is None else localctx._ID.text), currentFunctionName):
                error((0 if localctx._ID is None else localctx._ID.line), ": Identificador " + (None if localctx._ID is None else localctx._ID.text) + " ya fue declarado")

            self.state = 144
            self.match(LienzoParser.EQUALS)
            self.state = 145
            localctx._ss_expresion = self.ss_expresion()
            self.state = 146
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
            self.state = 149
            localctx._tipo = self.tipo()
            self.state = 150
            self.match(LienzoParser.T__1)
            self.state = 151
            localctx._INTEGRAL_CONSTANT = self.match(LienzoParser.INTEGRAL_CONSTANT)
            self.state = 152
            self.match(LienzoParser.T__2)
            self.state = 153
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 154
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
            self.state = 157
            localctx._tipoFunc = self.tipoFunc()
            self.state = 158
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

            self.state = 160
            self.match(LienzoParser.T__3)
            self.state = 169
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 161
                self.parametro()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__4:
                    self.state = 162
                    self.match(LienzoParser.T__4)
                    self.state = 163
                    self.parametro()
                    self.state = 168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 171
            self.match(LienzoParser.T__5)
            self.state = 172
            self.match(LienzoParser.T__6)
            self.state = 173
            self.cuerpo()
            self.state = 174
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
            self.state = 179
            token = self._input.LA(1)
            if token in [LienzoParser.TEXTO, LienzoParser.BOLEANO, LienzoParser.NUMERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.tipo()

            elif token in [LienzoParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
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
            self.state = 181
            localctx._tipo = self.tipo()
            self.state = 183
            _la = self._input.LA(1)
            if _la==LienzoParser.MODIFICABLE:
                self.state = 182
                localctx._MODIFICABLE = self.match(LienzoParser.MODIFICABLE)


            self.state = 185
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
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.TEXTO) | (1 << LienzoParser.BOLEANO) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 188
                self.declaracion()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & ((1 << (LienzoParser.COLOR - 34)) | (1 << (LienzoParser.VELOCIDAD - 34)) | (1 << (LienzoParser.MOVER - 34)) | (1 << (LienzoParser.GIRAR - 34)) | (1 << (LienzoParser.LEVANTAR - 34)) | (1 << (LienzoParser.BAJAR - 34)) | (1 << (LienzoParser.MIENTRAS - 34)) | (1 << (LienzoParser.REGRESAR - 34)) | (1 << (LienzoParser.SI - 34)) | (1 << (LienzoParser.LEER - 34)) | (1 << (LienzoParser.POSICION_X - 34)) | (1 << (LienzoParser.POSICION_Y - 34)) | (1 << (LienzoParser.ESCRIBIR - 34)) | (1 << (LienzoParser.IMPRIMIR - 34)) | (1 << (LienzoParser.ID - 34)))) != 0):
                self.state = 194
                self.instruccion_aux()
                self.state = 199
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
            self.state = 209
            token = self._input.LA(1)
            if token in [LienzoParser.COLOR, LienzoParser.VELOCIDAD, LienzoParser.MOVER, LienzoParser.GIRAR, LienzoParser.LEVANTAR, LienzoParser.BAJAR, LienzoParser.MIENTRAS, LienzoParser.REGRESAR, LienzoParser.SI, LienzoParser.LEER, LienzoParser.POSICION_X, LienzoParser.POSICION_Y, LienzoParser.ESCRIBIR, LienzoParser.IMPRIMIR, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.instruccion_aux()

            elif token in [LienzoParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(LienzoParser.T__6)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & ((1 << (LienzoParser.COLOR - 34)) | (1 << (LienzoParser.VELOCIDAD - 34)) | (1 << (LienzoParser.MOVER - 34)) | (1 << (LienzoParser.GIRAR - 34)) | (1 << (LienzoParser.LEVANTAR - 34)) | (1 << (LienzoParser.BAJAR - 34)) | (1 << (LienzoParser.MIENTRAS - 34)) | (1 << (LienzoParser.REGRESAR - 34)) | (1 << (LienzoParser.SI - 34)) | (1 << (LienzoParser.LEER - 34)) | (1 << (LienzoParser.POSICION_X - 34)) | (1 << (LienzoParser.POSICION_Y - 34)) | (1 << (LienzoParser.ESCRIBIR - 34)) | (1 << (LienzoParser.IMPRIMIR - 34)) | (1 << (LienzoParser.ID - 34)))) != 0):
                    self.state = 202
                    self.instruccion_aux()
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 208
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
            self.state = 221
            token = self._input.LA(1)
            if token in [LienzoParser.COLOR, LienzoParser.VELOCIDAD, LienzoParser.MOVER, LienzoParser.GIRAR, LienzoParser.LEVANTAR, LienzoParser.BAJAR, LienzoParser.REGRESAR, LienzoParser.LEER, LienzoParser.POSICION_X, LienzoParser.POSICION_Y, LienzoParser.ESCRIBIR, LienzoParser.IMPRIMIR, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self._errHandler.sync(self);
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 211
                    self.asignacion()
                    pass

                elif la_ == 2:
                    self.state = 212
                    self.llamadaFuncionPredefinida()
                    pass

                elif la_ == 3:
                    self.state = 213
                    self.llamadaFuncion()
                    pass

                elif la_ == 4:
                    self.state = 214
                    self.regresar()
                    pass


                self.state = 217
                self.match(LienzoParser.T__0)

            elif token in [LienzoParser.SI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.condicional()

            elif token in [LienzoParser.MIENTRAS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
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
            self.state = 223
            localctx._REGRESAR = self.match(LienzoParser.REGRESAR)
            self.state = 224
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


        def imprimir_no_ln(self):
            return self.getTypedRuleContext(LienzoParser.Imprimir_no_lnContext,0)


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


        def velocidad_pluma(self):
            return self.getTypedRuleContext(LienzoParser.Velocidad_plumaContext,0)


        def posicion_x_pluma(self):
            return self.getTypedRuleContext(LienzoParser.Posicion_x_plumaContext,0)


        def posicion_y_pluma(self):
            return self.getTypedRuleContext(LienzoParser.Posicion_y_plumaContext,0)


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
            self.state = 241
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.lectura()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.escritura()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 229
                self.imprimir()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 230
                self.imprimir_no_ln()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 231
                self.mover_adelante()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 232
                self.mover_atras()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 233
                self.girar_izquierda()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 234
                self.girar_derecha()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 235
                self.cambio_color()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 236
                self.subir_pluma()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 237
                self.bajar_pluma()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 238
                self.velocidad_pluma()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 239
                self.posicion_x_pluma()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 240
                self.posicion_y_pluma()
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
            self.state = 243
            self.match(LienzoParser.LEER)
            self.state = 244
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
            self.state = 247
            self.match(LienzoParser.ESCRIBIR)
            self.state = 248
            localctx._ss_expresion = self.ss_expresion()

            cuadruplos.addCuadruplo(currentFunctionName, WRITE, localctx._ss_expresion.valor, None, None, False)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Imprimir_no_lnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext

        def IMPRIMIR(self):
            return self.getToken(LienzoParser.IMPRIMIR, 0)

        def SIN(self):
            return self.getToken(LienzoParser.SIN, 0)

        def SALTO(self):
            return self.getToken(LienzoParser.SALTO, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_imprimir_no_ln

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimir_no_ln" ):
                listener.enterImprimir_no_ln(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimir_no_ln" ):
                listener.exitImprimir_no_ln(self)




    def imprimir_no_ln(self):

        localctx = LienzoParser.Imprimir_no_lnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_imprimir_no_ln)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(LienzoParser.IMPRIMIR)
            self.state = 252
            self.match(LienzoParser.SIN)
            self.state = 253
            self.match(LienzoParser.SALTO)
            self.state = 254
            localctx._ss_expresion = self.ss_expresion()

            cuadruplos.addCuadruplo(currentFunctionName, PRINT, localctx._ss_expresion.valor, None, None, False)

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
        self.enterRule(localctx, 36, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(LienzoParser.IMPRIMIR)
            self.state = 258
            localctx._ss_expresion = self.ss_expresion()

            cuadruplos.addCuadruplo(currentFunctionName, PRINTLN, localctx._ss_expresion.valor, None, None, False)

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
        self.enterRule(localctx, 38, self.RULE_mover_adelante)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(LienzoParser.MOVER)
            self.state = 262
            self.match(LienzoParser.ADELANTE)
            self.state = 263
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
        self.enterRule(localctx, 40, self.RULE_mover_atras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(LienzoParser.MOVER)
            self.state = 267
            self.match(LienzoParser.ATRAS)
            self.state = 268
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
        self.enterRule(localctx, 42, self.RULE_girar_derecha)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(LienzoParser.GIRAR)
            self.state = 272
            self.match(LienzoParser.DERECHA)
            self.state = 273
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
        self.enterRule(localctx, 44, self.RULE_girar_izquierda)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(LienzoParser.GIRAR)
            self.state = 277
            self.match(LienzoParser.IZQUIERDA)
            self.state = 278
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
        self.enterRule(localctx, 46, self.RULE_subir_pluma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(LienzoParser.LEVANTAR)
            self.state = 282
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
        self.enterRule(localctx, 48, self.RULE_bajar_pluma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(LienzoParser.BAJAR)
            self.state = 286
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
        self.enterRule(localctx, 50, self.RULE_cambio_color)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(LienzoParser.COLOR)
            self.state = 290
            self.match(LienzoParser.DE)
            self.state = 291
            self.match(LienzoParser.PLUMA)
            self.state = 292
            self.match(LienzoParser.EQUALS)
            self.state = 293
            localctx._color = self.color()

            cuadruplos.addCuadruplo(currentFunctionName, COLOR_CHANGE, (None if localctx._color is None else self._input.getText((localctx._color.start,localctx._color.stop))), None, None, False)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Velocidad_plumaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext

        def VELOCIDAD(self):
            return self.getToken(LienzoParser.VELOCIDAD, 0)

        def DE(self):
            return self.getToken(LienzoParser.DE, 0)

        def PLUMA(self):
            return self.getToken(LienzoParser.PLUMA, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_velocidad_pluma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVelocidad_pluma" ):
                listener.enterVelocidad_pluma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVelocidad_pluma" ):
                listener.exitVelocidad_pluma(self)




    def velocidad_pluma(self):

        localctx = LienzoParser.Velocidad_plumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_velocidad_pluma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(LienzoParser.VELOCIDAD)
            self.state = 297
            self.match(LienzoParser.DE)
            self.state = 298
            self.match(LienzoParser.PLUMA)
            self.state = 299
            self.match(LienzoParser.EQUALS)
            self.state = 300
            localctx._ss_expresion = self.ss_expresion()

            if localctx._ss_expresion.type == NUMERO:
                cuadruplos.addCuadruplo(currentFunctionName, SETSPEED, localctx._ss_expresion.valor, None, None, False)
            else:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "La velocidad debe ser un numero")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Posicion_x_plumaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext

        def POSICION_X(self):
            return self.getToken(LienzoParser.POSICION_X, 0)

        def DE(self):
            return self.getToken(LienzoParser.DE, 0)

        def PLUMA(self):
            return self.getToken(LienzoParser.PLUMA, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_posicion_x_pluma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosicion_x_pluma" ):
                listener.enterPosicion_x_pluma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosicion_x_pluma" ):
                listener.exitPosicion_x_pluma(self)




    def posicion_x_pluma(self):

        localctx = LienzoParser.Posicion_x_plumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_posicion_x_pluma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(LienzoParser.POSICION_X)
            self.state = 304
            self.match(LienzoParser.DE)
            self.state = 305
            self.match(LienzoParser.PLUMA)
            self.state = 306
            self.match(LienzoParser.EQUALS)
            self.state = 307
            localctx._ss_expresion = self.ss_expresion()

            if localctx._ss_expresion.type == NUMERO:
                cuadruplos.addCuadruplo(currentFunctionName, PEN_POSX, localctx._ss_expresion.valor, None, None, False)
            else:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "La coordenada x debe ser un numero")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Posicion_y_plumaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ss_expresion = None # Ss_expresionContext

        def POSICION_Y(self):
            return self.getToken(LienzoParser.POSICION_Y, 0)

        def DE(self):
            return self.getToken(LienzoParser.DE, 0)

        def PLUMA(self):
            return self.getToken(LienzoParser.PLUMA, 0)

        def ss_expresion(self):
            return self.getTypedRuleContext(LienzoParser.Ss_expresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_posicion_y_pluma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosicion_y_pluma" ):
                listener.enterPosicion_y_pluma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosicion_y_pluma" ):
                listener.exitPosicion_y_pluma(self)




    def posicion_y_pluma(self):

        localctx = LienzoParser.Posicion_y_plumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_posicion_y_pluma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(LienzoParser.POSICION_Y)
            self.state = 311
            self.match(LienzoParser.DE)
            self.state = 312
            self.match(LienzoParser.PLUMA)
            self.state = 313
            self.match(LienzoParser.EQUALS)
            self.state = 314
            localctx._ss_expresion = self.ss_expresion()

            if localctx._ss_expresion.type == NUMERO:
                cuadruplos.addCuadruplo(currentFunctionName, PEN_POSY, localctx._ss_expresion.valor, None, None, False)
            else:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "La coordenada y debe ser un numero")

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
        self.enterRule(localctx, 58, self.RULE_asignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 322
            _la = self._input.LA(1)
            if _la==LienzoParser.T__1:
                self.state = 318
                localctx.arr = self.match(LienzoParser.T__1)
                self.state = 319
                localctx.indice = self.ss_expresion()
                self.state = 320
                self.match(LienzoParser.T__2)


            self.state = 324
            self.match(LienzoParser.EQUALS)
            self.state = 325
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
        self.enterRule(localctx, 60, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
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
        self.enterRule(localctx, 62, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(LienzoParser.SI)
            self.state = 331
            localctx._ss_expresion = self.ss_expresion()

            if localctx._ss_expresion.type != BOLEANO:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "el estatuto 'si' necesita una boleano")
            else:
                cuadruplos.addCuadruplo(currentFunctionName, GOTOF, localctx._ss_expresion.valor, None, None, False)
                cuadruplos.pushPilaSaltos(cuadruplos.last())

            self.state = 333
            self.bloque_instrucciones()
            self.state = 337
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 334
                self.match(LienzoParser.SINO)

                cuadruplos.addCuadruplo(currentFunctionName, GOTO,None,None,None,False)
                cuadruplos.editCuadruplo(cuadruplos.popPilaSaltos(),cuadruplos.current())
                cuadruplos.pushPilaSaltos(cuadruplos.last())

                self.state = 336
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
        self.enterRule(localctx, 64, self.RULE_mientrasQue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(LienzoParser.MIENTRAS)
            self.state = 342
            self.match(LienzoParser.QUE)

            cuadruplos.pushPilaSaltos(cuadruplos.current())

            self.state = 344
            localctx._ss_expresion = self.ss_expresion()

            if localctx._ss_expresion.type != BOLEANO:
                error((None if localctx._ss_expresion is None else localctx._ss_expresion.start).line, "el estatuto 'mientras que' necesita una boleano")
            else:
                cuadruplos.addCuadruplo(currentFunctionName, GOTOF,localctx._ss_expresion.valor,None,None,False)
                cuadruplos.pushPilaSaltos(cuadruplos.last())

            self.state = 346
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
        self.enterRule(localctx, 66, self.RULE_llamadaFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            localctx._ID = self.match(LienzoParser.ID)

            functionType = namespaceTable.getFunctionType((None if localctx._ID is None else localctx._ID.text))
            if not functionType:
                error((0 if localctx._ID is None else localctx._ID.line), ": llamada a funcion " + (None if localctx._ID is None else localctx._ID.text) + " inexistente")
                localctx.valor = None
            else:
                localctx.type = None if functionType == "nada" else functionType
                cuadruplos.addCuadruplo(currentFunctionName, ERA, (None if localctx._ID is None else localctx._ID.text), None, None, False)
                localctx.valor = memoryregisters.getMemoryRegister((None if localctx._ID is None else localctx._ID.text), "")

            self.state = 351
            self.match(LienzoParser.T__3)

            k = 0

            self.state = 364
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__3) | (1 << LienzoParser.T__17) | (1 << LienzoParser.T__21))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (LienzoParser.BOOLEAN_CONSTANT - 67)) | (1 << (LienzoParser.INTEGRAL_CONSTANT - 67)) | (1 << (LienzoParser.NUMERIC_CONSTANT - 67)) | (1 << (LienzoParser.STRING_CONSTANT - 67)) | (1 << (LienzoParser.ID - 67)))) != 0):
                self.state = 353
                localctx.ss_exp1 = self.ss_expresion()

                if namespaceTable.argumentAgree((None if localctx._ID is None else localctx._ID.text), k, (None if localctx.ss_exp1 is None else self._input.getText((localctx.ss_exp1.start,localctx.ss_exp1.stop))), localctx.ss_exp1.type):
                    cuadruplos.addCuadruplo(currentFunctionName, PARAM, localctx.ss_exp1.valor, namespaceTable.parameterReference((None if localctx._ID is None else localctx._ID.text), k), None, False)
                else:
                    error((None if localctx.ss_exp1 is None else localctx.ss_exp1.start).line, ": argumento #" + k + "no concuerda con el parametro esperado")
                k += 1

                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__4:
                    self.state = 355
                    self.match(LienzoParser.T__4)
                    self.state = 356
                    localctx.ss_exp2 = self.ss_expresion()

                    if namespaceTable.argumentAgree((None if localctx._ID is None else localctx._ID.text), k, (None if localctx.ss_exp2 is None else self._input.getText((localctx.ss_exp2.start,localctx.ss_exp2.stop))), localctx.ss_exp2.type):
                        cuadruplos.addCuadruplo(currentFunctionName, PARAM, localctx.ss_exp2.valor, namespaceTable.parameterReference((None if localctx._ID is None else localctx._ID.text), k), None, False)
                    else:
                        error((None if localctx.ss_exp1 is None else localctx.ss_exp1.start).line, ": argumento #" + k + "no concuerda con el parametro esperado")
                    k += 1

                    self.state = 363
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 366
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
        self.enterRule(localctx, 68, self.RULE_ss_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            localctx.s_exp1 = self.s_expresion()

            localctx.type = localctx.s_exp1.type
            localctx.valor = localctx.s_exp1.valor

            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.T__8 or _la==LienzoParser.T__9:
                self.state = 371
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__8 or _la==LienzoParser.T__9):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 372
                localctx.s_exp2 = self.s_expresion()

                tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.s_exp2.type]
                if not tipo:
                    error(op.line, ": operador " + (None if localctx.op is None else localctx.op.text) + " no puede ser aplicado a " + localctx.type +" y a " + localctx.s_exp2.type)
                else:
                    namespaceTable.addTemporal(currentFunctionName, tipo)
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text), localctx.valor, localctx.s_exp2.valor)
                localctx.type = tipo

                self.state = 379
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
        self.enterRule(localctx, 70, self.RULE_s_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            localctx.exp1 = self.expresion()

            localctx.type = localctx.exp1.type
            localctx.valor = localctx.exp1.valor

            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12) | (1 << LienzoParser.T__13) | (1 << LienzoParser.T__14) | (1 << LienzoParser.T__15))) != 0):
                self.state = 382
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12) | (1 << LienzoParser.T__13) | (1 << LienzoParser.T__14) | (1 << LienzoParser.T__15))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 383
                localctx.exp2 = self.expresion()

                tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.exp2.type]
                if not tipo:
                    error((0 if localctx.op is None else localctx.op.line), ": operador " + (None if localctx.op is None else localctx.op.text) + " no puede ser aplicado a " + localctx.type + " y a " + localctx.exp2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text),localctx.valor,localctx.exp2.valor)
                    namespaceTable.addTemporal(currentFunctionName, tipo)
                localctx.type = tipo

                self.state = 391
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
        self.enterRule(localctx, 72, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            localctx.term1 = self.termino()

            localctx.type = localctx.term1.type
            localctx.valor = localctx.term1.valor

            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.T__16 or _la==LienzoParser.T__17:
                self.state = 394
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__16 or _la==LienzoParser.T__17):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 395
                localctx.term2 = self.termino()

                tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.term2.type]
                if not tipo:
                    error((0 if localctx.op is None else localctx.op.line), ": operador " + (None if localctx.op is None else localctx.op.text) + " no puede ser aplicado a " + localctx.type + " y a " + localctx.term2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text),localctx.valor,localctx.term2.valor)
                    namespaceTable.addTemporal(currentFunctionName, tipo)
                localctx.type = tipo

                self.state = 403
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
        self.enterRule(localctx, 74, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            localctx.factor1 = self.factor()

            localctx.type = localctx.factor1.type
            localctx.valor = localctx.factor1.valor

            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__18) | (1 << LienzoParser.T__19) | (1 << LienzoParser.T__20))) != 0):
                self.state = 406
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__18) | (1 << LienzoParser.T__19) | (1 << LienzoParser.T__20))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 407
                localctx.factor2 = self.factor()

                tipo = cubo[localctx.type][(None if localctx.op is None else localctx.op.text)][localctx.factor2.type]
                if not tipo:
                    error((0 if localctx.op is None else localctx.op.line), ": operador " + (None if localctx.op is None else localctx.op.text) + " no puede ser aplicado a " + localctx.type + " y a " + localctx.factor2.type)
                else:
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, (None if localctx.op is None else localctx.op.text),localctx.valor,localctx.factor2.valor)
                    namespaceTable.addTemporal(currentFunctionName, tipo)
                localctx.type = tipo

                self.state = 414
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
        self.enterRule(localctx, 76, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 430
            token = self._input.LA(1)
            if token in [LienzoParser.T__3, LienzoParser.T__21, LienzoParser.BOOLEAN_CONSTANT, LienzoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                _la = self._input.LA(1)
                if _la==LienzoParser.T__21:
                    self.state = 415
                    localctx.neg = self.match(LienzoParser.T__21)


                self.state = 418
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
                self.state = 423
                _la = self._input.LA(1)
                if _la==LienzoParser.T__17:
                    self.state = 422
                    localctx.neg = self.match(LienzoParser.T__17)


                self.state = 425
                localctx.n = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==LienzoParser.INTEGRAL_CONSTANT or _la==LienzoParser.NUMERIC_CONSTANT):
                    localctx.n = self._errHandler.recoverInline(self)
                else:
                    self.consume()

                localctx.type = NUMERO

                if (None if localctx.neg is None else localctx.neg.text):
                    localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, MINUS, 0, num((None if localctx.n is None else localctx.n.text)))
                    namespaceTable.addTemporal(currentFunctionName, localctx.type)
                else:
                    localctx.valor = num((None if localctx.n is None else localctx.n.text))


            elif token in [LienzoParser.STRING_CONSTANT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 428
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
        self.enterRule(localctx, 78, self.RULE_factor_aux)
        self._la = 0 # Token type
        try:
            self.state = 450
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                localctx._ID = self.match(LienzoParser.ID)
                self.state = 437
                _la = self._input.LA(1)
                if _la==LienzoParser.T__1:
                    self.state = 433
                    localctx.arr = self.match(LienzoParser.T__1)
                    self.state = 434
                    localctx._ss_expresion = self.ss_expresion()
                    self.state = 435
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
                self.state = 440
                localctx._BOOLEAN_CONSTANT = self.match(LienzoParser.BOOLEAN_CONSTANT)

                localctx.type = BOLEANO
                localctx.valor = True if (None if localctx._BOOLEAN_CONSTANT is None else localctx._BOOLEAN_CONSTANT.text) == 'verdadero' else False

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                localctx.lf = localctx._llamadaFuncion = self.llamadaFuncion()

                functionType = localctx._llamadaFuncion.type
                localctx.type = functionType if functionType != "nada" else None
                localctx.valor = cuadruplos.addCuadruplo(currentFunctionName, ASSIGN, localctx.lf.valor, None)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 445
                self.match(LienzoParser.T__3)
                self.state = 446
                localctx._ss_expresion = self.ss_expresion()
                self.state = 447
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





