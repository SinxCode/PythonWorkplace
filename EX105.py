def notas(*n, sit = False):
    """
        -> Função para analisar notas e situações.
    :param: n: Uma ou mais notas do aluno (aceita várias)
    :param: sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma

    """
    dicionario = dict()
    dicionario['Quantidade'] = len(n)
    dicionario['Maior'] = max(n)
    dicionario['Menor'] = min(n)
    #dicionario['Soma'] = sum(n)
    dicionario['Média'] = sum(n)/len(n)
    if sit:
        if dicionario['Média'] >=7:
            dicionario['Situação'] = 'Aprovado.'
        if dicionario['Média'] >=5:
            dicionario['Situação'] = 'Recuperação'
        else:
            dicionario['Situação']= 'Reprovado'
        
    return dicionario


resp = notas(1.2,5,6.5,5,7,5, sit=True)
print(resp)

