tupla = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ')

while True:
    n = int(input('Digite um número de 0 a 10: '))
    if 0 <= n <=10:
        break
print(f' Você digitou: {tupla[n]}') 
