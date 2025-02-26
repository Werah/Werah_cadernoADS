n1 = 0
n2 = 0
resultado = 0
while (n1 != -888) or (n2 != -888):
    print ("Digite '-888' para encerrar o programa")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print ("Escolha a operação desejada")
    print ("------------------------")
    print ("1 - Soma")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    operacao = int(input(" "))
    if (operacao == 1):
        resultado = n1 + n2
    elif (operacao == 2):
        resultado = n1 - n2
    elif (operacao == 3):
        resultado = n1 * n2
    elif (operacao == 4):
        resultado = n1 / n2
    else:
        ("Algo deu errado")
    print ("O resultado é: ", resultado)

valor_dolar = 1243871
