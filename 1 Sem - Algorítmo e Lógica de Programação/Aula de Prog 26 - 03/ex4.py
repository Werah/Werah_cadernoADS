idade = int(input("Informe a sua idade: "))
print ("-------------")
print ("Você possui habilitação?")
print ("1 = SIM")
print ("2 = NÃO")
hab = int(input("Digite 1 ou 2"))
if idade >= 18 and hab == 1:
    print ("Você pode dirigir")
else:
    print ("VOCÊ DEVE SER ELIMINADO")
