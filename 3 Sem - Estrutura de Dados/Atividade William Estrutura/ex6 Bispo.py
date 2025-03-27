while True:
    valores= []
    # entrada dos valores: valor_a e valor_b
    valor_a = int(input("Digite o valor: "))
    valor_b = int(input("Digite outro valor: "))
    # verifica e compara os valores
    if valor_a < valor_b:   #se o primeiro for menor que o segundo, então...
        for i in range (valor_a,valor_b+1): #lista cada valor de um número até o outro
            valores.append(i) #guarda na lista
    else:
        for i in range(valor_a,valor_b-1,-1):
            valores.append(i)
    print("Lista de valores: ",valores)

    # Pergunta se deseja continuar
    continuar = input("Deseja continuar? (S/N): ")
    if continuar == 'N':
        print("FIM")
        break