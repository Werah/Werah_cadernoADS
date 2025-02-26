import time
cont = 0
while (cont < 1):
    print("-------Calculadora-------")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair do Programa")
    print("--------------------------")
    tipo = int(input("Escolha uma operação:"))
    if (tipo == 1):
        print("-------SOMA-------")
        n1 = int(input("Digite o 1º Valor:"))
        n2 = int(input("Digite o 2º Valor:"))
        n3 = n1 + n2
        print(f"O Resultado da Soma é: {n3}")
        time.sleep(2)
    elif tipo == 2:
        print("-------SUBTRAÇÃO-------")
        n1 = int(input("Digite o 1º Valor:"))
        n2 = int(input("Digite o 2º Valor:"))
        n3 = n1 - n2
        print(f"O Resultado da Subtração é: {n3}")
        time.sleep(2)
    elif tipo == 3:
        print("-------MULTIPLICAÇÃO-------")
        n1 = int(input("Digite o 1º Valor:"))
        n2 = int(input("Digite o 2º Valor:"))
        n3 = n1 * n2
        print(f"O Resultado da Multiplicação é: {n3}")
        time.sleep(2)
    elif tipo == 4:
        print("-------DIVISÃO-------")
        n1 = int(input("Digite o 1º Valor:"))
        n2 = int(input("Digite o 2º Valor:"))
        n3 = n1 / n2
        print(f"O Resultado da Divisão é: {n3}")
        time.sleep(2)
    elif tipo == 0:
        print("-------SAIR-------")
        cont = 2
    else:
        print("Opção Invalida, tente novamente!")
