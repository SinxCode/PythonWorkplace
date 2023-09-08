n = (int(input('Digite o 1ª número: ')),
     int(input('Digite o 2ª número: ')),
     int(input('Digite o 3ª número: ')),
     int(input('Digite o 4ª número: ')))
print(f'Você digitou os números: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ',end='')
for num in n:
    if n % 2 ==0:
        print(num, end=' ')
    
