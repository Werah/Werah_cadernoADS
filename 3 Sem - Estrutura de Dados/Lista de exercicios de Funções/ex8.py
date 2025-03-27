'''8. Função que remove todos os números negativos de uma lista
Entrada: [-3, 5, -2, 7, 0] | Saída esperada: [5, 7, 0]'''

numeros = [-3, 5, -2, 7, 0]

def removerNeg(numeros):
    for numero in numeros:
        if numero < 0:
            numeros.remove(numero)
    print(numeros)

removerNeg(numeros)