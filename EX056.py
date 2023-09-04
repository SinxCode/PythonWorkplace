nome = ''
maior =0
media = 0
soma = 0
media = 0
mulher = 0
for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    n = input('Informe o nome da {}ª pessoa: '.format(c))
    i = int(input('Informe a idade da {}ª pessoa '.format(c)))
    s = int(input('''Informe o sexo:
              [1] Masculino
              [2] Feminino '''))
    soma = soma+i
    media = soma / c
    if s ==1 and c ==1:
        maior = i
        nome = n
    if s == 1 and i > maior:
        maior = i
        nome = n
    if s == 2 and i < 20:
        mulher = mulher+1       

print('A média das idades informadas é: {} '.format(media))                  
print('O homem mais velho informado é: {} '.format(nome))
print('O número de mulheres menores do que 20 anos é: {}'.format(mulher))

