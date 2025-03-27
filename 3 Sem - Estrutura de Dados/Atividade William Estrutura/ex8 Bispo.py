# a) Escrever todas as letras do alfabeto maiúsculas e minúsculas
alfabeto_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabeto_minusculas = "abcdefghijklmnopqrstuvwxyz"

print("Letras maiúsculas:", end=" ") # utilizar o end para não quebrar linha
for letra in alfabeto_maiusculas: # listar todas as letras através do laço de repetição
    print(letra, end=" ")

print("\nLetras minúsculas:", end=" ")
for letra in alfabeto_minusculas:
    print(letra, end=" ")

print("\n")

# b) Exibir a soma dos números de 0 a 100
soma_numeros = 0
for i in range(101):
    soma_numeros += i
print("Soma dos números de 0 a 100:", soma_numeros)
print("\n")

# c) Exibir a soma dos 100 primeiros números pares
soma_pares = 0
contador = 0  # conta quantos números pares foram somados
num = 0  # começa do primeiro número par

while contador < 100:
    soma_pares += num
    num += 2  #pula para o próximo número par
    contador += 1

print("Soma dos 100 primeiros números pares:", soma_pares)
print("\n")

# d) calcular o perímetro de um pentágono
lado = float(input("Digite o valor do lado do pentágono: "))
perimetro = 5 * lado
print("Perímetro do pentágono:", perimetro)