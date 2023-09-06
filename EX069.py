i=0
h=0
m=0
print('=-' * 20)
while True:
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()
    escolha = str(input('Deseja cadastrar mais pessoas? [S/N]')).strip().upper()
    if escolha == 'N':
        break
    if idade > 18:
        i = i+1
    if sexo == 'M':
        h = h+1
    if sexo == 'F' and idade < 20:
        m = m+1
print('=-' * 20)
print(f'Número de pessoas maiores de idade: {i}')
print(f'Número de homens cadastrados: {h}')
print(f'Número de mulheres abaixo de 20 anos: {m}')
print('=-' * 20)
