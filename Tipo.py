from enum import Enum


class Tipo(Enum):
    SCLASSE = 'class'
    SINDENTIFIER = 'indentifier'
    SPONTO = '.'
    SVIRGULA = ','
    SMAIS = '+'
    SMENOS = '-'
    SMULTIPLICA = '*'
    SABREPARENTESES = '('
    SFECHAPARENTESES = ')'
    SABRECHAVES = '{'
    SFECHACHAVES = '}'
    SABRECOLCHETES = '['
    SFECHACOLCHETES = ']'
    SPONTOEVIRGULA = ';'
    SATRIBUICAO = '='
    SMENOR = '<'
    SAND = '&&'
    SESCLAMACAO = '!'
    SNUMERO = 'numero'
    SPUBLIC = "public"
    SSTATIC = "static"
    SVOID = "void"
    SMAIN = "main"
    SSTRING = "String"
    SEXTENDS = "extends"
    SRETURN = 'return'
    SINT = "int"
    SBOOLEAN = "boolean"
    SIF = "if"
    SELFE = "else"
    SWHILE = 'while'
    SSYSTEMOUTPRINTLN = "System.out.println"
    SLENGTH = "length"
    STRUE = "true"
    SFALSE = "false"
    STHIS = "this"
    SNEW = "new"
    SERRO = "erro"
