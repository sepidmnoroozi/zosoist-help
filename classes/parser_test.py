from classes.code_generator import CodeGenerator

import classes.lexer as l
from classes.nonterminal import Nonterminal

#start

import ply.yacc as yacc

import lexer as l

class Parser:
    def __init__(self):
        self.t_counter = -1
        self.l_counter = -1
        self.code_generator = CodeGenerator()
        self.code_list = []

    tokens = l.tokens
    def p_program(self, p):
        '''program : macros classes'''
        print('''program -> macros classes''')

    def p_macros(self, p):
        """macros : macros macro"""
        print("""macros -> macros macro""")

    def p_macros_e(self, p):
        """macros : """
        print("""macros ->/* Lambda */""")

    def p_macro(self, p):
        """macro : reference"""
        print("""macro -> reference""")

    def p_reference(self, p):
        """reference : REFERENCE STRING"""
        print("""reference -> REFERENCE STRING""")

    def p_classes(self, p):
        """classes : classes class"""
        print("""classes -> classes class""")

    def p_classes_e(self, p):
        """classes : """
        print("""classes ->/* Lambda */""")

    def p_class(self, p):
        """class : CLASS ID LCB symbol_decs RCB"""
        print("""class -> CLASS ID LCB symbol_decs RCB""")

    def p_symbol_decs(self, p):
        """symbol_decs : symbol_decs symbol_dec"""
        print("""symbol_decs -> symbol_decs symbol_dec""")

    def p_symbol_decs_e(self, p):
        """symbol_decs : """
        print("""symbol_decs ->/* Lambda */""")

    def p_symbol_dec_1(self, p):
        """symbol_dec : var_dec"""
        print("""symbol_dec -> var_dec""")

    def p_symbol_dec_2(self, p):
        """symbol_dec : func_dec"""
        print("""symbol_dec -> func_dec""")

    def p_var_dec(self, p):
        """var_dec : var_type var_list SEMICOLON"""
        print("""var_dec -> var_type var_list SEMICOLON""")

    def p_var_type_1(self, p):
        """var_type : return_type"""
        print("""var_type -> return_type""")

    # lvalue1
    def p_var_type_1_1(self, p):
        """var_type : lvalue1"""
        print("""var_type -> lvalue1""")

    def p_var_type_2(self, p):
        """var_type : STATIC return_type"""
        print("""var_type -> STATIC return_type""")

    def p_var_type_2_1(self, p):
        """var_type : STATIC lvalue1"""
        print("""var_type -> STATIC lvalue1""")

    def p_return_type_1(self, p):
        """return_type : INT_TYPE"""
        print("""return_type -> INT_TYPE""")

    def p_return_type_2(self, p):
        """return_type : REAL_TYPE"""
        print("""return_type -> REAL_TYPE""")

    def p_return_type_3(self, p):
        """return_type : BOOL_TYPE"""
        print("""return_type -> BOOL_TYPE""")

    def p_return_type_4(self, p):
        """return_type : STRING_TYPE"""
        print("""return_type -> STRING_TYPE""")

    # def p_return_type_5(self, p):
    #     """return_type : ID"""

    def p_var_list_1(self, p):
        """var_list : var_list COMMA var_list_item"""
        p[0] = Nonterminal()
        print("""var_list -> var_list COMMA var_list_item""")

    def p_var_list_2(self, p):
        """var_list : var_list_item"""
        print("""var_list -> var_list_item""")

    def p_item1(self, p):
        """item1 : ID ASSIGNMENT exp"""
        print("""item1 -> ID ASSIGNMENT exp""")

    def p_var_list_item_2(self, p):
        """var_list_item : item1"""
        print("""var_list_item -> item1""")

    def p_var_list_item_1(self, p):
        """var_list_item : ID"""
        p[0] = Nonterminal()
        p[0].value = p[1]
        print("""var_list_item -> ID""")

    ############2
    def p_func_dec(self, p):
        """func_dec : var_type func_body"""
        print("""func_dec -> var_type func_body""")

    def p_func_dec_1(self, p):
        """func_dec : VOID func_body"""
        print("""func_dec -> VOID func_body""")

    def p_func_dec_2(self, p):
        """func_dec : STATIC VOID func_body"""
        print("""func_dec -> STATIC VOID func_body""")

    def p_func_body(self, p):
        """func_body : ID LP formal_arguments RP block"""
        print("""func_body -> ID LP formal_arguments RP block""")

    def p_formal_arguments(self, p):
        """formal_arguments : formal_arguments_list"""
        print("""formal_arguments -> formal_arguments_list""")

    def p_formal_arguments_e(self, p):
        """formal_arguments : """
        print("""formal_arguments ->/* Lambda */""")

    def p_formal_arguments_list(self, p):
        """formal_arguments_list : formal_arguments_list COMMA formal_argument"""
        print("""formal_arguments_list -> formal_arguments_list COMMA formal_argument""")

    def p_formal_arguments_list_1(self, p):
        """formal_arguments_list : formal_argument"""
        print("""formal_arguments_list -> formal_argument""")

    def p_formal_argument(self, p):
        """formal_argument : return_type ID"""
        print("""formal_argument -> return_type ID""")

    # lvalue1
    def p_formal_argument_1(self, p):
        """formal_argument : lvalue1 ID"""
        print("""formal_argument -> lvalue1 ID""")

    def p_block(self, p):
        """block : LCB statements_list RCB"""
        p[0] = p[2]
        print("""block -> LCB statements_list RCB""")

    def p_block_s(self, p):
        """block : statement"""
        p[0] = p[1]
        print("""block -> statement""")

    def p_statements_list(self, p):
        """statements_list : statements_list statement"""
        print("""statements_list -> statements_list statement""")
        p[0] = Nonterminal()
        p[0].code = p[1].code + p[2].code
        # print(p[0].code)

    def p_statements_list_e(self, p):
        """statements_list : """
        p[0] = Nonterminal()
        p[0].code = ""
        print("""statements_list ->/* Lambda */""")

    def p_statement(self, p):
        """statement : SEMICOLON"""
        p[0] = Nonterminal()
        print("""statement -> SEMICOLON""")

    def p_statement0(self, p):
        """statement : exp SEMICOLON"""
        p[0] = p[1]
        # %prec EXPE
        print("""statement -> exp""")

    def p_statement_1(self, p):
        """statement : assignment"""
        p[0] = p[1]
        print("""statement -> assignment""")

    def p_statement_2(self, p):
        """statement : print"""
        print("""statement -> print""")

    def p_statement_3(self, p):
        """statement : statement_var_dec"""
        p[0] = p[1]
        print("""statement -> statement_var_dec""")

    def p_statement_4(self, p):
        """statement : if"""
        p[0] = p[1]
        print("""statement -> if""")

    def p_statement_5(self, p):
        """statement : for"""
        p[0] = p[1]
        print("""statement -> for""")

    def p_statement_6(self, p):
        """statement : while"""
        p[0] = p[1]
        print("""statement -> while""")

    def p_statement_7(self, p):
        """statement : return"""
        print("""statement -> return""")

    def p_statement_8(self, p):
        """statement : break"""
        print("""statement -> break""")

    def p_statement_9(self, p):
        """statement : continue"""
        print("""statement -> continue""")

    ############3
    def p_assignment(self, p):
        """assignment : lvalue ASSIGNMENT exp SEMICOLON"""
        # print("""assignment -> lvalue ASSIGNMENT exp SEMICOLON""")
        p[0] = Nonterminal()

        if p[3].place != "":
            p[0].code = "L" + str(len(self.code_list)) + ": " + p[1].value + "=" + p[3].place + ";"
            p[0].address = len(self.code_list)
            self.code_list.append(p[0].code)
            print(self.code_list)
        elif p[3].value != "":
            p[0].code = "L" + str(len(self.code_list)) + ": " + p[1].value + "=" + p[3].value + ";"
            p[0].address = len(self.code_list)
            self.code_list.append(p[0].code)
            print(self.code_list)
        else:
            true_label = len(self.code_list)
            false_label = true_label + 2

            c = "L" + str(true_label) + ": " + p[1].value + "=" + "true" + ";"
            self.code_list.append(c)
            d = "L" + str(len(self.code_list)) + ": " + "goto " + str(false_label + 1) + ";"
            self.code_list.append(d)

            c = "L" + str(false_label) + ": " + p[1].value + "=" + "false" + ";"
            self.code_list.append(c)

            d = "L" + str(false_label + 1) + ": "
            self.code_list.append(d)

            for code in self.code_list:
                index = self.code_list.index(code)
                if "goto" in code and "_" in code:
                    if "if" in code:
                        new_code = code.replace("_", "L" + str(true_label))
                        self.code_list[index] = new_code
                    else:
                        new_code = code.replace("_", "L" + str(false_label))
                        self.code_list[index] = new_code

            print(self.code_list)

    def p_lvalue_1(self, p):
        """lvalue : lvalue1 %prec LVALI"""
        p[0] = p[1]
        print("""lvalue -> lvalue1""")

    def p_lvalue_2(self, p):
        """lvalue : lvalue2 %prec LVAL"""
        print("""lvalue -> lvalue2""")

    def p_lval2(self, p):
        """lvalue2 : ID DOT ID"""
        print("""lvalue2 -> ID DOT ID""")

    def p_lval1(self, p):
        """lvalue1 : ID"""
        p[0] = Nonterminal()
        p[0].value = p[1]
        print("""lvalue1 -> ID""")

    def p_print(self, p):
        """print : PRINT LP STRING RP SEMICOLON"""
        print("""print -> PRINT LP STRING RP SEMICOLON""")

    def p_statement_var_dec(self, p):
        """statement_var_dec : return_type var_list SEMICOLON"""
        p[0] = Nonterminal()
        print("""statement_var_dec -> return_type var_list SEMICOLON""")

    def p_statement_var_dec_1(self, p):
        """statement_var_dec : lvalue1 var_list SEMICOLON"""
        print("""statement_var_dec -> lvalue1 var_list SEMICOLON""")

    # lvalue1
    def p_m(self, p):
        """m : """
        p[0] = Nonterminal()
        p[0].quad = len(self.code_list)

    def p_n(self, p):
        """n : """

    def p_if_1(self, p):
        """if : IF LP exp RP block %prec IF"""
        print("""if -> IF LP exp RP block""")
        print("***************************************************")
        p[0] = Nonterminal()
        print(p[3].true_list)
        print(p[5].code)

        token_list = p[5].code.split(':')
        self.backpatch(p[3].true_list, token_list[0])

        token_list = token_list[-2].split(";")
        # print(token_list[-1])

        num = int(token_list[-1].replace("L", ""))
        num = num + 1

        self.backpatch(p[3].false_list, "L"+ str(len(self.code_list)))
        code = "L"+ str(len(self.code_list)) + ": "
        self.code_list.append(code)

        print(self.code_list)


    def p_if_2(self, p):
        """if : IF LP exp RP block ELSE block %prec ELSE"""
        #%prec IF2
        print("""if -> IF LP exp RP block ELSE block""")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        p[0] = Nonterminal()
        print("true list")
        print(p[3].true_list)
        print("false list")
        print(p[3].false_list)
        print("if code")
        print(p[5].code)
        true_code = p[5].code
        print("else code")
        false_code = p[7].code
        print(p[7].code)

        token_list = true_code.split(':')
        self.backpatch(p[3].true_list, token_list[0])
        #
        token_list = false_code.split(':')
        self.backpatch(p[3].false_list, token_list[0])

        print(self.code_list)

    def p_if_3(self, p):
        """if : IF LP exp RP block elseifs %prec prec2"""
        print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        p[0] = Nonterminal()
        p[0].list = []
        p[3].list = []
        p[3].list.append(p[3].true_list)
        p[3].list.append(p[3].false_list)

        num_of_elseifs = len(p[6].list)

        p[0].list = p[6].list
        p[0].list.insert(0, p[3].list)
        # print(p[0].list)
        p[0].code_list = p[6].code
        p[0].code_list.insert(0, p[5].code)
        # print(p[0].code)

        next_code_label = str(self.get_num_of_last_label(p[0].code_list[-1]) + 1)
        code = "L" + next_code_label + ": "
        self.code_list.append(code)

        if_list = p[0].list[0]
        self.backpatch(if_list[0], self.get_start(p[0].code_list[0]))
        self.backpatch(if_list[1], "L" + str(p[0].list[1][0][0]))

        for i in range(1, num_of_elseifs + 1):
            c = p[0].code_list[i]
            c_list = c.split(";")
            code_in_code_list = c_list[-2] + ";"
            index = self.code_list.index(code_in_code_list)
            new_code_in_code_list = code_in_code_list + "goto" + "L" + next_code_label
            self.code_list.insert(index, new_code_in_code_list)
            self.code_list.pop(index + 1)
            c = c + "goto " + "L" + next_code_label
            p[0].code_list[i] = c

        for i in range(1, num_of_elseifs + 1):
            list = p[0].list[i]
            self.backpatch(list[0], self.get_start(p[0].code_list[i]))
            if i == num_of_elseifs:
                self.backpatch(list[1], self.get_start(p[0].code_list[-1]))
            else:
                self.backpatch(list[1], code)

        print(self.code_list)
        print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

    def p_if_4(self, p):
        """if : IF LP exp RP block elseifs ELSE block %prec prec1"""
        print("""if -> IF LP exp RP block elseifs ELSE block""")
        print("heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        p[0] = Nonterminal()
        p[0].list = []
        p[3].list = []
        p[3].list.append(p[3].true_list)
        p[3].list.append(p[3].false_list)

        num_of_elseifs = len(p[6].list)

        p[0].list = p[6].list
        p[0].list.insert(0, p[3].list)
        # print(p[0].list)
        p[0].code_list = p[6].code
        p[0].code_list.insert(0, p[5].code)
        p[0].code_list.insert(len(p[0].code_list), p[8].code)
        # print(p[0].code)

        next_code_label = str(self.get_num_of_last_label(p[0].code_list[-1])+1)
        code = "L"+next_code_label+": "
        self.code_list.append(code)

        if_list = p[0].list[0]
        self.backpatch(if_list[0], self.get_start(p[0].code_list[0]))
        self.backpatch(if_list[1], "L" + str(p[0].list[1][0][0]))

        for i in range(1, num_of_elseifs+1):
            c = p[0].code_list[i]
            c_list = c.split(";")
            code_in_code_list = c_list[-2]+";"
            index = self.code_list.index(code_in_code_list)
            new_code_in_code_list = code_in_code_list + "goto" + "L"+next_code_label
            self.code_list.insert(index, new_code_in_code_list)
            self.code_list.pop(index+1)
            c = c + "goto " + "L"+next_code_label
            p[0].code_list[i] = c

        for i in range(1, num_of_elseifs + 1):
            list = p[0].list[i]
            self.backpatch(list[0], self.get_start(p[0].code_list[i]))
            if i == num_of_elseifs:
                self.backpatch(list[1], self.get_start(p[0].code_list[-1]))
            else:
                self.backpatch(list[1], "L" + str(p[0].list[i + 1][0][0]))

        print(self.code_list)

    def p_elseifs_1(self, p):
        """elseifs : elseifs elseif"""
        print("""elseifs -> elseifs elseif""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].code.append(p[2].code)
        p[0].list = p[1].list
        p[0].list.append(p[2].list)
        # print(p[0].list)
        # print(p[0].code)



    def p_elseifs_2(self, p):
        """elseifs : elseif"""
        print("""elseifs -> elseif""")
        p[0] = Nonterminal()
        p[0].code = []
        p[0].code.append(p[1].code)
        p[0].list = []
        p[0].list.append(p[1].list)
        # print("))))))))))))))))))))))))))))))))))))))))))))))")
        # print(p[0].list)
        # print(p[0].code)



    def p_elseif(self, p):
        """elseif : ELSEIF LP exp RP block %prec ELSEIF"""
        print("""elseif -> ELSEIF LP exp RP block""")
        # print("true_list")
        # print(p[3].true_list)
        # print("false_list")
        # print(p[3].false_list)
        # print("code block")
        # print(p[5].code)

        p[0] = Nonterminal()
        p[0].code = p[5].code
        p[0].list = []
        p[0].list.append(p[3].true_list)
        p[0].list.append(p[3].false_list)
        # print("****************************")
        # print(p[0].list)


        # p[0].pure_code_list




    def p_for(self, p):
        """for : FOR LP ID IN exp TO exp STEPS exp RP block"""
        print("""for -> FOR LP ID IN exp TO exp STEPS exp RP block""")

    def p_while(self, p):
        """while : WHILE LP exp RP block"""
        print("""while -> WHILE LP exp RP block""")

    def p_return(self, p):
        """return : RETURN exp SEMICOLON"""
        print("""return -> RETURN exp SEMICOLON""")

    def p_break(self, p):
        """break : BREAK SEMICOLON"""
        print("""break -> BREAK SEMICOLON""")

    def p_continue(self, p):
        """continue : CONTINUE SEMICOLON"""
        print("""continue -> CONTINUE SEMICOLON""")

    #######4
    # fourth page
    def p_exp(self, p):
        """exp : INTEGER"""
        print("""exp -> INTEGER""")
        p[0] = Nonterminal()
        p[0].type = "int"
        p[0].value = p[1]

    def p_exp_1(self, p):
        """exp : REAL"""
        p[0] = Nonterminal()
        p[0].type = "real"
        p[0].value = p[1]
        # print("""exp -> REAL""")

    def p_exp_2(self, p):
        """exp : TRUE"""
        p[0] = Nonterminal()
        p[0].type = "bool"
        next_quad = len(self.code_list)
        p[0].true_list = [next_quad]
        p[0].m = next_quad + 1
        code = "L" + str(next_quad) + ": " + "goto _" + ";"
        self.code_list.append(code)
        # print("""exp -> TRUE""")

    def p_exp_3(self, p):
        """exp : FALSE"""
        # print("""exp -> FALSE""")
        p[0] = Nonterminal()
        next_quad = len(self.code_list)
        p[0].false_list = [next_quad]
        p[0].m = next_quad + 1
        code = "L" + str(next_quad) + ": " + "goto _" + ";"
        self.code_list.append(code)

    def p_exp_4(self, p):
        """exp : STRING"""
        print("""exp -> STRING""")

    def p_exp_5(self, p):
        """exp : lvalue"""
        p[0] = p[1]
        # print("""exp -> lvalue""")

    def p_exp_6(self, p):
        """exp : binary_operation %prec BIOP"""
        p[0] = p[1]
        # print("""exp -> binary_operation""")

    def p_exp_7(self, p):
        """exp : logical_operation"""
        p[0] = p[1]
        # print("""exp -> logical_operation""")

    def p_exp_8(self, p):
        """exp : comparison_operation %prec COMOP"""
        p[0] = p[1]
        # print("""exp -> comparison_operation""")

    def p_exp_9(self, p):
        """exp : bitwise_operation %prec BITOP"""
        print("""exp -> bitwise_operation""")

    def p_exp_10(self, p):
        """exp : unary_operation"""
        p[0] = p[1]
        # print("""exp -> unary_operation""")

    def p_exp_11(self, p):
        """exp : LP exp RP"""
        p[0] = p[1]
        # print("""exp -> LP exp RP""")

    def p_exp_12(self, p):
        """exp : function_call"""
        print("""exp -> function_call""")

    def p_binary_operation(self, p):
        """binary_operation : exp ADDITION exp """
        print("""binary_operation -> exp ADDITION exp """)
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_binary_operation_1(self, p):
        """binary_operation : exp SUBTRACTION exp"""
        print("""binary_operation -> exp SUBTRACTION exp""")
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_binary_operation_2(self, p):
        """binary_operation : exp MULTIPLICATION exp"""
        print("""binary_operation -> exp MULTIPLICATION exp""")
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_binary_operation_3(self, p):
        """binary_operation : exp DIVISION exp"""
        print("""binary_operation -> exp DIVISION exp""")
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_binary_operation_4(self, p):
        """binary_operation : exp MODULO exp"""
        print("""binary_operation -> exp MODULO exp""")
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_binary_operation_5(self, p):
        """binary_operation : exp POWER exp"""
        print("""binary_operation -> exp POWER exp""")
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_binary_operation_6(self, p):
        """binary_operation : exp SHIFT_LEFT exp"""
        print("""binary_operation -> exp SHIFT_LEFT exp""")
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_binary_operation_7(self, p):
        """binary_operation : exp SHIFT_RIGHT exp"""
        print("""binary_operation -> exp SHIFT_RIGHT exp""")
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_logical_operation(self, p):
        """logical_operation : exp AND exp"""
        print("""logical_operation -> exp AND exp""")
        p[0] = Nonterminal()
        m = p[1].m
        self.backpatch(p[1].true_list, m)
        p[0].false_list = p[1].false_list + p[3].false_list
        p[0].true_list = p[3].true_list

        p[0].code = self.code_list
        print(self.code_list)

    def p_logical_operation_1(self, p):
        """logical_operation : exp OR exp"""
        print("""logical_operation -> exp OR exp""")
        p[0] = Nonterminal()
        m = p[1].m
        self.backpatch(p[1].false_list, m)
        p[0].true_list = p[1].true_list + p[3].true_list
        p[0].false_list = p[3].false_list

        p[0].code = self.code_list
        print(self.code_list)

    #######5
    def p_comparison_operation_1(self, p):
        """comparison_operation : exp LT exp"""
        print("""comparison_operation -> exp LT exp""")
        self.code_generator.generate_boolean_code(p, self.code_list)

    def p_comparison_operation_2(self, p):
        """comparison_operation : exp LE exp"""
        print("""comparison_operation -> exp LE exp""")
        self.code_generator.generate_boolean_code(p, self.code_list)

    def p_comparison_operation_3(self, p):
        """comparison_operation : exp GT exp"""
        print("""comparison_operation -> exp GT exp""")
        self.code_generator.generate_boolean_code(p, self.code_list)

    def p_comparison_operation_4(self, p):
        """comparison_operation : exp GE exp"""
        print("""comparison_operation -> exp GE exp""")
        self.code_generator.generate_boolean_code(p, self.code_list)

    def p_comparison_operation_5(self, p):
        """comparison_operation : exp EQ exp"""
        print("""comparison_operation -> exp EQ exp""")
        self.code_generator.generate_boolean_code(p, self.code_list)

    def p_comparison_operation_6(self, p):
        """comparison_operation : exp NE exp"""
        print("""comparison_operation -> exp NE exp""")
        self.code_generator.generate_boolean_code(p, self.code_list)

    def p_bitwise_operation_1(self, p):
        """bitwise_operation : exp BITWISE_AND exp"""
        print("""bitwise_operation -> exp BITWISE_AND exp""")
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_bitwise_operation_2(self, p):
        """bitwise_operation : exp BITWISE_OR exp"""
        print("""bitwise_operation -> exp BITWISE_OR exp""")
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_unary_operation_1(self, p):
        """unary_operation : SUBTRACTION exp %prec UMINUS"""
        print("""unary_operation -> SUBTRACTION exp""")
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_unary_operation_2(self, p):
        """unary_operation : NOT exp"""
        print("""unary_operation -> NOT exp""")
        p[0] = Nonterminal()
        p[0].place = self.new_temp()
        arg1 = p[1]
        arg2 = p[2].value
        p[0].code = "L" + str(len(self.code_list)) + ": " + p[0].place + "=" + arg1 + arg2 + ";"

        self.code_list.append(p[0].code)
        print(self.code_list)

    def p_unary_operation_3(self, p):
        """unary_operation : BITWISE_NOT exp"""
        print("""unary_operation -> BITWISE_NOT exp""")
        self.code_generator.generate_arithmetic_code(p, self.new_temp(), self.code_list)

    def p_function_call_2(self, p):
        """function_call : lvalue2 function_call_body"""
        print("""function_call -> lvalue2 function_call_body""")

    def p_function_call_1(self, p):
        """function_call : lvalue1 function_call_body"""
        print("""function_call -> lvalue1 function_call_body""")

    def p_function_call_body(self, p):
        """function_call_body : LP actual_arguments RP"""
        print("""function_call_body -> LP actual_arguments RP""")

    def p_actual_arguments(self, p):
        """actual_arguments : actual_arguments_list"""
        print("""actual_arguments -> actual_arguments_list""")

    def p_actual_arguments_e(self, p):
        """actual_arguments : """
        print("""actual_arguments ->/* Lambda */""")

    def p_actual_arguments_list_1(self, p):
        """actual_arguments_list : actual_arguments_list COMMA exp"""
        print("""actual_arguments_list -> actual_arguments_list COMMA exp""")

    def p_actual_arguments_list_2(self, p):
        """actual_arguments_list : exp"""
        print("""actual_arguments_list -> exp""")

    # def p_id_rule(self, p):
    #     """id_rule : ID"""


    precedence = (
        ('nonassoc', 'prec2'),
        ('nonassoc', 'prec1'),
        ('nonassoc', 'LVALI'),
        ('nonassoc', 'LVAL'),
        ('nonassoc', 'BIOP'),
        ('nonassoc', 'COMOP'),
        ('nonassoc', 'BITOP'),
        ('left', 'IF'),
        ('left', 'ELSE'),
        ('left', 'ELSEIF'),
        ('left', 'COMMA'),
        ('left', 'ASSIGNMENT'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'NOT'),
        ('left', 'BITWISE_OR'),
        ('left', 'BITWISE_AND'),
        ('left', 'BITWISE_NOT'),
        ('left', 'LE', 'EQ', 'NE', 'GE', 'GT', 'LT'),
        # ('left', 'SHIFT_LEFT', 'SHIFT_RIGHT'),
        ('left', 'ADDITION', 'SUBTRACTION'),
        ('left', 'MULTIPLICATION', 'DIVISION'),
        ('left', 'SHIFT_LEFT', 'SHIFT_RIGHT'),
        ('left', 'POWER'),
        ('left', 'MODULO'),
        ('left', 'UMINUS'),
        ('left', 'RP', 'LP'),

    )

    def new_temp(self):
        self.t_counter += 1
        return "TT" + str(self.t_counter)

    def new_label(self):
        self.l_counter += 1
        return "L" + str(self.l_counter)

    def backpatch(self, in_list, m):
        # print("backpatch")
        # print(in_list)
        # print(m)
        for index in in_list:
            # print("in for")
            # print(index)
            # print(m)
            code = self.code_list[index]
            # print(code)
            new_code = code.replace("_", str(m))
            # print(code)
            self.code_list[index] = new_code

    def get_start(self, s):
        s_list = s.split(":")
        return s_list[0]
    def get_num_of_last_label(self, s):
        s_list = s.split(";")
        s_list = s_list[-2].split(':')
        num = int(s_list[0].replace("L",""))
        return num

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
