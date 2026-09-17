notas=[8,7,9,10,6]
notat=0
notaf=0
for suma in range (5):
    notaf=notas[suma]
    notat=notaf+notat
    suma=suma+1
    
promedio=notat/5

print(promedio)