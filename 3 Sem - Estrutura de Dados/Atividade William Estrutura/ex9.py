#9. solicitar a idade de 5 pessoas e exibir a maior e menor idade, além da média das
# idades.

#Variavel para contar maior e menor idade, e soma das idades para média.
maior_idade = int(0)
menor_idade = int(0)
soma_idades = 0
#loop de for de 0 até 4 que pega as idades, para ficar de 1 até 5, soma o i+1
for i in range (0,5):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
#ifs que comparam a idade digitada com o valor de maior e menor, para pegar o valor correto
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade or menor_idade == 0: #o or ==0 é para substuir o primeiro valor definido na variavel
        menor_idade = idade
#soma o valor da média com a idade digitada para dividir no final
    soma_idades+=idade
#aumenta o contador para exibir a pessoa correta


print(f"A maior idade é {maior_idade} anos!")
print(f"A menor idade é {menor_idade} anos!")
#divide o valor da média pelo número de repetições do ciclo (tem q somar +1 pq começa no 0)
print(f"A soma_idades de idades é {soma_idades/(i+1)} anos!")




