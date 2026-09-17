lista=[]
def mayor_de_tres(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n3:
        return n2
    else:
        return n3
   
    for i in range(3):
        nums=float(input("¿Cuales son los numeros?" ))
        lista.append(nums)
    print(mayor_de_tres(lista[0],lista[1],lista[2]))