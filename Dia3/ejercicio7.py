def minutos_a_horas(minutos):
    horas=minutos//60
    calc=minutos%60
    print(f"{horas} Horas y {calc} Minutos")
while True:
    try:
        min=int(input("Ingrese los minutos "))
        minutos_a_horas(min)
        break
    except ValueError:
        print("Ingresa un valor numerico")