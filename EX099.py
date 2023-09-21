from time import sleep
def maior(*n):
    print('Analisando valores: ')
    print('=-'*30)   
    for pos, valor in enumerate(n):
        print(f'{valor}',end=' ', flush=True)
        pos = pos+1
        sleep(0.5)  
    print(f' foram informados {pos} valores e o maior é {max(n)}', end='', flush=True)
    sleep(0.5)

print('=-' * 30)
maior(5,10,8,9,1,2,11,55)
print()
maior(5,10,8,9,1)