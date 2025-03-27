'''4. Função que calcula a média de notas de 5 alunos
Use uma lista para armazenar notas e uma função para calcular e exibir a média.'''

notas = []

def funcMedia(notas):
    for i in range(5):
        nota = float(input(f"Digite a nota do {i+1}º aluno: "))
        notas.append(nota)
    print(f"As notas são: {notas}")
    media = sum(notas)/len(notas)
    print(f"A média da turma foi: {media}")

funcMedia(notas)