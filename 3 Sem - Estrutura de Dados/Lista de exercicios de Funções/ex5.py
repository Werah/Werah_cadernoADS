'''5. Função que verifica se um nome existe na lista
Entrada: lista de nomes + nome a procurar | Saída: 'Nome encontrado' ou 'Nome não encontrado'''

nomes = ["Paulo", "Vitor", "Guarnieri"]

def verificarNome(listaNomes):
    print(f"Lista de nomes: {listaNomes}")
    nome = input("Digite o nome que você deseja pesquisar: ").capitalize()
    if nome in listaNomes:
        print("Nome encontrado")
    else:
        print("Nome não encontrado")

verificarNome(nomes)