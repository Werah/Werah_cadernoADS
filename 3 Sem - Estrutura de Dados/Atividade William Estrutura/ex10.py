#10.solicitar a idade e altura de 5 pessoas. Ao final, exibir qual a pessoa mais alta, a
# mais baixa, a mais nova e a mais velha.


#Variavel para contar a maior e menor idade, maior e menor altura.
cont_ordem = 0
maior_altura = float("-inf")
menor_altura = float("inf")
maior_idade = float("-inf")
menor_idade = float("inf")
#Variavel para exibir qual a pessoa correta no final
pessoa_maior_altura = 0
pessoa_menor_altura = 0
pessoa_maior_idade = 0
pessoa_menor_idade = 0
#loop de for de 0 até 4 que pega as idades, para ficar de 1 até 5, soma o i+1
for i in range (0,5):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    altura = float(input(f"Digite a altura da {i+1}ª pessoa: "))
#ifs que comparam a idade digitada com o valor de maior e menor, para pegar o valor correto
    if idade > maior_idade:
        maior_idade = idade
        pessoa_maior_idade = i+1 #i+1 para mostrar de 1 até 5 no lugar de 0 até 4
    if idade < menor_idade:
        menor_idade = idade
        pessoa_menor_idade = i+1  
#mesma coisa que os de cima porém com altura
    if altura > maior_altura:
        maior_altura = altura
        pessoa_maior_altura = i + 1
    if altura < menor_altura:
        menor_altura = altura
        pessoa_menor_altura = i + 1 

print(f"A maior idade é a da {pessoa_maior_idade}ª pessoa!")
print(f"A menor idade é a da {pessoa_menor_idade}ª pessoa!")
print(f"A maior altura é a da {pessoa_maior_altura}ª pessoa!")
print(f"A menor altura é a da {pessoa_menor_altura}ª pessoa!")
