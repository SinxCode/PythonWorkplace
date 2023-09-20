from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    
    if fim < inicio:
        if passo < 0:
            passo = passo * -1
        passo = passo * -1

    if passo > 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim + 1, passo):
            print(f'{c}, ', end='', flush=True) #flush = True é para que desativar o buff de espera (sleep) que aconteceria na tela
            sleep(0.5)  
        print('Fim!')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim - 1, passo):     
            print(f'{c}, ', end='', flush=True)
            sleep(0.5) 
        print('Fim!')


print('=-' * 30)
contador(1, 10, 1)
print('=-' * 30)
contador(10, 0, -2)
print('=-' * 30)
print('AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
Passo = int(input('Passo: '))
print('=-' * 30)
contador(inicio, fim, Passo)