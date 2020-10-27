f = open("viajes.txt", "r")
listaDestinos=[]
for aline in f:
    if ':' in aline:
        print(aline)
        destination = aline.split(':')
        listaDestinos.append(destination)
print(listaDestinos)