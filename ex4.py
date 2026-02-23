salario=float(input("Digite o salário do funcionário: "))
reajuste=int(input("Digite o reajuste do funcionário: "))
perceltualreajuste=(reajuste/100)+1
salariofinal=salario*perceltualreajuste

print("Salário a pós reajuste: ",salariofinal)
