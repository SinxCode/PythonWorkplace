n = 0
c = 0
s = 0

while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    c = c+1
    s = s + n
print(f'Foram digitados {c} valores e a soma deles é: {s}')    