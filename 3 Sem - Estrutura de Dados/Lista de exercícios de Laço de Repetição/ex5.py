#5.  Pesquisa sobre Nível de Satisfação e Tempo de Residência: 
#   A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, 
#   coletando dados sobre o nível de satisfação com a cidade e tempo de residência. A prefeitura deseja saber:
#   a) média do nível de satisfação da população;
#   b) tempo de residência médio na cidade;
#  c) percentual de pessoas insatisfeitas;
#  d) percentual de pessoas que residem na cidade há mais de 10 anos.
#  A pesquisa termina quando for inserido o valor -1 para o nível de satisfação.

somaTempRes = 0
satisf = 0
insatisf = 0
resMais10 = 0
cont = 0
while True:
    sat = input(f"Digite o nível de satisfação da {cont+1}ª pessoa (S para Satisfeito, I para Insatisfeito, ou X para sair): ").upper()
    if sat == "X":
        break
    if sat not in ["S", "I"]:
        print("Entrada inválida. Digite S para Satisfeito ou I para Insatisfeito.")
        continue
    tempRes = int(input(f"Digite o tempo de residência (em anos) da {cont+1}ª pessoa: "))
    somaTempRes += tempRes
    cont += 1
    if sat == "S":
        satisf += 1
    else:
        insatisf += 1
    if tempRes > 10:
        resMais10 += 1
if cont > 0:
    mediaTempRes = somaTempRes / cont
    percSatisf = (satisf / cont) * 100
    percInsatisf = (insatisf / cont) * 100
    percResMais10 = (resMais10 / cont) * 100
    print("\nResultados da pesquisa:")
    print(f"a) Percentual de pessoas satisfeitas: {percSatisf:.2f}%")
    print(f"b) Percentual de pessoas insatisfeitas: {percInsatisf:.2f}%")
    print(f"c) Tempo de residência médio: {mediaTempRes:.2f} anos")
    print(f"d) Percentual de pessoas que residem há mais de 10 anos: {percResMais10:.2f}%")
else:
    print("Nenhuma pessoa foi cadastrada.")