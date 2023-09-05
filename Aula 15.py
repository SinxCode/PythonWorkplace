n = 0
s = 0
while True:   
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print(f'A soma vale: {s} ') ##atualização do python permite utilizar apenas um f minusculo antes da string para mostrar o valor, não é necessário utilizar .format


