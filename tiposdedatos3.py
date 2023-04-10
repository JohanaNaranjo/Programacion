#Diccionarios

palabras_ingles={"Hello" : "Hola", "Day" : "Día", "Veinte" : 20}
print(palabras_ingles)
print(palabras_ingles["Day"])

#Si quiero cambiar el valor y volver a imprimirlo puedo hacer lo siguiente       

palabras_ingles["Hello"] = "Salut"
print(palabras_ingles)
print(palabras_ingles["Hello"])

palabras_ingles["Night"] = "Noche"
print(palabras_ingles)

#Función para borrar
del(palabras_ingles["Night"])
print(palabras_ingles)


print(palabras_ingles["Veinte"] + 1)

#Para imprimir solo la palabra
for palabra in palabras_ingles:
    print(palabra)

#Imprimir el significado
for clave in palabras_ingles:
    print(palabras_ingles[clave])

#Imprimir palabra y significado
for clave1 in palabras_ingles:
    print(f"{clave1} : {palabras_ingles[clave1]}")

#Imprimir palabra y significado otro tipo de for
for  key, valor in palabras_ingles.items():
    print(key,valor)

#si se requiere hacer una lista de productos.

producto={
    "id" : 2,
    "Nombre" : "Nevera",
    "Precio" : 2000000,
    "stock" : 20
}

print(producto)