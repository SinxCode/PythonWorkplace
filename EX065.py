m = 0
c = 0
t = ''
maior = 0
menor = 0
total = 0
while t != 'N':
    n = int(input('Digite um número inteiro: '))
    t = str(input('Deseja digitar mais um número? [S/N] ')).strip().upper()
    c = c + 1
    total = total + n
    m = total/c
    if n > maior:
        maior = n
    if n < maior:
        menor = n    
print('A soma dos números informados é: {}'.format(total))
print('A media dos números informados é: {}'.format(m))
print('O maior número informado é: {}'.format(maior))
print('O menor número informado é: {}'.format(menor))          
