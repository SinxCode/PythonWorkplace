pessoa = list()
conjunto = list()
c = 0 #Não é necessário um contador, pode se utilizar o len
maior = 0
menor = 0
while True:
    pessoa.append(input('Digite o nome: '))
    pessoa.append(int(input('Digite o peso: ')))
    #c = c + 1
    if len(conjunto) ==0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    conjunto.append(pessoa[:])
    pessoa.clear()
    resposta = input('Deseja cadastrar mais uma pessoa? [S/N]').strip().upper()
    if resposta =='N':
        break
print(f'Ao total foram cadastrados: {len(conjunto)} pessoas! ')
print(f'O maior peso foi de {maior}Kg, cujo as pessoas são: ', end='')
for p in conjunto:
    if p[1] == maior:
        print(f'{p[0]}; ',end='')
print(f'\nO menor peso foi de {menor}Kg, cujo as pessoas são: ',end='')
for p in conjunto:
    if p[1] == menor:
        print(f'{p[0]}; ',end='')


