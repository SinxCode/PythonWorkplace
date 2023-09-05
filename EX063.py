n1 = int(input('Digite um número inteiro: '))
t1 = 0
t2 = 1
print('{} > {} '.format(t1, t2), end='')
c = 3
while c <= n1:
    t3 = t1 + t2
    print(' > {} '.format(t3),end='')
    t1 = t2
    t2 = t3
    c = c+1
print(' > Fim')   