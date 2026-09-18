sumatotal=0
valor=1
while True:
    try:
        while valor!=0:
                valor=int(input("Ingresa un valor "))
                if valor==0:
                    break
                sumatotal=valor+sumatotal
                valor=valor-1
                print(sumatotal)
    except ValueError:
        print("Ingrese un numero valido")