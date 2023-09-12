lista = list()
menor = 0
for c in range(0,5):
    n = int(input('Informe um valor: '))
    if c == 0 or n > lista[-1]: # Compara o valor digitado com o último valor da lista
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <=lista[pos]:
                lista.insert(pos,n)
                break
            pos = pos + 1
print (lista)