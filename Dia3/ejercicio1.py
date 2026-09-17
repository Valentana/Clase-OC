def celsius_a_fahrenheit(cel):
    fah=(cel*9/5)+32
    return fah
celcius=float(input("cuantos grados celsius hacen?"))
print(celsius_a_fahrenheit(celcius))