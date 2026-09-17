def puede_votar(edad):
     
    if edad>=16:
         return "Puede votar"
    else:
         return "Aun no puede votar"
while True:
     try:
          años=int(input("Ingrese su edad "))
          print(puede_votar(años))
          break
     except ValueError:
          print("Ingresa un valor numerico ")

        