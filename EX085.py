valores = [[], []]
for c in range (0,7):
    n = (int(input(f'Digite o {c+1}ª valor: ')))
    c = c + 1
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort() #Ordena em ordem crescente apenas os dados do indice 0
valores[1].sort() #Ordena em ordem crescente apenas os dados do indice 1
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímapres digitados foram: {valores[1]}')


    
