while True:
    try:
        n1= float(input("Ingresa el primer valor "))
        n2=float(input("Ingresa el segundo valor "))

        if n2==0:
            print("no es posible divir por cero")
        else:
            resultado= n1/n2
            print(f"El resultado de la division es de {resultado}")
        break
    except ValueError:
        print("Ingrese un numero valido")