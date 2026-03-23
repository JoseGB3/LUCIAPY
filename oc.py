while True:
    salario=float(input("Digite o salario do funcionario:R$ "))
    plano=int(input("Digite o plano de trabalho do funcionário: "))
    if(plano==1):
        salario=salario*1.1
    else:
        if(plano==2):
            salario=salario*1.15
        else:
            if(plano==3):
                salario=salario*1.2
    print(f"O novo salário é{salario:.2f}")
    
    resposta=input("Deseja continuar s/n")
    if resposta=="n":
        break

