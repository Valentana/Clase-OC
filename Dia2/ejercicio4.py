frase=input("escriba una frase ")
con=0
for i in frase:
    if i in "aAeEiIoOuU":
        con=con+1
        

print(f"Tu palabra tiene {con} vocales")