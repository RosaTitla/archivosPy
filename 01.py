myfile=open('abc.txt',"r")
contadorLineas=0
for linea in myfile:
    contadorLineas += 1
    print(linea.rstrip())
print('Total de lineas', contadorLineas)
