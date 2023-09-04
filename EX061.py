
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
c = 1
while c <=10:
    print('{} > '.format(termo),end='')
    termo = termo + razao
    c = c+1
print('Fim')    
