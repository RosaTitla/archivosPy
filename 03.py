try:
    myfile=open('abc.txt')
except:
    print('No se puede abrir el archivo')
    quit()  # no quiero que continues
else:
    linea=myfile.read(50) #lee los primeros 50 caracteres
    print(linea)
    myfile.close()