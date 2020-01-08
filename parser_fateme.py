import ply.yacc as yacc
import lexer # Import lexer information
tokens = lexer.tokens # Need token list

def p_program(p):
 '''program : macros classes'''


def p_macros(p):
    """macros : macros macro"""

def p_macros_e(p):
    """macros : """

def p_macro(p):
    """macro : reference"""
def p_reference(p):
    """reference : REFERENCE STRING"""
def p_classes(p):
    """classes : classes class"""
def p_classes_e(p):
    """classes : """
def p_class(p):
    """class : CLASS ID LCB  symbol_decs  RCB"""
def p_symbol_decs(p):
    """symbol_decs : symbol_decs symbol_dec"""
def p_symbol_decs_e(p):
    """symbol_decs : """
def p_symbol_dec_1(p):
    """symbol_dec : var_dec"""
def p_symbol_dec_2(p):
    """symbol_dec : func_dec"""
def p_var_dec(p):
    """var_dec : var_type var_list SEMICOLON"""
def p_var_type_1(p):
    """var_type : return_type"""
def p_var_type_2(p):
    """var_type : STATIC return_type"""
def p_return_type_1(p):
    """return_type : INT_TYPE"""
def p_return_type_2(p):
    """return_type : REAL_TYPE"""
def p_return_type_3(p):
    """return_type : BOOL_TYPE"""
def p_return_type_4(p):
    """return_type : STRING_TYPE"""
def p_return_type_5(p):
    """return_type : ID"""
def p_var_list_1(p):
    """var_list : var_list COMMA var_list_item"""
def p_var_list_2(p):
    """var_list : var_list_item"""
def p_var_list_item_1(p):
    """var_list_item : ID"""
def p_var_list_item_2(p):
    """var_list_item : ID ASSIGNMENT exp"""
############2
def p_func_dec(p):
    """func_dec : var_type func_body"""


def p_func_dec_1(p):
    """func_dec : VOID func_body"""


def p_func_dec_2(p):
    """func_dec : STATIC VOID func_body"""


def p_func_body(p):
    """func_body : ID LP formal_arguments RP block"""


def p_formal_arguments(p):
    """formal_arguments : formal_arguments_list"""


def p_formal_arguments_e(p):
    """formal_arguments : """


def p_formal_arguments_list(p):
    """formal_arguments_list : formal_arguments_list  """


def p_formal_arguments_list_1(p):
    """formal_arguments_list : formal_argument """


def p_formal_argument(p):
    """formal_argument : return_type ID """


def p_block(p):
    """block : LCB statements_list RCB """


def p_block_s(p):
    """block : statement """


def p_statements_list(p):
    """statements_list : statements_list statement"""


def p_statements_list_e(p):
    """statements_list : """


def p_statement(p):
    """statement : exp"""


def p_statement_1(p):
    """statement : assignment"""


def p_statement_2(p):
    """statement : PRINT""" 
    
def p_statement_3(p):
    """statement : statement_var_dec"""
        
def p_statement_4(p):
    """statement : IF"""

def p_statement_5(p):
    """statement : FOR"""
    
def p_statement_6(p):
    """statement : WHILE"""
    
def p_statement_7(p):
    """statement : RETURN"""
    
def p_statement_8(p):
    """statement : BREAK"""
    
def p_statement_9(p):
    """statement : CONTINUE"""
    
############3
def p_assignment(p):
    """assignment : lvalue ASSIGNMENT exp SEMICOLON"""
def p_lvalue_1(p):
    """lvalue : ID"""
def p_lvalue_2(p):
    """lvalue : ID DOT ID"""
def p_print(p):
    """print : PRINT LP STRING RP SEMICOLON"""
def p_statement_var_dec(p):
    """statement_var_dec : return_type var_list SEMICOLON"""
def p_if(p):
    """if : IF LP exp RP block elseif_blocks else_block"""
def p_elseif_blocks(p):
    """elseif_blocks : elseifs"""
def p_elseif_blocks_e(p):
    """elseif_blocks : """
def p_elseifs_1(p):
    """elseifs : elseifs elseif """
def p_elseifs_2(p):
    """elseifs : elseif """
def p_elseif(p):
    """elseif : ELSEIF LP exp RP block """
def p_else_block(p):
    """else_block : ELSE block """
def p_else_block_e(p):
    """else_block : """
def p_for(p):
    """for : FOR LP ID IN exp TO exp STEPS exp RP block """
def p_while(p):
    """while : WHILE LP exp RP block """
def p_return(p):
    """return : RETURN exp SEMICOLON """
def p_break(p):
    """break : BREAK SEMICOLON """
def p_continue(p):
    """continue : CONTINUE SEMICOLON """
#######4
# fourth page
def p_exp(p):
    """exp : INTEGER """


def p_exp_1(p):
    """exp : REAL """


def p_exp_2(p):
    """exp : TRUE """


def p_exp_3(p):
    """exp : FALSE """


def p_exp_4(p):
    """exp : STRING"""


def p_exp_5(p):
    """exp : lvalue"""


def p_exp_6(p):
    """exp : binary_operation"""


def p_exp_7(p):
    """exp : logical_operation"""


def p_exp_8(p):
    """exp : comparison_operation"""


def p_exp_9(p):
    """exp : bitwise_operation"""


def p_exp_10(p):
    """exp : unary_operation"""


def p_exp_11(p):
    """exp : LP exp RP """


def p_exp_12(p):
    """exp : function_call"""


def p_binary_operation(p):
    """binary_operation : exp ADDITION exp """

def p_binary_operation_1(p):
    """binary_operation : exp SUBTRACTION exp"""

def p_binary_operation_2(p):
    """binary_operation : exp MULTIPLICATION exp"""
    
def p_binary_operation_3(p):
    """binary_operation : exp DIVISION exp"""

def p_binary_operation_4(p):
    """binary_operation : exp MODULO exp"""
    
def p_binary_operation_5(p):
    """binary_operation : exp POWER exp"""
    
def p_binary_operation_6(p):
    """binary_operation : exp SHIFT_LEFT exp"""
    
def p_binary_operation_7(p):
    """binary_operation : exp SHIFT_RIGHT exp"""

def p_logical_operation(p):
    """logical_operation : exp AND exp"""
    
def p_logical_operation_1(p):
    """logical_operation : exp OR exp"""


#######5
def p_comparison_operation_1(p):
    """comparison_operation : exp LT exp"""
def p_comparison_operation_2(p):
    """comparison_operation : exp LE exp"""
def p_comparison_operation_3(p):
    """comparison_operation : exp GT exp"""
def p_comparison_operation_4(p):
    """comparison_operation : exp GE exp"""
def p_comparison_operation_5(p):
    """comparison_operation : exp EQ exp"""
def p_comparison_operation_6(p):
    """comparison_operation : exp NE exp"""
def p_bitwise_operation_1(p):
    """bitwise_operation : exp BITWISE_AND exp"""
def p_bitwise_operation_2(p):
    """bitwise_operation : exp BITWISE_OR exp"""
def p_unary_operation_1(p):
    """unary_operation : SUBTRACTION exp"""
def p_unary_operation_2(p):
    """unary_operation : NOT exp"""
def p_unary_operation_3(p):
    """unary_operation : BITWISE_NOT exp"""
def p_function_call_1(p):
    """function_call : ID function_call_body"""
def p_function_call_2(p):
    """function_call : ID DOT ID function_call_body"""

def p_function_call_body(p):
    """function_call_body : LP actual_arguments RP """


def p_actual_arguments(p):
    """actual_arguments : actual_arguments_list"""


def p_actual_arguments_e(p):
    """actual_arguments : """


def p_actual_arguments_list_1(p):
    """actual_arguments_list : actual_arguments_list COMMA exp"""


def p_actual_arguments_list_2(p):
    """actual_arguments_list : exp"""


yacc.yacc()
path = "mainInput.txt"
f = open(path, 'r')
text = f.read()
f.close()
yacc.parse(text, lexer.build(), debug=False)
# Parse some text
