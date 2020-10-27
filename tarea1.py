#El siguiente archivo de muestra llamado studentdata.txt contiene una línea para cada estudiante en una clase imaginaria. El nombre de los estudiantes es lo primero en cada línea, seguido de algunos puntajes de exámenes. La cantidad de puntajes puede ser diferente para cada estudiante.
#Using the text file estudiantes.txt write a program that prints out the names of students that have more than six quiz scores.
#Usando el archivo de texto studentdata.txt, escriba un programa que imprima los nombres de los estudiantes que tienen más de seis puntajes en las pruebas.

f = open("estudiante.txt", "r")

for aline in f:
    items = aline.split()
    print(items)
    if len(items[1:]) > 6:
        print(items[0])

f.close()