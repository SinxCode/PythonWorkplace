lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #Tuplas são váriaveis compostas - Uma tupla recebe () para atribuição de valores e são imutáveis
print(lanche)#Irá mostrar todos os valores dentro da tupla
print(lanche[0])#Irá mostrar o primeiro valor dentro da tupla
print(lanche[1:])#Irá mostrar todos os valores da tupla a partir do index 1 (suco)
print(lanche[-2])#Irá trazer o segundo valor de trás pra frente
print(lanche[:1])#Irá trazer até o index 1
print(len(lanche))#Conta a quantidade de index da tupla
print(sorted(lanche))#Irá trazer todos os valores ordenados

for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi demais!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi demais!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

a = (2, 5, 4)
b = (5, 8, 1 ,2)
c = a + b #Irá unir ambas tuplas
print(c) 
print(len(c))
print(c.count(5))
print(c.index(8 , 1))#O número dps da virgula indica o ponto de partida para verificação

pessoa = ('Sinx', 24, 'M', 66.5)
#del(pessoa) deletaria a tupla pessoa
print(pessoa)


