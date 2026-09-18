while True:
    try:    
        n1 = float(input("Ingresa el primer valor "))
        n2 = float(input("Ingresa el segundo valor "))

        if n1>n2:
            print(f"{n1} es el mas grande ")
        elif n2>n1:
            print(f"{n2} es el mas grande ")
        else:
            print("Los dos numeros son iguales")
        break
    except ValueError:
        print("Ingrese un numero valido")