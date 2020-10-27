try:
    myfile=open('abc.txt', 'r')
except:
    print('No se puede abrir el archivo')
    quit()  # no quiero que continues
else:
    for linea in myfile:
        linea1=linea.rstrip() #rigth \n\n
        lista=linea1.split(' ')
        print(lista)
    myfile.close()
i=input('nombre')
