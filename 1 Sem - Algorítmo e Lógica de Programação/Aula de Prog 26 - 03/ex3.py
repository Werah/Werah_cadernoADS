vprod = float(input("Informe o valor do produto: "))
print ("--------------")
print ("1 - À Vista")
print ("2 - A Prazo")
metodo = float(input("Escolha o metodo de pagamento (1 ou 2): "))
if metodo == 1:
    vfinal = vprod * 0.9
    print (f"Pagamento a Vista: R${vfinal}")
elif metodo == 2:
    print (f"Pagamento a Prazo: R${vprod}")
else:
    print ("VOCÊ DEVE SER EXTERMINADO")
