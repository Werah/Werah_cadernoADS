l1 = float(input("Digite o 1º lado do triangulo: "))
l2 = float(input("Digite o 2º lado do triangulo: "))
l3 = float(input("Digite o 3º lado do triangulo: "))

if (l1 == l2 == l3):
    print ("O triangulo é equilátero")
elif (l1 == l2 != l3) or (l1 == l3 != l2) or (l2 == l3 != l1):
    print ("O triangulo é isóceles")
elif (l1 != l2 != l3):
    print ("O triangulo é escaleno")
