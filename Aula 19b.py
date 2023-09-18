brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)
print(brasil) 
#Criamos 2 dicionários, e jogamos para dentro de uma lista.
print(brasil[0])
print(brasil[0]['uf']) #Traz o indice 0 da lista Brasil o valor da chave uf
print(brasil[1]['sigla'])#Traz o indice 1 da lista Brasil o valor da chave sigla
