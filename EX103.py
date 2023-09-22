def ficha(nome ='', gols = 0 ):
    if nome == '':
        return f'<Nome desconhecido>, marcou 0 gols.'
    else:
        return f'{nome} marcou {gols} gols.'
    

print('=-' * 30)
jogador = input('Informe o nome do jogador: ')
gol = input('Informe a quantidade de gols marcados: ')

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if jogador.strip()=='':
    r = ficha(gols=gol)
else:
    r = ficha(jogador,gol)
print('=-' * 30)
print(r)
    

