l1 = float(input("Digite o 1º angulo interno do triangulo: "))
l2 = float(input("Digite o 2º angulo interno do triangulo: "))
l3 = float(input("Digite o 3º angulo interno do triangulo: "))

if (l1 + l2 + l3) != 180:
    print ("A soma dos angulos não deu 180º, logo não e um triangulo")
elif l1 == 60 and l2 == 60 and l3 == 60:
    print ("O triangulo é equilátero")
elif (l1 > 90 or l2 > 90 or l3 > 90):
    print ("O triangulo é obtusângulo")
elif (l1 == 90 or l2 == 90 or l3 == 90):
    print ("O triangulo é retângulo")
elif (l1 < 90 and l2 < 90 and l3 < 90):
    print ("O triangulo é acutângulo")
