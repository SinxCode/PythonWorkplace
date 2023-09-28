try: #Tenta fazer o código
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: #Traz o erro, se existir. 
                          #Não é obrigatório fazer o Exception, só se quiser saber qual erro aconteceu
    print(f'Problema encontrado foi {erro.__class__} :(')
else: #Traz o resultado casa não haja erro.
    print(f'O resultado é {r}')
finally: #Acontece idenpentende se der erro ou não
    print('Volte sempre')