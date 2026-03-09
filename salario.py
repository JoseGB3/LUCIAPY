salario=float(input("Digite o salário do funcionário:R$ "))
if(salario<500):
    print("O Novo salario é: ",salario*1.15)
if(500<=salario<=1000):
    print("O novo salário é:",salario*1.1)
if(salario>1000):
    print("O novo salario é: ",salario*1.05)
