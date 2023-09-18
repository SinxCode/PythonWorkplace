estado = dict()
brasil = list()
for c in range (0,3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['Sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy()) #Método para copiar dados de dicionário para dentro de uma lista
print(brasil)

for e in brasil:
    print(e) #Para cada estado (linha) em Brasil

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}' )

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

