
#4. O cardápio de uma lanchonete é o seguinte:
#Especificação     Código      Preço
#Cachorro quente   100   1,20
#Bauru simples     101   1,30
#Bauru com ovo     102   1,50
#Hambúrger         103   1,20
#Cheeseburguer     104   1,30
#Refrigerante      105   1,00

#Escrever um algoritmo que leia o código do item pedido, 
#a quantidade e calcule o 
#valor a ser pago por aquele lanche. Considere que a cada 
#execução somente será calculado um item.


cod = int(input("Digite qual o código do pedido selecionado: "))

if cod == 100: 
    produto = "Cachorro Quente"
    prec = 1.20
elif cod == 101:
    produto = "Bauru Simples"
    prec = 1.30
elif cod ==102:
    produto = "Bauru com ovo"
    prec = 1.50
elif cod == 103:
    produto = "Hambúrger"
    prec = 1.20
elif cod == 104:
    produto = "Chesseburger"
    prec = 1.30
else:
    produto = "Refrigerante"
    prec = 1.00

qtd = int(input(f"Item escolhido: {produto}\npreço por unidade: {prec}\nDigite a quantidade desejada: "))
precFinal = qtd*prec
print (f"Pedido final {qtd} {produto}\nValor Final: R${precFinal}")