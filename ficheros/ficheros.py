#Un fichero es un archivo de texto

#nombre ="Johana"
"""
nombre = str(input("Ingrese su nombre: "))
print(nombre)


Para guardar el valor del nombre se realiza una base de datos o un fichero de texto que se guarda en el archivo ficheros.txt
"""

def leer_fichero():

    file = open('file.txt', 'r') #Abrir fichero o codigo de texto en modo lectura

    dato = file.read()

    file.close()

    print(dato)

#leer_fichero()

def escribir_fichero():

    file = open('file.txt', 'w') # Para escribir el fichero sobre lo que hay encima en el documento de texto 

    dato = "\n Ingrese su nombre: \n"

    file.write(dato)

    file.close()

#leer_fichero()

file = open('file.txt', 'a') # El modo a es para agregar en el fichero la información
dato = "\n Escriba su edad: "
file.write(dato)
file.close()
leer_fichero()

