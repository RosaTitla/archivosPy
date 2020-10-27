permisosLetra = ['---','--x','-w-','-wr','r--','r-x','rw-','rwx']
permisoL=''
permisoCad = input("permiso")
for letra in permisoCad:
    permisoL+=permisosLetra[int(letra)]
print('Permsio en número: {} permiso en letras: {}'.format(permisoCad,permisoL))

