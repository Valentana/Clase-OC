def es_par(numero):
    if numero%2==0:
        return True
    else:
        return False
while True:
    try:
        num=int(input("¿Cual es el numero? "))
        print(es_par(num))
        break
    except ValueError:
        print("Ingrese un numero valido")