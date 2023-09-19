dicionario = dict()
gols = list()
total = 0
print('=-'*30)
print(f'{"CADASTRO JOGADOR DE FUTEBOL":^55}')
print('=-'*30)
dicionario['Nome'] = input('Informe o nome do jogador: ')
n = int(input('Informe quantas partidas ele jogou: '))
for c in range (1, n + 1):
  gols.append(int(input(f'Quantos gols na partida {c}ª Partida: ')))
dicionario['Gols'] = gols
dicionario['Total'] = sum(gols)
print('=-' * 30)
print(f'O jogador: {dicionario["Nome"]} jogou {len(dicionario["Gols"])} partidas')
for i, v in enumerate(dicionario['Gols']):
  print(f'   -> Na {i+1}ª fez {v} gols')
print('=-'*30)
print(f'Foi um total de: {dicionario["Total"]}')
print('=-'*30)





   
