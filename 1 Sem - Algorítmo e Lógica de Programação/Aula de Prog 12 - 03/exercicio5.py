nome = input("Infome o nome do vendedor: ")
sal = float(input("Infome o salário do vendedor: "))
vendas = float(input("Infome o total de vendas do vendedor no mês: "))
com = vendas*0.15
final = com+sal
print ("O vendedor {} recebeu no final do mês R${}".format(nome,com),
       "\nde comissão, totalizando R${} de salário!".format(final))
