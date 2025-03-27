#5.  Pesquisa sobre Nível de Satisfação e Tempo de Residência: 
#   A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, 
#   coletando dados sobre o nível de satisfação com a cidade e tempo de residência. A prefeitura deseja saber:
#   a) média do nível de satisfação da população;
#   b) tempo de residência médio na cidade;
#  c) percentual de pessoas insatisfeitas;
#  d) percentual de pessoas que residem na cidade há mais de 10 anos.
#  A pesquisa termina quando for inserido o valor -1 para o nível de satisfação.

somaSat = 0
somaTempRes = 0
insatisf = 0
resMais10 = 0
cont = 0
while True:
    sat = int(input(f"Digite o nível de satisfação da {cont+1}ª pessoa (0 a 10, ou -1 para sair): "))
    if sat == -1:
        break
    if sat < 0 or sat > 10:
        print("Nível de satisfação inválido. Digite um valor entre 0 e 10.")
        continue
    tempRes = int(input(f"Digite o tempo de residência (em anos) da {cont+1}ª pessoa: "))
    somaSat += sat
    somaTempRes += tempRes
    cont += 1
    if sat <= 5:
        insatisf += 1
    if tempRes > 10:
        resMais10 += 1
if cont > 0:
    mediaSat = somaSat / cont
    mediaTempRes = somaTempRes / cont
    percInsatisf = (insatisf / cont) * 100
    percResMais10 = (resMais10 / cont) * 100
    print("\nResultados da pesquisa:")
    print(f"a) Média do nível de satisfação: {mediaSat:.2f}")
    print(f"b) Tempo de residência médio: {mediaTempRes:.2f} anos")
    print(f"c) Percentual de pessoas insatisfeitas: {percInsatisf:.2f}%")
    print(f"d) Percentual de pessoas que residem há mais de 10 anos: {percResMais10:.2f}%")
else:
    print("Nenhuma pessoa foi cadastrada.")