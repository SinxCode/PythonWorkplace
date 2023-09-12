lista = list()
c= 0
e = input('Digite uma expressão: ')
for simb in e:
    if simb =='(':
        lista.append('(')
        print(lista)
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            print(lista)
            lista.append(')')
            print(lista)
            break
print(lista)
if len(lista) == 0:
    print('A expressão é válida!')
else:
    print('A expressão é invalida')