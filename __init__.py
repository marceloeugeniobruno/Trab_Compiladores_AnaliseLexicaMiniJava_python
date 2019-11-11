from Compiladores.Copiladores import Lexico

analisador_lexico = Lexico('teste.txt')
li = analisador_lexico.get_token()

for i in li:
    print(f'{i}')
