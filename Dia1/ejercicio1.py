while True:
    try:
        Cuenta = float(input("Cuanto es la cuenta?"))
        Propina= int(input("Cuanta propina queres dejar?"))
        Total= Cuenta + Propina
        print(f"{Total} este es el total a pagar")
        break
    except ValueError:
        print("Ingrese un numero valido")