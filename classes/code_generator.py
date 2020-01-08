from classes.nonterminal import Nonterminal

class CodeGenerator:
    def __init__(self):
        pass
    def generate_arithmetic_code(self,p,tmp):
        p[0] = Nonterminal()
        p[0].place = tmp
        if len(p) == 4 :
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


            p[0].code = p[0].place + "=" + arg1 + p[2] + arg2
            print(p[0].code)
        elif len(p) == 3:

            arg1 = ""
            arg2 = ""

            if p[2].place == "":
                arg1 = p[2].value
            else:
                arg1 = p[2].place

            p[0].code = p[0].place + "=" + p[1] + arg1
            print(p[0].code)