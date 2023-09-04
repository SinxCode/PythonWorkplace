import random
from emoji import emojize
#:1st_place_medal:
#:loudly_crying_face:
#:smiling_face_with_horns:
#:smiling_face_with_sunglasses:
#:chicken:
#Joguinho
import pygame

pygame.init()
pygame.mixer.music.load('8 Bit Menu.mp3')
pygame.mixer_music.play()

print(emojize('Olá! Você Gosta de jogos? Pois muito bem, o que acha de tentar me vencer? :smiling_face_with_horns:'))
escolha = input('Deseja tentar vencer a máquina? (S) ou (N)? ').upper()

if escolha == 'N':
        pygame.init()
        pygame.mixer.music.load('Game Over (8-Bit Music).mp3')
        pygame.mixer.music.play()
        input(emojize('Foi o que pensei... covarde! :chicken:\nAperte qualquer tecla para sair.' ))

else:
    pygame.init()
    pygame.mixer.music.load('Lights Theme 8-Bit.mp3')
    pygame.mixer.music.play()
    print('Que comece o jogo!')
    n = random.randint(1, 5)  # Corrigido para gerar um número entre 1 e 5
    resultado = int(input('Eu acabei de pensar em número inteiro de 1 a 5, adivinhe qual é: '))
    print('Vejamos...')
    if resultado == n:
        pygame.init()
        pygame.mixer.music.load('Tema da Vitória - Fórmula 1 (8-BIT Cover).mp3')
        pygame.mixer.music.play()
        input(emojize('Parabéns! Você me venceu! :1st_place_medal:\nAperte qualquer tecla para sair!'))
    else:
        pygame.init()
        pygame.mixer.music.load('Sadness And Sorrow 8 Bit.mp3')
        pygame.mixer.music.play()
        input(emojize(
            'Hahahaha! :smiling_face_with_sunglasses: Você perdeu! Chore para mamãe :loudly_crying_face:\nAperte qualquer tecla para sair! '))


