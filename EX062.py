primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
c = 1
nt = ''
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while c <=total:
        print('{} > '.format(termo), end='')
        termo = termo + razao
        c = c+1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')    
        