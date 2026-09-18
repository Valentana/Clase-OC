import random
numero=random.randint(1,100)
respuesta=0
while True:
    try:
        while respuesta !=numero:
            respuesta=int (input("Ingresa un numero "))
            if respuesta>numero:
                print("El numero es mas chico ")
            else:
                print("El numero es mas grande")
        print("Adivinaste")
        break
    except ValueError:
        print("Ingrese un numero valido")
