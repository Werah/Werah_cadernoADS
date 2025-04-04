

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
alunos = ["Quico", "Zinho", "Lindo", "Branco"]

presenca = []
for i in range(5):
    listaPresenca = []
    for j in range(4):
        while True:
            try:
                diaPresenca = int(input(f"1 - Presença || 2 - Ausencia\n{dias[i]}, {alunos[j]}: "))
                print(dias[i], alunos[j])
                if diaPresenca == 1:
                    listaPresenca.append("Presente")
                    break
                elif diaPresenca == 2:
                    listaPresenca.append("Ausente")
                    break
                else:
                    print("Apenas 1 ou 2")
            except ValueError:
                print("Apenas 1 ou 2")
    presenca.append(listaPresenca)

print("        ",alunos)
cont = 0
for listaPresenca in presenca:
    print(dias[cont],listaPresenca)
    cont+=1