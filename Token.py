class Token:

    def __init__(self, tipo='', lexema='', linha=0, coluna=0):
        self.tipo = tipo
        self.lexema = lexema
        self.linha = linha
        self.coluna = coluna
        self.escopo = ''
        self.valor = None

    def __str__(self):
        return f'Tipo -> {self.tipo} Lexema -> {self.lexema} Linha -> {self.linha} Coluna -> {self.coluna} ' \
               f'Escopo -> {self.escopo} valor -> {self.valor}'
