lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #Tuplas são váriaveis compostas - Uma tupla recebe () para atribuição de valores e são imutáveis
print(lanche)#Irá mostrar todos os valores dentro da tupla
print(lanche[0])#Irá mostrar o primeiro valor dentro da tupla
print(lanche[1:])#Irá mostrar todos os valores da tupla a partir do index 1 (suco)
print(lanche[-2])#Irá trazer o segundo valor de trás pra frente
print(lanche[:1])#Irá trazer até o index 1
print(len(lanche))#Conta a quantidade de index da tupla

for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi demais!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi demais!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
