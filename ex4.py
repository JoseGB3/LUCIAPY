salario=float(input("Digite o salário do funcionário: "))
reajuste=int(input("Digite o reajuste do funcionário: "))
reajc=(reajuste/100)+1
salariofinal=salario*reajc

print("Salário pós reajuste: ",salariofinal)
