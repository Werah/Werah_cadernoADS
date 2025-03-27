#2. Fazer um programa em python que imprime uma tabela com a tabuada de 1 a 9,
#O usuário deve pedir qual tabuada quer ver e o sistema mostra a referida tatuaba.


# Solicita ao usuário um número para ver a tabuada
num = int(input("Digite um número entre 1 e 9 para ver a tabuada: "))

# Verifica se o número está dentro do intervalo permitido
if 1 <= num <= 9:
    print(f"\nTabuada do {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
else:
    print("Por favor, digite um número entre 1 e 9.")