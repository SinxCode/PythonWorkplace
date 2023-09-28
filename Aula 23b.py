try: #Tenta fazer o código
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): #Verifica se o erro é do tipo valor ou type
    print('Poxa... Tivemos um problema com o tipo de dado que vc digitou.')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}')
else: 
    print(f'O resultado é {r}')
finally: 
    print('Volte sempre')