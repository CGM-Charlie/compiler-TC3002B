# Generated from compilerV1.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

 
from variableTable import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$")
        buf.write("\u0106\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\5\3F\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\7\4N\n\4\f\4\16\4Q\13\4\3\5\3\5\3\5\3\5\5\5")
        buf.write("W\n\5\3\6\3\6\3\7\3\7\5\7]\n\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\tt\n\t\3\t\5\tw\n\t\3\n\3\n\7\n{\n\n\f\n\16\n")
        buf.write("~\13\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13\u0087\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\r\u0099\n\r\3\r\5\r\u009c\n\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u00a4\n\16\3\16\5\16\u00a7\n\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00af\n\17\3\17\5")
        buf.write("\17\u00b2\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00c2\n\20\3\21\3")
        buf.write("\21\3\21\5\21\u00c7\n\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00d7\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\5\26")
        buf.write("\u00ed\n\26\3\26\5\26\u00f0\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\5\30\u00fb\n\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u0102\n\31\3\32\3\32\3\32\2\2\33\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\2\4\3")
        buf.write("\2\n\13\3\2\"#\2\u0107\2\64\3\2\2\2\4E\3\2\2\2\6G\3\2")
        buf.write("\2\2\bR\3\2\2\2\nX\3\2\2\2\fZ\3\2\2\2\16^\3\2\2\2\20v")
        buf.write("\3\2\2\2\22x\3\2\2\2\24\u0086\3\2\2\2\26\u0088\3\2\2\2")
        buf.write("\30\u0090\3\2\2\2\32\u009d\3\2\2\2\34\u00a8\3\2\2\2\36")
        buf.write("\u00c1\3\2\2\2 \u00c6\3\2\2\2\"\u00c8\3\2\2\2$\u00d6\3")
        buf.write("\2\2\2&\u00d8\3\2\2\2(\u00e2\3\2\2\2*\u00ef\3\2\2\2,\u00f1")
        buf.write("\3\2\2\2.\u00f7\3\2\2\2\60\u0101\3\2\2\2\62\u0103\3\2")
        buf.write("\2\2\64\65\b\2\1\2\65\66\b\2\1\2\66\67\7\3\2\2\678\7!")
        buf.write("\2\289\7\4\2\29:\5\4\3\2:;\5\f\7\2;<\7\5\2\2<=\b\2\1\2")
        buf.write("=>\5\22\n\2>?\b\2\1\2?@\7\6\2\2@A\b\2\1\2A\3\3\2\2\2B")
        buf.write("C\7\7\2\2CF\5\6\4\2DF\3\2\2\2EB\3\2\2\2ED\3\2\2\2F\5\3")
        buf.write("\2\2\2GH\5\b\5\2HI\7\b\2\2IJ\5\n\6\2JK\7\4\2\2KO\b\4\1")
        buf.write("\2LN\5\6\4\2ML\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P")
        buf.write("\7\3\2\2\2QO\3\2\2\2RS\7!\2\2SV\b\5\1\2TU\7\t\2\2UW\5")
        buf.write("\b\5\2VT\3\2\2\2VW\3\2\2\2W\t\3\2\2\2XY\t\2\2\2Y\13\3")
        buf.write("\2\2\2Z\\\5\16\b\2[]\5\f\7\2\\[\3\2\2\2\\]\3\2\2\2]\r")
        buf.write("\3\2\2\2^_\7\f\2\2_`\7!\2\2`a\b\b\1\2ab\7\r\2\2bc\5\20")
        buf.write("\t\2cd\7\16\2\2de\7\17\2\2ef\5\4\3\2fg\b\b\1\2gh\5\22")
        buf.write("\n\2hi\b\b\1\2ij\7\20\2\2jk\7\4\2\2k\17\3\2\2\2lm\7!\2")
        buf.write("\2mn\b\t\1\2no\7\b\2\2op\5\n\6\2ps\b\t\1\2qr\7\t\2\2r")
        buf.write("t\5\20\t\2sq\3\2\2\2st\3\2\2\2tw\3\2\2\2uw\3\2\2\2vl\3")
        buf.write("\2\2\2vu\3\2\2\2w\21\3\2\2\2x|\7\21\2\2y{\5\24\13\2zy")
        buf.write("\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\177\3\2\2\2~|")
        buf.write("\3\2\2\2\177\u0080\7\22\2\2\u0080\23\3\2\2\2\u0081\u0087")
        buf.write("\5\26\f\2\u0082\u0087\5\"\22\2\u0083\u0087\5&\24\2\u0084")
        buf.write("\u0087\5(\25\2\u0085\u0087\5,\27\2\u0086\u0081\3\2\2\2")
        buf.write("\u0086\u0082\3\2\2\2\u0086\u0083\3\2\2\2\u0086\u0084\3")
        buf.write("\2\2\2\u0086\u0085\3\2\2\2\u0087\25\3\2\2\2\u0088\u0089")
        buf.write("\7!\2\2\u0089\u008a\b\f\1\2\u008a\u008b\7\23\2\2\u008b")
        buf.write("\u008c\b\f\1\2\u008c\u008d\5\30\r\2\u008d\u008e\b\f\1")
        buf.write("\2\u008e\u008f\7\4\2\2\u008f\27\3\2\2\2\u0090\u0091\5")
        buf.write("\32\16\2\u0091\u009b\b\r\1\2\u0092\u0093\7\24\2\2\u0093")
        buf.write("\u0099\b\r\1\2\u0094\u0095\7\25\2\2\u0095\u0099\b\r\1")
        buf.write("\2\u0096\u0097\7\26\2\2\u0097\u0099\b\r\1\2\u0098\u0092")
        buf.write("\3\2\2\2\u0098\u0094\3\2\2\2\u0098\u0096\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\u009c\5\30\r\2\u009b\u0098\3\2\2")
        buf.write("\2\u009b\u009c\3\2\2\2\u009c\31\3\2\2\2\u009d\u009e\5")
        buf.write("\34\17\2\u009e\u00a6\b\16\1\2\u009f\u00a0\7\27\2\2\u00a0")
        buf.write("\u00a4\b\16\1\2\u00a1\u00a2\7\30\2\2\u00a2\u00a4\b\16")
        buf.write("\1\2\u00a3\u009f\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5")
        buf.write("\3\2\2\2\u00a5\u00a7\5\32\16\2\u00a6\u00a3\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a7\33\3\2\2\2\u00a8\u00a9\5\36\20\2")
        buf.write("\u00a9\u00b1\b\17\1\2\u00aa\u00ab\7\31\2\2\u00ab\u00af")
        buf.write("\b\17\1\2\u00ac\u00ad\7\32\2\2\u00ad\u00af\b\17\1\2\u00ae")
        buf.write("\u00aa\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\3\2\2\2")
        buf.write("\u00b0\u00b2\5\34\17\2\u00b1\u00ae\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\35\3\2\2\2\u00b3\u00b4\7\r\2\2\u00b4\u00b5")
        buf.write("\b\20\1\2\u00b5\u00b6\5\30\r\2\u00b6\u00b7\7\16\2\2\u00b7")
        buf.write("\u00b8\b\20\1\2\u00b8\u00c2\3\2\2\2\u00b9\u00ba\5 \21")
        buf.write("\2\u00ba\u00bb\7!\2\2\u00bb\u00bc\b\20\1\2\u00bc\u00c2")
        buf.write("\3\2\2\2\u00bd\u00be\5 \21\2\u00be\u00bf\5\62\32\2\u00bf")
        buf.write("\u00c0\b\20\1\2\u00c0\u00c2\3\2\2\2\u00c1\u00b3\3\2\2")
        buf.write("\2\u00c1\u00b9\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c2\37\3")
        buf.write("\2\2\2\u00c3\u00c7\7\27\2\2\u00c4\u00c7\7\30\2\2\u00c5")
        buf.write("\u00c7\3\2\2\2\u00c6\u00c3\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c5\3\2\2\2\u00c7!\3\2\2\2\u00c8\u00c9\7\33\2")
        buf.write("\2\u00c9\u00ca\7\r\2\2\u00ca\u00cb\5\30\r\2\u00cb\u00cc")
        buf.write("\7\16\2\2\u00cc\u00cd\b\22\1\2\u00cd\u00ce\5\22\n\2\u00ce")
        buf.write("\u00cf\5$\23\2\u00cf\u00d0\7\4\2\2\u00d0\u00d1\b\22\1")
        buf.write("\2\u00d1#\3\2\2\2\u00d2\u00d3\b\23\1\2\u00d3\u00d4\7\34")
        buf.write("\2\2\u00d4\u00d7\5\22\n\2\u00d5\u00d7\3\2\2\2\u00d6\u00d2")
        buf.write("\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7%\3\2\2\2\u00d8\u00d9")
        buf.write("\7\35\2\2\u00d9\u00da\b\24\1\2\u00da\u00db\5\22\n\2\u00db")
        buf.write("\u00dc\7\36\2\2\u00dc\u00dd\7\r\2\2\u00dd\u00de\5\30\r")
        buf.write("\2\u00de\u00df\7\16\2\2\u00df\u00e0\b\24\1\2\u00e0\u00e1")
        buf.write("\7\4\2\2\u00e1\'\3\2\2\2\u00e2\u00e3\7!\2\2\u00e3\u00e4")
        buf.write("\7\r\2\2\u00e4\u00e5\5*\26\2\u00e5\u00e6\7\16\2\2\u00e6")
        buf.write("\u00e7\b\25\1\2\u00e7\u00e8\7\4\2\2\u00e8)\3\2\2\2\u00e9")
        buf.write("\u00ec\5\30\r\2\u00ea\u00eb\7\t\2\2\u00eb\u00ed\5*\26")
        buf.write("\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00f0")
        buf.write("\3\2\2\2\u00ee\u00f0\3\2\2\2\u00ef\u00e9\3\2\2\2\u00ef")
        buf.write("\u00ee\3\2\2\2\u00f0+\3\2\2\2\u00f1\u00f2\7\37\2\2\u00f2")
        buf.write("\u00f3\7\r\2\2\u00f3\u00f4\5.\30\2\u00f4\u00f5\7\16\2")
        buf.write("\2\u00f5\u00f6\7\4\2\2\u00f6-\3\2\2\2\u00f7\u00fa\5\60")
        buf.write("\31\2\u00f8\u00f9\7\t\2\2\u00f9\u00fb\5.\30\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb/\3\2\2\2\u00fc\u00fd")
        buf.write("\5\30\r\2\u00fd\u00fe\b\31\1\2\u00fe\u0102\3\2\2\2\u00ff")
        buf.write("\u0100\7 \2\2\u0100\u0102\b\31\1\2\u0101\u00fc\3\2\2\2")
        buf.write("\u0101\u00ff\3\2\2\2\u0102\61\3\2\2\2\u0103\u0104\t\3")
        buf.write("\2\2\u0104\63\3\2\2\2\27EOV\\sv|\u0086\u0098\u009b\u00a3")
        buf.write("\u00a6\u00ae\u00b1\u00c1\u00c6\u00d6\u00ec\u00ef\u00fa")
        buf.write("\u0101")
        return buf.getvalue()


class compilerV1Parser ( Parser ):

    grammarFileName = "compilerV1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'end'", 
                     "'var'", "':'", "','", "'int'", "'float'", "'void'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'='", "'<'", 
                     "'>'", "'!='", "'+'", "'-'", "'*'", "'/'", "'if'", 
                     "'else'", "'while'", "'do'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "ID", "INT", "FLOAT", 
                      "WS" ]

    RULE_program = 0
    RULE_vars_ = 1
    RULE_vars_helper = 2
    RULE_id_var = 3
    RULE_type_ = 4
    RULE_funcs = 5
    RULE_func = 6
    RULE_param = 7
    RULE_body = 8
    RULE_statement = 9
    RULE_assign = 10
    RULE_expression = 11
    RULE_exp = 12
    RULE_term = 13
    RULE_factor = 14
    RULE_factor_sign = 15
    RULE_condition = 16
    RULE_else_statement = 17
    RULE_cycle = 18
    RULE_f_call = 19
    RULE_f_call_exp = 20
    RULE_print_ = 21
    RULE_print_exp = 22
    RULE_print_exp_arg = 23
    RULE_cte = 24

    ruleNames =  [ "program", "vars_", "vars_helper", "id_var", "type_", 
                   "funcs", "func", "param", "body", "statement", "assign", 
                   "expression", "exp", "term", "factor", "factor_sign", 
                   "condition", "else_statement", "cycle", "f_call", "f_call_exp", 
                   "print_", "print_exp", "print_exp_arg", "cte" ]

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
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    STRING=30
    ID=31
    INT=32
    FLOAT=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compilerV1Parser.ID, 0)

        def vars_(self):
            return self.getTypedRuleContext(compilerV1Parser.Vars_Context,0)


        def funcs(self):
            return self.getTypedRuleContext(compilerV1Parser.FuncsContext,0)


        def body(self):
            return self.getTypedRuleContext(compilerV1Parser.BodyContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = compilerV1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            addFunction("global", {}, 0)
            initMainFuncQuad()
            self.state = 52
            self.match(compilerV1Parser.T__0)
            self.state = 53
            self.match(compilerV1Parser.ID)
            self.state = 54
            self.match(compilerV1Parser.T__1)
            self.state = 55
            self.vars_()
            self.state = 56
            self.funcs()
            self.state = 57
            self.match(compilerV1Parser.T__2)
            setFuncQuadStart(True)
            self.state = 59
            self.body()
            printFuncTable()
            self.state = 61
            self.match(compilerV1Parser.T__3)
            printExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vars_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_helper(self):
            return self.getTypedRuleContext(compilerV1Parser.Vars_helperContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_vars_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars_" ):
                listener.enterVars_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars_" ):
                listener.exitVars_(self)




    def vars_(self):

        localctx = compilerV1Parser.Vars_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vars_)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compilerV1Parser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(compilerV1Parser.T__4)
                self.state = 65
                self.vars_helper()
                pass
            elif token in [compilerV1Parser.T__9, compilerV1Parser.T__14]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vars_helperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._type_ = None # Type_Context

        def id_var(self):
            return self.getTypedRuleContext(compilerV1Parser.Id_varContext,0)


        def type_(self):
            return self.getTypedRuleContext(compilerV1Parser.Type_Context,0)


        def vars_helper(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compilerV1Parser.Vars_helperContext)
            else:
                return self.getTypedRuleContext(compilerV1Parser.Vars_helperContext,i)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_vars_helper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars_helper" ):
                listener.enterVars_helper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars_helper" ):
                listener.exitVars_helper(self)




    def vars_helper(self):

        localctx = compilerV1Parser.Vars_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vars_helper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.id_var()
            self.state = 70
            self.match(compilerV1Parser.T__5)
            self.state = 71
            localctx._type_ = self.type_()
            self.state = 72
            self.match(compilerV1Parser.T__1)
            addVar((None if localctx._type_ is None else self._input.getText(localctx._type_.start,localctx._type_.stop)), (None if localctx._type_ is None else localctx._type_.start).line)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 74
                    self.vars_helper() 
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(compilerV1Parser.ID, 0)

        def id_var(self):
            return self.getTypedRuleContext(compilerV1Parser.Id_varContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_id_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_var" ):
                listener.enterId_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_var" ):
                listener.exitId_var(self)




    def id_var(self):

        localctx = compilerV1Parser.Id_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_id_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            localctx._ID = self.match(compilerV1Parser.ID)
            addID((None if localctx._ID is None else localctx._ID.text))
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==compilerV1Parser.T__6:
                self.state = 82
                self.match(compilerV1Parser.T__6)
                self.state = 83
                self.id_var()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return compilerV1Parser.RULE_type_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_" ):
                listener.enterType_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_" ):
                listener.exitType_(self)




    def type_(self):

        localctx = compilerV1Parser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==compilerV1Parser.T__7 or _la==compilerV1Parser.T__8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func(self):
            return self.getTypedRuleContext(compilerV1Parser.FuncContext,0)


        def funcs(self):
            return self.getTypedRuleContext(compilerV1Parser.FuncsContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)




    def funcs(self):

        localctx = compilerV1Parser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.func()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==compilerV1Parser.T__9:
                self.state = 89
                self.funcs()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(compilerV1Parser.ID, 0)

        def param(self):
            return self.getTypedRuleContext(compilerV1Parser.ParamContext,0)


        def vars_(self):
            return self.getTypedRuleContext(compilerV1Parser.Vars_Context,0)


        def body(self):
            return self.getTypedRuleContext(compilerV1Parser.BodyContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = compilerV1Parser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(compilerV1Parser.T__9)
            self.state = 93
            localctx._ID = self.match(compilerV1Parser.ID)
            addFunction((None if localctx._ID is None else localctx._ID.text), {}, (0 if localctx._ID is None else localctx._ID.line))
            self.state = 95
            self.match(compilerV1Parser.T__10)
            self.state = 96
            self.param()
            self.state = 97
            self.match(compilerV1Parser.T__11)
            self.state = 98
            self.match(compilerV1Parser.T__12)
            self.state = 99
            self.vars_()
            setFuncQuadStart(False)
            self.state = 101
            self.body()
            setFuncQuadEnd()
            self.state = 103
            self.match(compilerV1Parser.T__13)
            self.state = 104
            self.match(compilerV1Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._type_ = None # Type_Context

        def ID(self):
            return self.getToken(compilerV1Parser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(compilerV1Parser.Type_Context,0)


        def param(self):
            return self.getTypedRuleContext(compilerV1Parser.ParamContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = compilerV1Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compilerV1Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                localctx._ID = self.match(compilerV1Parser.ID)
                addID((None if localctx._ID is None else localctx._ID.text))
                self.state = 108
                self.match(compilerV1Parser.T__5)
                self.state = 109
                localctx._type_ = self.type_()
                addVar((None if localctx._type_ is None else self._input.getText(localctx._type_.start,localctx._type_.stop)), (None if localctx._type_ is None else localctx._type_.start).line)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==compilerV1Parser.T__6:
                    self.state = 111
                    self.match(compilerV1Parser.T__6)
                    self.state = 112
                    self.param()


                pass
            elif token in [compilerV1Parser.T__11]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compilerV1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(compilerV1Parser.StatementContext,i)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = compilerV1Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(compilerV1Parser.T__14)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << compilerV1Parser.T__24) | (1 << compilerV1Parser.T__26) | (1 << compilerV1Parser.T__28) | (1 << compilerV1Parser.ID))) != 0):
                self.state = 119
                self.statement()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(compilerV1Parser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(compilerV1Parser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(compilerV1Parser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(compilerV1Parser.CycleContext,0)


        def f_call(self):
            return self.getTypedRuleContext(compilerV1Parser.F_callContext,0)


        def print_(self):
            return self.getTypedRuleContext(compilerV1Parser.Print_Context,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = compilerV1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 131
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(compilerV1Parser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(compilerV1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = compilerV1Parser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            localctx._ID = self.match(compilerV1Parser.ID)
            quadAddOperand((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line), True)
            self.state = 136
            self.match(compilerV1Parser.T__16)
            quadAddOperator("=")
            self.state = 138
            self.expression()
            quadCheckAssign()
            self.state = 140
            self.match(compilerV1Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(compilerV1Parser.ExpContext,0)


        def expression(self):
            return self.getTypedRuleContext(compilerV1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = compilerV1Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.exp()
            quadCheckBoolean()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << compilerV1Parser.T__17) | (1 << compilerV1Parser.T__18) | (1 << compilerV1Parser.T__19))) != 0):
                self.state = 150
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [compilerV1Parser.T__17]:
                    self.state = 144
                    self.match(compilerV1Parser.T__17)
                    quadAddOperator("<")
                    pass
                elif token in [compilerV1Parser.T__18]:
                    self.state = 146
                    self.match(compilerV1Parser.T__18)
                    quadAddOperator(">")
                    pass
                elif token in [compilerV1Parser.T__19]:
                    self.state = 148
                    self.match(compilerV1Parser.T__19)
                    quadAddOperator("!=")
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 152
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compilerV1Parser.TermContext,0)


        def exp(self):
            return self.getTypedRuleContext(compilerV1Parser.ExpContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = compilerV1Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.term()
            quadCheckSumOrSub()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==compilerV1Parser.T__20 or _la==compilerV1Parser.T__21:
                self.state = 161
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [compilerV1Parser.T__20]:
                    self.state = 157
                    self.match(compilerV1Parser.T__20)
                    quadAddOperator("+")
                    pass
                elif token in [compilerV1Parser.T__21]:
                    self.state = 159
                    self.match(compilerV1Parser.T__21)
                    quadAddOperator("-")
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 163
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compilerV1Parser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(compilerV1Parser.TermContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = compilerV1Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.factor()
            quadCheckMultOrDiv()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==compilerV1Parser.T__22 or _la==compilerV1Parser.T__23:
                self.state = 172
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [compilerV1Parser.T__22]:
                    self.state = 168
                    self.match(compilerV1Parser.T__22)
                    quadAddOperator("*")
                    pass
                elif token in [compilerV1Parser.T__23]:
                    self.state = 170
                    self.match(compilerV1Parser.T__23)
                    quadAddOperator("/")
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 174
                self.term()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._factor_sign = None # Factor_signContext
            self._ID = None # Token
            self._cte = None # CteContext

        def expression(self):
            return self.getTypedRuleContext(compilerV1Parser.ExpressionContext,0)


        def factor_sign(self):
            return self.getTypedRuleContext(compilerV1Parser.Factor_signContext,0)


        def ID(self):
            return self.getToken(compilerV1Parser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(compilerV1Parser.CteContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = compilerV1Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_factor)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(compilerV1Parser.T__10)
                quadAddOperator("(")
                self.state = 179
                self.expression()
                self.state = 180
                self.match(compilerV1Parser.T__11)
                quadPopOperator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                localctx._factor_sign = self.factor_sign()
                self.state = 184
                localctx._ID = self.match(compilerV1Parser.ID)
                quadAddOperand("{}{}".format((None if localctx._factor_sign is None else self._input.getText(localctx._factor_sign.start,localctx._factor_sign.stop)), (None if localctx._ID is None else localctx._ID.text)), (0 if localctx._ID is None else localctx._ID.line), True)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                localctx._factor_sign = self.factor_sign()
                self.state = 188
                localctx._cte = self.cte()
                quadAddOperand("{}{}".format((None if localctx._factor_sign is None else self._input.getText(localctx._factor_sign.start,localctx._factor_sign.stop)), (None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop))), (None if localctx._factor_sign is None else localctx._factor_sign.start).line)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factor_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return compilerV1Parser.RULE_factor_sign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_sign" ):
                listener.enterFactor_sign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_sign" ):
                listener.exitFactor_sign(self)




    def factor_sign(self):

        localctx = compilerV1Parser.Factor_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_factor_sign)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compilerV1Parser.T__20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(compilerV1Parser.T__20)
                pass
            elif token in [compilerV1Parser.T__21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(compilerV1Parser.T__21)
                pass
            elif token in [compilerV1Parser.ID, compilerV1Parser.INT, compilerV1Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(compilerV1Parser.ExpressionContext,0)


        def body(self):
            return self.getTypedRuleContext(compilerV1Parser.BodyContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(compilerV1Parser.Else_statementContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = compilerV1Parser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(compilerV1Parser.T__24)
            self.state = 199
            self.match(compilerV1Parser.T__10)
            self.state = 200
            self.expression()
            self.state = 201
            self.match(compilerV1Parser.T__11)
            quadCheckIf()
            self.state = 203
            self.body()
            self.state = 204
            self.else_statement()
            self.state = 205
            self.match(compilerV1Parser.T__1)
            quadEndIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(compilerV1Parser.BodyContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)




    def else_statement(self):

        localctx = compilerV1Parser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_else_statement)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compilerV1Parser.T__25]:
                self.enterOuterAlt(localctx, 1)
                quadCheckElse()
                self.state = 209
                self.match(compilerV1Parser.T__25)
                self.state = 210
                self.body()
                pass
            elif token in [compilerV1Parser.T__1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(compilerV1Parser.BodyContext,0)


        def expression(self):
            return self.getTypedRuleContext(compilerV1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)




    def cycle(self):

        localctx = compilerV1Parser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(compilerV1Parser.T__26)
            quadCheckWhile()
            self.state = 216
            self.body()
            self.state = 217
            self.match(compilerV1Parser.T__27)
            self.state = 218
            self.match(compilerV1Parser.T__10)
            self.state = 219
            self.expression()
            self.state = 220
            self.match(compilerV1Parser.T__11)
            quadEvaluateWhile()
            self.state = 222
            self.match(compilerV1Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(compilerV1Parser.ID, 0)

        def f_call_exp(self):
            return self.getTypedRuleContext(compilerV1Parser.F_call_expContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_f_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call" ):
                listener.enterF_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call" ):
                listener.exitF_call(self)




    def f_call(self):

        localctx = compilerV1Parser.F_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_f_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            localctx._ID = self.match(compilerV1Parser.ID)
            self.state = 225
            self.match(compilerV1Parser.T__10)
            self.state = 226
            self.f_call_exp()
            self.state = 227
            self.match(compilerV1Parser.T__11)
            quadInitFunctionCall((None if localctx._ID is None else localctx._ID.text))
            self.state = 229
            self.match(compilerV1Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_call_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(compilerV1Parser.ExpressionContext,0)


        def f_call_exp(self):
            return self.getTypedRuleContext(compilerV1Parser.F_call_expContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_f_call_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call_exp" ):
                listener.enterF_call_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call_exp" ):
                listener.exitF_call_exp(self)




    def f_call_exp(self):

        localctx = compilerV1Parser.F_call_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_f_call_exp)
        self._la = 0 # Token type
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compilerV1Parser.T__10, compilerV1Parser.T__20, compilerV1Parser.T__21, compilerV1Parser.ID, compilerV1Parser.INT, compilerV1Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.expression()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==compilerV1Parser.T__6:
                    self.state = 232
                    self.match(compilerV1Parser.T__6)
                    self.state = 233
                    self.f_call_exp()


                pass
            elif token in [compilerV1Parser.T__11]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_exp(self):
            return self.getTypedRuleContext(compilerV1Parser.Print_expContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_print_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_" ):
                listener.enterPrint_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_" ):
                listener.exitPrint_(self)




    def print_(self):

        localctx = compilerV1Parser.Print_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_print_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(compilerV1Parser.T__28)
            self.state = 240
            self.match(compilerV1Parser.T__10)
            self.state = 241
            self.print_exp()
            self.state = 242
            self.match(compilerV1Parser.T__11)
            self.state = 243
            self.match(compilerV1Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_exp_arg(self):
            return self.getTypedRuleContext(compilerV1Parser.Print_exp_argContext,0)


        def print_exp(self):
            return self.getTypedRuleContext(compilerV1Parser.Print_expContext,0)


        def getRuleIndex(self):
            return compilerV1Parser.RULE_print_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_exp" ):
                listener.enterPrint_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_exp" ):
                listener.exitPrint_exp(self)




    def print_exp(self):

        localctx = compilerV1Parser.Print_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_print_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.print_exp_arg()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==compilerV1Parser.T__6:
                self.state = 246
                self.match(compilerV1Parser.T__6)
                self.state = 247
                self.print_exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_exp_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._STRING = None # Token

        def expression(self):
            return self.getTypedRuleContext(compilerV1Parser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(compilerV1Parser.STRING, 0)

        def getRuleIndex(self):
            return compilerV1Parser.RULE_print_exp_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_exp_arg" ):
                listener.enterPrint_exp_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_exp_arg" ):
                listener.exitPrint_exp_arg(self)




    def print_exp_arg(self):

        localctx = compilerV1Parser.Print_exp_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_print_exp_arg)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compilerV1Parser.T__10, compilerV1Parser.T__20, compilerV1Parser.T__21, compilerV1Parser.ID, compilerV1Parser.INT, compilerV1Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.expression()
                quadPrintExpression()
                pass
            elif token in [compilerV1Parser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                localctx._STRING = self.match(compilerV1Parser.STRING)
                quadPrintString((None if localctx._STRING is None else localctx._STRING.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compilerV1Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(compilerV1Parser.FLOAT, 0)

        def getRuleIndex(self):
            return compilerV1Parser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)




    def cte(self):

        localctx = compilerV1Parser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            _la = self._input.LA(1)
            if not(_la==compilerV1Parser.INT or _la==compilerV1Parser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





