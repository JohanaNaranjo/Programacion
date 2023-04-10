nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
persona_maculina= True
persona_femenina = False

#Comparación
if nombre == "Johana":
    print("Es cierto la variable nombre es Johana")
elif nombre == "Mario":
    print("Tú nombre es Mario")
else:
    print("Tú nombre no está en la base de datos.")

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

if persona_maculina == True or persona_femenina==False:
    print("Una de las dos condiciones se cumple")
else:
    print("No se cumple las condiciones")
