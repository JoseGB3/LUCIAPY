
#// div sem resto(quantas notas de (X) vao dar de troco?
#% da o resto depois de dar (X) notas, quanto sobra? para proximo calculo?
valor_compra=float(input("Digite o valor da compra: "))
valor_pago=float(input("Digite o valor pago pelo cliente: "))
troco=valor_pago-valor_compra
#agora vamos colocar quantas unidades de cada cédula vai dar de troco.
notas100=troco//100
troco=troco%100

notas50=troco//50
troco=troco%50

notas20=troco//20
troco=troco%20

notas10=troco//10
troco=troco%10

notas5=troco//5
troco=troco%5

notas2=troco//2
troco=troco%2

notas1=troco//1

print("Quantas notas de 100 você vai dar de troco: ",notas100)
print("Quantas notas de 50 você vai dar de troco: ",notas50)
print("Quantas notas de 20 você vai dar de troco: ",notas20)
print("Quantas notas de 10 você vai dar de troco: ",notas10)
print("Quantas notas de 5 você vai dar de troco: ",notas5)
print("Quantas notas de 2 você vai dar de troco: ",notas2)
print("Quantas moedas de 1 você vai dar de troco: ",notas1)


