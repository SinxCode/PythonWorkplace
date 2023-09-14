galera = list()
dado = list()
maior = 0
menor = 0
for c in range(0,3):
    dado.append(input('Informe seu nome: '))
    dado.append(int(input('Informe sua idade: ')))
    galera.append(dado[:]) #Copia as informações digitadas dentro da lista dado, para lista galera.
    dado.clear() #Limpa a lista dado, pois ela já está copiada para galera.
print(galera)

for p in galera:
    if p [1] >=21: #Verifica a idade que está no indice 1 dos dados da lista de galera
        print(f'{p[0]} é maior de idade.')
        maior = maior + 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor = menor + 1
print(f'Temos {maior} maiores de idade e {menor} menores de idade.')