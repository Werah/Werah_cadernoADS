'''4. Simule um jogo da velha. Crie uma matriz 3x3 e permita que dois jogadores joguem alternadamente,
escolhendo a linha e a coluna onde querem marcar (X ou O).
Não permita sobrescrever posições já ocupadas e exiba o tabuleiro a cada jogada.'''

tabuleiro = []
cont = 0
for i in range(3):
    linha = []
    for j in range(3):
        cont+=1
        linha.append(str(cont))
    tabuleiro.append(linha)

def ganhou():
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2]:
            return linha[0]
    
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna]:
            return tabuleiro[0][coluna]
    
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return tabuleiro[0][2]
    
    return None

turno = 1
jogador = "o"

while True:
    for linha in tabuleiro:
        print(linha)
    print("-----------------------------")
    try:
        jogada = int(input(f"Turno: {turno} | Jogador: {jogador}\nEscolha em qual casa jogar: "))
        if jogada < 1 or jogada >9:
            print("EScolha um valor válido")
            continue
    except ValueError:
        print("Digite um valor válido!")
        continue
    linha = (jogada-1) // 3
    coluna = (jogada-1) % 3
    if tabuleiro[linha][coluna] not in ["o", "x"]:
        tabuleiro[linha][coluna] = jogador
        turno+=1
    else:
        print("Essa casa já está ocupada, escolha outra")
        continue
    ganhador = ganhou()
    if ganhador:
        print(f"O jogador {ganhador} venceu!")
        break
    
    if turno == 9:
        print("Velha!")
        break

    jogador = "x" if jogador == "o" else "o"





'''00 01 02
A1|A2|A3
10 11 12
B1|B2|B3
20 21 22
C1|C2|C3'''