pessoa = dict()
galera = list()
soma = 0
media = 0
print('=-' * 30)
print(f'{"CADASTRO DE PESSOAS":^55}')
print('=-' * 30)
while True:
    pessoa.clear() #Limpa o dicionario para o próximo cadastro
    pessoa['Nome'] = input('Nome: ')
    while True:
        pessoa['Sexo'] = input('Sexo [M/F]: ').strip().upper()
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma = soma + pessoa['Idade']
    galera.append(pessoa.copy()) #Copia dicionario pra dentro da lista
    while True:
         r = str(input('Quer continuar? [S/N]')).upper().strip()
         if r in 'SN':
            break
         print('ERRO! Responda apenas S ou N')
    if r == 'N':
        break
print('-='*30 )
print(f'Ao todo temos: {len(galera)} pessoas cadastradas.')
media = soma/len(galera)
print(f'A média de idade é de: {media:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]} ', end='')
print()
print('Lista de pessoas com idade acima da média: ')
for p in galera:
    if p['Idade'] >=media:
        for k, v in p.items():
            print(f'{k} = {v} ')
print('=-' *30)
print(f'{"<<<FIM>>>":^55}')
print('=-' *30)

