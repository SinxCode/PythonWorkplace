media = dict()
media['Nome'] = input('Digite o nome do aluno: ')
media['Media'] = float(input('Digite a média do aluno: '))
if media['Media'] < 7.5:
    media['Situação'] = 'Reprovado'
else:
    media['Situação'] = 'Aprovado'
#print(f'O nome é igual a {media["Nome"]}')
#print(f'A média é igual a {media["Media"]}')
#print(f'A situação é igual a {media["Situação"]}')
for k, v in media.items():
    print(f'{k} é igual a {v}' ) #Este for faz exatamente o mesmo que as 3 últimas linhas, para cada key e valor dentro dos itens de media, print
