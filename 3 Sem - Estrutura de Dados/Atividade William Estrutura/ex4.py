#4. Fazer um programa em "python" que pergunte um valor em graus Fahrenheit e imprime na tela o correspondente em graus Celsius usando as fórmulas que seguem.
# a) Usar uma variável double para ler o valor em Fahrenheit e a fórmula C=(f-32.0) * (5.0/9.0).


# Solicita ao usuário um valor em Fahrenheit
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Converte para Celsius
celsius = (fahrenheit - 32.0) * (5.0 / 9.0)

# Exibe o resultado
print(f"{fahrenheit:.2f}°F equivale a {celsius:.2f}°C")