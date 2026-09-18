numerosecreto=4
while True:
    try:
        numero=int(input("Intenta adivinar el numero "))

        if numero==numerosecreto:
            print("Adivinaste")
        else:
            print("Fallaste")
            break
    except ValueError:
        print("Ingrese un numero valido")