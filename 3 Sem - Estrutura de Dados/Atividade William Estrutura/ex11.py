#11. Tereza tem 1,70m e cresce 2 centimetros por ano, enquanto Lola tem
# 1,10m e cresce 3 centimetros por ano. Construir um programa em python que
# calcule e imprima quantos anos serão necessários para que Lola seja
# maior que Tereza (Utilize a estrutura while).

#Variaveis que vão guardar a altura e o contador de anos
lola = 1.10
tereza = 1.70
contador_anos = 0

#Loop infinito que vai somar a altura a cada ciclo e aumentar 1 ano
while True:
    lola = (lola+0.03)
    tereza = (tereza+0.02)
    contador_anos+=1
#Quando lola for mais alta que tereza o loop vai parar
    if lola > tereza:
        break

print(f"Após {contador_anos} Lola será maior, pois terá {lola:.2f}m, e Tereza:{tereza:.2f}m")