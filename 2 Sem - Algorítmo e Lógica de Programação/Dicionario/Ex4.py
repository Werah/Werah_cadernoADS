jogador = {}
listaGol = []
jogador['nome'] = str(input("Digite o nome do Jogador: "))
jogador['qtdJogos'] = int(input(f"Quantos jogos {jogador['nome']} jogo?: "))

for i in range(0, jogador['qtdJogos']):
    gols = int(input(f"Quantos gols na partida {i+1}: "))
    listaGol.append(gols)
jogador['gol'] = listaGol
totalGol = 0

for i in range(len(listaGol)):
    totalGol += listaGol[i]
jogador['totalGols'] = totalGol


print("\nNome: ", jogador['nome'],
      "\nQuantidade de Partidas: ", jogador['qtdJogos'],
      "\nGols Feitos: ", jogador['gol'],
      "\nTotal de Gols: ", jogador['totalGols'])    
