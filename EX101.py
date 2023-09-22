def voto(nasc = 0):
    from datetime import datetime
    ano = datetime.now().year
    idade = ano - nasc
    if  18 <= idade < 65:
        r = f'com {idade} anos: Voto Obrigatório.'
    elif  16 <= idade < 18 or idade >= 65:
        r = f'com {idade} anos: Voto Opcional.'
    else:
        r = f'com {idade} anos: Voto Negado.'
   
    return r

   
print('=-' * 30)
print(f'{"VERIFICAÇÃO DE ELIGIBILIDADE DE VOTO":^55}')
print('=-' * 30)

resultado = int(input('Informe o ano de seu nascimento: '))
votacao = voto(resultado)

print(votacao)    
