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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2E")
        buf.write("\u01fa\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\6\26")
        buf.write("\u00b7\n\26\r\26\16\26\u00b8\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\38\38\38\38\39\39\39\39\39\39")
        buf.write("\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\3>\3>\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\5@\u01d0\n@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3")
        buf.write("A\3A\3B\6B\u01df\nB\rB\16B\u01e0\3B\3B\6B\u01e5\nB\rB")
        buf.write("\16B\u01e6\5B\u01e9\nB\3C\3C\7C\u01ed\nC\fC\16C\u01f0")
        buf.write("\13C\3C\3C\3D\3D\7D\u01f6\nD\fD\16D\u01f9\13D\2\2E\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w")
        buf.write("=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\3\2\7\5\2\13")
        buf.write("\f\17\17\"\"\3\2\62;\3\2$$\4\2C\\c|\5\2\62;C\\c|\u0200")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u0089\3\2\2")
        buf.write("\2\5\u008b\3\2\2\2\7\u008d\3\2\2\2\t\u008f\3\2\2\2\13")
        buf.write("\u0091\3\2\2\2\r\u0093\3\2\2\2\17\u0095\3\2\2\2\21\u0097")
        buf.write("\3\2\2\2\23\u0099\3\2\2\2\25\u009c\3\2\2\2\27\u009f\3")
        buf.write("\2\2\2\31\u00a1\3\2\2\2\33\u00a3\3\2\2\2\35\u00a6\3\2")
        buf.write("\2\2\37\u00a9\3\2\2\2!\u00ab\3\2\2\2#\u00ad\3\2\2\2%\u00af")
        buf.write("\3\2\2\2\'\u00b1\3\2\2\2)\u00b3\3\2\2\2+\u00b6\3\2\2\2")
        buf.write("-\u00bc\3\2\2\2/\u00c3\3\2\2\2\61\u00c8\3\2\2\2\63\u00ce")
        buf.write("\3\2\2\2\65\u00d7\3\2\2\2\67\u00dc\3\2\2\29\u00e3\3\2")
        buf.write("\2\2;\u00e9\3\2\2\2=\u00f0\3\2\2\2?\u00f8\3\2\2\2A\u00fd")
        buf.write("\3\2\2\2C\u0102\3\2\2\2E\u0108\3\2\2\2G\u010f\3\2\2\2")
        buf.write("I\u0111\3\2\2\2K\u0118\3\2\2\2M\u011c\3\2\2\2O\u011f\3")
        buf.write("\2\2\2Q\u0122\3\2\2\2S\u0128\3\2\2\2U\u0131\3\2\2\2W\u0137")
        buf.write("\3\2\2\2Y\u013d\3\2\2\2[\u0145\3\2\2\2]\u014f\3\2\2\2")
        buf.write("_\u0158\3\2\2\2a\u015e\3\2\2\2c\u0164\3\2\2\2e\u016b\3")
        buf.write("\2\2\2g\u0172\3\2\2\2i\u017b\3\2\2\2k\u0184\3\2\2\2m\u0188")
        buf.write("\3\2\2\2o\u018b\3\2\2\2q\u0190\3\2\2\2s\u0196\3\2\2\2")
        buf.write("u\u019b\3\2\2\2w\u01a3\3\2\2\2y\u01aa\3\2\2\2{\u01b3\3")
        buf.write("\2\2\2}\u01bc\3\2\2\2\177\u01cf\3\2\2\2\u0081\u01d1\3")
        buf.write("\2\2\2\u0083\u01de\3\2\2\2\u0085\u01ea\3\2\2\2\u0087\u01f3")
        buf.write("\3\2\2\2\u0089\u008a\7=\2\2\u008a\4\3\2\2\2\u008b\u008c")
        buf.write("\7*\2\2\u008c\6\3\2\2\2\u008d\u008e\7.\2\2\u008e\b\3\2")
        buf.write("\2\2\u008f\u0090\7+\2\2\u0090\n\3\2\2\2\u0091\u0092\7")
        buf.write("}\2\2\u0092\f\3\2\2\2\u0093\u0094\7\177\2\2\u0094\16\3")
        buf.write("\2\2\2\u0095\u0096\7(\2\2\u0096\20\3\2\2\2\u0097\u0098")
        buf.write("\7~\2\2\u0098\22\3\2\2\2\u0099\u009a\7?\2\2\u009a\u009b")
        buf.write("\7?\2\2\u009b\24\3\2\2\2\u009c\u009d\7#\2\2\u009d\u009e")
        buf.write("\7?\2\2\u009e\26\3\2\2\2\u009f\u00a0\7@\2\2\u00a0\30\3")
        buf.write("\2\2\2\u00a1\u00a2\7>\2\2\u00a2\32\3\2\2\2\u00a3\u00a4")
        buf.write("\7@\2\2\u00a4\u00a5\7?\2\2\u00a5\34\3\2\2\2\u00a6\u00a7")
        buf.write("\7>\2\2\u00a7\u00a8\7?\2\2\u00a8\36\3\2\2\2\u00a9\u00aa")
        buf.write("\7-\2\2\u00aa \3\2\2\2\u00ab\u00ac\7/\2\2\u00ac\"\3\2")
        buf.write("\2\2\u00ad\u00ae\7,\2\2\u00ae$\3\2\2\2\u00af\u00b0\7\61")
        buf.write("\2\2\u00b0&\3\2\2\2\u00b1\u00b2\7\'\2\2\u00b2(\3\2\2\2")
        buf.write("\u00b3\u00b4\7#\2\2\u00b4*\3\2\2\2\u00b5\u00b7\t\2\2\2")
        buf.write("\u00b6\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b6\3")
        buf.write("\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb")
        buf.write("\b\26\2\2\u00bb,\3\2\2\2\u00bc\u00bd\7i\2\2\u00bd\u00be")
        buf.write("\7n\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7d\2\2\u00c0\u00c1")
        buf.write("\7c\2\2\u00c1\u00c2\7n\2\2\u00c2.\3\2\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7l\2\2\u00c6\u00c7")
        buf.write("\7q\2\2\u00c7\60\3\2\2\2\u00c8\u00c9\7x\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7f\2\2\u00cc\u00cd")
        buf.write("\7g\2\2\u00cd\62\3\2\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0")
        buf.write("\7o\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\64\3\2\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9")
        buf.write("\7|\2\2\u00d9\u00da\7w\2\2\u00da\u00db\7n\2\2\u00db\66")
        buf.write("\3\2\2\2\u00dc\u00dd\7d\2\2\u00dd\u00de\7n\2\2\u00de\u00df")
        buf.write("\7c\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7e\2\2\u00e1\u00e2")
        buf.write("\7q\2\2\u00e28\3\2\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5")
        buf.write("\7g\2\2\u00e5\u00e6\7i\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8:\3\2\2\2\u00e9\u00ea\7o\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee")
        buf.write("\7f\2\2\u00ee\u00ef\7q\2\2\u00ef<\3\2\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4")
        buf.write("\7c\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7l\2\2\u00f6\u00f7")
        buf.write("\7c\2\2\u00f7>\3\2\2\2\u00f8\u00f9\7e\2\2\u00f9\u00fa")
        buf.write("\7c\2\2\u00fa\u00fb\7h\2\2\u00fb\u00fc\7g\2\2\u00fc@\3")
        buf.write("\2\2\2\u00fd\u00fe\7i\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7u\2\2\u0101B\3\2\2\2\u0102\u0103")
        buf.write("\7e\2\2\u0103\u0104\7q\2\2\u0104\u0105\7n\2\2\u0105\u0106")
        buf.write("\7q\2\2\u0106\u0107\7t\2\2\u0107D\3\2\2\2\u0108\u0109")
        buf.write("\7n\2\2\u0109\u010a\7k\2\2\u010a\u010b\7g\2\2\u010b\u010c")
        buf.write("\7p\2\2\u010c\u010d\7|\2\2\u010d\u010e\7q\2\2\u010eF\3")
        buf.write("\2\2\2\u010f\u0110\7?\2\2\u0110H\3\2\2\2\u0111\u0112\7")
        buf.write("v\2\2\u0112\u0113\7c\2\2\u0113\u0114\7o\2\2\u0114\u0115")
        buf.write("\7c\2\2\u0115\u0116\7p\2\2\u0116\u0117\7q\2\2\u0117J\3")
        buf.write("\2\2\2\u0118\u0119\7r\2\2\u0119\u011a\7q\2\2\u011a\u011b")
        buf.write("\7t\2\2\u011bL\3\2\2\2\u011c\u011d\7f\2\2\u011d\u011e")
        buf.write("\7g\2\2\u011eN\3\2\2\2\u011f\u0120\7g\2\2\u0120\u0121")
        buf.write("\7p\2\2\u0121P\3\2\2\2\u0122\u0123\7o\2\2\u0123\u0124")
        buf.write("\7q\2\2\u0124\u0125\7x\2\2\u0125\u0126\7g\2\2\u0126\u0127")
        buf.write("\7t\2\2\u0127R\3\2\2\2\u0128\u0129\7c\2\2\u0129\u012a")
        buf.write("\7f\2\2\u012a\u012b\7g\2\2\u012b\u012c\7n\2\2\u012c\u012d")
        buf.write("\7c\2\2\u012d\u012e\7p\2\2\u012e\u012f\7v\2\2\u012f\u0130")
        buf.write("\7g\2\2\u0130T\3\2\2\2\u0131\u0132\7c\2\2\u0132\u0133")
        buf.write("\7v\2\2\u0133\u0134\7t\2\2\u0134\u0135\7c\2\2\u0135\u0136")
        buf.write("\7u\2\2\u0136V\3\2\2\2\u0137\u0138\7i\2\2\u0138\u0139")
        buf.write("\7k\2\2\u0139\u013a\7t\2\2\u013a\u013b\7c\2\2\u013b\u013c")
        buf.write("\7t\2\2\u013cX\3\2\2\2\u013d\u013e\7f\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7t\2\2\u0140\u0141\7g\2\2\u0141\u0142")
        buf.write("\7e\2\2\u0142\u0143\7j\2\2\u0143\u0144\7c\2\2\u0144Z\3")
        buf.write("\2\2\2\u0145\u0146\7k\2\2\u0146\u0147\7|\2\2\u0147\u0148")
        buf.write("\7s\2\2\u0148\u0149\7w\2\2\u0149\u014a\7k\2\2\u014a\u014b")
        buf.write("\7g\2\2\u014b\u014c\7t\2\2\u014c\u014d\7f\2\2\u014d\u014e")
        buf.write("\7c\2\2\u014e\\\3\2\2\2\u014f\u0150\7n\2\2\u0150\u0151")
        buf.write("\7g\2\2\u0151\u0152\7x\2\2\u0152\u0153\7c\2\2\u0153\u0154")
        buf.write("\7p\2\2\u0154\u0155\7v\2\2\u0155\u0156\7c\2\2\u0156\u0157")
        buf.write("\7t\2\2\u0157^\3\2\2\2\u0158\u0159\7d\2\2\u0159\u015a")
        buf.write("\7c\2\2\u015a\u015b\7l\2\2\u015b\u015c\7c\2\2\u015c\u015d")
        buf.write("\7t\2\2\u015d`\3\2\2\2\u015e\u015f\7r\2\2\u015f\u0160")
        buf.write("\7n\2\2\u0160\u0161\7w\2\2\u0161\u0162\7o\2\2\u0162\u0163")
        buf.write("\7c\2\2\u0163b\3\2\2\2\u0164\u0165\7f\2\2\u0165\u0166")
        buf.write("\7k\2\2\u0166\u0167\7d\2\2\u0167\u0168\7w\2\2\u0168\u0169")
        buf.write("\7l\2\2\u0169\u016a\7q\2\2\u016ad\3\2\2\2\u016b\u016c")
        buf.write("\7f\2\2\u016c\u016d\7q\2\2\u016d\u016e\7t\2\2\u016e\u016f")
        buf.write("\7o\2\2\u016f\u0170\7k\2\2\u0170\u0171\7t\2\2\u0171f\3")
        buf.write("\2\2\2\u0172\u0173\7o\2\2\u0173\u0174\7k\2\2\u0174\u0175")
        buf.write("\7g\2\2\u0175\u0176\7p\2\2\u0176\u0177\7v\2\2\u0177\u0178")
        buf.write("\7t\2\2\u0178\u0179\7c\2\2\u0179\u017a\7u\2\2\u017ah\3")
        buf.write("\2\2\2\u017b\u017c\7t\2\2\u017c\u017d\7g\2\2\u017d\u017e")
        buf.write("\7i\2\2\u017e\u017f\7t\2\2\u017f\u0180\7g\2\2\u0180\u0181")
        buf.write("\7u\2\2\u0181\u0182\7c\2\2\u0182\u0183\7t\2\2\u0183j\3")
        buf.write("\2\2\2\u0184\u0185\7s\2\2\u0185\u0186\7w\2\2\u0186\u0187")
        buf.write("\7g\2\2\u0187l\3\2\2\2\u0188\u0189\7u\2\2\u0189\u018a")
        buf.write("\7k\2\2\u018an\3\2\2\2\u018b\u018c\7u\2\2\u018c\u018d")
        buf.write("\7k\2\2\u018d\u018e\7p\2\2\u018e\u018f\7q\2\2\u018fp\3")
        buf.write("\2\2\2\u0190\u0191\7v\2\2\u0191\u0192\7g\2\2\u0192\u0193")
        buf.write("\7z\2\2\u0193\u0194\7v\2\2\u0194\u0195\7q\2\2\u0195r\3")
        buf.write("\2\2\2\u0196\u0197\7n\2\2\u0197\u0198\7g\2\2\u0198\u0199")
        buf.write("\7g\2\2\u0199\u019a\7t\2\2\u019at\3\2\2\2\u019b\u019c")
        buf.write("\7d\2\2\u019c\u019d\7q\2\2\u019d\u019e\7n\2\2\u019e\u019f")
        buf.write("\7g\2\2\u019f\u01a0\7c\2\2\u01a0\u01a1\7p\2\2\u01a1\u01a2")
        buf.write("\7q\2\2\u01a2v\3\2\2\2\u01a3\u01a4\7p\2\2\u01a4\u01a5")
        buf.write("\7w\2\2\u01a5\u01a6\7o\2\2\u01a6\u01a7\7g\2\2\u01a7\u01a8")
        buf.write("\7t\2\2\u01a8\u01a9\7q\2\2\u01a9x\3\2\2\2\u01aa\u01ab")
        buf.write("\7g\2\2\u01ab\u01ac\7u\2\2\u01ac\u01ad\7e\2\2\u01ad\u01ae")
        buf.write("\7t\2\2\u01ae\u01af\7k\2\2\u01af\u01b0\7d\2\2\u01b0\u01b1")
        buf.write("\7k\2\2\u01b1\u01b2\7t\2\2\u01b2z\3\2\2\2\u01b3\u01b4")
        buf.write("\7k\2\2\u01b4\u01b5\7o\2\2\u01b5\u01b6\7r\2\2\u01b6\u01b7")
        buf.write("\7t\2\2\u01b7\u01b8\7k\2\2\u01b8\u01b9\7o\2\2\u01b9\u01ba")
        buf.write("\7k\2\2\u01ba\u01bb\7t\2\2\u01bb|\3\2\2\2\u01bc\u01bd")
        buf.write("\7p\2\2\u01bd\u01be\7c\2\2\u01be\u01bf\7f\2\2\u01bf\u01c0")
        buf.write("\7c\2\2\u01c0~\3\2\2\2\u01c1\u01c2\7x\2\2\u01c2\u01c3")
        buf.write("\7g\2\2\u01c3\u01c4\7t\2\2\u01c4\u01c5\7f\2\2\u01c5\u01c6")
        buf.write("\7c\2\2\u01c6\u01c7\7f\2\2\u01c7\u01c8\7g\2\2\u01c8\u01c9")
        buf.write("\7t\2\2\u01c9\u01d0\7q\2\2\u01ca\u01cb\7h\2\2\u01cb\u01cc")
        buf.write("\7c\2\2\u01cc\u01cd\7n\2\2\u01cd\u01ce\7u\2\2\u01ce\u01d0")
        buf.write("\7q\2\2\u01cf\u01c1\3\2\2\2\u01cf\u01ca\3\2\2\2\u01d0")
        buf.write("\u0080\3\2\2\2\u01d1\u01d2\7o\2\2\u01d2\u01d3\7q\2\2\u01d3")
        buf.write("\u01d4\7f\2\2\u01d4\u01d5\7k\2\2\u01d5\u01d6\7h\2\2\u01d6")
        buf.write("\u01d7\7k\2\2\u01d7\u01d8\7e\2\2\u01d8\u01d9\7c\2\2\u01d9")
        buf.write("\u01da\7d\2\2\u01da\u01db\7n\2\2\u01db\u01dc\7g\2\2\u01dc")
        buf.write("\u0082\3\2\2\2\u01dd\u01df\t\3\2\2\u01de\u01dd\3\2\2\2")
        buf.write("\u01df\u01e0\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3")
        buf.write("\2\2\2\u01e1\u01e8\3\2\2\2\u01e2\u01e4\7\60\2\2\u01e3")
        buf.write("\u01e5\t\3\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2")
        buf.write("\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e9\3")
        buf.write("\2\2\2\u01e8\u01e2\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u0084")
        buf.write("\3\2\2\2\u01ea\u01ee\7$\2\2\u01eb\u01ed\n\4\2\2\u01ec")
        buf.write("\u01eb\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2")
        buf.write("\u01ee\u01ef\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01ee\3")
        buf.write("\2\2\2\u01f1\u01f2\7$\2\2\u01f2\u0086\3\2\2\2\u01f3\u01f7")
        buf.write("\t\5\2\2\u01f4\u01f6\t\6\2\2\u01f5\u01f4\3\2\2\2\u01f6")
        buf.write("\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u0088\3\2\2\2\u01f9\u01f7\3\2\2\2\n\2\u00b8\u01cf")
        buf.write("\u01e0\u01e6\u01e8\u01ee\u01f7\3\b\2\2")
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
    REGRESAR = 52
    QUE = 53
    SI = 54
    SINO = 55
    TEXTO = 56
    LEER = 57
    BOLEANO = 58
    NUMERO = 59
    ESCRIBIR = 60
    IMPRIMIR = 61
    NADA = 62
    BOOLEAN_CONSTANT = 63
    MODIFICABLE = 64
    NUMERIC_CONSTANT = 65
    STRING_CONSTANT = 66
    ID = 67

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'('", "','", "')'", "'{'", "'}'", "'&'", "'|'", "'=='", 
            "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'global'", "'rojo'", "'verde'", "'amarillo'", 
            "'azul'", "'blanco'", "'negro'", "'morado'", "'naranja'", "'cafe'", 
            "'gris'", "'color'", "'lienzo'", "'='", "'tamano'", "'por'", 
            "'de'", "'en'", "'mover'", "'adelante'", "'atras'", "'girar'", 
            "'derecha'", "'izquierda'", "'levantar'", "'bajar'", "'pluma'", 
            "'dibujo'", "'dormir'", "'mientras'", "'regresar'", "'que'", 
            "'si'", "'sino'", "'texto'", "'leer'", "'boleano'", "'numero'", 
            "'escribir'", "'imprimir'", "'nada'", "'modificable'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "GLOBAL", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", 
            "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", "LIENZO", 
            "EQUALS", "TAMANO", "POR", "DE", "EN", "MOVER", "ADELANTE", 
            "ATRAS", "GIRAR", "DERECHA", "IZQUIERDA", "LEVANTAR", "BAJAR", 
            "PLUMA", "DIBUJO", "DORMIR", "MIENTRAS", "REGRESAR", "QUE", 
            "SI", "SINO", "TEXTO", "LEER", "BOLEANO", "NUMERO", "ESCRIBIR", 
            "IMPRIMIR", "NADA", "BOOLEAN_CONSTANT", "MODIFICABLE", "NUMERIC_CONSTANT", 
            "STRING_CONSTANT", "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "WS", "GLOBAL", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", 
                  "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", "COLOR", 
                  "LIENZO", "EQUALS", "TAMANO", "POR", "DE", "EN", "MOVER", 
                  "ADELANTE", "ATRAS", "GIRAR", "DERECHA", "IZQUIERDA", 
                  "LEVANTAR", "BAJAR", "PLUMA", "DIBUJO", "DORMIR", "MIENTRAS", 
                  "REGRESAR", "QUE", "SI", "SINO", "TEXTO", "LEER", "BOLEANO", 
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


