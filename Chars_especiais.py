def Char_especiais(char):
    if char == '&':
        return 196
    elif char == '.':
        return 50
    elif char == ',':
        return 51
    elif char == '+':
        return 52
    elif char == '-':
        return 53
    elif char == '*':
        return 54
    elif char == '(':
        return 55
    elif char == ')':
        return 56
    elif char == '{':
        return 57
    elif char == '}':
        return 58
    elif char == '[':
        return 59
    elif char == ']':
        return 60
    elif char == ';':
        return 61
    elif char == '=':
        return 62
    elif char == '<':
        return 63
    elif char == '!':
        return 64
    else:
        return 0


def espacos(ch):
    if Char_especiais(ch) > 0:
        return Char_especiais(ch)
    elif ch in [' ', '\n', '\t']:
        return 900
    else:
        return 2
