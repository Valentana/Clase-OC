def calcular_precio_final(precio, descuento):
    preciof=precio-(precio*descuento/100)
    return preciof
while True:
    try:
        precioO=float(input("ingrese el precio "))
        desc=int(input("ingrese el descuento "))
        print(calcular_precio_final(precioO,desc))
        break
    except ValueError:
        print("Ingresa un valor numerico")