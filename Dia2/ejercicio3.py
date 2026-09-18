while True:
    try:
        numero=int(input("Inserta un numero "))
        for multiplicacion in range(1,11):
            resultado=multiplicacion*numero
            print(f"{numero}*{multiplicacion} = {resultado}")
    except ValueError:
        print("Por favor, inserta un numero valido.")