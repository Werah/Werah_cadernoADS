while True:
    desconto = 0
    juros = 0
    valor_final = 0

    # Entrada do valor do boleto
    valor_a_pagar = float(input("Digite o valor do boleto: "))

    # Escolha da forma de pagamento
    escolha_pagamento = input("\nFormas de Pagamento\n1. À vista\n2. À prazo\nQual a forma de pagamento desejada?\n")

    # Verifica a escolha e aplica descontos
    if escolha_pagamento == "1": #Pagamento à vista
        if valor_a_pagar <100:
            desconto = valor_a_pagar*(5/100) #Desconto de 5%
            valor_final = valor_a_pagar-desconto
            print(f"Desconto: R$ {desconto}")
            print(f"Preço final com desconto: R$ {valor_final}")
        else:
            desconto = valor_a_pagar*(8 / 100) #Desconto de 8%
            valor_final = valor_a_pagar-desconto
            print(f"Desconto: R$ {desconto}")
            print(f"Preço final com desconto: R$ {valor_final}")

    elif escolha_pagamento == "2": # Pagamento à prazo
        if valor_a_pagar<100:
            juros = valor_a_pagar*(10/100) #Acréscimo de 10%
            valor_final = valor_a_pagar+juros
            print(f"Juros: R$ {juros}")
            print(f"Preço final com juros: R${valor_final}")
        else:
            juros = valor_a_pagar*(5/100) # Acréscimo de 5%
            valor_final = valor_a_pagar+juros
            print(f"Juros: R$ {juros}")
            print(f"Preço final com juros: R${valor_final}")
    else: #Em caso do usuário digitar alguma opção diferente das mostradas acima
        print("Opção inválida. Tente novamente!")
        continue #volta ao início do loop

    # pergunta se quer continuar
    continuar = input("Deseja continuar? (S/N): ")
    if continuar == 'N':
        print("FIM")
        break