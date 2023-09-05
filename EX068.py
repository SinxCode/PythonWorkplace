from random import randint
print('=-' * 20)
print('Jogo do Par ou Ímpar')
print('=-' * 20)
nome = str(input('Diga o seu nome: '))
vitorias = 0
while True:
    vitorias = vitorias
    total = 0
    escolha = int(input('''Escolha entre:
                        [1] PAR
                        [2] ÍMPAR '''))
    if escolha == 1:
        print(f'Ok, {nome}! Você escolheu PAR!')
    else:
        print(f'Ok, {nome}! Você escolheu ÍMPAR!')    
    jogador = int(input('Agora digite um valor inteiro: '))
    maquina = randint(1, 10)
    print('=-' * 20)
    print(f'Sua escolha foi: {jogador} ')
    print(f'Escolha da máquina foi: {maquina}')
    print('=-' * 20)
    total = jogador + maquina
    if total % 2 ==0 and escolha == 1:
        print(f'Parabéns, {nome}! Você venceu!')
        vitorias = vitorias + 1
        print(f'Total de vitórias: {vitorias}')
        print('=-' * 20)
    elif total % 2 != 0 and escolha ==2:
        print(f'Parabéns, {nome}! Você venceu!')
        vitorias = vitorias + 1
        print(f'Total de vitórias: {vitorias}')
        print('=-' * 20)    
    else:
        break
print('Infelizmente você foi DERROTADO pela Machine')
print(f'Total de vitórias em sequência: {vitorias}')
str(input('Aperte algo pra sair: '))

        
    

                

        
    
