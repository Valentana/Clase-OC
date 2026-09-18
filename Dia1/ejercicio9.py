while True:
    try:
        precio=float(input("Ingrese el valor del producto "))
        descuento=int(input("Ingrese el valor de descuento "))
        precio_descontado=descuento*100/precio
        preciofinal=precio-precio_descontado
        print(f"Se descontaron {precio_descontado} y el precio final es de {preciofinal}")
        break
    except ValueError: 
        print("Ingrese un numero valido")   