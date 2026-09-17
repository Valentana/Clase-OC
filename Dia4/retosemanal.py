saldo=1000
dinero=0
def verificar_contrasena(pin):
    if pin==1234 :
        return True
    else:
        return False
    
def retirar(monto):
    global saldo
    if dinero<= saldo:
        saldo=saldo-dinero
        print(f"Retiraste {dinero} y te quedan {saldo}")
    else:
        print("Saldo insuficiente")


while True:
    while True:
        try:
            contrasena=int(input("Ingresa la contraseña "))
            break
        except ValueError:
            print("Ingresa un valor numerico ")
    
    if verificar_contrasena(contrasena)==True:
        print("Bienvenido ")
        try:
            dinero=int(input("Ingrese el monto a retirar "))
            retirar(dinero)
            break

        except:
            print("Ingresa un valor numerico ")
    
    else:
        print("Intenta devuelta")


