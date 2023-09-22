''' #INTERACTIVE HELP
help() #Ajuda interativa
help(print) #Explica como funciona a função desejada, no exemplo foi o print '''

#DOCSTRINGS
def contador(i,f,p): #Para criar uma docstring basta digitar 3 aspas duplas na linha abaixo a declaração da função como abaixo
    """""
        Faz uma contagem e mostra na tela.
        :param i: Inicio da contagem
        :param f: Fim da contagem
        :param p: Passo da contagem
        :return: sem retorno
    """""
    c = i
    while c <=f:
        print(f'{c} ',end='')
        c = c + p
    print('Fim!')

help(contador)
