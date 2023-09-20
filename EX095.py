jogador = dict()
gols = list()
jogadores = list()
print('=-' * 30)
print(f'{"CADASTRO DE JOGADORES":^55}')
print('=-' * 30)
while True:
    gols.clear()
    jogador.clear()
    jogador['Nome'] = input('Nome do jogador: ')
    n = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Partidas'] = n
    for c in range(1, n + 1):
        gols.append(int(input(f'Quantos gols na {c}ª Partida? ')))
    jogador['Gols'] = gols.copy()
    jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())
    print('=-' * 30)
    while True:
        r = input('Deseja continuar? [S/N]').strip().upper()
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N! ')
    if r == 'N':
        break
    print('=-' * 30)
print(jogadores.index(jogador))
print('=-' * 30)
print(f'{"COD":<5} {"NOME":<15} {"PARTIDAS:":<15} {"GOLS":<15} {"TOTAL":<15}')
print('-'*60)
for i, v in enumerate(jogadores):
    print(f'{i}{"":^5}{v["Nome"]:^5}{"":^15}{v["Partidas"]}{"":^13}{v["Gols"]}{"":^10}{v["Total"]}{"":^13}')    
print()
while True:
    print('=-'*30)
    while True:
        p = int(input('Mostrar dados de qual jogador? [COD] (999 encerra o programa) '))
        if 0 <= p < len(jogadores):
            break
        if p == 999:
            print('=-'*30)
            print('Foi um prazer ajudar!')
            break
        print(f'ERRO! Não existe jogador com o código {p}! Tente novamente.')
    for i, v in enumerate(jogadores):
        if i == p:
         print(f'{"--":>5}LEVANTAMENTO DO JOGADOR: {v["Nome"]}:')
         for i in range(0, len(v['Gols'])):
             print(f'{"":>6}Na {i}ª partida fez: {v["Gols"][i]} gols')
    if p == 999:
        break
print('<< VOLTE SEMPRE >>')

    

    
        
            





