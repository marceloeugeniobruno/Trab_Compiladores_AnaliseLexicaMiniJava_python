# Trab_Compiladores_AnaliseLexicaMiniJava_python
Este é apenas um trabalho academico de analise lexica se compiladores
ainda tem muitos erros que tem que ser corrigidos. ao meu entendmento o código não está bom. tambem ainda nao descrevi
o que faz cada bloco.


3 atualização
A principio foi corrigido os erro lexicos
a


#2 comit####
Ainda estamos corrigindo os erros no analisador Lexico.
o primeiro erro corrigido foi na linha XXX. foi na atribuição do estado, foi equivocadamente colocado no estado 1, que acarretava em erro da proxima palavra
o segundo erro que foi corrgdo foi nos nas entre as linhas 166 a 169 foi adicionada uma instrução



if self.estado == 129:
    self.estado = 906
else:
    self.estado = 907
    
    
Tambem foi detectado um erro bem grave antes da atribuiçõa dos estados fins de cada palavra encontrada, quando a palavra encontrada se difere das palavras reservadas o programa faz bem sua fnção atribuuindo a um identificador, mas caso contrário se digitarmos as palavras 'c', 'cl', 'cla', 'clas' o programa coloca como o lexema class (que até dá a idéia de desevolver um interpretador que faz esse tipo de interpretação). e esse é o próximo passo a ser corrigido.



#######

Este é um analisador lexico elaborado para a disciplina de compiladores.
Elaborado por: Marcelo Eugênio Bruno de Azevedo
---->	Arquivos e descrições
-> Compiladores.py
Principal arquivo do analisador léxico e onde está localizado a classe léxico
Para execução é necessário passar o arquivo por parâmetro léxico(“nome do arquivo se tiver na mesma pasta”).
Exitem duas funções que retornarão listas a get_token() que retornará a lista de todos os tokens encontrados no arquivo e a get_lista () que retornará a lista de todos os caracteres contidos no arquivo importado.
O procedimento analisa() é o responsável por colocar na lista de tokens cada token encontrado do arquivo.
No momento ainda tenho que resolver tratar os estados 3 e 99. E a último caractere da lista. No inicio verifica se o caractere está na lista de carcteres aceitos. Como ainda não tratei os erros, quando o erro ocorre nada mais é colocado na lista de tokens. 
-> Chars_especiais.py
Este arquivo contem duas funções def Char_especiais(char) e def espaços(char)
Estas funções retornam um estado de acordo com o char que é encaminhado.
->Estado_zero.py
Esse arquivo contem 3 funções, uma delas é uma lista de caracteres aceitos pela linguagem. Função def Chars_aceitos(). Essa função é chada pela função Analisa_char(estado, char) e retorna estado de erro quando encontra um caractere não aceito.
E a principal função que é a estado def zero (char) ela rearna um estado de acordo com o primeiro caractere que  encontrar quando está no estado 0.
->Tokem.py 
E a classe tokem ela é usada quando um novo tokem é gerado
Tipo.py 
Enumera o tipo do tokem.

