'''sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
print('Obrigado!')   '''

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos! Por favor, informe o seu sexo com M ou F: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))    