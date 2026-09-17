def crear_email(nombre, apellido):
    email=f"{nombre}.{apellido}@empresa.com"
    return email
nom=(input("Ingrese su nombre "))
ape=(input("Ingrese su apellido "))
print(crear_email(nom,ape))