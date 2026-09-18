while True:
    try:
        celsius=float(input("Ingresa la temperatura en celsuis"))
        fahrenheit= (celsius * 9/5) + 32
        print(fahrenheit)
        break
    except ValueError:
        print("Ingrese un numero valido")