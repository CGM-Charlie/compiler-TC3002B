# Generated from compilerV1.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compilerV1Parser import compilerV1Parser
else:
    from compilerV1Parser import compilerV1Parser
 
from variableTable import *


# This class defines a complete listener for a parse tree produced by compilerV1Parser.
class compilerV1Listener(ParseTreeListener):

    # Enter a parse tree produced by compilerV1Parser#program.
    def enterProgram(self, ctx:compilerV1Parser.ProgramContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#program.
    def exitProgram(self, ctx:compilerV1Parser.ProgramContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#vars_.
    def enterVars_(self, ctx:compilerV1Parser.Vars_Context):
        pass

    # Exit a parse tree produced by compilerV1Parser#vars_.
    def exitVars_(self, ctx:compilerV1Parser.Vars_Context):
        pass


    # Enter a parse tree produced by compilerV1Parser#vars_helper.
    def enterVars_helper(self, ctx:compilerV1Parser.Vars_helperContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#vars_helper.
    def exitVars_helper(self, ctx:compilerV1Parser.Vars_helperContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#id_var.
    def enterId_var(self, ctx:compilerV1Parser.Id_varContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#id_var.
    def exitId_var(self, ctx:compilerV1Parser.Id_varContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#type_.
    def enterType_(self, ctx:compilerV1Parser.Type_Context):
        pass

    # Exit a parse tree produced by compilerV1Parser#type_.
    def exitType_(self, ctx:compilerV1Parser.Type_Context):
        pass


    # Enter a parse tree produced by compilerV1Parser#funcs.
    def enterFuncs(self, ctx:compilerV1Parser.FuncsContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#funcs.
    def exitFuncs(self, ctx:compilerV1Parser.FuncsContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#func.
    def enterFunc(self, ctx:compilerV1Parser.FuncContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#func.
    def exitFunc(self, ctx:compilerV1Parser.FuncContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#param.
    def enterParam(self, ctx:compilerV1Parser.ParamContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#param.
    def exitParam(self, ctx:compilerV1Parser.ParamContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#body.
    def enterBody(self, ctx:compilerV1Parser.BodyContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#body.
    def exitBody(self, ctx:compilerV1Parser.BodyContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#statement.
    def enterStatement(self, ctx:compilerV1Parser.StatementContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#statement.
    def exitStatement(self, ctx:compilerV1Parser.StatementContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#assign.
    def enterAssign(self, ctx:compilerV1Parser.AssignContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#assign.
    def exitAssign(self, ctx:compilerV1Parser.AssignContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#expression.
    def enterExpression(self, ctx:compilerV1Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#expression.
    def exitExpression(self, ctx:compilerV1Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#exp.
    def enterExp(self, ctx:compilerV1Parser.ExpContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#exp.
    def exitExp(self, ctx:compilerV1Parser.ExpContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#term.
    def enterTerm(self, ctx:compilerV1Parser.TermContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#term.
    def exitTerm(self, ctx:compilerV1Parser.TermContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#factor.
    def enterFactor(self, ctx:compilerV1Parser.FactorContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#factor.
    def exitFactor(self, ctx:compilerV1Parser.FactorContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#factor_sign.
    def enterFactor_sign(self, ctx:compilerV1Parser.Factor_signContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#factor_sign.
    def exitFactor_sign(self, ctx:compilerV1Parser.Factor_signContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#condition.
    def enterCondition(self, ctx:compilerV1Parser.ConditionContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#condition.
    def exitCondition(self, ctx:compilerV1Parser.ConditionContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#else_statement.
    def enterElse_statement(self, ctx:compilerV1Parser.Else_statementContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#else_statement.
    def exitElse_statement(self, ctx:compilerV1Parser.Else_statementContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#cycle.
    def enterCycle(self, ctx:compilerV1Parser.CycleContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#cycle.
    def exitCycle(self, ctx:compilerV1Parser.CycleContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#f_call.
    def enterF_call(self, ctx:compilerV1Parser.F_callContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#f_call.
    def exitF_call(self, ctx:compilerV1Parser.F_callContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#f_call_exp.
    def enterF_call_exp(self, ctx:compilerV1Parser.F_call_expContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#f_call_exp.
    def exitF_call_exp(self, ctx:compilerV1Parser.F_call_expContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#print_.
    def enterPrint_(self, ctx:compilerV1Parser.Print_Context):
        pass

    # Exit a parse tree produced by compilerV1Parser#print_.
    def exitPrint_(self, ctx:compilerV1Parser.Print_Context):
        pass


    # Enter a parse tree produced by compilerV1Parser#print_exp.
    def enterPrint_exp(self, ctx:compilerV1Parser.Print_expContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#print_exp.
    def exitPrint_exp(self, ctx:compilerV1Parser.Print_expContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#print_exp_arg.
    def enterPrint_exp_arg(self, ctx:compilerV1Parser.Print_exp_argContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#print_exp_arg.
    def exitPrint_exp_arg(self, ctx:compilerV1Parser.Print_exp_argContext):
        pass


    # Enter a parse tree produced by compilerV1Parser#cte.
    def enterCte(self, ctx:compilerV1Parser.CteContext):
        pass

    # Exit a parse tree produced by compilerV1Parser#cte.
    def exitCte(self, ctx:compilerV1Parser.CteContext):
        pass



del compilerV1Parser