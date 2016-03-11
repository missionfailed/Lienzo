# Generated from Lienzo.g4 by ANTLR 4.5.2
from antlr4 import *
from io import StringIO


from namespace import NamespaceTable

namespaceTable = NamespaceTable()
currentFunctionName = ""
currentParameterList = []


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2G")
        buf.write("\u01fd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\6\30\u00bf\n\30\r\30\16\30\u00c0")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\39\39\39\39\39\3:\3:\3:")
        buf.write("\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3C\6C\u01e3\nC\rC\16C\u01e4\3D\3D\7D\u01e9\nD\fD")
        buf.write("\16D\u01ec\13D\3D\3D\3E\3E\7E\u01f2\nE\fE\16E\u01f5\13")
        buf.write("E\3F\3F\7F\u01f9\nF\fF\16F\u01fc\13F\2\2G\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177")
        buf.write("A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\3\2\b\5\2")
        buf.write("\13\f\17\17\"\"\3\2\62;\3\2$$\3\2C\\\4\2C\\c|\3\2c|\u0201")
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
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\3\u008d\3\2\2\2\5\u008f\3\2\2\2\7\u0091")
        buf.write("\3\2\2\2\t\u0093\3\2\2\2\13\u0095\3\2\2\2\r\u0097\3\2")
        buf.write("\2\2\17\u0099\3\2\2\2\21\u009b\3\2\2\2\23\u009d\3\2\2")
        buf.write("\2\25\u009f\3\2\2\2\27\u00a1\3\2\2\2\31\u00a3\3\2\2\2")
        buf.write("\33\u00a5\3\2\2\2\35\u00a7\3\2\2\2\37\u00a9\3\2\2\2!\u00ab")
        buf.write("\3\2\2\2#\u00ad\3\2\2\2%\u00b0\3\2\2\2\'\u00b3\3\2\2\2")
        buf.write(")\u00b6\3\2\2\2+\u00b9\3\2\2\2-\u00bb\3\2\2\2/\u00be\3")
        buf.write("\2\2\2\61\u00c4\3\2\2\2\63\u00cb\3\2\2\2\65\u00d6\3\2")
        buf.write("\2\2\67\u00de\3\2\2\29\u00e1\3\2\2\2;\u00e7\3\2\2\2=\u00f2")
        buf.write("\3\2\2\2?\u00fc\3\2\2\2A\u0101\3\2\2\2C\u0107\3\2\2\2")
        buf.write("E\u0110\3\2\2\2G\u0115\3\2\2\2I\u011c\3\2\2\2K\u0122\3")
        buf.write("\2\2\2M\u0129\3\2\2\2O\u0131\3\2\2\2Q\u0136\3\2\2\2S\u013b")
        buf.write("\3\2\2\2U\u0145\3\2\2\2W\u014b\3\2\2\2Y\u0152\3\2\2\2")
        buf.write("[\u0154\3\2\2\2]\u015b\3\2\2\2_\u015f\3\2\2\2a\u0162\3")
        buf.write("\2\2\2c\u016b\3\2\2\2e\u016d\3\2\2\2g\u016f\3\2\2\2i\u0179")
        buf.write("\3\2\2\2k\u0180\3\2\2\2m\u0189\3\2\2\2o\u018d\3\2\2\2")
        buf.write("q\u0190\3\2\2\2s\u0195\3\2\2\2u\u019d\3\2\2\2w\u01a7\3")
        buf.write("\2\2\2y\u01ae\3\2\2\2{\u01b8\3\2\2\2}\u01c0\3\2\2\2\177")
        buf.write("\u01c5\3\2\2\2\u0081\u01cf\3\2\2\2\u0083\u01d5\3\2\2\2")
        buf.write("\u0085\u01e2\3\2\2\2\u0087\u01e6\3\2\2\2\u0089\u01ef\3")
        buf.write("\2\2\2\u008b\u01f6\3\2\2\2\u008d\u008e\7}\2\2\u008e\4")
        buf.write("\3\2\2\2\u008f\u0090\7\177\2\2\u0090\6\3\2\2\2\u0091\u0092")
        buf.write("\7=\2\2\u0092\b\3\2\2\2\u0093\u0094\7.\2\2\u0094\n\3\2")
        buf.write("\2\2\u0095\u0096\7*\2\2\u0096\f\3\2\2\2\u0097\u0098\7")
        buf.write("+\2\2\u0098\16\3\2\2\2\u0099\u009a\7]\2\2\u009a\20\3\2")
        buf.write("\2\2\u009b\u009c\7_\2\2\u009c\22\3\2\2\2\u009d\u009e\7")
        buf.write("-\2\2\u009e\24\3\2\2\2\u009f\u00a0\7/\2\2\u00a0\26\3\2")
        buf.write("\2\2\u00a1\u00a2\7,\2\2\u00a2\30\3\2\2\2\u00a3\u00a4\7")
        buf.write("\61\2\2\u00a4\32\3\2\2\2\u00a5\u00a6\7\'\2\2\u00a6\34")
        buf.write("\3\2\2\2\u00a7\u00a8\7#\2\2\u00a8\36\3\2\2\2\u00a9\u00aa")
        buf.write("\7@\2\2\u00aa \3\2\2\2\u00ab\u00ac\7>\2\2\u00ac\"\3\2")
        buf.write("\2\2\u00ad\u00ae\7@\2\2\u00ae\u00af\7?\2\2\u00af$\3\2")
        buf.write("\2\2\u00b0\u00b1\7>\2\2\u00b1\u00b2\7?\2\2\u00b2&\3\2")
        buf.write("\2\2\u00b3\u00b4\7?\2\2\u00b4\u00b5\7?\2\2\u00b5(\3\2")
        buf.write("\2\2\u00b6\u00b7\7#\2\2\u00b7\u00b8\7?\2\2\u00b8*\3\2")
        buf.write("\2\2\u00b9\u00ba\7(\2\2\u00ba,\3\2\2\2\u00bb\u00bc\7~")
        buf.write("\2\2\u00bc.\3\2\2\2\u00bd\u00bf\t\2\2\2\u00be\u00bd\3")
        buf.write("\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\b\30\2\2\u00c3")
        buf.write("\60\3\2\2\2\u00c4\u00c5\7f\2\2\u00c5\u00c6\7k\2\2\u00c6")
        buf.write("\u00c7\7d\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7l\2\2\u00c9")
        buf.write("\u00ca\7q\2\2\u00ca\62\3\2\2\2\u00cb\u00cc\7o\2\2\u00cc")
        buf.write("\u00cd\7c\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf\7g\2\2\u00cf")
        buf.write("\u00d0\7t\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7c\2\2\u00d2")
        buf.write("\u00d3\7n\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7u\2\2\u00d5")
        buf.write("\64\3\2\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7n\2\2\u00d8")
        buf.write("\u00d9\7c\2\2\u00d9\u00da\7o\2\2\u00da\u00db\7c\2\2\u00db")
        buf.write("\u00dc\7f\2\2\u00dc\u00dd\7q\2\2\u00dd\66\3\2\2\2\u00de")
        buf.write("\u00df\7f\2\2\u00df\u00e0\7g\2\2\u00e08\3\2\2\2\u00e1")
        buf.write("\u00e2\7q\2\2\u00e2\u00e3\7x\2\2\u00e3\u00e4\7c\2\2\u00e4")
        buf.write("\u00e5\7n\2\2\u00e5\u00e6\7q\2\2\u00e6:\3\2\2\2\u00e7")
        buf.write("\u00e8\7t\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea\7e\2\2\u00ea")
        buf.write("\u00eb\7v\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7p\2\2\u00ed")
        buf.write("\u00ee\7i\2\2\u00ee\u00ef\7w\2\2\u00ef\u00f0\7n\2\2\u00f0")
        buf.write("\u00f1\7q\2\2\u00f1<\3\2\2\2\u00f2\u00f3\7v\2\2\u00f3")
        buf.write("\u00f4\7t\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7c\2\2\u00f6")
        buf.write("\u00f7\7p\2\2\u00f7\u00f8\7i\2\2\u00f8\u00f9\7w\2\2\u00f9")
        buf.write("\u00fa\7n\2\2\u00fa\u00fb\7q\2\2\u00fb>\3\2\2\2\u00fc")
        buf.write("\u00fd\7t\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7l\2\2\u00ff")
        buf.write("\u0100\7q\2\2\u0100@\3\2\2\2\u0101\u0102\7x\2\2\u0102")
        buf.write("\u0103\7g\2\2\u0103\u0104\7t\2\2\u0104\u0105\7f\2\2\u0105")
        buf.write("\u0106\7g\2\2\u0106B\3\2\2\2\u0107\u0108\7c\2\2\u0108")
        buf.write("\u0109\7o\2\2\u0109\u010a\7c\2\2\u010a\u010b\7t\2\2\u010b")
        buf.write("\u010c\7k\2\2\u010c\u010d\7n\2\2\u010d\u010e\7n\2\2\u010e")
        buf.write("\u010f\7q\2\2\u010fD\3\2\2\2\u0110\u0111\7c\2\2\u0111")
        buf.write("\u0112\7|\2\2\u0112\u0113\7w\2\2\u0113\u0114\7n\2\2\u0114")
        buf.write("F\3\2\2\2\u0115\u0116\7d\2\2\u0116\u0117\7n\2\2\u0117")
        buf.write("\u0118\7c\2\2\u0118\u0119\7p\2\2\u0119\u011a\7e\2\2\u011a")
        buf.write("\u011b\7q\2\2\u011bH\3\2\2\2\u011c\u011d\7p\2\2\u011d")
        buf.write("\u011e\7g\2\2\u011e\u011f\7i\2\2\u011f\u0120\7t\2\2\u0120")
        buf.write("\u0121\7q\2\2\u0121J\3\2\2\2\u0122\u0123\7o\2\2\u0123")
        buf.write("\u0124\7q\2\2\u0124\u0125\7t\2\2\u0125\u0126\7c\2\2\u0126")
        buf.write("\u0127\7f\2\2\u0127\u0128\7q\2\2\u0128L\3\2\2\2\u0129")
        buf.write("\u012a\7p\2\2\u012a\u012b\7c\2\2\u012b\u012c\7t\2\2\u012c")
        buf.write("\u012d\7c\2\2\u012d\u012e\7p\2\2\u012e\u012f\7l\2\2\u012f")
        buf.write("\u0130\7c\2\2\u0130N\3\2\2\2\u0131\u0132\7e\2\2\u0132")
        buf.write("\u0133\7c\2\2\u0133\u0134\7h\2\2\u0134\u0135\7g\2\2\u0135")
        buf.write("P\3\2\2\2\u0136\u0137\7i\2\2\u0137\u0138\7t\2\2\u0138")
        buf.write("\u0139\7k\2\2\u0139\u013a\7u\2\2\u013aR\3\2\2\2\u013b")
        buf.write("\u013c\7g\2\2\u013c\u013d\7u\2\2\u013d\u013e\7e\2\2\u013e")
        buf.write("\u013f\7g\2\2\u013f\u0140\7p\2\2\u0140\u0141\7c\2\2\u0141")
        buf.write("\u0142\7t\2\2\u0142\u0143\7k\2\2\u0143\u0144\7q\2\2\u0144")
        buf.write("T\3\2\2\2\u0145\u0146\7e\2\2\u0146\u0147\7q\2\2\u0147")
        buf.write("\u0148\7n\2\2\u0148\u0149\7q\2\2\u0149\u014a\7t\2\2\u014a")
        buf.write("V\3\2\2\2\u014b\u014c\7n\2\2\u014c\u014d\7k\2\2\u014d")
        buf.write("\u014e\7g\2\2\u014e\u014f\7p\2\2\u014f\u0150\7|\2\2\u0150")
        buf.write("\u0151\7q\2\2\u0151X\3\2\2\2\u0152\u0153\7?\2\2\u0153")
        buf.write("Z\3\2\2\2\u0154\u0155\7v\2\2\u0155\u0156\7c\2\2\u0156")
        buf.write("\u0157\7o\2\2\u0157\u0158\7c\2\2\u0158\u0159\7p\2\2\u0159")
        buf.write("\u015a\7q\2\2\u015a\\\3\2\2\2\u015b\u015c\7r\2\2\u015c")
        buf.write("\u015d\7q\2\2\u015d\u015e\7t\2\2\u015e^\3\2\2\2\u015f")
        buf.write("\u0160\7g\2\2\u0160\u0161\7p\2\2\u0161`\3\2\2\2\u0162")
        buf.write("\u0163\7r\2\2\u0163\u0164\7q\2\2\u0164\u0165\7u\2\2\u0165")
        buf.write("\u0166\7k\2\2\u0166\u0167\7e\2\2\u0167\u0168\7k\2\2\u0168")
        buf.write("\u0169\7q\2\2\u0169\u016a\7p\2\2\u016ab\3\2\2\2\u016b")
        buf.write("\u016c\7z\2\2\u016cd\3\2\2\2\u016d\u016e\7{\2\2\u016e")
        buf.write("f\3\2\2\2\u016f\u0170\7c\2\2\u0170\u0171\7p\2\2\u0171")
        buf.write("\u0172\7k\2\2\u0172\u0173\7o\2\2\u0173\u0174\7c\2\2\u0174")
        buf.write("\u0175\7e\2\2\u0175\u0176\7k\2\2\u0176\u0177\7q\2\2\u0177")
        buf.write("\u0178\7p\2\2\u0178h\3\2\2\2\u0179\u017a\7f\2\2\u017a")
        buf.write("\u017b\7q\2\2\u017b\u017c\7t\2\2\u017c\u017d\7o\2\2\u017d")
        buf.write("\u017e\7k\2\2\u017e\u017f\7t\2\2\u017fj\3\2\2\2\u0180")
        buf.write("\u0181\7o\2\2\u0181\u0182\7k\2\2\u0182\u0183\7g\2\2\u0183")
        buf.write("\u0184\7p\2\2\u0184\u0185\7v\2\2\u0185\u0186\7t\2\2\u0186")
        buf.write("\u0187\7c\2\2\u0187\u0188\7u\2\2\u0188l\3\2\2\2\u0189")
        buf.write("\u018a\7s\2\2\u018a\u018b\7w\2\2\u018b\u018c\7g\2\2\u018c")
        buf.write("n\3\2\2\2\u018d\u018e\7u\2\2\u018e\u018f\7k\2\2\u018f")
        buf.write("p\3\2\2\2\u0190\u0191\7u\2\2\u0191\u0192\7k\2\2\u0192")
        buf.write("\u0193\7p\2\2\u0193\u0194\7q\2\2\u0194r\3\2\2\2\u0195")
        buf.write("\u0196\7o\2\2\u0196\u0197\7g\2\2\u0197\u0198\7p\2\2\u0198")
        buf.write("\u0199\7u\2\2\u0199\u019a\7c\2\2\u019a\u019b\7l\2\2\u019b")
        buf.write("\u019c\7g\2\2\u019ct\3\2\2\2\u019d\u019e\7e\2\2\u019e")
        buf.write("\u019f\7q\2\2\u019f\u01a0\7p\2\2\u01a0\u01a1\7f\2\2\u01a1")
        buf.write("\u01a2\7k\2\2\u01a2\u01a3\7e\2\2\u01a3\u01a4\7k\2\2\u01a4")
        buf.write("\u01a5\7q\2\2\u01a5\u01a6\7p\2\2\u01a6v\3\2\2\2\u01a7")
        buf.write("\u01a8\7p\2\2\u01a8\u01a9\7w\2\2\u01a9\u01aa\7o\2\2\u01aa")
        buf.write("\u01ab\7g\2\2\u01ab\u01ac\7t\2\2\u01ac\u01ad\7q\2\2\u01ad")
        buf.write("x\3\2\2\2\u01ae\u01af\7h\2\2\u01af\u01b0\7w\2\2\u01b0")
        buf.write("\u01b1\7p\2\2\u01b1\u01b2\7e\2\2\u01b2\u01b3\7k\2\2\u01b3")
        buf.write("\u01b4\7q\2\2\u01b4\u01b5\7p\2\2\u01b5\u01b6\7g\2\2\u01b6")
        buf.write("\u01b7\7u\2\2\u01b7z\3\2\2\2\u01b8\u01b9\7o\2\2\u01b9")
        buf.write("\u01ba\7q\2\2\u01ba\u01bb\7u\2\2\u01bb\u01bc\7v\2\2\u01bc")
        buf.write("\u01bd\7t\2\2\u01bd\u01be\7c\2\2\u01be\u01bf\7t\2\2\u01bf")
        buf.write("|\3\2\2\2\u01c0\u01c1\7p\2\2\u01c1\u01c2\7c\2\2\u01c2")
        buf.write("\u01c3\7f\2\2\u01c3\u01c4\7c\2\2\u01c4~\3\2\2\2\u01c5")
        buf.write("\u01c6\7x\2\2\u01c6\u01c7\7g\2\2\u01c7\u01c8\7t\2\2\u01c8")
        buf.write("\u01c9\7f\2\2\u01c9\u01ca\7c\2\2\u01ca\u01cb\7f\2\2\u01cb")
        buf.write("\u01cc\7g\2\2\u01cc\u01cd\7t\2\2\u01cd\u01ce\7q\2\2\u01ce")
        buf.write("\u0080\3\2\2\2\u01cf\u01d0\7h\2\2\u01d0\u01d1\7c\2\2\u01d1")
        buf.write("\u01d2\7n\2\2\u01d2\u01d3\7u\2\2\u01d3\u01d4\7q\2\2\u01d4")
        buf.write("\u0082\3\2\2\2\u01d5\u01d6\7o\2\2\u01d6\u01d7\7q\2\2\u01d7")
        buf.write("\u01d8\7f\2\2\u01d8\u01d9\7k\2\2\u01d9\u01da\7h\2\2\u01da")
        buf.write("\u01db\7k\2\2\u01db\u01dc\7e\2\2\u01dc\u01dd\7c\2\2\u01dd")
        buf.write("\u01de\7d\2\2\u01de\u01df\7n\2\2\u01df\u01e0\7g\2\2\u01e0")
        buf.write("\u0084\3\2\2\2\u01e1\u01e3\t\3\2\2\u01e2\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e4\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3")
        buf.write("\2\2\2\u01e5\u0086\3\2\2\2\u01e6\u01ea\7$\2\2\u01e7\u01e9")
        buf.write("\n\4\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec\3\2\2\2\u01ea")
        buf.write("\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ed\3\2\2\2")
        buf.write("\u01ec\u01ea\3\2\2\2\u01ed\u01ee\7$\2\2\u01ee\u0088\3")
        buf.write("\2\2\2\u01ef\u01f3\t\5\2\2\u01f0\u01f2\t\6\2\2\u01f1\u01f0")
        buf.write("\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3")
        buf.write("\u01f4\3\2\2\2\u01f4\u008a\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f6\u01fa\t\7\2\2\u01f7\u01f9\t\6\2\2\u01f8\u01f7\3")
        buf.write("\2\2\2\u01f9\u01fc\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb")
        buf.write("\3\2\2\2\u01fb\u008c\3\2\2\2\u01fc\u01fa\3\2\2\2\b\2\u00c0")
        buf.write("\u01e4\u01ea\u01f3\u01fa\3\b\2\2")
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
    CONDICION = 58
    NUMERO = 59
    FUNCIONES = 60
    MOSTRAR = 61
    NADA = 62
    VERDADERO = 63
    FALSO = 64
    MODIFICABLE = 65
    INTEGER_VALUE = 66
    STRING_VALUE = 67
    NOMBRE_PROPIO = 68
    ID = 69

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "';'", "','", "'('", "')'", "'['", "']'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'>'", "'<'", "'>='", "'<='", 
            "'=='", "'!='", "'&'", "'|'", "'dibujo'", "'materiales'", "'llamado'", 
            "'de'", "'ovalo'", "'rectangulo'", "'triangulo'", "'rojo'", 
            "'verde'", "'amarillo'", "'azul'", "'blanco'", "'negro'", "'morado'", 
            "'naranja'", "'cafe'", "'gris'", "'escenario'", "'color'", "'lienzo'", 
            "'='", "'tamano'", "'por'", "'en'", "'posicion'", "'x'", "'y'", 
            "'animacion'", "'dormir'", "'mientras'", "'que'", "'si'", "'sino'", 
            "'mensaje'", "'condicion'", "'numero'", "'funciones'", "'mostrar'", 
            "'nada'", "'verdadero'", "'falso'", "'modificable'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "DIBUJO", "MATERIALES", "LLAMADO", "DE", "OVALO", "RECTANGULO", 
            "TRIANGULO", "ROJO", "VERDE", "AMARILLO", "AZUL", "BLANCO", 
            "NEGRO", "MORADO", "NARANJA", "CAFE", "GRIS", "ESCENARIO", "COLOR", 
            "LIENZO", "EQUALS", "TAMANO", "POR", "EN", "POSICION", "X", 
            "Y", "ANIMACION", "DORMIR", "MIENTRAS", "QUE", "SI", "SINO", 
            "MENSAJE", "CONDICION", "NUMERO", "FUNCIONES", "MOSTRAR", "NADA", 
            "VERDADERO", "FALSO", "MODIFICABLE", "INTEGER_VALUE", "STRING_VALUE", 
            "NOMBRE_PROPIO", "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "WS", "DIBUJO", "MATERIALES", "LLAMADO", 
                  "DE", "OVALO", "RECTANGULO", "TRIANGULO", "ROJO", "VERDE", 
                  "AMARILLO", "AZUL", "BLANCO", "NEGRO", "MORADO", "NARANJA", 
                  "CAFE", "GRIS", "ESCENARIO", "COLOR", "LIENZO", "EQUALS", 
                  "TAMANO", "POR", "EN", "POSICION", "X", "Y", "ANIMACION", 
                  "DORMIR", "MIENTRAS", "QUE", "SI", "SINO", "MENSAJE", 
                  "CONDICION", "NUMERO", "FUNCIONES", "MOSTRAR", "NADA", 
                  "VERDADERO", "FALSO", "MODIFICABLE", "INTEGER_VALUE", 
                  "STRING_VALUE", "NOMBRE_PROPIO", "ID" ]

    grammarFileName = "Lienzo.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


