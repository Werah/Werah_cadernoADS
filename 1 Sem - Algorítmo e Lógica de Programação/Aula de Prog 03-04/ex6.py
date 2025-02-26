print ("Estado Civil \ns = Solteiro \nc = Casado \nd = Divorciado \nv = Viuvo")
opc = input ("Escolha um opção (digite a letra s, c, d ou v): ")
if opc.lower() == "s":
    print ("A opção selecionada foi Solteiro!")
elif opc.lower() == "c":
    print ("A opção selecionada foi Casado!")
elif opc.lower() == "d":
    print ("A opção selecionada foi Divorciado!")
elif opc.lower() == "v":
    print ("A opção selecionada foi Viuvo!")
else:
    print ("Opção Inválida")

