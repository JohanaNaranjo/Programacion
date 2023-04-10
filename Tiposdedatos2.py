"""Pueden ser listas de carateres o números o se pueden tener listas dentro de ptra lista como en la variable apellidos"""
nombres =["Gaston","Antonio","David","Johana"]
edades=[20,21,23,24,19,8,6,80]
numeros =[3,5,7,0,13,15]
apellidos = [
    ["Fernandes","Benitez"],
    ["Benavides, Naranjo"],
    ["Ariza","Pinzón"],20, True
]
"""
print(nombres)

nombres.append("Ramón")
print(nombres)
#Para eliminar un elemento de la lista, la lista va enumerda en posiciones desde el 0 hasta infinito
nombres.pop(1)
print(nombres)

cant_elementos = len(nombres)

print(cant_elementos)
#Acceder al elemento de una lista (-1 es el último elemento)
print(nombres[-1])
print(nombres[-2])
print(nombres[0:3])"""

"""
print(apellidos)
print(apellidos[0])
print(apellidos[0][1])"""

#Imprimir el numero maxmo de la lista edades
print(f"""El número mayor es:
{max(edades)}""")

#Imprimir el numero minimo de la lista edades
print(f"""El número menor es:
{min(edades)}""")

#Imprimir la lista ordenada de menor a mayor
print(f"""La lista en orden es:
{sorted(edades)}""")

#Remover un elemento en especifico de la lista
edades.remove(19)
print(edades)

#Dar la vuelta a a lista del ultimo al primero
"""edades.reverse()
print(edades)"""

#extend estender una lista entre otra
edades.extend(numeros)
print(edades)



for nombre in nombres:
    print(nombre)

pares=[]
for i in range(100):
    if i % 2 ==0:
        pares.append(i)
print(pares)

pares=[i for i in range(100) if i % 2>0]
print(pares)
