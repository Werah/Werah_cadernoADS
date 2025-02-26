import time
import math
cont = 0
while (cont < 1):
    print("-------Calculadora-------")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Exponeciação")
    print("6 - Raiz Quadrada")
    print("7 - Logaritmo")
    print("8 - Fatoração")
    print("9 - Porcentagem")
    print("0 - Sair do Programa")
    print("--------------------------")
    tipo = float(input("Escolha uma operação:"))
    if (tipo == 1):
        print("-------SOMA-------")
        n1 = float(input("Digite o 1º Valor:"))
        n2 = float(input("Digite o 2º Valor:"))
        n3 = n1 + n2
        print(f"O Resultado da Soma é: {n3}")
        time.sleep(2)
    elif tipo == 2:
        print("-------SUBTRAÇÃO-------")
        n1 = float(input("Digite o 1º Valor:"))
        n2 = float(input("Digite o 2º Valor:"))
        n3 = n1 - n2
        print(f"O Resultado da Subtração é: {n3}")
        time.sleep(2)
    elif tipo == 3:
        print("-------MULTIPLICAÇÃO-------")
        n1 = float(input("Digite o 1º Valor:"))
        n2 = float(input("Digite o 2º Valor:"))
        n3 = n1 * n2
        print(f"O Resultado da Multiplicação é: {n3}")
        time.sleep(2)
    elif tipo == 4:
        print("-------DIVISÃO-------")
        n1 = float(input("Digite o 1º Valor:"))
        n2 = float(input("Digite o 2º Valor:"))
        n3 = n1 / n2
        print(f"O Resultado da Divisão é: {n3}")
    elif tipo == 5:
        print("-------EXPONECIAÇÃO-------")
        n1 = float(input("Digite o 1º Valor:"))
        n2 = float(input("Digite o 2º Valor:"))
        n3 = n1 ** n2
        print(f"O Resultado da Potencia é: {n3}")
        time.sleep(2)
    elif tipo == 6:
        print("-------RAIZ QUADRADA-------")
        n1 = float(input("Digite o Valor:"))
        n3 = math.sqrt(n1)
        print(f"O Resultado da Radiação é: {n3}")
        time.sleep(2)
    elif tipo == 7:
        print("-------LOGARITMO-------")
        n1 = float(input("Digite o 1º Valor:"))
        n2 = float(input("Digite o 2º Valor:"))
        n3 = math.log(n1, n2)
        print(f"O Resultado do Logaritmo é: {n3}")
        time.sleep(2)
    elif tipo == 8:
        print("-------FATORAÇÃO-------")
        n1 = float(input("Digite o Valor:"))
        n3 = math.factorial(n1)
        print(f"O Resultado da Fatoração é: {n3}")
        time.sleep(2)
    elif tipo == 9:
        print("-------PORCENTAGEM-------")
        n1 = float(input("Digite o 1º Valor:"))
        n2 = float(input("Digite o 2º Valor:"))
        n3 = 100 * (n1/n2)
        print(f"O Resultado da Porcentagem é: {n3}%")
        time.sleep(2)
    elif tipo == 0:
        print("-------SAIR-------")
        break
    else:
        print("Opção Invalida, tente novamente!")
