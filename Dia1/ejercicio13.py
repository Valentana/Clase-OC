while True:
    try:
        nota= float(input("Ingresa la nota "))
        if nota>=6:
            print("Aprobado")
        else:
            print("Reprobado")
        break
    except ValueError:
        print("Ingrese un numero valido")