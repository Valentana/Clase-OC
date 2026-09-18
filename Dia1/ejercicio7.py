while True:
    try:
        horast=float(input("Ingresa las horas trabajadas en el mes "))
        tarifa= float (input("Ingresa la tarifa por hora "))
        salario= horast*tarifa
        print(f" El salario es de {salario}")
        break
    except ValueError:
        print("Ingrese un numero valido")