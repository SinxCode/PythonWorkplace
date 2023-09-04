n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
maior = 1
index = 0
while index != 5:
    print('-='*20)
    index = int(input('''Informe a operação desejada:
                  [1] Soma
                  [2] Multiplicação
                  [3] Maior
                  [4] Novos números
                  [5] Sair do programa '''))
    print('-='*20)
    if index ==1:
        print('A soma dos números informado é: {} '.format(n1+n2))
    elif index ==2:
        print('A multiplicação dos números informados é: {}'.format(n1*n2))
    elif index ==3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre os digitados é: {}'.format(maior))
    elif index ==4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif index ==5:
        print('Finalizado')
    else:
        print('Opção inválida! Tente novamente.')
print('Fim')        
        
        


           


