def cuadarado(numero):
    resultado=numero*numero
    return resultado
while True:
    try:
        num=float(input("¿Cual es el numero que quieres elevar al cuadrado? "))
        print(cuadarado(num))
        break
    except ValueError:
        print("Ingrese un numero valido")