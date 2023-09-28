from Aula22_Uteis import *  #O Asterisco importa todos os dados da biblioteca 
                            #sem a necessidade de escrever o nome dela + '.' nos códigos

num = int(input('Digite um número: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro(num)}.')
print(f'O triplo de {num} é {triplo(num)}.')