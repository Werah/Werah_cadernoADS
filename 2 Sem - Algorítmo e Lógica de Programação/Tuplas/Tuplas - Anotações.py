#TUPLAS
# Uma é um conjunto de elementos.
# Quando a tupla é criada ela não pode ser alterada, adicionar ou remover elementos
#tudo que já estava dentro dela vai se manter, mesmo que as variaveis internas mudem.
#Posições na tupla:
tupla = (10, 20, 30, 40, 50)
         #0  #1  #2  #3  #4
#------------------------------------------------------

#Para representar um elemento na tupla tem que usar []
##print(tupla[0]) # Mostra somente o elemento 0
##print(tupla[0:2]) # Mostra do 0 até o 2
##print(tupla[1:]) # Mostra do 1 até o final 
#------------------------------------------------------

#Exemplo de Erro:
##num = (10, 20, 30, 40)
##num[1] = 25 #Alterar o 20 para 25
##print(num[1]) #Printar o "25", dá erro, pq a tupla n pode ser alterada
#------------------------------------------------------

#Maneiras de printar a tupla inteira:
##for i in tupla: # Printa na ordem crescente
##    print(i)

##for i in reversed(tupla): # Printa na ordem decrescente
##    print(i)

# Usando o RANGE, precisa identificar qual elemento da tupla será exibido com o colchete []
##for i in range(0, len(tupla)):
##    print(tupla[i])

# Para organizar numeros desordenados usa a função sorted, ela também lê todos os números
##print(sorted(tupla))
##print(sorted(tupla, reverse=True))
#------------------------------------------------------

#Exibindo Valor e Posição na tupla:
#> Usando enumerate() #OBS: Se não especificar o POS, ele vai aparecer no começo da linha
#por causa do 
##for iPos, iVal in enumerate(tupla):
##    print(f"Posição {iPos}: {iVal}")enumerate.

#> Usando o range()
##for i in range(0, len(tupla)):
##    print(f"Posição {i}: {tupla[i]}") #Novamente, precisa especificar qual elemento por ser o RANGE
#------------------------------------------------------

#SOMA DE TUPLAS #tupla é de 10 a 50
##tupla2 = (60, 70, 80, 90, 100)
##tuplaSoma = tupla + tupla2 # Ele vai somar os valores, então ele considera duplicatas,
#podendo ficar (10, 10, 10)
##print(tuplaSoma)
#------------------------------------------------------

#As tuplas aceitam varios tipos de valor
##pessoa = ("José", 40, "M", 75.5)
##print(pessoa)