import math

while True:
    # entrada dos valores valor_a e valor_b

    valor_a = float(input("Digite um número: "))
    valor_b = float(input("Digite outro número: "))

    # cálculos
    soma = valor_a +valor_b
    produto = valor_a * (valor_b**2)
    raiz = math.sqrt(valor_a**2 + valor_b**2)
    seno = math.sin(valor_a-valor_b)
    modulo = abs(valor_a)

    #saída
    print(f"\nResultados para {valor_a} e {valor_b}:")
    print(f"Soma: {soma}")
    print(f"Produto de {valor_a} pelo quadrado de {valor_b}: {produto}")
    print(f"Raiz quadrada da soma dos quadrados: {raiz}")
    print(f"Seno da diferença de {valor_a} por {valor_b}: {seno}")
    print(f"Módulo de {valor_a}: {modulo}\n")

    # pergunta se deseja continuar
    continuar = input("Deseja continuar? (S/N): ")
    if continuar == 'N':
        print("FIM")
        break