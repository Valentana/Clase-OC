productos={
    "manzana":"1000",
    "pera":"500"
}
while True:
    try:
        pedido=input("Que queres pedir ")
        cantidad=float(input("Cuantos kilos "))

        precio=productos.get(pedido)
        preciof=float(precio)*cantidad
        print(f"El precio es de {preciof}")
        break
    except ValueError:
        print("Ingrese una cantidad valida")
    except TypeError:
        print("Ingrese un pedido valido")