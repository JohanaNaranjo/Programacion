#Sets y tuplas en python, las tuplas no se puede modificar, son tipos de datos raros que se utilizan en casos especiales.

tupla = (100, "hello", ["familia", "amigos"],{"hello" : "hello"})

print(tupla)
print(tupla[0])
print(tupla[-1])

print(len(tupla))

#Convertir tupla en lista para agregar contenido y volver a convertitr en tupla e imprimi
tupla=list(tupla)
tupla.append(200)
tupla[0]=300
tupla = tuple(tupla)
print(tupla)

#Creamos un set, es un set de datos donde no puede hber datos repetidos

nuestro_set = {20, 23, 45, 24, 24, 24, 24, 89, 9, 90, 70, 0, 0}
print(nuestro_set)
ordenado=sorted(nuestro_set)
print(ordenado)
