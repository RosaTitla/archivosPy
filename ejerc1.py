myfiles=open('abc.txt')
for linea in myfiles:
    lista = linea.split(' ')
print('lista')
print(lista)

myfile=open('consultas.txt')
for linea in myfile:
    print(linea)
    linea=linea.rstrip()
    if linea.startswith('select'):
        print(linea)
    if not '@utpuebla' in linea:
        continue
    print(linea)

acum=0
myfile=open('consultas.txt')
for linea in myfile:
    linea=linea.rstrip()
    acum=acum+len(linea)
print('total de caracteres archivo', acum)

#Usando el archivo school_prompt2.txt, busque el número de caracteres en el archivo y asigne ese valor a la variable num_char

num_char=0
myfile2=open('abc.txt')
for linea in myfile2:
    num_char=num_char+len(linea)
print('total de caracteres', num_char)

num_lines=0
myfile2=open('abc.txt')
for linea in myfile2:
    num_lines+=1
print('total de caracteres', num_lines)

#The ../ means to go up one level in the directory structure

myfile2=open('../abc.txt')
first_forty=myfile2.read(40)
print(first_forty)
print(len(first_forty))

#Typically, you will specify a
# relative file path, which says where
# to find the file to open, relative to the directory
# where the code is running from. For example,
# the file myPythonProgram.py
# could contain the code open('../myData/data2.txt', 'r').
# The ../ means to go up one level
# in the directory structure,

myfile2=open('../../xyz.txt')
first_forty=myfile2.read(40)
print(first_forty)
print(len(first_forty))

myfile2=open('textos/abcd.txt')
first_forty=myfile2.read(40)
print(first_forty)
print(len(first_forty))