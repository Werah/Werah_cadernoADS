#3. Fazer um programa python que solicita um número decimal e imprime o correspondente em hexa, Binário e octal. 
#Refaça pedindo pra que o usuário informe o tipo de numero, se octal, binário ou decimal e mostre as suas conversões.


def converter_decimal(numero):
    print(f"Decimal: {numero}")
    print(f"Binário: {bin(numero)[2:]}")
    print(f"Octal: {oct(numero)[2:]}")
    print(f"Hexadecimal: {hex(numero)[2:].upper()}")

def converter_outros(numero, tipo):
    if tipo == "bin":
        decimal = int(numero, 2)
    elif tipo == "oct":
        decimal = int(numero, 8)
    else:
        decimal = int(numero)  # decimal

    converter_decimal(decimal)

# Versão 1: Converter de decimal para outros formatos
num_decimal = int(input("Digite um número decimal: "))
converter_decimal(num_decimal)

print("\nAgora, escolha o tipo de número que deseja converter:")
tipo = input("Digite 'dec' para decimal, 'bin' para binário ou 'oct' para octal: ").strip().lower()
numero = input(f"Digite um número no formato {tipo}: ").strip()

converter_outros(numero, tipo)