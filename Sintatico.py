from Compiladores import li
from Compiladores.Tipo import Tipo


class Sintatico:

    def __init__(self, token=[]):
        self.contador = 0
        self.token = token
        self.escopo = []
        self.ts = []
        self.tabela_simbolo()
        # print(self.escopo)

    def adiciona_ecopo(self, escopo):
        self.escopo.append(escopo)

    def remove_escopo(self):
        self.escopo.pop()

    def expression(self):
        """
Expression	::=	Expression ( "&&" | "<" | "+" | "-" | "*" ) Expression
                Expression "[" Expression "]"
                Expression "." "length"
                Expression "." Identifier "(" ( Expression ( "," Expression )* )? ")"
                <INTEGER_LITERAL>
                "true"
                "false"
                Identifier
                "this"
                "new" "int" "[" Expression "]"
                "new" Identifier "(" ")"
                "!" Expression
                "(" Expression ")"
        """
        pass

    def statemant(self):
        """
        Statemant::=
            "{" (Statment)* "}"
            "if" "(" Expresion ")"  Statemant "else" Statemant
            "while" "(" Expresion ")"  Statemant
            "systen.out.println" "(" Expresion ") ";"
            Identifier "=" Expresion ";"
            Identifier "[" Expresion "]" "=" Expresion ";"
        """
        # TODO Verifica se ABRE CHAVES
        if self.token[self.contador].tipo == Tipo.SABRECHAVES:
            self.contador += 1
            self.statemant()
            #TODO Verifica se FECHA CHAVES
            if self.token[self.contador].tipo == Tipo.SFECHACHAVES:
                self.contador += 1
        # TODO: VERIFICA se é 'if'
        elif self.token[self.contador].tipo == Tipo.SIF:
            self.adiciona_ecopo(f'if_linha_{self.token[self.contador].linha}_Col_{self.token[self.contador].coluna}')
            self.contador += 1
            # TODO: VERIFICA se ABRE PARENTESES
            if self.token[self.contador].tipo == Tipo.SABREPARENTESES:
                self.contador += 1
                # TODO: chamar a função Expresion
                self.expression()
                # TODO: VERIFICA se FECHA PARENTESES
                if self.token[self.contador].tipo == Tipo.SFECHAPARENTESES:
                    self.contador += 1
                    if self.token[self.contador].tipo == Tipo.SFECHACHAVES:
                        self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                        print(f'ERRO Semantico: {self.token[self.contador]} || falta a condição do SE')
                    self.statemant()
                    if self.token[self.contador].tipo == Tipo.SELFE:
                        self.contador += 1
                        if self.token[self.contador].tipo == Tipo.SFECHACHAVES:
                            self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                            print(f'ERRO Semantico: {self.token[self.contador]} || falta a condição do ENTÃO')
                        self.statemant()
                        self.remove_escopo()
                    else:
                        self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                        print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se a palavra "else"')
                else:
                    self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                    print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um FECHA PARENTESES')
            else:
                self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um ABRE PARENTESES')
        # TODO: verifica se é 'Systenten.out.println'
        elif self.token[self.contador].tipo == Tipo.SSYSTEMOUTPRINTLN:
            self.contador += 1
            # TODO: VERIFICA se ABRE PARENTESES
            if self.token[self.contador].tipo == Tipo.SABREPARENTESES:
                self.contador += 1
                # TODO: chamar a função Expresion
                self.expression()
                # TODO: VERIFICA se FECHA PARENTESES
                if self.token[self.contador].tipo == Tipo.SFECHAPARENTESES:
                    self.contador += 1
                else:
                    self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                    print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um FECHA PARENTESES')
            else:
                self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um ABRE PARENTESES')
        # TODO: verifica se é uum identificador
        elif self.token[self.contador].tipo == Tipo.SINDENTIFIER:
            # TODO Inserir na tabela de simbolos<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<--
            self.contador += 1
            if self.token[self.contador].tipo == Tipo.SABRECOLCHETES:
                self. contador += 1
                self.expression()
                if self.token[self.contador].tipo == Tipo.SFECHACOLCHETES:
                    self.contador += 1
                else:
                    print('ERRO FECHA COLCHETES')
            if self.token[self.contador].tipo == Tipo.SATRIBUICAO:
                self.contador += 1
                self.expression()
                if self.token[self.contador].tipo == Tipo.SPONTOEVIRGULA:
                    self.contador += 1
                else:
                    print('erro ponto e virgula')
            else:
                print('erro de atribuicao')

        # TODO Verifica a condição while --->   "while" "(" Expresion ")"  Statemant <---
        elif self.token[self.contador].tipo == Tipo.SWHILE:
            self.adiciona_ecopo(f'if_linha_{self.token[self.contador].linha}_Col_{self.token[self.contador].coluna}')
            self.contador += 1
            # TODO: VERIFICA se ABRE PARENTESES
            if self.token[self.contador].tipo == Tipo.SABREPARENTESES:
                self.contador += 1
                # TODO: chamar a função Expresion
                self.expression()
                # TODO: VERIFICA se FECHA PARENTESES
                if self.token[self.contador].tipo == Tipo.SFECHAPARENTESES:
                    self.contador += 1
                    self.statemant()
                else:
                    self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                    print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um FECHA PARENTESES')
            else:
                self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um ABRE PARENTESES')
        elif self.token[self.contador].tipo == Tipo.SFECHACHAVES:
            pass
        else:
            self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
            print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se "if" || "while" || "Identificador" || ABRE CHAVES')

    def main_class(self):
        # MainClass ::= "Class" Indentifier "{" "pupblic" "static" "void" "main" "(" "String" "[" "]" Indentifier ")" "{"Statmant"}" "}"
        # TODO: verifica a palavra 'class'
        if self.token[self.contador].tipo == Tipo.SCLASSE:
            self.contador += 1
            # TODO: verifica se é um indentificador
            if self.token[self.contador].tipo == Tipo.SINDENTIFIER:
                self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                self.ts.append(self.token[self.contador])
                self.adiciona_ecopo(self.token[self.contador].lexema)
                self.contador += 1
                # TODO: verifica se ABRE Chaves
                if self.token[self.contador].tipo == Tipo.SABRECHAVES:
                    self.contador += 1
                    # TODO: verifica a palavra 'public'
                    if self.token[self.contador].tipo == Tipo.SPUBLIC:
                        self.contador += 1
                        # TODO: verifica a palavra static
                        if self.token[self.contador].tipo == Tipo.SSTATIC:
                            self.contador += 1
                            # TODO: verifica a palavra void
                            if self.token[self.contador].tipo == Tipo.SVOID:
                                self.contador += 1
                                # TODO: verifica a palavra main
                                if self.token[self.contador].tipo == Tipo.SMAIN:
                                    self.contador += 1
                                    # TODO: verifica verifica se ABRE parenteses
                                    if self.token[self.contador].tipo == Tipo.SABREPARENTESES:
                                        self.contador += 1
                                        #TODO: Verifica a palavra String
                                        if self.token[self.contador].tipo == Tipo.SSTRING:
                                            self.contador += 1
                                            # TODO: verifica verifica se ABRE colchetes
                                            if self.token[self.contador].tipo == Tipo.SABRECOLCHETES:
                                                self.contador += 1
                                                # TODO: verifica verifica se FECHA colchetes
                                                if self.token[self.contador].tipo == Tipo.SFECHACOLCHETES:
                                                    self.contador += 1
                                                    # TODO: verifica se é um identificador
                                                    if self.token[self.contador].tipo == Tipo.SINDENTIFIER:
                                                        self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                                        self.ts.append(self.token[self.contador])
                                                        self.contador += 1
                                                        # TODO: verifica se FECHA parenteses
                                                        if self.token[self.contador].tipo == Tipo.SFECHAPARENTESES:
                                                            self.contador += 1
                                                            # TODO: verifica se ABRE chaves
                                                            if self.token[self.contador].tipo == Tipo.SABRECHAVES:
                                                                self.contador += 1
                                                                # TODO: verifica CHAMA A FUNÇÃO statmant
                                                                self.statemant()
                                                                #self.contador += 1
                                                                # TODO: verifica se FECHA Chaves
                                                                if self.token[self.contador].tipo == Tipo.SFECHACHAVES:
                                                                    self.contador += 1
                                                                    # TODO: verifica se FECHA Chaves
                                                                    if self.token[self.contador].tipo == Tipo.SFECHACHAVES:
                                                                        self.remove_escopo()
                                                                        print('FIM')
                                                                    else:
                                                                        self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                                                        print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um FECHA CHAVES')
                                                                else:
                                                                    self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                                                    print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um FECHA CHAVES')
                                                            else:
                                                                self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                                                print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um ABRE CHAVES')
                                                        else:
                                                            self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                                            print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um FECHA PARENTESES')
                                                    else:
                                                        self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                                        print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um IDENTIFICADOR')
                                                else:
                                                    self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                                    print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um FECHA COLCHETES')
                                            else:
                                                self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                                print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um ABRE COLCHETES')
                                        else:
                                            self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                            print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se a palavra "String"')
                                    else:
                                        self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                        print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um "ABRE PARENTESES"')
                                else:
                                    self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                    print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se a palavra "main"')
                            else:
                                self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                                print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se a palavra "void"')
                        else:
                            self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                            print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se a palavra "ststic"')
                    else:
                        self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                        print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se a palavra "public"')
                else:
                    self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                    print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um ABRE CHAVES')
            else:
                self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
                print(f'ERRO Semantico: {self.token[self.contador]} || esperava-se um IDENTIFICADOR')
        else:
            self.token[self.contador].escopo = self.escopo[len(self.escopo) - 1]
            print(f'ERRO Semantico: {self.token[self.contador]} || Palavra esperada -> "class"')

        print(self.token[self.contador].tipo)

    def class_declaration(self):
        x = 1

    def tabela_simbolo(self):
        # goal ::= MainClass (ClassDeclaration)* <EOF>
        self.adiciona_ecopo("Global")
        self.main_class()
        if self.contador < len(self.token):
            self.class_declaration()
        return self.ts


# print(li)
si = Sintatico(li)
