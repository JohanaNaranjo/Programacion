tabla =int(input("Ingrese la tabla a calcular: "))
limite = int(input(f"Ingrese el limite de la tabla del {tabla}, que desea calcular: "))
"""for estructura for i in range (especificar el rango)
i es el indice, in range que es en un rango de numero
si se pone la coma es decir que va a ir aumentando de 2 en dos de 3 en 3 depende el limite   
for i in range (limite,2): """

"""for i in range (limite):
    print(f"{tabla} x {i+1} = {tabla * (i+1)}")
"""
"""El while es parecido al for solo que se dice hasta cuando se va a ejecutar, se ejecuta mientras la condición sea valida
"""
num=1
while limite >= num:
    print(f"{tabla} x {num} = {tabla * num}")
    num=num+1