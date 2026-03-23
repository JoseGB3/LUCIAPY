x=int(input("Digite um valor x: "))
y=int(input("Digite um valor y: "))
escolha=int(input("Digite sua escolha (1-4): "))
match(escolha):
    case 1:
        print((x+y)/2)
    case 2:
        if(x<y):
            x,y=y,x
        print(x-y)
    case 3:
        print(x*y)
    case 4:
        print(x/y)
    case _:
        print("numero invalido")
