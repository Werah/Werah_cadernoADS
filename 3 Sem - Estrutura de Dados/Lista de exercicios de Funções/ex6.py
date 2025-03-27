'''6. Função que conta quantas palavras possuem mais de 5 letras
Entrada: ['computador', 'mouse', 'cabo', 'teclado'] | Saída: 2'''

palavras = ['computador', 'mouse', 'cabo', 'teclado']

def funcContLetras(palavras):
    cont = 0
    for palavra in palavras:
        if len(palavra) > 5:
            cont += 1
    print(f"O numero de palavras com mais de 5 letras é: {cont}")

resultado = funcContLetras(palavras)