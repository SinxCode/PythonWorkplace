total = 0
print('=-' * 20)
print('Tabuada')
print('=-' * 20)
while True:
    c = 0
    n = int(input('Informe um número inteiro: '))
    if n < 0:
        break
    print('=-'*20)
    while c < 10:
        c = c + 1
        total = n * c
        print(f'{n} x {c} = {total} ')
    print('=-'*20)        
print('Fim')        
