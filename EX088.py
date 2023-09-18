import random
from time import sleep
print('=-' * 30)
print(f'{"JOGO MEGA SENA":^55}')
print('=-' * 30)
jogo = [[]]
n = int(input('Digite quantos palpites deseja: '))
print('=-' * 30)
for c in range(1, n+1):
    for j in range(1,6+1):
        jogo[0].append(random.randint(1,60))
    jogo[0].sort()
    print(f'O {c}ª palpite é: {jogo}')
    sleep(1)
    jogo[0].clear()
print('=-' * 30)


