teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])#Criando cópia da lista teste e jogando dentro da lista galera
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)
#### No Exemplo acima ao printar galera há 2 dados na lista, isso porque copiamos a lista teste
#### antes da primeira mudança nas linhas 6 e  7, ou seja podemos armazenar dados que foram modificados.
