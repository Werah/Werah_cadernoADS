alt = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso/(alt*alt)

print(imc)
if imc < 17:
    print ("Muito abaixo do Peso")
elif imc >=17 and imc <= 18.4:
    print ("Abaixo do Peso")
elif imc >=18.5 and imc <= 24.9:
    print ("Peso Ideal")
elif imc >=25 and imc <= 29.9:
    print ("Acima do Peso")
elif imc >=30 and imc <= 34.9:
    print ("Obesidade I")
elif imc >=35 and imc <= 40:
    print ("Obesidade II")
elif imc > 40:
    print ("Obesidade III")
else: print ("algo deu errado")



