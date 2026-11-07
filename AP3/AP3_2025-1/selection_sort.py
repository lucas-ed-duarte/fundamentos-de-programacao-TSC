import random

def gerar_vetor():
    n = int(input('Tamanho do vetor: '))
    vetor = []
    for _ in range(n):
        vetor.append(random.randint(1, 100))
    return vetor

def imprimir_vetor(vetor):
    for x in vetor:
        print(x, end=" ")
    print()

def selection_sort(vetor):
    n = len(vetor)
    for i in range(n):
        menor_idx = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[menor_idx]:
                menor_idx = j
        vetor[i], vetor[menor_idx] = vetor[menor_idx], vetor[i]

vetor = gerar_vetor()          
imprimir_vetor(vetor)          
selection_sort(vetor)          
imprimir_vetor(vetor)          