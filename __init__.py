from Compiladores.Copiladores import Lexico

le = Lexico('teste.txt')
li = le.get_token()
for i in li:
    print(f'{i}')

