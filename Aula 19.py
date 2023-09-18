pessoas = {'nome': 'Sinx', 'sexo': 'M', 'idade':24 } #Dicionários são declarados com chaves '{}' ou  dict()
print(pessoas)
print(pessoas['nome'])#Printa o valor dentro da chave "nome"
#del pessoas['sexo'] apagaria a chave sexo
#pessoas['nome'] = 'Leandro' - substituiria o nome 'Sinx' por 'Leandro'
pessoas['peso'] = 60 #Adiciona um novo elemento no dicionário
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())#Printa somente as chaves do dicionário
print(pessoas.values())#Printa somente os valores dentro do dicionario
print(pessoas.items())#Printa os itens do dicionario
for k in pessoas.keys(): #Para cada chave dentro de chave
    print(k)
for k in pessoas.values(): #Para cada chave dentro de valor
    print(k)
for k, v in pessoas.items(): #Substitui o enummarate
    print(f'{k} = {v}')
