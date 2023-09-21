#Funções com parâmetros opcionais
def somar(a=0, b=0, c=0): #Ao colocar que 1 ou mais parametros receberia 0, se por acaso não informarmos algum parametro no código principal, ele irá recer o valor de 0 e não dará erro.
    s = a + b + c
    print(f'A soma vale {s}')


somar(3,2)




#Escopo de variáveis
def teste():
    x = 8
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')


n = 2 #Mesmo n tendo sido declaro fora da função, ele funciona como uma variável global no código ou escopo global, pois está no código principal
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}') Essa linha retornaria um erro, pois X está declarado somente dentro da função, o que chamamos de escopo local

def funcao():
    n1 = 4 #N1 local
    print(f'N1 dentro vale {n1}')


n1 = 2 #N1 global
funcao()
print(f'N1 fora vale {n1}')
