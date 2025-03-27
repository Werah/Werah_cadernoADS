'''7. Sistema de notas com cadastro, média e aprovação
Crie 3 funções: uma para cadastrar nome e notas, outra para calcular média e outra para exibir resultado
final.'''

nomes = []
notas = []

def cadastrarAluno(nomes,notas):
    nome = input("Digite no nome do aluno: ")
    nomes.append(nome)
    for i in range(4):
        nota = float(input(f"{i+1}ª nota do aluno {nome}: "))
        notas.append(nota)

def calcMedia(notas):
    media = sum(notas)/len(notas)
    return media

def exibirResultado(nomes,notas):
    print(f"A média do aluno {nomes[0]} é: {mediaFinal}")

cadastrarAluno(nomes,notas)
mediaFinal = calcMedia(notas)
exibirResultado(nomes,notas)

