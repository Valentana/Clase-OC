while True:
    try:
        nota1= float(input("Ingresa la primer nota "))
        nota2= float(input("Ingresa la segunda nota "))
        nota3= float(input("Ingresa la tercer nota "))
        notafinal= (nota1+nota2+nota3)/3
        print(notafinal)
        break
    except ValueError:
        print("Ingrese un numero valido")