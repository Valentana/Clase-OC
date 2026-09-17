productos={
    "manzana":"1000",
    "pera":"500"
}
pedido=input("Que queres pedir ")
cantidad=float(input("Cuantos kilos "))

precio=productos.get(pedido)
preciof=float(precio)*cantidad
print(f"El precio es de {preciof}")
