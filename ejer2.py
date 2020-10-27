#nombre  consultas.txt
nombre=input('nombre del archivo')
try:
    miArchivoVar=open(nombre)
except:
    print('No se puede abrir el archivo')
    quit()   #no quiero que continues
else:
    contador=0
    for l in miArchivoVar:
        contador+=1
    print('totla de lineas', contador)
    miArchivoVar.close()