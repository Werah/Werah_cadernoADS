sal = int(1000)
au = 0.15
ano = 1997

sal = sal+(sal * au)
print(f"1996: O aumento está em {au}, o salário é de R${sal},00")
for x in range(1997, 2024+1):
    au = au * 2
    sal = sal+(sal * au)
    print(f"{ano}: O aumento está em {au}, o salário é de R${sal},00")
    ano += 1
