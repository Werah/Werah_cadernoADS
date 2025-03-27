"""3. Função que recebe uma lista de números e imprime o dobro de cada número
Entrada: [2, 4, 6] | Saída esperada: 4, 8, 12 (um por linha)."""

numeros = [2, 4, 6]

def funcDobrar(numeros):
    for numero in numeros:
        print (numero * 2)

funcDobrar(numeros)