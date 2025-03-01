# 8. Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e mostre-os em ordem decrescente.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

print(f"Valores lidos: A = {A}, B = {B}, C = {C}")

# Ordena os valores em ordem decrescente
valores = sorted([A, B, C], reverse=True)

print(f"Valores em ordem decrescente: {valores[0]}, {valores[1]}, {valores[2]}")