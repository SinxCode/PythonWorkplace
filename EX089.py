boletim = list()
m = 0
while True:
    nome = (input('Digite o nome do aluno: '))
    n1 = (float(input('Digite a primeira nota: ')))
    n2 = (float(input('Digite a segunda nota: ')))
    m = (n1+n2)/2
    boletim.append([nome, [n1,n2],m])
    r = input('Deseja incluir outro boletim? [S/N]').strip().upper()
    if r == 'N':
        break 
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')  
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')

while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('Finalizado')
        break
    if opc <=len(boletim) -1:
        print(F'Notas de {boletim[opc][0]} são {boletim[opc][1]} ')
print('Fim')

