def remove_espacos(frase):
    return frase.replace(" ", "")

def conta_vogais_consoantes(frase):
    vogais = "aeiouáéíóúâêôãõàèìòùäëïöü"
    qtd_vogais = 0
    qtd_consoantes = 0
    
    for char in frase.lower():
        if char in vogais:
            qtd_vogais += 1
        elif char.isalpha():
            qtd_consoantes += 1
            
    return qtd_vogais, qtd_consoantes

def eh_palindromo(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return eh_palindromo(s[1:-1])

frase = input("Digite uma frase: ")

frase_sem_espacos = remove_espacos(frase)
print(f"A frase sem espaços é {frase_sem_espacos}")

v, c = conta_vogais_consoantes(frase)
print(f"A quantidade de vogais de '{frase}' é {v} e a quantidade de consoantes é {c}")

if eh_palindromo(frase_sem_espacos):
    print(f"{frase_sem_espacos} é palindroma")
else:
    print(f"{frase_sem_espacos} não é palindroma")