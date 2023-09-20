def dobra(lst): #Atribuindo uma função a uma lista
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos] * 2 #Está dobrando cada valor da lista chamada "Valores definidos abaixo"
        pos = pos + 1


valores = [6, 3, 9, 1, 0 , 2]
dobra(valores)
print(valores)
