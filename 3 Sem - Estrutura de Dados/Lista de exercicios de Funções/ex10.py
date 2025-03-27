'''10. Sistema de controle de estoque
Crie um sistema com funções para adicionar, remover, listar e buscar produtos usando menu com while e
listas. '''

estoque = []

def mostrarMenu():
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Listar produtos")
    print("4. Buscar produto")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def adicionarProduto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    produto = {"nome": nome, "quantidade": quantidade}
    estoque.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")

def removerProduto():
    nome = input("Digite o nome do produto a remover: ")
    for produto in estoque:
        if produto["nome"] == nome:
            estoque.remove(produto)
            print(f"Produto '{nome}' removido com sucesso!")
            return
    print("Produto não encontrado!")

def listarProdutos():
    if not estoque:
        print("Estoque vazio!")
    else:
        print("\n=== LISTA DE PRODUTOS ===")
        for produto in estoque:
            print(f"{produto['nome']}: {produto['quantidade']} unidades")

def buscarProduto():
    nome = input("Digite o nome do produto a buscar: ")
    for produto in estoque:
        if produto["nome"] == nome:
            print(f"Produto encontrado - {produto['nome']}: {produto['quantidade']} unidades")
            return
    print("Produto não encontrado!")

while True:
    opcao = mostrarMenu()
    
    if opcao == "1":
        adicionarProduto()
    elif opcao == "2":
        removerProduto()
    elif opcao == "3":
        listarProdutos()
    elif opcao == "4":
        buscarProduto()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")