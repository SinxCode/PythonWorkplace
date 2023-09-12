num = [2,5,9,1] #Para criar uma lista se usa colchetes '[]'
num[2] = 3 #Lista são mutáveis, aqui estou substituindo o valor do indice 2 (9) para 3
num.append(7) #Estou adicionando um valor a lista
num.sort #Ordena os valores em ordem crescente ou alfabetica
num.sort(reverse=True) #Ordena os valores em ordem decrescente
num.insert(2,0) #Insere um valor a partir de um indice, nesse caso o indice 2 e a lista aumentaria
num.pop() #Elimina o último valor da lista
num.pop(2) #Elimina o valor do indice 2
num.remove(2) #Remove o valor especificado (2), caso o valor se repita na lista, eliminará o que aparece primeiro
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4') #Verifica se o valor existe na lista para remove-lo
print(num)
print(f'Essa lista tem {len(num)} elementos.')
