cambio= 1000
while True:
    try:
        dolares=int(input("cuantos dolares tenes "))
        total= cambio*dolares
        print(f"el valor de tus dolares a pesos es de {total}")
        break
    except ValueError:
        print("Ingrese un numero valido")