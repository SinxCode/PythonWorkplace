c=0
classificacao = ('SÃO PAULO', 'PALMEIRAS', 'ATLÉTICO MINEIRO', 'BOTA FOGO', 'SANTOS', 'CURITIBA', 'CORINTHIANS', 'FLUMINENSE', 'FLAMENGO', 'VASCO')
print(f'Os 4 primeiros colocados são: \n{classificacao[0:4]}')
print(f'Os 4 últimos colocados são:\n{classificacao[-4:]}')
print(f'Lista de times em ordem alfabética:\n{sorted(classificacao)}')
print(f'A posição do time Bota fogo é {classificacao.index("BOTA FOGO")+1}ª')