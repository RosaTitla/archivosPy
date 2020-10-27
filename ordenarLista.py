#fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
for line in fh:
    linea=line.rstrip()
    palabras=linea.split(' ')
    #print(palabras)
    for palabra in palabras:
        if palabra not in lst:
            #print(palabra)
            lst.append(palabra)
lst.sort()
print(lst)


