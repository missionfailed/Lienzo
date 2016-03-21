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

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2H")
        buf.write("\u0208\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\6\30\u00c1\n\30\r\30\16")
        buf.write("\30\u00c2\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\39\39\39\39\3")
        buf.write("9\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3")
        buf.write("@\3A\3A\5A\u01d0\nA\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3C\3")
        buf.write("C\3C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3E\6")
        buf.write("E\u01ef\nE\rE\16E\u01f0\3E\3E\6E\u01f5\nE\rE\16E\u01f6")
        buf.write("\5E\u01f9\nE\3F\3F\7F\u01fd\nF\fF\16F\u0200\13F\3F\3F")
        buf.write("\3G\6G\u0205\nG\rG\16G\u0206\2\2H\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\3\2\6\5\2")
        buf.write("\13\f\17\17\"\"\3\2\62;\3\2$$\4\2C\\c|\u020e\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u0091")
        buf.write("\3\2\2\2\7\u0093\3\2\2\2\t\u0095\3\2\2\2\13\u0097\3\2")
        buf.write("\2\2\r\u0099\3\2\2\2\17\u009b\3\2\2\2\21\u009d\3\2\2\2")
        buf.write("\23\u009f\3\2\2\2\25\u00a1\3\2\2\2\27\u00a3\3\2\2\2\31")
        buf.write("\u00a6\3\2\2\2\33\u00a9\3\2\2\2\35\u00ab\3\2\2\2\37\u00ad")
        buf.write("\3\2\2\2!\u00b0\3\2\2\2#\u00b3\3\2\2\2%\u00b5\3\2\2\2")
        buf.write("\'\u00b7\3\2\2\2)\u00b9\3\2\2\2+\u00bb\3\2\2\2-\u00bd")
        buf.write("\3\2\2\2/\u00c0\3\2\2\2\61\u00c6\3\2\2\2\63\u00cd\3\2")
        buf.write("\2\2\65\u00d8\3\2\2\2\67\u00e0\3\2\2\29\u00e3\3\2\2\2")
        buf.write(";\u00e9\3\2\2\2=\u00f4\3\2\2\2?\u00fe\3\2\2\2A\u0103\3")
        buf.write("\2\2\2C\u0109\3\2\2\2E\u0112\3\2\2\2G\u0117\3\2\2\2I\u011e")
        buf.write("\3\2\2\2K\u0124\3\2\2\2M\u012b\3\2\2\2O\u0133\3\2\2\2")
        buf.write("Q\u0138\3\2\2\2S\u013d\3\2\2\2U\u0147\3\2\2\2W\u014d\3")
        buf.write("\2\2\2Y\u0154\3\2\2\2[\u0156\3\2\2\2]\u015d\3\2\2\2_\u0161")
        buf.write("\3\2\2\2a\u0164\3\2\2\2c\u016d\3\2\2\2e\u016f\3\2\2\2")
        buf.write("g\u0171\3\2\2\2i\u017b\3\2\2\2k\u0182\3\2\2\2m\u018b\3")
        buf.write("\2\2\2o\u018f\3\2\2\2q\u0192\3\2\2\2s\u0197\3\2\2\2u\u019f")
        buf.write("\3\2\2\2w\u01a4\3\2\2\2y\u01ae\3\2\2\2{\u01b5\3\2\2\2")
        buf.write("}\u01bf\3\2\2\2\177\u01c8\3\2\2\2\u0081\u01cf\3\2\2\2")
        buf.write("\u0083\u01d1\3\2\2\2\u0085\u01db\3\2\2\2\u0087\u01e1\3")
        buf.write("\2\2\2\u0089\u01ee\3\2\2\2\u008b\u01fa\3\2\2\2\u008d\u0204")
        buf.write("\3\2\2\2\u008f\u0090\7}\2\2\u0090\4\3\2\2\2\u0091\u0092")
        buf.write("\7\177\2\2\u0092\6\3\2\2\2\u0093\u0094\7=\2\2\u0094\b")
        buf.write("\3\2\2\2\u0095\u0096\7.\2\2\u0096\n\3\2\2\2\u0097\u0098")
        buf.write("\7*\2\2\u0098\f\3\2\2\2\u0099\u009a\7+\2\2\u009a\16\3")
        buf.write("\2\2\2\u009b\u009c\7]\2\2\u009c\20\3\2\2\2\u009d\u009e")
        buf.write("\7_\2\2\u009e\22\3\2\2\2\u009f\u00a0\7(\2\2\u00a0\24\3")
        buf.write("\2\2\2\u00a1\u00a2\7~\2\2\u00a2\26\3\2\2\2\u00a3\u00a4")
        buf.write("\7?\2\2\u00a4\u00a5\7?\2\2\u00a5\30\3\2\2\2\u00a6\u00a7")
        buf.write("\7#\2\2\u00a7\u00a8\7?\2\2\u00a8\32\3\2\2\2\u00a9\u00aa")
        buf.write("\7@\2\2\u00aa\34\3\2\2\2\u00ab\u00ac\7>\2\2\u00ac\36\3")
        buf.write("\2\2\2\u00ad\u00ae\7@\2\2\u00ae\u00af\7?\2\2\u00af \3")
        buf.write("\2\2\2\u00b0\u00b1\7>\2\2\u00b1\u00b2\7?\2\2\u00b2\"\3")
        buf.write("\2\2\2\u00b3\u00b4\7-\2\2\u00b4$\3\2\2\2\u00b5\u00b6\7")
        buf.write("/\2\2\u00b6&\3\2\2\2\u00b7\u00b8\7,\2\2\u00b8(\3\2\2\2")
        buf.write("\u00b9\u00ba\7\61\2\2\u00ba*\3\2\2\2\u00bb\u00bc\7\'\2")
        buf.write("\2\u00bc,\3\2\2\2\u00bd\u00be\7#\2\2\u00be.\3\2\2\2\u00bf")
        buf.write("\u00c1\t\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\3")
        buf.write("\2\2\2\u00c4\u00c5\b\30\2\2\u00c5\60\3\2\2\2\u00c6\u00c7")
        buf.write("\7f\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7d\2\2\u00c9\u00ca")
        buf.write("\7w\2\2\u00ca\u00cb\7l\2\2\u00cb\u00cc\7q\2\2\u00cc\62")
        buf.write("\3\2\2\2\u00cd\u00ce\7o\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\u00d7\7u\2\2\u00d7\64\3\2\2\2\u00d8\u00d9")
        buf.write("\7n\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7c\2\2\u00db\u00dc")
        buf.write("\7o\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de\7f\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\66\3\2\2\2\u00e0\u00e1\7f\2\2\u00e1\u00e2")
        buf.write("\7g\2\2\u00e28\3\2\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7x\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8:\3\2\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed\7v\2\2\u00ed\u00ee")
        buf.write("\7c\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7i\2\2\u00f0\u00f1")
        buf.write("\7w\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7q\2\2\u00f3<\3")
        buf.write("\2\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7")
        buf.write("\7k\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa")
        buf.write("\7i\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd>\3\2\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7q\2\2\u0100\u0101\7l\2\2\u0101\u0102\7q\2\2\u0102@\3")
        buf.write("\2\2\2\u0103\u0104\7x\2\2\u0104\u0105\7g\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106\u0107\7f\2\2\u0107\u0108\7g\2\2\u0108B\3")
        buf.write("\2\2\2\u0109\u010a\7c\2\2\u010a\u010b\7o\2\2\u010b\u010c")
        buf.write("\7c\2\2\u010c\u010d\7t\2\2\u010d\u010e\7k\2\2\u010e\u010f")
        buf.write("\7n\2\2\u010f\u0110\7n\2\2\u0110\u0111\7q\2\2\u0111D\3")
        buf.write("\2\2\2\u0112\u0113\7c\2\2\u0113\u0114\7|\2\2\u0114\u0115")
        buf.write("\7w\2\2\u0115\u0116\7n\2\2\u0116F\3\2\2\2\u0117\u0118")
        buf.write("\7d\2\2\u0118\u0119\7n\2\2\u0119\u011a\7c\2\2\u011a\u011b")
        buf.write("\7p\2\2\u011b\u011c\7e\2\2\u011c\u011d\7q\2\2\u011dH\3")
        buf.write("\2\2\2\u011e\u011f\7p\2\2\u011f\u0120\7g\2\2\u0120\u0121")
        buf.write("\7i\2\2\u0121\u0122\7t\2\2\u0122\u0123\7q\2\2\u0123J\3")
        buf.write("\2\2\2\u0124\u0125\7o\2\2\u0125\u0126\7q\2\2\u0126\u0127")
        buf.write("\7t\2\2\u0127\u0128\7c\2\2\u0128\u0129\7f\2\2\u0129\u012a")
        buf.write("\7q\2\2\u012aL\3\2\2\2\u012b\u012c\7p\2\2\u012c\u012d")
        buf.write("\7c\2\2\u012d\u012e\7t\2\2\u012e\u012f\7c\2\2\u012f\u0130")
        buf.write("\7p\2\2\u0130\u0131\7l\2\2\u0131\u0132\7c\2\2\u0132N\3")
        buf.write("\2\2\2\u0133\u0134\7e\2\2\u0134\u0135\7c\2\2\u0135\u0136")
        buf.write("\7h\2\2\u0136\u0137\7g\2\2\u0137P\3\2\2\2\u0138\u0139")
        buf.write("\7i\2\2\u0139\u013a\7t\2\2\u013a\u013b\7k\2\2\u013b\u013c")
        buf.write("\7u\2\2\u013cR\3\2\2\2\u013d\u013e\7g\2\2\u013e\u013f")
        buf.write("\7u\2\2\u013f\u0140\7e\2\2\u0140\u0141\7g\2\2\u0141\u0142")
        buf.write("\7p\2\2\u0142\u0143\7c\2\2\u0143\u0144\7t\2\2\u0144\u0145")
        buf.write("\7k\2\2\u0145\u0146\7q\2\2\u0146T\3\2\2\2\u0147\u0148")
        buf.write("\7e\2\2\u0148\u0149\7q\2\2\u0149\u014a\7n\2\2\u014a\u014b")
        buf.write("\7q\2\2\u014b\u014c\7t\2\2\u014cV\3\2\2\2\u014d\u014e")
        buf.write("\7n\2\2\u014e\u014f\7k\2\2\u014f\u0150\7g\2\2\u0150\u0151")
        buf.write("\7p\2\2\u0151\u0152\7|\2\2\u0152\u0153\7q\2\2\u0153X\3")
        buf.write("\2\2\2\u0154\u0155\7?\2\2\u0155Z\3\2\2\2\u0156\u0157\7")
        buf.write("v\2\2\u0157\u0158\7c\2\2\u0158\u0159\7o\2\2\u0159\u015a")
        buf.write("\7c\2\2\u015a\u015b\7p\2\2\u015b\u015c\7q\2\2\u015c\\")
        buf.write("\3\2\2\2\u015d\u015e\7r\2\2\u015e\u015f\7q\2\2\u015f\u0160")
        buf.write("\7t\2\2\u0160^\3\2\2\2\u0161\u0162\7g\2\2\u0162\u0163")
        buf.write("\7p\2\2\u0163`\3\2\2\2\u0164\u0165\7r\2\2\u0165\u0166")
        buf.write("\7q\2\2\u0166\u0167\7u\2\2\u0167\u0168\7k\2\2\u0168\u0169")
        buf.write("\7e\2\2\u0169\u016a\7k\2\2\u016a\u016b\7q\2\2\u016b\u016c")
        buf.write("\7p\2\2\u016cb\3\2\2\2\u016d\u016e\7z\2\2\u016ed\3\2\2")
        buf.write("\2\u016f\u0170\7{\2\2\u0170f\3\2\2\2\u0171\u0172\7c\2")
        buf.write("\2\u0172\u0173\7p\2\2\u0173\u0174\7k\2\2\u0174\u0175\7")
        buf.write("o\2\2\u0175\u0176\7c\2\2\u0176\u0177\7e\2\2\u0177\u0178")
        buf.write("\7k\2\2\u0178\u0179\7q\2\2\u0179\u017a\7p\2\2\u017ah\3")
        buf.write("\2\2\2\u017b\u017c\7f\2\2\u017c\u017d\7q\2\2\u017d\u017e")
        buf.write("\7t\2\2\u017e\u017f\7o\2\2\u017f\u0180\7k\2\2\u0180\u0181")
        buf.write("\7t\2\2\u0181j\3\2\2\2\u0182\u0183\7o\2\2\u0183\u0184")
        buf.write("\7k\2\2\u0184\u0185\7g\2\2\u0185\u0186\7p\2\2\u0186\u0187")
        buf.write("\7v\2\2\u0187\u0188\7t\2\2\u0188\u0189\7c\2\2\u0189\u018a")
        buf.write("\7u\2\2\u018al\3\2\2\2\u018b\u018c\7s\2\2\u018c\u018d")
        buf.write("\7w\2\2\u018d\u018e\7g\2\2\u018en\3\2\2\2\u018f\u0190")
        buf.write("\7u\2\2\u0190\u0191\7k\2\2\u0191p\3\2\2\2\u0192\u0193")
        buf.write("\7u\2\2\u0193\u0194\7k\2\2\u0194\u0195\7p\2\2\u0195\u0196")
        buf.write("\7q\2\2\u0196r\3\2\2\2\u0197\u0198\7o\2\2\u0198\u0199")
        buf.write("\7g\2\2\u0199\u019a\7p\2\2\u019a\u019b\7u\2\2\u019b\u019c")
        buf.write("\7c\2\2\u019c\u019d\7l\2\2\u019d\u019e\7g\2\2\u019et\3")
        buf.write("\2\2\2\u019f\u01a0\7n\2\2\u01a0\u01a1\7g\2\2\u01a1\u01a2")
        buf.write("\7g\2\2\u01a2\u01a3\7t\2\2\u01a3v\3\2\2\2\u01a4\u01a5")
        buf.write("\7e\2\2\u01a5\u01a6\7q\2\2\u01a6\u01a7\7p\2\2\u01a7\u01a8")
        buf.write("\7f\2\2\u01a8\u01a9\7k\2\2\u01a9\u01aa\7e\2\2\u01aa\u01ab")
        buf.write("\7k\2\2\u01ab\u01ac\7q\2\2\u01ac\u01ad\7p\2\2\u01adx\3")
        buf.write("\2\2\2\u01ae\u01af\7p\2\2\u01af\u01b0\7w\2\2\u01b0\u01b1")
        buf.write("\7o\2\2\u01b1\u01b2\7g\2\2\u01b2\u01b3\7t\2\2\u01b3\u01b4")
        buf.write("\7q\2\2\u01b4z\3\2\2\2\u01b5\u01b6\7h\2\2\u01b6\u01b7")
        buf.write("\7w\2\2\u01b7\u01b8\7p\2\2\u01b8\u01b9\7e\2\2\u01b9\u01ba")
        buf.write("\7k\2\2\u01ba\u01bb\7q\2\2\u01bb\u01bc\7p\2\2\u01bc\u01bd")
        buf.write("\7g\2\2\u01bd\u01be\7u\2\2\u01be|\3\2\2\2\u01bf\u01c0")
        buf.write("\7g\2\2\u01c0\u01c1\7u\2\2\u01c1\u01c2\7e\2\2\u01c2\u01c3")
        buf.write("\7t\2\2\u01c3\u01c4\7k\2\2\u01c4\u01c5\7d\2\2\u01c5\u01c6")
        buf.write("\7k\2\2\u01c6\u01c7\7t\2\2\u01c7~\3\2\2\2\u01c8\u01c9")
        buf.write("\7p\2\2\u01c9\u01ca\7c\2\2\u01ca\u01cb\7f\2\2\u01cb\u01cc")
        buf.write("\7c\2\2\u01cc\u0080\3\2\2\2\u01cd\u01d0\5\u0083B\2\u01ce")
        buf.write("\u01d0\5\u0085C\2\u01cf\u01cd\3\2\2\2\u01cf\u01ce\3\2")
        buf.write("\2\2\u01d0\u0082\3\2\2\2\u01d1\u01d2\7x\2\2\u01d2\u01d3")
        buf.write("\7g\2\2\u01d3\u01d4\7t\2\2\u01d4\u01d5\7f\2\2\u01d5\u01d6")
        buf.write("\7c\2\2\u01d6\u01d7\7f\2\2\u01d7\u01d8\7g\2\2\u01d8\u01d9")
        buf.write("\7t\2\2\u01d9\u01da\7q\2\2\u01da\u0084\3\2\2\2\u01db\u01dc")
        buf.write("\7h\2\2\u01dc\u01dd\7c\2\2\u01dd\u01de\7n\2\2\u01de\u01df")
        buf.write("\7u\2\2\u01df\u01e0\7q\2\2\u01e0\u0086\3\2\2\2\u01e1\u01e2")
        buf.write("\7o\2\2\u01e2\u01e3\7q\2\2\u01e3\u01e4\7f\2\2\u01e4\u01e5")
        buf.write("\7k\2\2\u01e5\u01e6\7h\2\2\u01e6\u01e7\7k\2\2\u01e7\u01e8")
        buf.write("\7e\2\2\u01e8\u01e9\7c\2\2\u01e9\u01ea\7d\2\2\u01ea\u01eb")
        buf.write("\7n\2\2\u01eb\u01ec\7g\2\2\u01ec\u0088\3\2\2\2\u01ed\u01ef")
        buf.write("\t\3\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f8\3\2\2\2")
        buf.write("\u01f2\u01f4\7\60\2\2\u01f3\u01f5\t\3\2\2\u01f4\u01f3")
        buf.write("\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6")
        buf.write("\u01f7\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8\u01f2\3\2\2\2")
        buf.write("\u01f8\u01f9\3\2\2\2\u01f9\u008a\3\2\2\2\u01fa\u01fe\7")
        buf.write("$\2\2\u01fb\u01fd\n\4\2\2\u01fc\u01fb\3\2\2\2\u01fd\u0200")
        buf.write("\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0201\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0202\7$\2\2")
        buf.write("\u0202\u008c\3\2\2\2\u0203\u0205\t\5\2\2\u0204\u0203\3")
        buf.write("\2\2\2\u0205\u0206\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207")
        buf.write("\3\2\2\2\u0207\u008e\3\2\2\2\n\2\u00c2\u01cf\u01f0\u01f6")
        buf.write("\u01f8\u01fe\u0206\3\b\2\2")
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
    T__20 = 21
    T__21 = 22
    WS = 23
    DIBUJO = 24
    MATERIALES = 25
    LLAMADO = 26
    DE = 27
    OVALO = 28
    RECTANGULO = 29
    TRIANGULO = 30
    ROJO = 31
    VERDE = 32
    AMARILLO = 33
    AZUL = 34
    BLANCO = 35
    NEGRO = 36
    MORADO = 37
    NARANJA = 38
    CAFE = 39
    GRIS = 40
    ESCENARIO = 41
    COLOR = 42
    LIENZO = 43
    EQUALS = 44
    TAMANO = 45
    POR = 46
    EN = 47
    POSICION = 48
    X = 49
    Y = 50
    ANIMACION = 51
    DORMIR = 52
    MIENTRAS = 53
    QUE = 54
    SI = 55
    SINO = 56
    MENSAJE = 57
    LEER = 58
    CONDICION = 59
    NUMERO = 60
    FUNCIONES = 61
    ESCRIBIR = 62
    NADA = 63
    CONDITION_CONSTANT = 64
    VERDADERO = 65
    FALSO = 66
    MODIFICABLE = 67
    NUMERIC_CONSTANT = 68
    STRING_CONSTANT = 69
    ID = 70

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "';'", "','", "'('", "')'", "'['", "']'", "'&'", 
            "'|'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'dibujo'", "'materiales'", 
            "'llamado'", "'de'", "'ovalo'", "'rectangulo'", "'triangulo'", 
            "'rojo'", "'verde'", "'amarillo'", "'azul'", "'blanco'", "'negro'", 
            "'morado'", "'naranja'", "'cafe'", "'gris'", "'escenario'", 
            "'color'", "'lienzo'", "'='", "'tamano'", "'por'", "'en'", "'posicion'", 
            "'x'", "'y'", "'animacion'", "'dormir'", "'mientras'", "'que'", 
            "'si'", "'sino'", "'mensaje'", "'leer'", "'condicion'", "'numero'", 
            "'funciones'", "'escribir'", "'nada'", "'verdadero'", "'falso'", 
            "'modificable'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "DIBUJO", "MATERIALES", "LLAMADO", "DE", "OVALO", "RECTANGULO", 
            "TRIANGULO", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", 
            "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", "ESCENARIO", "COLOR", 
            "LIENZO", "EQUALS", "TAMANO", "POR", "EN", "POSICION", "X", 
            "Y", "ANIMACION", "DORMIR", "MIENTRAS", "QUE", "SI", "SINO", 
            "MENSAJE", "LEER", "CONDICION", "NUMERO", "FUNCIONES", "ESCRIBIR", 
            "NADA", "CONDITION_CONSTANT", "VERDADERO", "FALSO", "MODIFICABLE", 
            "NUMERIC_CONSTANT", "STRING_CONSTANT", "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "WS", "DIBUJO", "MATERIALES", "LLAMADO", 
                  "DE", "OVALO", "RECTANGULO", "TRIANGULO", "ROJO", "VERDE", 
                  "AMARILLO", "AZUL", "BLANCO", "NEGRO", "MORADO", "NARANJA", 
                  "CAFE", "GRIS", "ESCENARIO", "COLOR", "LIENZO", "EQUALS", 
                  "TAMANO", "POR", "EN", "POSICION", "X", "Y", "ANIMACION", 
                  "DORMIR", "MIENTRAS", "QUE", "SI", "SINO", "MENSAJE", 
                  "LEER", "CONDICION", "NUMERO", "FUNCIONES", "ESCRIBIR", 
                  "NADA", "CONDITION_CONSTANT", "VERDADERO", "FALSO", "MODIFICABLE", 
                  "NUMERIC_CONSTANT", "STRING_CONSTANT", "ID" ]

    grammarFileName = "Lienzo.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


