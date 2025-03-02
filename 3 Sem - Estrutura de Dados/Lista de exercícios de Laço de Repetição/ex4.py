#4.  Pesquisa sobre Profissão e Renda: 
#   A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, 
#   coletando dados sobre a profissão e renda mensal. A prefeitura deseja saber:
#   a) média da renda mensal da população;
#   b) profissão com maior média de renda;
#   c) percentual de pessoas desempregadas;
#   d) percentual de pessoas com renda acima de R$ 5000,00.
#   A pesquisa termina quando for inserido o valor "x" para a renda.

prof = {}
renda = []
cont = 0; desempregado = 0; rico = 0
while True:
    profissao = input("Digite sua profissão, ou X para sair: ").title()
    if profissao == "X":
        break
    if prof == "desempregado":
        desempregado += 1
    rendaPessoa = float(input(f"Digite a renda mensal da {cont+1}ª pessoa (ex: 1200.00): "))
    renda.append(rendaPessoa)
    if rendaPessoa > 5000:
        rico +=1
    cont += 1
    if profissao in prof:
        prof[profissao]["Salario"] += rendaPessoa
        prof[profissao]["Quantidade"] += 1
    else:
        prof[profissao] = {"Salario": rendaPessoa, "Quantidade": 1}

for qualProf, qtd in prof.items():
    print(f"{qualProf} - {qtd['Quantidade']} Cadastro(s) - R$ {qtd['Salario']:.2f}")

profissaoRico = None
maiorMedia = 0
for qualProf, qtd in prof.items():
    media = qtd["Salario"] /qtd["Quantidade"]
    if media > maiorMedia:
        maiorMedia = media
        profissaoRico = qualProf

print("------------------")
print(f"Média mensal da população: R${sum(renda)/cont:.2f}")
print(f"Profissão com maior média de renda: {profissaoRico} R${maiorMedia:.2f}")
print(f"Percentual de pessoas desempregadas: {(desempregado/cont)*100:.2f}%")
print(f"Percentual de pessoas com renda acima de R$ 5000,00: {(rico/cont)*100:.2f}%")