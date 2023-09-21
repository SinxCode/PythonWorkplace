
def teste(b):
    print('=-' * 30)
    global a #o Global transforma a váriavel a em global, ou seja, independente de onde ela esteja no códico seu valor será 8.
    a = 8
    b = b + 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    print('=-'*30)

a = 5
teste(a)
print(f'A fora vale {a}')
print('=-'*30)



#Utilizando Return
def somar(a=0, b=0, c=0):
    s = a + b + c
    #print(f'A soma vale {s}') Nesse caso, substituimos o print com a variavel da soma por um retorno, dessa maneira podemos manipular S de formas diferentes. 
    return s
   

r1 = somar(3,2,5)
r2 = somar(2,2,5)
r3 = somar(1,4,6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}') #O return possibilita personalizarmos a resposta com mais resultados diferentes, por exemplo
                                                #Ao invés de termos 3 prints pra cada resposta, temos apenas 1

