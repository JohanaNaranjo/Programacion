#definir función
"""def saludar():
    print("Hola que tal :)")
"""
def saludar_per(persona):
    print(f"Hola que tal {persona}")

nombre=str(input("Ingrese su nombre: "))
#saludar()
saludar_per(nombre)

def adicion(num1,num2):
    print(f"{num1} + {num2} = {round((num1 + num2),2)}")

def sustraccion(num1,num2):
    print(f"{num1} - {num2} = {round((num1 - num2),2)}")

def multiplicacion(num1,num2):
    print(f"{num1} x {num2} = {round((num1 * num2),2)}")

def division(num1,num2):
    print(f"{num1} / {num2} = {round((num1 / num2),2)}")



def programa():
    menu = int(input(""" 
Ingrese la operación que desea calcular: 
[1] Adición
[2] Sustracción
[3] Multiplicación
[4] División
[5] Salir
>>>>> """))
    if menu>=1 and menu<=4:
        n=float(input("Ingrese el primer número: "))
        m=float(input("Ingrese el segundo número: "))
        if menu == 1:
            adicion(n,m)
        elif menu ==2:
            sustraccion(n,m)
        elif menu==3:
            multiplicacion(n,m)
        elif menu==4:
            division(n,m)
    elif menu==5:
        print("Saliendo del programa")
        exit()
    else:
        print("Está opción no es válida. ")
        
while True:
    programa()

