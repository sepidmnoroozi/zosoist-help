from classes.nonterminal import Nonterminal

class CodeGenerator:
    def __init__(self):
        pass

    def generate_arithmetic_code(self, p, tmp, code_list):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        p[0] = Nonterminal()
        p[0].place = tmp
        if len(p) == 4:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^4")
            arg1 = ""
            arg2 = ""

            if p[1].place == "":
                arg1 = p[1].value
            else:
                arg1 = p[1].place

            if p[3].place == "":
                arg2 = p[3].value
            else:
                arg2 = p[3].place

            p[0].code = "L" + str(len(code_list)) + ": " + p[0].place + "=" + arg1 + p[2] + arg2 + ";"
            print(p[0].code)
            code_list.append(p[0].code)
            print(code_list)

        elif len(p) == 3:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^3")
            arg1 = ""
            arg2 = ""

            if p[2].place == "":
                arg1 = p[2].value
            else:
                arg1 = p[2].place

            p[0].code = "L" + str(len(code_list)) + ": " + p[0].place + "=" + p[1] + arg1 + ";"
            print(p[0].code)
            code_list.append(p[0].code)
            print(code_list)

    def generate_boolean_code(self, p, code_list):
        p[0] = Nonterminal()
        next_quad = len(code_list)
        p[0].true_list = [next_quad]
        p[0].false_list = [next_quad + 1]

        if p[1].place != "" and p[3].place != "":
            code = "L" + str(next_quad) + ": " + "if " + p[1].place + p[2] + p[3].place + " goto _" + ";"
        elif p[1].place != "" and p[3].place == "":
            code = "L" + str(next_quad) + ": " + "if " + p[1].place + p[2] + p[3].value + " goto _" + ";"
        elif p[1].place == "" and p[3].place != "":
            code = "L" + str(next_quad) + ": " + "if " + p[1].value + p[2] + p[3].place + " goto _" + ";"
        else:
            code = "L" + str(next_quad) + ": " + "if " + p[1].value + p[2] + p[3].value + " goto _" + ";"

        code_list.append(code)

        code = "L" + str(next_quad + 1) + ": " + 'goto _' + ";"
        code_list.append(code)

        p[0].m = next_quad + 2
        p[0].code = code_list
        p[0].type = "bool"

        print("comparison_operation -> exp "+p[2]+" exp")
        print(code_list)
