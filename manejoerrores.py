

# Para cuando se tiene un error de que el usuario ingrese un numero o palabras que no estan dentro del menu y asi conseguir que el menu contiue y no se estropee el programa o menu

def programa():
    try:
       menu = int(input(""" 
Ingrese la operación que desea calcular: \n
[1] Adición
[2] Sustracción
[3] Multiplicación
[4] División
[5] Salir\n
>>>>>  """))
       print(f"Ha ingresado la opción {menu}")
       if menu>=6 or menu<=0:
           print("Está opción no es válida, ingrese un valor entre 1 y 5")
       if menu == 5:
           exit()
    except ValueError as error:
        print(f"\nNo puede ingresar este dato, error: {error}")

#Permite que el menu se vuelva a repetir hasta que de la opción de salir 5
while True:
   programa()