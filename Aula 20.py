def soma(a, b): #Declaramos uma função com o 'def' + 'nome da função' + '()' + ':'
    print(f'A = {a} B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


def lin(): #Função sem parâmetros
    print('=-' * 30)


#Programa principal é o que chamaos depois de uma declaração de função e normalmente pulamos 2 linhas depois da def por identação
lin()       #Chamando uma função
soma(4, 5)  #Chamando uma função com parâmetros
lin()
soma(a = 8, b = 9) #Támbem é possível especificar o parâmetro com a sua variável e mudar ordem se desejado
lin()
soma(b = 2, a = 1)
lin()

