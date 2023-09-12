valores = list()
for cont in range(0,5): #Pegando uma range de 5 valores
    valores.append(int(input('Digite um valor: ')))#Adicionando valores a lista pelo teclado
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2,3,4,7]
b = a # cria uma ligação entre listas
b[2] = 8 #Isso mudará ambos valores na lista a e b
b = a[:] #Cria uma cópia da lista a em b
b[2] = 5 #Agora irá mudar o valor somente na lista b, pois ela é uma cópia de a
print(f'Lista A: {a}')
print(f'Lista B: {b}')

