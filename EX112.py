def leiaint(msg):
    while True:
        try:
            r = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro. Digite um valor válido!\033[m')
            continue #Faz voltar pro laço
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar o dado!\033[m')  
            break  
        else:
            print(f'O usuário digitou o número {r}')
            return r


def leiafloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro. Digite um valor válido!\033[m')
            continue #Faz voltar pro laço
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar o dado!\033[m')  
            break  
        else:
            print(f'O usuário digitou o número {r}')
            return r
        

n = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')
print(f'O numero inteiro digitado foi {n} e o real foi {f}')
