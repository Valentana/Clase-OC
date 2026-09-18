while True:
    try:
        peso= float(input("Ingresa el peso en kilos "))
        altura= float(input("Ingresa tu altura en metros "))
        imc= peso/(altura*altura)
        print(f"Tu imc es de {imc}")
        break
    except ValueError:
        print("Ingrese un numero valido")
