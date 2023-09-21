def fatorial(n = 1):
    f = 1
    for c in range (n, 0, -1):
        f = f * c
    return f

print('-='*30)
num = int(input('Número: '))
print(f'O fatorial de {num} é igual a {fatorial(num)}')


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}. {f3}')

print('=-' * 30)

def par(n = 0):
    if n % 2 ==0:
        return True
    else:
        return False
    

num = int(input('Número: '))
if par(num):
    print('É Par!')
else:
    print('É impar')

    