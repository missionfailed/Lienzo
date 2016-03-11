# Generated from Lienzo.g4 by ANTLR 4.5.2
# encoding: utf-8
from antlr4 import *
from io import StringIO


from namespace import NamespaceTable
import sys

namespaceTable = NamespaceTable()
currentFunctionName = ""

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3G")
        buf.write("\u0153\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\7\3Q\n\3\f\3\16\3T\13\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7")
        buf.write("\7r\n\7\f\7\16\7u\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\7\r\u0097")
        buf.write("\n\r\f\r\16\r\u009a\13\r\3\r\7\r\u009d\n\r\f\r\16\r\u00a0")
        buf.write("\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00b1\n\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\7\24\u00cd\n\24\f\24\16\24\u00d0\13\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\5\26\u00df\n\26\3\27\3\27\3\27\3\27\3\27\3\27\7")
        buf.write("\27\u00e7\n\27\f\27\16\27\u00ea\13\27\3\27\3\27\3\27\3")
        buf.write("\27\7\27\u00f0\n\27\f\27\16\27\u00f3\13\27\3\27\5\27\u00f6")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\7\30\u00fd\n\30\f\30\16")
        buf.write("\30\u0100\13\30\5\30\u0102\n\30\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\5\31\u010a\n\31\3\32\3\32\3\32\5\32\u010f\n\32")
        buf.write("\3\33\5\33\u0112\n\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u011e\n\33\3\34\3\34\3\34\5\34")
        buf.write("\u0123\n\34\3\35\3\35\3\35\5\35\u0128\n\35\3\36\3\36\3")
        buf.write("\36\7\36\u012d\n\36\f\36\16\36\u0130\13\36\3\36\3\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3")
        buf.write(" \5 \u0140\n \3!\3!\3!\7!\u0145\n!\f!\16!\u0148\13!\5")
        buf.write("!\u014a\n!\3\"\3\"\5\"\u014e\n\"\3\"\3\"\3\"\3\"\2\2#")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@B\2\13\3\2\36 \3\2!*\3\2\63\64\3\2;=\4\2EE")
        buf.write("GG\3\2\13\f\3\2\r\17\3\2\21\26\3\2\27\30\u0153\2D\3\2")
        buf.write("\2\2\4M\3\2\2\2\6W\3\2\2\2\bd\3\2\2\2\nf\3\2\2\2\fh\3")
        buf.write("\2\2\2\16x\3\2\2\2\20~\3\2\2\2\22\u0086\3\2\2\2\24\u008d")
        buf.write("\3\2\2\2\26\u008f\3\2\2\2\30\u0098\3\2\2\2\32\u00a1\3")
        buf.write("\2\2\2\34\u00b0\3\2\2\2\36\u00b4\3\2\2\2 \u00b9\3\2\2")
        buf.write("\2\"\u00bb\3\2\2\2$\u00c2\3\2\2\2&\u00c5\3\2\2\2(\u00d3")
        buf.write("\3\2\2\2*\u00d9\3\2\2\2,\u00e0\3\2\2\2.\u00f7\3\2\2\2")
        buf.write("\60\u0106\3\2\2\2\62\u010b\3\2\2\2\64\u0111\3\2\2\2\66")
        buf.write("\u011f\3\2\2\28\u0124\3\2\2\2:\u0129\3\2\2\2<\u0133\3")
        buf.write("\2\2\2>\u013f\3\2\2\2@\u0149\3\2\2\2B\u014b\3\2\2\2DE")
        buf.write("\7\32\2\2EF\7\3\2\2FG\5\4\3\2GH\5\f\7\2HI\5:\36\2IJ\5")
        buf.write("\26\f\2JK\7\4\2\2KL\7\2\2\3L\3\3\2\2\2MN\7\33\2\2NR\7")
        buf.write("\3\2\2OQ\5\6\4\2PO\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2")
        buf.write("\2SU\3\2\2\2TR\3\2\2\2UV\7\4\2\2V\5\3\2\2\2WX\7D\2\2X")
        buf.write("Y\5\b\5\2YZ\5\n\6\2Z[\7\34\2\2[\\\7F\2\2\\]\7\35\2\2]")
        buf.write("^\5\60\31\2^_\7\60\2\2_`\5\60\31\2`a\7\5\2\2ab\3\2\2\2")
        buf.write("bc\b\4\1\2c\7\3\2\2\2de\t\2\2\2e\t\3\2\2\2fg\t\3\2\2g")
        buf.write("\13\3\2\2\2hi\7+\2\2ij\7\3\2\2jk\5\16\b\2kl\7\5\2\2lm")
        buf.write("\5\20\t\2ms\7\5\2\2no\5\22\n\2op\7\5\2\2pr\3\2\2\2qn\3")
        buf.write("\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2")
        buf.write("\2vw\7\4\2\2w\r\3\2\2\2xy\7,\2\2yz\7\35\2\2z{\7-\2\2{")
        buf.write("|\7.\2\2|}\5\n\6\2}\17\3\2\2\2~\177\7/\2\2\177\u0080\7")
        buf.write("\35\2\2\u0080\u0081\7-\2\2\u0081\u0082\7.\2\2\u0082\u0083")
        buf.write("\5\60\31\2\u0083\u0084\7\60\2\2\u0084\u0085\5\60\31\2")
        buf.write("\u0085\21\3\2\2\2\u0086\u0087\7\62\2\2\u0087\u0088\5\24")
        buf.write("\13\2\u0088\u0089\7\35\2\2\u0089\u008a\5*\26\2\u008a\u008b")
        buf.write("\7.\2\2\u008b\u008c\5\60\31\2\u008c\23\3\2\2\2\u008d\u008e")
        buf.write("\t\4\2\2\u008e\25\3\2\2\2\u008f\u0090\7\65\2\2\u0090\u0091")
        buf.write("\b\f\1\2\u0091\u0092\7\3\2\2\u0092\u0093\5\30\r\2\u0093")
        buf.write("\u0094\7\4\2\2\u0094\27\3\2\2\2\u0095\u0097\5\32\16\2")
        buf.write("\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0096\3")
        buf.write("\2\2\2\u0098\u0099\3\2\2\2\u0099\u009e\3\2\2\2\u009a\u0098")
        buf.write("\3\2\2\2\u009b\u009d\5\34\17\2\u009c\u009b\3\2\2\2\u009d")
        buf.write("\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\31\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a2\5 \21")
        buf.write("\2\u00a2\u00a3\7G\2\2\u00a3\u00a4\7.\2\2\u00a4\u00a5\5")
        buf.write("8\35\2\u00a5\u00a6\7\5\2\2\u00a6\u00a7\b\16\1\2\u00a7")
        buf.write("\33\3\2\2\2\u00a8\u00b1\5\36\20\2\u00a9\u00b1\5\"\22\2")
        buf.write("\u00aa\u00b1\5$\23\2\u00ab\u00b1\5&\24\2\u00ac\u00b1\5")
        buf.write("(\25\2\u00ad\u00b1\5\22\n\2\u00ae\u00b1\5,\27\2\u00af")
        buf.write("\u00b1\5.\30\2\u00b0\u00a8\3\2\2\2\u00b0\u00a9\3\2\2\2")
        buf.write("\u00b0\u00aa\3\2\2\2\u00b0\u00ab\3\2\2\2\u00b0\u00ac\3")
        buf.write("\2\2\2\u00b0\u00ad\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\7\5\2\2\u00b3")
        buf.write("\35\3\2\2\2\u00b4\u00b5\7G\2\2\u00b5\u00b6\7.\2\2\u00b6")
        buf.write("\u00b7\58\35\2\u00b7\u00b8\b\20\1\2\u00b8\37\3\2\2\2\u00b9")
        buf.write("\u00ba\t\5\2\2\u00ba!\3\2\2\2\u00bb\u00bc\7?\2\2\u00bc")
        buf.write("\u00bd\t\6\2\2\u00bd\u00be\7\61\2\2\u00be\u00bf\5\60\31")
        buf.write("\2\u00bf\u00c0\7\6\2\2\u00c0\u00c1\5\60\31\2\u00c1#\3")
        buf.write("\2\2\2\u00c2\u00c3\7\66\2\2\u00c3\u00c4\5\60\31\2\u00c4")
        buf.write("%\3\2\2\2\u00c5\u00c6\7\67\2\2\u00c6\u00c7\78\2\2\u00c7")
        buf.write("\u00c8\7\7\2\2\u00c8\u00c9\58\35\2\u00c9\u00ca\7\b\2\2")
        buf.write("\u00ca\u00ce\7\3\2\2\u00cb\u00cd\5\34\17\2\u00cc\u00cb")
        buf.write("\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00ce\3\2\2\2")
        buf.write("\u00d1\u00d2\7\4\2\2\u00d2\'\3\2\2\2\u00d3\u00d4\7,\2")
        buf.write("\2\u00d4\u00d5\7\35\2\2\u00d5\u00d6\5*\26\2\u00d6\u00d7")
        buf.write("\7.\2\2\u00d7\u00d8\5\n\6\2\u00d8)\3\2\2\2\u00d9\u00de")
        buf.write("\7F\2\2\u00da\u00db\7\t\2\2\u00db\u00dc\5\60\31\2\u00dc")
        buf.write("\u00dd\7\n\2\2\u00dd\u00df\3\2\2\2\u00de\u00da\3\2\2\2")
        buf.write("\u00de\u00df\3\2\2\2\u00df+\3\2\2\2\u00e0\u00e1\79\2\2")
        buf.write("\u00e1\u00e2\7\7\2\2\u00e2\u00e3\58\35\2\u00e3\u00e4\7")
        buf.write("\b\2\2\u00e4\u00e8\7\3\2\2\u00e5\u00e7\5\34\17\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00e8\3")
        buf.write("\2\2\2\u00eb\u00f5\7\4\2\2\u00ec\u00ed\7:\2\2\u00ed\u00f1")
        buf.write("\7\3\2\2\u00ee\u00f0\5\34\17\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write("\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2\u00f4\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f6\7")
        buf.write("\4\2\2\u00f5\u00ec\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6-")
        buf.write("\3\2\2\2\u00f7\u00f8\7G\2\2\u00f8\u0101\7\7\2\2\u00f9")
        buf.write("\u00fe\58\35\2\u00fa\u00fb\7\6\2\2\u00fb\u00fd\58\35\2")
        buf.write("\u00fc\u00fa\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3")
        buf.write("\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0101\u00f9\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("\u0103\3\2\2\2\u0103\u0104\7\b\2\2\u0104\u0105\b\30\1")
        buf.write("\2\u0105/\3\2\2\2\u0106\u0109\5\62\32\2\u0107\u0108\t")
        buf.write("\7\2\2\u0108\u010a\5\60\31\2\u0109\u0107\3\2\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u010a\61\3\2\2\2\u010b\u010e\5\64\33\2")
        buf.write("\u010c\u010d\t\b\2\2\u010d\u010f\5\62\32\2\u010e\u010c")
        buf.write("\3\2\2\2\u010e\u010f\3\2\2\2\u010f\63\3\2\2\2\u0110\u0112")
        buf.write("\7\20\2\2\u0111\u0110\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write("\u011d\3\2\2\2\u0113\u011e\7G\2\2\u0114\u011e\5.\30\2")
        buf.write("\u0115\u011e\7D\2\2\u0116\u011e\7A\2\2\u0117\u011e\7B")
        buf.write("\2\2\u0118\u011e\7E\2\2\u0119\u011a\7\7\2\2\u011a\u011b")
        buf.write("\5\60\31\2\u011b\u011c\7\b\2\2\u011c\u011e\3\2\2\2\u011d")
        buf.write("\u0113\3\2\2\2\u011d\u0114\3\2\2\2\u011d\u0115\3\2\2\2")
        buf.write("\u011d\u0116\3\2\2\2\u011d\u0117\3\2\2\2\u011d\u0118\3")
        buf.write("\2\2\2\u011d\u0119\3\2\2\2\u011e\65\3\2\2\2\u011f\u0122")
        buf.write("\5\60\31\2\u0120\u0121\t\t\2\2\u0121\u0123\5\66\34\2\u0122")
        buf.write("\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\67\3\2\2\2\u0124")
        buf.write("\u0127\5\66\34\2\u0125\u0126\t\n\2\2\u0126\u0128\58\35")
        buf.write("\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u01289\3\2")
        buf.write("\2\2\u0129\u012a\7>\2\2\u012a\u012e\7\3\2\2\u012b\u012d")
        buf.write("\5<\37\2\u012c\u012b\3\2\2\2\u012d\u0130\3\2\2\2\u012e")
        buf.write("\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0131\3\2\2\2")
        buf.write("\u0130\u012e\3\2\2\2\u0131\u0132\7\4\2\2\u0132;\3\2\2")
        buf.write("\2\u0133\u0134\5> \2\u0134\u0135\7G\2\2\u0135\u0136\b")
        buf.write("\37\1\2\u0136\u0137\7\7\2\2\u0137\u0138\5@!\2\u0138\u0139")
        buf.write("\7\b\2\2\u0139\u013a\7\3\2\2\u013a\u013b\5\30\r\2\u013b")
        buf.write("\u013c\7\4\2\2\u013c=\3\2\2\2\u013d\u0140\5 \21\2\u013e")
        buf.write("\u0140\7@\2\2\u013f\u013d\3\2\2\2\u013f\u013e\3\2\2\2")
        buf.write("\u0140?\3\2\2\2\u0141\u0146\5B\"\2\u0142\u0143\7\6\2\2")
        buf.write("\u0143\u0145\5B\"\2\u0144\u0142\3\2\2\2\u0145\u0148\3")
        buf.write("\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u014a")
        buf.write("\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u0141\3\2\2\2\u0149")
        buf.write("\u014a\3\2\2\2\u014aA\3\2\2\2\u014b\u014d\5 \21\2\u014c")
        buf.write("\u014e\7C\2\2\u014d\u014c\3\2\2\2\u014d\u014e\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f\u0150\7G\2\2\u0150\u0151\b")
        buf.write("\"\1\2\u0151C\3\2\2\2\31Rs\u0098\u009e\u00b0\u00ce\u00de")
        buf.write("\u00e8\u00f1\u00f5\u00fe\u0101\u0109\u010e\u0111\u011d")
        buf.write("\u0122\u0127\u012e\u013f\u0146\u0149\u014d")
        return buf.getvalue()


class LienzoParser ( Parser ):

    grammarFileName = "Lienzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "','", "'('", "')'", 
                     "'['", "']'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", "'&'", 
                     "'|'", "<INVALID>", "'dibujo'", "'materiales'", "'llamado'", 
                     "'de'", "'ovalo'", "'rectangulo'", "'triangulo'", "'rojo'", 
                     "'verde'", "'amarillo'", "'azul'", "'blanco'", "'negro'", 
                     "'morado'", "'naranja'", "'cafe'", "'gris'", "'escenario'", 
                     "'color'", "'lienzo'", "'='", "'tamano'", "'por'", 
                     "'en'", "'posicion'", "'x'", "'y'", "'animacion'", 
                     "'dormir'", "'mientras'", "'que'", "'si'", "'sino'", 
                     "'mensaje'", "'condicion'", "'numero'", "'funciones'", 
                     "'mostrar'", "'nada'", "'verdadero'", "'falso'", "'modificable'" ]

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
                      "NUMERO", "FUNCIONES", "MOSTRAR", "NADA", "VERDADERO", 
                      "FALSO", "MODIFICABLE", "INTEGER_VALUE", "STRING_VALUE", 
                      "NOMBRE_PROPIO", "ID" ]

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
    RULE_expresion = 23
    RULE_termino = 24
    RULE_factor = 25
    RULE_sexpresion = 26
    RULE_ssexpresion = 27
    RULE_funciones = 28
    RULE_func = 29
    RULE_tipoFunc = 30
    RULE_parametros = 31
    RULE_parametro = 32

    ruleNames =  [ "program", "materiales", "material", "tipoFigura", "color", 
                   "escenario", "colorLienzo", "tamanoLienzo", "posicion", 
                   "coord", "animacion", "cuerpo", "declaracion", "instruccion", 
                   "asignacion", "tipo", "mostrarMensaje", "dormir", "mientrasQue", 
                   "cambioColor", "figura", "condicional", "llamadaFuncion", 
                   "expresion", "termino", "factor", "sexpresion", "ssexpresion", 
                   "funciones", "func", "tipoFunc", "parametros", "parametro" ]

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
    VERDADERO=63
    FALSO=64
    MODIFICABLE=65
    INTEGER_VALUE=66
    STRING_VALUE=67
    NOMBRE_PROPIO=68
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
            while _la==LienzoParser.INTEGER_VALUE:
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

        def INTEGER_VALUE(self):
            return self.getToken(LienzoParser.INTEGER_VALUE, 0)

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
            self.match(LienzoParser.INTEGER_VALUE)
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

            # se anade material a la tabla de materiales, con figura como tipo

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
            self.state = 98
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
            self.state = 100
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
            self.state = 102
            self.match(LienzoParser.ESCENARIO)
            self.state = 103
            self.match(LienzoParser.T__0)
            self.state = 104
            self.colorLienzo()
            self.state = 105
            self.match(LienzoParser.T__2)
            self.state = 106
            self.tamanoLienzo()
            self.state = 107
            self.match(LienzoParser.T__2)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LienzoParser.POSICION:
                self.state = 108
                self.posicion()
                self.state = 109
                self.match(LienzoParser.T__2)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
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
            self.state = 118
            self.match(LienzoParser.COLOR)
            self.state = 119
            self.match(LienzoParser.DE)
            self.state = 120
            self.match(LienzoParser.LIENZO)
            self.state = 121
            self.match(LienzoParser.EQUALS)
            self.state = 122
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
            self.state = 124
            self.match(LienzoParser.TAMANO)
            self.state = 125
            self.match(LienzoParser.DE)
            self.state = 126
            self.match(LienzoParser.LIENZO)
            self.state = 127
            self.match(LienzoParser.EQUALS)
            self.state = 128
            self.expresion()
            self.state = 129
            self.match(LienzoParser.POR)
            self.state = 130
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
            self.state = 132
            self.match(LienzoParser.POSICION)
            self.state = 133
            self.coord()
            self.state = 134
            self.match(LienzoParser.DE)
            self.state = 135
            self.figura()
            self.state = 136
            self.match(LienzoParser.EQUALS)
            self.state = 137
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
            self.state = 139
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
            self.state = 141
            self.match(LienzoParser.ANIMACION)

            global currentFunctionName
            currentFunctionName = "animacion"
            namespaceTable.addFunction("animacion", "nada")

            self.state = 143
            self.match(LienzoParser.T__0)
            self.state = 144
            self.cuerpo()
            self.state = 145
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
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MENSAJE) | (1 << LienzoParser.CONDICION) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 147
                self.declaracion()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (LienzoParser.COLOR - 42)) | (1 << (LienzoParser.POSICION - 42)) | (1 << (LienzoParser.DORMIR - 42)) | (1 << (LienzoParser.MIENTRAS - 42)) | (1 << (LienzoParser.SI - 42)) | (1 << (LienzoParser.MOSTRAR - 42)) | (1 << (LienzoParser.ID - 42)))) != 0):
                self.state = 153
                self.instruccion()
                self.state = 158
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

        def tipo(self):
            return self.getTypedRuleContext(LienzoParser.TipoContext,0)


        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def ssexpresion(self):
            return self.getTypedRuleContext(LienzoParser.SsexpresionContext,0)


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
            self.state = 159
            localctx._tipo = self.tipo()
            self.state = 160
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 161
            self.match(LienzoParser.EQUALS)
            self.state = 162
            self.ssexpresion()
            self.state = 163
            self.match(LienzoParser.T__2)

            if not namespaceTable.addVariable((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))), currentFunctionName):
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": Variable", (None if localctx._ID is None else localctx._ID.text), "ya fue declarada")

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
            self.state = 174
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 166
                self.asignacion()
                pass

            elif la_ == 2:
                self.state = 167
                self.mostrarMensaje()
                pass

            elif la_ == 3:
                self.state = 168
                self.dormir()
                pass

            elif la_ == 4:
                self.state = 169
                self.mientrasQue()
                pass

            elif la_ == 5:
                self.state = 170
                self.cambioColor()
                pass

            elif la_ == 6:
                self.state = 171
                self.posicion()
                pass

            elif la_ == 7:
                self.state = 172
                self.condicional()
                pass

            elif la_ == 8:
                self.state = 173
                self.llamadaFuncion()
                pass


            self.state = 176
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

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def ssexpresion(self):
            return self.getTypedRuleContext(LienzoParser.SsexpresionContext,0)


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
            self.state = 178
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 179
            self.match(LienzoParser.EQUALS)
            self.state = 180
            self.ssexpresion()

            if not namespaceTable.variableExists((None if localctx._ID is None else localctx._ID.text), currentFunctionName):
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": Variable", (None if localctx._ID is None else localctx._ID.text), "no ha sido declarada")

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
            self.state = 183
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

        def STRING_VALUE(self):
            return self.getToken(LienzoParser.STRING_VALUE, 0)

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
            self.state = 185
            self.match(LienzoParser.MOSTRAR)
            self.state = 186
            _la = self._input.LA(1)
            if not(_la==LienzoParser.STRING_VALUE or _la==LienzoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 187
            self.match(LienzoParser.EN)
            self.state = 188
            self.expresion()
            self.state = 189
            self.match(LienzoParser.T__3)
            self.state = 190
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
            self.state = 192
            self.match(LienzoParser.DORMIR)
            self.state = 193
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

        def MIENTRAS(self):
            return self.getToken(LienzoParser.MIENTRAS, 0)

        def QUE(self):
            return self.getToken(LienzoParser.QUE, 0)

        def ssexpresion(self):
            return self.getTypedRuleContext(LienzoParser.SsexpresionContext,0)


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
            self.state = 195
            self.match(LienzoParser.MIENTRAS)
            self.state = 196
            self.match(LienzoParser.QUE)
            self.state = 197
            self.match(LienzoParser.T__4)
            self.state = 198
            self.ssexpresion()
            self.state = 199
            self.match(LienzoParser.T__5)
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

        def SI(self):
            return self.getToken(LienzoParser.SI, 0)

        def ssexpresion(self):
            return self.getTypedRuleContext(LienzoParser.SsexpresionContext,0)


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
            self.ssexpresion()
            self.state = 225
            self.match(LienzoParser.T__5)
            self.state = 226
            self.match(LienzoParser.T__0)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (LienzoParser.COLOR - 42)) | (1 << (LienzoParser.POSICION - 42)) | (1 << (LienzoParser.DORMIR - 42)) | (1 << (LienzoParser.MIENTRAS - 42)) | (1 << (LienzoParser.SI - 42)) | (1 << (LienzoParser.MOSTRAR - 42)) | (1 << (LienzoParser.ID - 42)))) != 0):
                self.state = 227
                self.instruccion()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 233
            self.match(LienzoParser.T__1)
            self.state = 243
            _la = self._input.LA(1)
            if _la==LienzoParser.SINO:
                self.state = 234
                self.match(LienzoParser.SINO)
                self.state = 235
                self.match(LienzoParser.T__0)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (LienzoParser.COLOR - 42)) | (1 << (LienzoParser.POSICION - 42)) | (1 << (LienzoParser.DORMIR - 42)) | (1 << (LienzoParser.MIENTRAS - 42)) | (1 << (LienzoParser.SI - 42)) | (1 << (LienzoParser.MOSTRAR - 42)) | (1 << (LienzoParser.ID - 42)))) != 0):
                    self.state = 236
                    self.instruccion()
                    self.state = 241
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 242
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
            self._ID = None # Token

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def ssexpresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.SsexpresionContext)
            else:
                return self.getTypedRuleContext(LienzoParser.SsexpresionContext,i)


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
            self.state = 245
            localctx._ID = self.match(LienzoParser.ID)
            self.state = 246
            self.match(LienzoParser.T__4)
            self.state = 255
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__4) | (1 << LienzoParser.T__13) | (1 << LienzoParser.VERDADERO))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (LienzoParser.FALSO - 64)) | (1 << (LienzoParser.INTEGER_VALUE - 64)) | (1 << (LienzoParser.STRING_VALUE - 64)) | (1 << (LienzoParser.ID - 64)))) != 0):
                self.state = 247
                self.ssexpresion()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__3:
                    self.state = 248
                    self.match(LienzoParser.T__3)
                    self.state = 249
                    self.ssexpresion()
                    self.state = 254
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 257
            self.match(LienzoParser.T__5)
             
            if not namespaceTable.functionExists((None if localctx._ID is None else localctx._ID.text)):
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": llamada a funcion", (None if localctx._ID is None else localctx._ID.text), "inexistente")

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

        def termino(self):
            return self.getTypedRuleContext(LienzoParser.TerminoContext,0)


        def expresion(self):
            return self.getTypedRuleContext(LienzoParser.ExpresionContext,0)


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
            self.state = 260
            self.termino()
            self.state = 263
            _la = self._input.LA(1)
            if _la==LienzoParser.T__8 or _la==LienzoParser.T__9:
                self.state = 261
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__8 or _la==LienzoParser.T__9):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 262
                self.expresion()


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

        def factor(self):
            return self.getTypedRuleContext(LienzoParser.FactorContext,0)


        def termino(self):
            return self.getTypedRuleContext(LienzoParser.TerminoContext,0)


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
            self.state = 265
            self.factor()
            self.state = 268
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12))) != 0):
                self.state = 266
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__10) | (1 << LienzoParser.T__11) | (1 << LienzoParser.T__12))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 267
                self.termino()


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

        def ID(self):
            return self.getToken(LienzoParser.ID, 0)

        def llamadaFuncion(self):
            return self.getTypedRuleContext(LienzoParser.LlamadaFuncionContext,0)


        def INTEGER_VALUE(self):
            return self.getToken(LienzoParser.INTEGER_VALUE, 0)

        def VERDADERO(self):
            return self.getToken(LienzoParser.VERDADERO, 0)

        def FALSO(self):
            return self.getToken(LienzoParser.FALSO, 0)

        def STRING_VALUE(self):
            return self.getToken(LienzoParser.STRING_VALUE, 0)

        def expresion(self):
            return self.getTypedRuleContext(LienzoParser.ExpresionContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            _la = self._input.LA(1)
            if _la==LienzoParser.T__13:
                self.state = 270
                self.match(LienzoParser.T__13)


            self.state = 283
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 273
                self.match(LienzoParser.ID)
                pass

            elif la_ == 2:
                self.state = 274
                self.llamadaFuncion()
                pass

            elif la_ == 3:
                self.state = 275
                self.match(LienzoParser.INTEGER_VALUE)
                pass

            elif la_ == 4:
                self.state = 276
                self.match(LienzoParser.VERDADERO)
                pass

            elif la_ == 5:
                self.state = 277
                self.match(LienzoParser.FALSO)
                pass

            elif la_ == 6:
                self.state = 278
                self.match(LienzoParser.STRING_VALUE)
                pass

            elif la_ == 7:
                self.state = 279
                self.match(LienzoParser.T__4)
                self.state = 280
                self.expresion()
                self.state = 281
                self.match(LienzoParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SexpresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(LienzoParser.ExpresionContext,0)


        def sexpresion(self):
            return self.getTypedRuleContext(LienzoParser.SexpresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_sexpresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSexpresion" ):
                listener.enterSexpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSexpresion" ):
                listener.exitSexpresion(self)




    def sexpresion(self):

        localctx = LienzoParser.SexpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_sexpresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.expresion()
            self.state = 288
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__14) | (1 << LienzoParser.T__15) | (1 << LienzoParser.T__16) | (1 << LienzoParser.T__17) | (1 << LienzoParser.T__18) | (1 << LienzoParser.T__19))) != 0):
                self.state = 286
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.T__14) | (1 << LienzoParser.T__15) | (1 << LienzoParser.T__16) | (1 << LienzoParser.T__17) | (1 << LienzoParser.T__18) | (1 << LienzoParser.T__19))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 287
                self.sexpresion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SsexpresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sexpresion(self):
            return self.getTypedRuleContext(LienzoParser.SexpresionContext,0)


        def ssexpresion(self):
            return self.getTypedRuleContext(LienzoParser.SsexpresionContext,0)


        def getRuleIndex(self):
            return LienzoParser.RULE_ssexpresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSsexpresion" ):
                listener.enterSsexpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSsexpresion" ):
                listener.exitSsexpresion(self)




    def ssexpresion(self):

        localctx = LienzoParser.SsexpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ssexpresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.sexpresion()
            self.state = 293
            _la = self._input.LA(1)
            if _la==LienzoParser.T__20 or _la==LienzoParser.T__21:
                self.state = 291
                _la = self._input.LA(1)
                if not(_la==LienzoParser.T__20 or _la==LienzoParser.T__21):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 292
                self.ssexpresion()


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
        self.enterRule(localctx, 56, self.RULE_funciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(LienzoParser.FUNCIONES)
            self.state = 296
            self.match(LienzoParser.T__0)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MENSAJE) | (1 << LienzoParser.CONDICION) | (1 << LienzoParser.NUMERO) | (1 << LienzoParser.NADA))) != 0):
                self.state = 297
                self.func()
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 303
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

        def parametros(self):
            return self.getTypedRuleContext(LienzoParser.ParametrosContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(LienzoParser.CuerpoContext,0)


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
        self.enterRule(localctx, 58, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            localctx._tipoFunc = self.tipoFunc()
            self.state = 306
            localctx._ID = self.match(LienzoParser.ID)

            global currentFunctionName
            currentFunctionName = (None if localctx._ID is None else localctx._ID.text)
            if not namespaceTable.addFunction(currentFunctionName, (None if localctx._tipoFunc is None else self._input.getText((localctx._tipoFunc.start,localctx._tipoFunc.stop)))):
                print("Error: linea", (0 if localctx._ID is None else localctx._ID.line), ": Funcion", (None if localctx._ID is None else localctx._ID.text), "ya fue declarada")

            self.state = 308
            self.match(LienzoParser.T__4)
            self.state = 309
            self.parametros()
            self.state = 310
            self.match(LienzoParser.T__5)
            self.state = 311
            self.match(LienzoParser.T__0)
            self.state = 312
            self.cuerpo()
            self.state = 313
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
        self.enterRule(localctx, 60, self.RULE_tipoFunc)
        try:
            self.state = 317
            token = self._input.LA(1)
            if token in [LienzoParser.MENSAJE, LienzoParser.CONDICION, LienzoParser.NUMERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.tipo()

            elif token in [LienzoParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
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

    class ParametrosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LienzoParser.ParametroContext)
            else:
                return self.getTypedRuleContext(LienzoParser.ParametroContext,i)


        def getRuleIndex(self):
            return LienzoParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = LienzoParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LienzoParser.MENSAJE) | (1 << LienzoParser.CONDICION) | (1 << LienzoParser.NUMERO))) != 0):
                self.state = 319
                self.parametro()
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LienzoParser.T__3:
                    self.state = 320
                    self.match(LienzoParser.T__3)
                    self.state = 321
                    self.parametro()
                    self.state = 326
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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
            self.state = 329
            localctx._tipo = self.tipo()
            self.state = 331
            _la = self._input.LA(1)
            if _la==LienzoParser.MODIFICABLE:
                self.state = 330
                localctx._MODIFICABLE = self.match(LienzoParser.MODIFICABLE)


            self.state = 333
            localctx._ID = self.match(LienzoParser.ID)

            if not namespaceTable.addParameter((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText((localctx._tipo.start,localctx._tipo.stop))), (None if localctx._MODIFICABLE is None else localctx._MODIFICABLE.text), currentFunctionName):
                print("Error: linea", (None if localctx._ID is None else localctx._ID.text), ": Parametro", (None if localctx._ID is None else localctx._ID.text), "ya fue declarado")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





