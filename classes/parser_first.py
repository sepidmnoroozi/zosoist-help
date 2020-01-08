import ply.yacc as yacc

import classes.lexer as l

class Parser:
    tokens = l.Lexer().tokens

    def p_program(self, p):
        '''program : macros classes'''


    def p_macros(self, p):
        """macros : macros macro"""


    def p_macros_e(self, p):
        """macros : """


    def p_macro(self, p):
        """macro : reference"""


    def p_reference(self, p):
        """reference : REFERENCE STRING"""


    def p_classes(self, p):
        """classes : classes class"""


    def p_classes_e(self, p):
        """classes : """


    def p_class(self, p):
        """class : CLASS ID LCB symbol_decs RCB"""


    def p_symbol_decs(self, p):
        """symbol_decs : symbol_decs symbol_dec"""


    def p_symbol_decs_e(self, p):
        """symbol_decs : """


    def p_symbol_dec_1(self, p):
        """symbol_dec : var_dec"""


    def p_symbol_dec_2(self, p):
        """symbol_dec : func_dec"""


    def p_var_dec(self, p):
        """var_dec : var_type var_list SEMICOLON"""


    def p_var_type_1(self, p):
        """var_type : return_type"""


    def p_var_type_2(self, p):
        """var_type : STATIC return_type"""


    def p_return_type_1(self, p):
        """return_type : INT_TYPE"""


    def p_return_type_2(self, p):
        """return_type : REAL_TYPE"""
    def p_return_type_3(self, p):
        """return_type : BOOL_TYPE"""
    def p_return_type_4(self, p):
        """return_type : STRING_TYPE"""
    def p_return_type_5(self, p):
        """return_type : ID"""

    def p_var_list_1(self, p):
        """var_list : var_list COMMA var_list_item"""
    def p_var_list_2(self, p):
        """var_list : var_list_item"""
    def p_var_list_item_1(self, p):
        """var_list_item : ID"""
    def p_var_list_item_2(self, p):
        """var_list_item : ID ASSIGNMENT exp"""

    ############2
    def p_func_dec(self, p):
        """func_dec : var_type func_body"""


    def p_func_dec_1(self, p):
        """func_dec : VOID func_body"""


    def p_func_dec_2(self, p):
        """func_dec : STATIC VOID func_body"""


    def p_func_body(self, p):
        """func_body : ID LP formal_arguments RP block"""


    def p_formal_arguments(self, p):
        """formal_arguments : formal_arguments_list"""


    def p_formal_arguments_e(self, p):
        """formal_arguments : """


    def p_formal_arguments_list(self, p):
        """formal_arguments_list : formal_arguments_list COMMA formal_argument"""


    def p_formal_arguments_list_1(self, p):
        """formal_arguments_list : formal_argument"""


    def p_formal_argument(self, p):
        """formal_argument : return_type ID"""


    def p_block(self, p):
        """block : LCB statements_list RCB"""


    def p_block_s(self, p):
        """block : statement"""


    def p_statements_list(self, p):
        """statements_list : statements_list statement"""


    def p_statements_list_e(self, p):
        """statements_list : """


    def p_statement(self, p):
        """statement : exp"""


    def p_statement_1(self, p):
        """statement : assignment"""


    def p_statement_2(self, p):
        """statement : print"""


    def p_statement_3(self, p):
        """statement : statement_var_dec"""


    def p_statement_4(self, p):
        """statement : if"""


    def p_statement_5(self, p):
        """statement : for"""


    def p_statement_6(self, p):
        """statement : while"""


    def p_statement_7(self, p):
        """statement : return"""


    def p_statement_8(self, p):
        """statement : break"""


    def p_statement_9(self, p):
        """statement : continue"""


    ############3
    def p_assignment(self, p):
        """assignment : lvalue ASSIGNMENT exp SEMICOLON"""


    def p_lvalue_1(self, p):
        """lvalue : ID"""

    def p_lvalue_2(self, p):
        """lvalue : ID DOT ID"""


    def p_print(self, p):
        """print : PRINT LP STRING RP SEMICOLON"""


    def p_statement_var_dec(self, p):
        """statement_var_dec : return_type var_list SEMICOLON"""


    def p_if(self, p):
        """if : IF LP exp RP block elseif_blocks else_block"""


    def p_elseif_blocks(self, p):
        """elseif_blocks : elseifs"""


    def p_elseif_blocks_e(self, p):
        """elseif_blocks : """


    def p_elseifs_1(self, p):
        """elseifs : elseifs elseif"""


    def p_elseifs_2(self, p):
        """elseifs : elseif"""


    def p_elseif(self, p):
        """elseif : ELSEIF LP exp RP block"""


    def p_else_block(self, p):
        """else_block : ELSE block"""


    def p_else_block_e(self, p):
        """else_block : """


    def p_for(self, p):
        """for : FOR LP ID IN exp TO exp STEPS exp RP block"""


    def p_while(self, p):
        """while : WHILE LP exp RP block"""


    def p_return(self, p):
        """return : RETURN exp SEMICOLON"""


    def p_break(self, p):
        """break : BREAK SEMICOLON"""


    def p_continue(self, p):
        """continue : CONTINUE SEMICOLON"""


    #######4
    # fourth page
    def p_exp(self, p):
        """exp : INTEGER"""


    def p_exp_1(self, p):
        """exp : REAL"""


    def p_exp_2(self, p):
        """exp : TRUE"""


    def p_exp_3(self, p):
        """exp : FALSE"""


    def p_exp_4(self, p):
        """exp : STRING"""


    def p_exp_5(self, p):
        """exp : lvalue"""


    def p_exp_6(self, p):
        """exp : binary_operation"""


    def p_exp_7(self, p):
        """exp : logical_operation"""


    def p_exp_8(self, p):
        """exp : comparison_operation"""


    def p_exp_9(self, p):
        """exp : bitwise_operation"""


    def p_exp_10(self, p):
        """exp : unary_operation"""


    def p_exp_11(self, p):
        """exp : LP exp RP"""


    def p_exp_12(self, p):
        """exp : function_call"""


    def p_binary_operation(self, p):
        """binary_operation : exp ADDITION exp """


    def p_binary_operation_1(self, p):
        """binary_operation : exp SUBTRACTION exp"""


    def p_binary_operation_2(self, p):
        """binary_operation : exp MULTIPLICATION exp"""


    def p_binary_operation_3(self, p):
        """binary_operation : exp DIVISION exp"""


    def p_binary_operation_4(self, p):
        """binary_operation : exp MODULO exp"""


    def p_binary_operation_5(self, p):
        """binary_operation : exp POWER exp"""


    def p_binary_operation_6(self, p):
        """binary_operation : exp SHIFT_LEFT exp"""


    def p_binary_operation_7(self, p):
        """binary_operation : exp SHIFT_RIGHT exp"""


    def p_logical_operation(self, p):
        """logical_operation : exp AND exp"""


    def p_logical_operation_1(self, p):
        """logical_operation : exp OR exp"""


    #######5
    def p_comparison_operation_1(self, p):
        """comparison_operation : exp LT exp"""


    def p_comparison_operation_2(self, p):
        """comparison_operation : exp LE exp"""


    def p_comparison_operation_3(self, p):
        """comparison_operation : exp GT exp"""


    def p_comparison_operation_4(self, p):
        """comparison_operation : exp GE exp"""


    def p_comparison_operation_5(self, p):
        """comparison_operation : exp EQ exp"""


    def p_comparison_operation_6(self, p):
        """comparison_operation : exp NE exp"""


    def p_bitwise_operation_1(self, p):
        """bitwise_operation : exp BITWISE_AND exp"""


    def p_bitwise_operation_2(self, p):
        """bitwise_operation : exp BITWISE_OR exp"""


    def p_unary_operation_1(self, p):
        """unary_operation : SUBTRACTION exp"""


    def p_unary_operation_2(self, p):
        """unary_operation : NOT exp"""


    def p_unary_operation_3(self, p):
        """unary_operation : BITWISE_NOT exp"""


    def p_function_call_1(self, p):
        """function_call : ID function_call_body"""


    def p_function_call_2(self, p):
        """function_call : ID DOT ID function_call_body"""


    def p_function_call_body(self, p):
        """function_call_body : LP actual_arguments RP"""


    def p_actual_arguments(self, p):
        """actual_arguments : actual_arguments_list"""


    def p_actual_arguments_e(self, p):
        """actual_arguments : """


    def p_actual_arguments_list_1(self, p):
        """actual_arguments_list : actual_arguments_list COMMA exp"""


    def p_actual_arguments_list_2(self, p):
        """actual_arguments_list : exp"""

    # def p_id_rule(self, p):
    #     """id_rule : ID"""

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser

