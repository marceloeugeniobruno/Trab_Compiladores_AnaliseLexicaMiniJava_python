from Compiladores.Chars_especiais import Char_especiais


def zero(char):
    """
    caso o estado seja zero essa função retornará o estado que vai a a máquina de acordo com o primeiro caractere
    encontrado
    :param char:
    :return:
    """
    if char.isnumeric():
        return 1
    elif char == ' ' or char == '\n' or char == '\t':
        return 0
    elif Char_especiais(char) > 0:
        return Char_especiais(char)
    elif char == 'b':
        return 101
    elif char == 'c':
        return 108
    elif char == 'e':
        return 113
    elif char == 'f':
        return 123
    elif char == 'i':
        return 128
    elif char == 'm':
        return 132
    elif char == 'n':
        return 136
    elif char == 'p':
        return 139
    elif char == 'r':
        return 145
    elif char == 's':
        return 151
    elif char == 'S':
        return 157
    elif char == 't':
        return 180
    elif char == 'v':
        return 187
    elif char == 'w':
        return 191
    elif char == 'l':
        return 198
    elif char in ['a', 'd', 'g', 'h', 'j', 'k', 'o', 'q', 'u', 'x', 'y', 'z', '_', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                  'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z']:
        return 2

def Chars_aceitos():
    l = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', '+', '-', '*', '(', ')', '{', '}', '[', ']', ';',
         '=', '<', '!', '\'', '\n', '\t', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
         'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z', '_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z', '/', ' ', '&']
    return l


def Analisa_char(estado, ch):

    if estado == 3 and (ch == ' ' or ch == '\n' or ch == '\t'):
        return 99
    elif estado < 3 and ch not in Chars_aceitos():
        return 3
    elif estado < 5 and ch not in Chars_aceitos():
        return 3
    return estado