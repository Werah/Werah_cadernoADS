ncadeira = int(input("Informe o número de cadeiras que irá comprar: "))

if ncadeira <= 50:
    vfinal = ncadeira * 45
    print (f"O valor final ficou em R${vfinal},00")
else:
    vfinal = ncadeira * 40
    print (f"O valor final ficou em R${vfinal},00")           
