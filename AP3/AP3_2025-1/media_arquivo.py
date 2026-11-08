def Q2(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    total = 0
    for linha in linhas:
        total += int(linha.strip())  
    
    if len(linhas) > 0:
        media = total / len(linhas)
    else:
        media = 0

    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'\nValor: {media}')

nome = input('Digite o nome do arquivo: ')
Q2(nome)