matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):#para cada linha
    for c in range(0,3):#cria 3 colunas
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()#pula a linha para cada linha formada