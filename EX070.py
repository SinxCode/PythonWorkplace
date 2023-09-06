m = 0
b = 0
t = 0
menor = 0
c= 0
barato =''
while True:
    produto = str(input('Informe o nome do produto: '))
    valor = float(input('Informe o valor do produto: '))
    c = c+1
    t = valor + t
    if valor > 1000:
        m = m+1
    escolha = str(input('Deseja cadastrar outro produto? [S/N] ')).strip().upper()
    if escolha == 'N':
        break
    if c ==1 or valor < menor:
        menor = valor
        barato = produto
    
print(f'Total dos produtos: R${t:.2f}')
print(f'Temos {m} produto acima de R$1000.00 ')
print(f'O produto mais barato foi {barato} e custa R$:{menor:.2f}')