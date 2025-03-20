#12. Refaça o Exercicio 04, porém o usuario tendo a opção de Escolher em qual
# escala ele irá digitar os graus e converta para o contrário. 

while True:
    escolha = int(input("Escolha qual conversão fazer:\n1 - ºF para ºC\n2 - ºC para ºF\n"))
    if escolha != 1 and escolha != 2:
        print("Opção invalida, tente novamente!")
    else:
        break

# Se o valor foi 1 - Solicita ao usuário um valor em Fahrenheit
if escolha == 1:
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
# Converte para Celsius
    celsius = (fahrenheit - 32.0) * (5.0 / 9.0)
    print(f"{fahrenheit:.2f}°F equivale a {celsius:.2f}°C")
else:
    celsius = float(input("Digite a temperatura em graus Fahrenheit: "))
# Converte para Fahrenheit
    fahrenheit = (celsius * (9 / 5)) + 32
    print(f"{celsius:.2f}°C equivale a {fahrenheit:.2f}°F")
