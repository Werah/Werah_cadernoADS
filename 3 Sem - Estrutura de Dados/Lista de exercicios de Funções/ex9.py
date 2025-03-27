'''9. Enquete com contagem de votos e resultado final
Crie uma função com menu de votação, uso de laço e uma função para determinar o vencedor.'''

votos = [0, 0, 0]

def votacao(votos):
    while True:
        print("-----------------------------------------------------------")
        print("1 - Candidato A\n2 - Candidato B\n3 - Candidato C\n0 - Sair e Exibir Resultados!")
        try:
            escolha = int(input("Digite o número do candidato: "))
        except ValueError:
            print("Por favor, digite apenas números!")
            continue
        if escolha == 0:
            break        
        elif 1 <= escolha <= 3:
            votos[escolha-1] += 1
            print(f"Voto registrado para o Candidato {'ABC'[escolha-1]}!")
        else:
            print("Escolha invalida, escolha entre 1, 2 ou 3!")
            continue
    print(votos)
    print(f"Total de votos: {sum(votos)}")
    maisVotos = max(votos)
    if votos.count(maisVotos) > 1:
        print("Houve um empate entre os candidatos!")
    else:
        candidatoVencedor = votos.index(maisVotos)
        print(f"O candidato mais votado foi: Candidato {'ABC'[candidatoVencedor]} com {maisVotos} votos!")

votacao(votos)
