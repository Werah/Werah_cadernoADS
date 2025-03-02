#2.  Pesquisa sobre Cor da Pele e Grau de Escolaridade: 
#   A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, 
#   coletando dados sobre a cor da pele e grau de escolaridade. A prefeitura deseja saber:
#   a) distribuição da população por cor da pele;
#   b) percentual de pessoas com ensino superior completo;
#   c) percentual de pessoas com ensino médio incompleto.
#   A pesquisa termina quando for inserido o valor -1 para cor da pele.

pele = {
    0: "Branco",
    1: "Pardo",
    2: "Negro",
    3: "Asiático",
    4: "Indigena"
}
peleCont = [0] * len(pele)

escola = {
    0: "Ensino Médio Incompleto",
    1: "Ensino Médio Completo",
    2: "Ensino Superior Incompleto",
    3: "Ensino Superior Completo",
}
escolaCont = [0] * len(escola)

cont = 0

while True:
    print("\nCor de pele:")
    for peleId, peleCor in pele.items():
        print(f"{peleId} - {peleCor}")
    peleCodigo = int(input(f"Digite a cor de pele da {cont+1}ª pessoa, ou -1 para sair: "))
    if peleCodigo == -1:
        break
    if peleCodigo in pele:
        peleCont[peleCodigo]+=1

        print("\nEscolaridade:")
        for escolaId, escolaTipo in escola.items():
            print(f"{escolaId} - {escolaTipo}")
        escolaCodigo = int(input(f"Digite a escolaridade da {cont+1}ª pessoa."))
        if escolaCodigo in escola:
            escolaCont[escolaCodigo]+=1    
        else:
            print("\nValor inválido, digite novamente.")

        cont+=1

    else:
        print("\nValor inválido, digite novamente.")


print("\nDistribuição da população por cor da pele:")
for peleCodigo, peleCor in pele.items():
    print(f"{peleCor}: {peleCont[peleCodigo]} pessoa(s)")

print("--------------------------")
print("Distribuição de pessoas por escolaridade:")
for escolaCodigo, escolaTipo in escola.items():
    print(f"{escolaTipo}: {peleCont[escolaCodigo]} pessoa(s)")

print("--------------------------")
if cont > 0:
    print(f"Porcentagem de pessoas com ensino medio incompleto: {(escolaCont[0]/cont)*100}%")
    print(f"Porcentagem de pessoas com ensino superior completo: {(escolaCont[3]/cont)*100}%")
