from datetime import datetime
ano = datetime.now().year
print('=-' * 30)
print(f'{"CADASTRO DE TRABALHADOR" :^55}')
print('=-' * 30)
cadastro = dict()
cadastro['Nome']=input('Informe seu nome: ')
nascimento=int(input('Informe seu ano de nascimento: '))
idade = ano - nascimento
cadastro['Idade'] = idade
cadastro['CTPS'] = int(input('Infome sua carteira de trabalho: '))
if cadastro['CTPS'] ==0:
    print('=-' * 30)
    for k, v in cadastro.items():
        print(f'{k}{"."*15:<15} {v}')
    print('=-' * 30)
else:
    contratacao = int(input('Digite o ano de sua contratação: '))
    cadastro['Contratação'] = contratacao
    aposentadoria = (ano + 35) - contratacao
    cadastro['Salário'] = float(input('Informe seu salário: '))
    cadastro['Aposentadoria'] = aposentadoria
    print('=-' * 30)
    for k, v in cadastro.items():
        print(f'{k} {"."*15:<15} {v}')
    print('=-' * 30)          
print(cadastro)
