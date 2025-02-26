sal = float(input("Digite o salário: "))
tmp = int(input("Digite o tempo de serviço (em anos inteiros): "))
idd = int(input("Digite informe a idade: "))
if sal < 4000 and tmp > 3 and idd > 30:
    print ("Receberá reajuste")
else:
    print ("Não receberá reajuste")
