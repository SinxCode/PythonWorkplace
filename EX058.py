from random import randint
print('-='*20)
t=1
n = randint(1,10)
print('Vamos Jogar! Acabei de pensar em um número de 1 a 10, qual número pensei?: ')
palpite = int(input('Digite um número entre 1 e 10: '))
while palpite != n:
    palpite= int(input('Você errou! Tente novamente: '))
    t = t+1
print('''Parabéns, você acertou! Eu pensei no número {}
      Número de tentativas: {}'''.format(n,t))   