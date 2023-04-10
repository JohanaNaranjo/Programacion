"""Hacer un programa que le pida al usuario que ingrese su edad y su sexo,
# si el usuario es mayor de edad y ademas es menor de 65 años le debe permitir
# al usuario quedarse en el programa, en caso
# contrario el programa debe deternese. Si es sexo es masculino que el programa
# salude al usuario como un caballero y si el sexo es femino que el programa salude al
# usuario como una dama
# -Para que el usuario ingrese su sexo hacer un menu con condiciones."""

edad =int(input("Ingrese su edad: "))
femenino = True



if edad >=18 and edad <=65:
    #comillas triples para poder hacer el menú
    sexo = int(input("""
Ingrese su sexo:
[1] Para Masculino
[2] Para Femenino
[3] Otro
>>>>>>> """))
    if sexo == 1:
        femenino = False
        print(f"Bienvenido caballero de {edad} años")
    elif sexo == 2:
        femenino = True
        print(f"Bienvenida dama de {edad} años")
    elif sexo==3:
        genero = str(input("Ingrese su genero: "))
        print(f"Welcome {edad} years old {genero}")
    else:
        print("Está opción no es válida.")
        exit()
        
else:
    print("Para usar el programa debe ser mayor a 18 y menor a 65 años.")
    exit()