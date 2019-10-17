from collections import deque
from Compiladores.Chars_especiais import Char_especiais, espacos
from Compiladores.Estado_zero import zero, Chars_aceitos, Analisa_char
from Compiladores.Tipo import Tipo
from Compiladores.Token import Token


class Lexico:

    def __init__(self, arquivo):
        self.coluna = 1
        self.linha = 1
        self.arquivo = open(arquivo)
        self.li = list(deque(self.arquivo.read()))
        self.arquivo.close()
        self.token = []
        self.palavra = []
        self.tipo = ''
        self.estado = 0
        self.esp = [' ', '\n', '\t', '.', ',', '+', '-', '*', '(', ')', '{', '}', '[', ']', ';', '=', '<', '!']
        self.vai = False
        self.contador = 0
        self.analisa()#TODO: linha 23 implementados no dia 16/10/19

    def get_lista(self):
        return self.li

    def get_token(self):
        return self.token

    def analisa(self):
        for ch in self.li:
            self.estado = Analisa_char(self.estado, ch)
            if ch == '/':
                if self.estado == 4:
                    self.estado = 5
                elif self.estado == 4:
                    self.estado = 3
                else:
                    self.estado = 4
            if self.estado == 0:
                self.estado = zero(ch)
            elif 1 < self.estado < 50:
                if self.estado == 2:
                    if Char_especiais(ch) > 2:
                        self.token.append(Token(Tipo('indentifier'), ''.join(self.palavra), self.linha,
                                                self.coluna - len(self.palavra) + 1))
                        self.estado = Char_especiais(ch)
                    if ch == '' or ch == '\n' or ch == '\t':
                        self.estado = 900
                    if self.estado == 3 and ch in [' ', '\n', '\t']:
                        self.estado = 99
            elif 100 < self.estado < 300:
                if 100 < self.estado < 108:
                    # verifica o lexema 'boolean'
                    if self.estado == 101 and ch == 'o':
                        self.estado = 102
                    elif self.estado == 102 and ch == 'o':
                        self.estado = 103
                    elif self.estado == 103 and ch == 'l':
                        self.estado = 104
                    elif self.estado == 104 and ch == 'e':
                        self.estado = 105
                    elif self.estado == 105 and ch == 'a':
                        self.estado = 106
                    elif self.estado == 106 and ch == 'n':
                        self.estado = 107
                    elif self.estado == 107 and (ch == ' ' or ch == '\n'):
                        self.estado = 901
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 901
                        else:
                            self.estado = 2
                elif 107 < self.estado < 113:
                    # verifica o lexema 'class'
                    if self.estado == 108 and ch == 'l':
                        self.estado = 109
                    elif self.estado == 109 and ch == 'a':
                        self.estado = 110
                    elif self.estado == 110 and ch == 's':
                        self.estado = 111
                    elif self.estado == 111 and ch == 's':
                        self.estado = 112
                    elif self.estado == 112 and (ch == ' ' or ch == '\n'):
                        self.estado = 902
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 902
                        else:
                            self.estado = 2
                elif 112 < self.estado < 123:
                    # verifica os lexemas 'else e extends'
                    if 112 < self.estado < 117:
                        if self.estado == 113 and (ch == 'l' or ch == 'x'):
                            if ch == 'l':
                                self.estado = 114
                            else:
                                self.estado = 117
                        elif self.estado == 114 and ch == 's':
                            self.estado = 115
                        elif self.estado == 115 and ch == 'e':
                            self.estado = 116
                        elif self.estado == 116 and (ch == ' ' or ch == '\n'):
                            self.estado = 903
                        else:
                            if espacos(ch) != 2:
                                self.vai = True
                                self.estado = 903
                            else:
                                self.estado = 2
                    else:
                        if self.estado == 117 and ch == 't':
                            self.estado = 118
                        elif self.estado == 118 and ch == 'e':
                            self.estado = 119
                        elif self.estado == 119 and ch == 'n':
                            self.estado = 120
                        elif self.estado == 120 and ch == 'd':
                            self.estado = 121
                        elif self.estado == 121 and ch == 's':
                            self.estado = 122
                        elif self.estado == 122 and (ch == ' ' or ch == '\n'):
                            self.estado = 904
                        else:
                            if espacos(ch) != 2:
                                self.vai = True
                                self.estado = 904
                            else:
                                self.estado = 2
                elif 122 < self.estado < 128:
                    # verifica a lexema 'false'
                    if self.estado == 123 and ch == 'a':
                        self.estado = 124
                    elif self.estado == 124 and ch == 'l':
                        self.estado = 125
                    elif self.estado == 125 and ch == 's':
                        self.estado = 126
                    elif self.estado == 126 and ch == 'e':
                        self.estado = 127
                    elif self.estado == 127 and (ch == ' ' or ch == '\n'):
                        self.estado = 905
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 905
                        else:
                            self.estado = 2
                elif 127 < self.estado < 132:
                    if self.estado == 128 and (ch == 'f' or ch == 'n'):
                        if ch == 'f':
                            self.estado = 129
                        else:
                            self.estado = 130
                    elif self.estado == 129 and (ch == ' ' or ch == '\n'):
                        self.estado = 906
                    elif self.estado == 130 and ch == 't':
                        self.estado = 131
                    elif self.estado == 131 and (ch == ' ' or ch == '\n'):
                        self.estado = 907
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 907
                        else:
                            self.estado = 2
                elif 131 < self.estado < 136:
                    if self.estado == 132 and ch == 'a':
                        self.estado = 133
                    elif self.estado == 133 and ch == 'i':
                        self.estado = 134
                    elif self.estado == 134 and ch == 'n':
                        self.estado = 135
                    elif self.estado == 135 and (ch == ' ' or ch == '\n'):
                        self.estado = 908
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 908
                        else:
                            self.estado = 2
                elif 135 < self.estado < 139:
                    if self.estado == 136 and ch == 'e':
                        self.estado = 137
                    elif self.estado == 137 and ch == 'w':
                        self.estado = 138
                    elif self.estado == 138 and (ch == ' ' or ch == '\n'):
                        self.estado = 909
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 909
                        else:
                            self.estado = 2
                elif 138 < self.estado < 145:
                    if self.estado == 139 and ch == 'u':
                        self.estado = 140
                    elif self.estado == 140 and ch == 'b':
                        self.estado = 141
                    elif self.estado == 141 and ch == 'l':
                        self.estado = 142
                    elif self.estado == 142 and ch == 'i':
                        self.estado = 143
                    elif self.estado == 143 and ch == 'c':
                        self.estado = 144
                    elif self.estado == 144 and (ch == ' ' or ch == '\n'):
                        self.estado = 910
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 910
                        else:
                            self.estado = 2
                elif 144 < self.estado < 151:
                    if self.estado == 145 and ch == 'e':
                        self.estado = 146
                    elif self.estado == 146 and ch == 't':
                        self.estado = 147
                    elif self.estado == 147 and ch == 'u':
                        self.estado = 148
                    elif self.estado == 148 and ch == 'r':
                        self.estado = 149
                    elif self.estado == 149 and ch == 'n':
                        self.estado = 150
                    elif self.estado == 150 and (ch == ' ' or ch == '\n'):
                        self.estado = 911
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 911
                        else:
                            self.estado = 2
                elif 150 < self.estado < 157:
                    if self.estado == 151 and ch == 't':
                        self.estado = 152
                    elif self.estado == 152 and ch == 'a':
                        self.estado = 153
                    elif self.estado == 153 and ch == 't':
                        self.estado = 154
                    elif self.estado == 154 and ch == 'i':
                        self.estado = 155
                    elif self.estado == 155 and ch == 'c':
                        self.estado = 156
                    elif self.estado == 156 and (ch == ' ' or ch == '\n'):
                        self.estado = 912
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 912
                        else:
                            self.estado = 2
                elif 156 < self.estado < 180:
                    if 156 < self.estado < 163:
                        if self.estado == 157 and (ch == 't' or ch == 'y'):
                            if ch == 't':
                                self.estado = 158
                            else:
                                self.estado = 163
                        elif self.estado == 158 and ch == 'r':
                            self.estado = 159
                        elif self.estado == 159 and ch == 'i':
                            self.estado = 160
                        elif self.estado == 160 and ch == 'n':
                            self.estado = 161
                        elif self.estado == 161 and ch == 'g':
                            self.estado = 162
                        elif self.estado == 162 and (ch == ' ' or ch == '\n'):
                            self.estado = 913
                        else:
                            if espacos(ch) != 2:
                                self.vai = True
                                self.estado = 913
                            else:
                                self.estado = 2
                    elif 162 < self.estado < 180:
                        if self.estado == 163 and ch == 's':
                            self.estado = 164
                        elif self.estado == 164 and ch == 't':
                            self.estado = 165
                        elif self.estado == 165 and ch == 'e':
                            self.estado = 166
                        elif self.estado == 166 and ch == 'm':
                            self.estado = 167
                        elif self.estado == 167 and ch == '.':
                            self.estado = 168
                        elif self.estado == 168 and ch == 'o':
                            self.estado = 169
                        elif self.estado == 169 and ch == 'u':
                            self.estado = 170
                        elif self.estado == 170 and ch == 't':
                            self.estado = 171
                        elif self.estado == 171 and ch == '.':
                            self.estado = 172
                        elif self.estado == 172 and ch == 'p':
                            self.estado = 173
                        elif self.estado == 173 and ch == 'r':
                            self.estado = 174
                        elif self.estado == 174 and ch == 'i':
                            self.estado = 175
                        elif self.estado == 175 and ch == 'n':
                            self.estado = 176
                        elif self.estado == 176 and ch == 't':
                            self.estado = 177
                        elif self.estado == 177 and ch == 'l':
                            self.estado = 178
                        elif self.estado == 178 and ch == 'n':
                            self.estado = 179
                        elif self.estado == 179 and (ch == ' ' or ch == '\n'):
                            self.estado = 914
                        else:
                            if espacos(ch) != 2:
                                self.vai = True
                                self.estado = 914
                            else:
                                self.estado = 2
                elif 179 < self.estado < 187:
                    if 179 < self.estado < 184:
                        if self.estado == 180 and (ch == 'h' or ch == 'r'):
                            if ch == 'h':
                                self.estado = 181
                            else:
                                self.estado = 184
                        elif self.estado == 181 and ch == 'i':
                            self.estado = 182
                        elif self.estado == 182 and ch == 's':
                            self.estado = 183
                        elif self.estado == 183 and (ch == ' ' or ch == '\n'):
                            self.estado = 915
                        else:
                            self.estado = espacos(ch)
                            if espacos(ch) != 2:
                                self.vai = True
                                self.estado = 915
                            else:
                                self.estado = 2
                    elif 183 < self.estado < 187:
                        if self.estado == 184 and ch == 'u':
                            self.estado = 185
                        elif self.estado == 185 and ch == 'e':
                            self.estado = 186
                        elif self.estado == 186 and (ch == ' ' or ch == '\n'):
                            self.estado = 916
                        else:
                            if espacos(ch) != 2:
                                self.vai = True
                                self.estado = 916
                            else:
                                self.estado = 2
                elif 186 < self.estado < 191:
                    if self.estado == 187 and ch == 'o':
                        self.estado = 188
                    elif self.estado == 188 and ch == 'i':
                        self.estado = 189
                    elif self.estado == 189 and ch == 'd':
                        self.estado = 190
                    elif self.estado == 190 and (ch == ' ' or ch == '\n'):
                        self.estado = 917
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 917
                        else:
                            self.estado = 2
                elif 190 < self.estado < 196:
                    if self.estado == 191 and ch == 'h':
                        self.estado = 192
                    elif self.estado == 192 and ch == 'i':
                        self.estado = 193
                    elif self.estado == 193 and ch == 'l':
                        self.estado = 194
                    elif self.estado == 194 and ch == 'e':
                        self.estado = 195
                    elif self.estado == 195 and (ch == ' ' or ch == '\n'):
                        self.estado = 918
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 918
                        else:
                            self.estado = 2
                elif 195 < self.estado < 198:
                    if self.estado == 196 and ch == '&':
                        self.estado = 197
                    elif self.estado == 197 and (ch == ' ' or ch == '\n'):
                        self.estado = 919
                    else:
                        if ch != '&':
                            self.estado = espacos(ch)
                            if self.estado == 196:
                                self.estado = 2
                        else:
                            self.estado = 2
                elif 197 < self.estado < 204:
                    if self.estado == 198 and ch == 'e':
                        self.estado = 199
                    elif self.estado == 199 and ch == 'n':
                        self.estado = 200
                    elif self.estado == 200 and ch == 'g':
                        self.estado = 201
                    elif self.estado == 201 and ch == 't':
                        self.estado = 202
                    elif self.estado == 202 and ch == 'h':
                        self.estado = 203
                    elif self.estado == 203 and (ch == ' ' or ch == '\n'):
                        self.estado = 920
                    else:
                        if espacos(ch) != 2:
                            self.vai = True
                            self.estado = 920
                        else:
                            self.estado = 2
            elif self.estado == 1:
                if ch.isdigit():
                    self.estado = 1
                elif ch in ['.', ',', '+', '-', '*', '(', ')', '{', '}', '[', ']', ';', '=', '<', '!']:
                    self.token.append(Token(Tipo('numero'), ''.join(self.palavra), self.linha, self.coluna - len(self.palavra) + 1))
                    self.estado = Char_especiais(ch)
                elif ch in [' ', '\n', '\t']:
                    self.estado = 923
                else:
                    self.estado = 3
            # TODO: estados finais
            if self.estado > 899 or 49 < self.estado < 65:
                if self.estado == 900:
                    self.token.append(Token(Tipo('indentifier'), ''.join(self.palavra), self.linha, self.coluna - len(self.palavra) + 1))
                if self.estado < 911:
                    if self.estado == 901:
                        self.token.append(Token(Tipo('boolean'), 'boolean', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 902:
                        self.token.append(Token(Tipo('class'), 'class', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 903:
                        self.token.append(Token(Tipo('else'), 'else', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 904:
                        self.token.append(Token(Tipo('extends'), 'extends', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 905:
                        self.token.append(Token(Tipo('false'), 'false', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 906:
                        self.token.append(Token(Tipo('if'), 'if', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 907:
                        self.token.append(Token(Tipo('int'), 'int', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 908:
                        self.token.append(Token(Tipo('main'), 'main', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 909:
                        self.token.append(Token(Tipo('new'), 'new', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 910:
                        self.token.append(Token(Tipo('public'), 'public', self.linha, self.coluna - len(self.palavra) + 1))
                elif 910 < self.estado < 923:
                    if self.estado == 911:
                        self.token.append(Token(Tipo('return'), 'return', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 912:
                        self.token.append(Token(Tipo('static'), 'static', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 913:
                        self.token.append(Token(Tipo('String'), 'String', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 914:
                        self.token.append(
                            Token(Tipo('System.out.println'), 'System.out.println', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 915:
                        self.token.append(Token(Tipo('this'), 'this', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 916:
                        self.token.append(Token(Tipo('true'), 'true', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 917:
                        self.token.append(Token(Tipo('void'), 'void', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 918:
                        self.token.append(Token(Tipo('while'), 'while', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 919:
                        self.token.append(Token(Tipo('&&'), '&&', self.linha, self.coluna - len(self.palavra) + 1))
                    elif self.estado == 920:
                        self.token.append(Token(Tipo('length'), 'length', self.linha, self.coluna - len(self.palavra) + 1))
                elif 920 < self.estado < 930:
                    if self.estado == 923:
                        self.token.append(Token(Tipo('numero'), ''.join(self.palavra), self.linha, self.coluna - len(self.palavra) + 1))
                if self.vai:
                    self.estado = Char_especiais(ch)
                if 49 < self.estado < 100:
                    if self.estado == 50:
                        self.token.append(Token(Tipo('.'), ch, self.linha, self.coluna))
                    elif self.estado == 51:
                        self.token.append(Token(Tipo(','), ch, self.linha, self.coluna))
                    elif self.estado == 52:
                        self.token.append(Token(Tipo('+'), ch, self.linha, self.coluna))
                    elif self.estado == 53:
                        self.token.append(Token(Tipo('-'), ch, self.linha, self.coluna))
                    elif self.estado == 54:
                        self.token.append(Token(Tipo('*'), ch, self.linha, self.coluna))
                    elif self.estado == 55:
                        self.token.append(Token(Tipo('('), ch, self.linha, self.coluna))
                    elif self.estado == 56:
                        self.token.append(Token(Tipo(')'), ch, self.linha, self.coluna))
                    elif self.estado == 57:
                        self.token.append(Token(Tipo('{'), ch, self.linha, self.coluna))
                    elif self.estado == 58:
                        self.token.append(Token(Tipo('}'), ch, self.linha, self.coluna))
                    elif self.estado == 59:
                        self.token.append(Token(Tipo('['), ch, self.linha, self.coluna))
                    elif self.estado == 60:
                        self.token.append(Token(Tipo(']'), ch, self.linha, self.coluna))
                    elif self.estado == 61:
                        self.token.append(Token(Tipo(';'), ch, self.linha, self.coluna))
                    elif self.estado == 62:
                        self.token.append(Token(Tipo('='), ch, self.linha, self.coluna))
                    elif self.estado == 63:
                        self.token.append(Token(Tipo('<'), ch, self.linha, self.coluna))
                    elif self.estado == 64:
                        self.token.append(Token(Tipo('!'), ch, self.linha, self.coluna))
                self.estado = 0
                self.palavra.clear()
            else:
                if ch not in [' ', '\n', '\t']:
                    self.palavra.append(ch)
            if self.estado == 99:
                self.token.append(Token(Tipo('erro'), ''.join(self.palavra), self.linha, self.coluna - len(self.palavra) + 1))
                self.palavra.clear()
                self.estado = 0
            self.contador += 1
            self.coluna += 1
            self.vai = False
            if ch == '\n':
                self.coluna = 0
                self.linha += 1
                if self.estado == 5:
                    self.palavra.clear()
                    self.estado = 1
            if self.contador == len(self.li):
                if ch not in [' ', '\n', '\t']:
                    if self.estado == 3:
                        self.token.append(Token(Tipo('erro'), ''.join(self.palavra), self.linha, self.coluna - len(self.palavra) + 1))
                    else:
                        self.token.append(Token(Tipo('indentifier'), ''.join(self.palavra), self.linha, self.coluna - len(self.palavra) + 1))
