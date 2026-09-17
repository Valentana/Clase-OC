def area_circulo(radio):
    area=3.1416*(radio*radio)
    return area
while True:
    try:
        ingreso=float(input("¿Cual es el radio del circulo? "))
        print(area_circulo(ingreso))
        break
    except ValueError:
        print("Ingresa un valor numerico")