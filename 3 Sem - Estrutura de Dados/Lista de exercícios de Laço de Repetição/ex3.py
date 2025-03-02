#3.  Pesquisa sobre Sexo e Estado Civil: 
#   A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, 
#   coletando dados sobre o sexo e estado civil. A prefeitura deseja saber:
#   a) distribuição da população por sexo;
#   b) percentual de pessoas solteiras;
#   c) quantidade de pessoas casadas;
#   d) percentual de pessoas divorciadas.
#   A pesquisa termina quando for inserido o valor "X" para o sexo.

sexo = {
    "M": "Masculino",
    "F": "Feminino"
}

estCivil = {
    "S": "Solteiro",
    "C": "Casado",
    "D": "Divorciado"
}

sexoCont = {"M": 0, "F": 0}
estCivilCont = {"S": 0, "C": 0, "D": 0}
cont = 0

while True:
    print("\nSexo:")
    for sexoId, sexoQual in sexo.items():
        print(f"{sexoId} - {sexoQual}")
    sexoCod = input(f"Digite o sexo da {cont+1}ª pessoa, ou X para sair: ").upper()
    if sexoCod == "X":
        break
    if sexoCod in sexo:
        sexoCont[sexoCod] += 1 
        print("\nEstado Civil:")
        for estCivilId, estCivilQual in estCivil.items():
            print(f"{estCivilId} - {estCivilQual}")
        estCivilCod = input(f"Digite o estado civil da {cont+1}ª pessoa: ").upper()
        
        if estCivilCod in estCivil:
            estCivilCont[estCivilCod] += 1
            cont+=1
        else:
            print("\nValor inválido, digite novamente.")
    else:
        print("\nValor inválido, digite novamente.")

print("\nDistribuição da população por sexo:")
for sexoId, sexoQual in sexo.items():
    print(f"{sexoQual}: {sexoCont[sexoId]} pessoa(s)")

print("--------------------------")

print("Distribuição de pessoas por estado civil:")
for estCivilId, estCivilQual in estCivil.items():
    print(f"{estCivilQual}: {estCivilCont[estCivilId]} pessoa(s)")

print("--------------------------")
if cont > 0:
    percentual_solteiras = (estCivilCont["S"] / cont) * 100
    print(f"Percentual de pessoas solteiras: {percentual_solteiras:.2f}%")
    print(f"Quantidade de pessoas casadas: {estCivilCont['C']}")
    percentual_divorciadas = (estCivilCont["D"] / cont) * 100
    print(f"Percentual de pessoas divorciadas: {percentual_divorciadas:.2f}%")
else:
    print("Nenhuma pessoa foi cadastrada.")