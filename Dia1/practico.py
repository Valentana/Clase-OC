anioactual=2026
while True:
    try:
        nacimiento= int(input("Ingrsa tu año de nacimiento "))
        edad= anioactual-nacimiento
        if edad>=18:
            print("Eres mayor de edad ")
        else:
            print("Eres menor de edad")
        break
    except ValueError:
        print("Ingrese un numero valido")
