"""2. Função que adiciona nomes a uma lista
Crie uma função que leia 5 nomes via input() e retorne uma lista com todos eles usando .append()."""

def funcNomes():
    nomes = []
    for i in range (5):
        nome = input(f"Digite o {i+1}º nome: ")
        nomes.append(nome)
    return nomes

listaNomes = funcNomes()
print (listaNomes)