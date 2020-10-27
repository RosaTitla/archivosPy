try:
    myfile=open('abc.txt')
except:
    print('No se puede abrir el archivo')
    quit()  # no quiero que continues
else:
    for linea in myfile:
        print(linea)
    myfile.close()

i=input('nombre')



