#Herencia

#Super calses y clases hijas

class Animal:

    def __init__(self, edad, numero_patas, alimentacion):
        self.edad = edad
        self.numero_patas = numero_patas
        self.alimentacion = alimentacion
    
    def caminar(self):
        print("El animal camina")

    def corre(self):
        print("El animal corre")

#Clase heredada la estructura es nombre(clase que se va a heredar)
class Perro(Animal):
    #Ya tiene los atributos que heredo de la clse Animal, como son la edad, numero de patas y alimentación. Aqui lo que se va a definir es los atributos de la clase perro.
    #Se puede colocar como variable no es necesario crear un constructor

    raza = None
    ladrido = None
    pelaje = None

    def ladrar(self):
        print("El perro ladra")

    def morder(self):
        print("El perro muerde")
    
    def __str__(self):
        return f"{self.edad}, {self.numero_patas}, {self.alimentacion}"

class Gato(Animal):
    #pass #Se utiliza para que le diga a python que salte la clase
    def saltar(self):
        print("El gato salta")
 
gato = Gato(2, 4, "Vegetariano")
print(gato)
gato.caminar()
gato.corre()
gato.saltar()


perro = Perro(5, 4, "Carnívoro")
print(perro)

perro.raza = "Labrador"
perro.ladrido = "Fuerte"
perro.pelaje = "Gris"

print(perro.raza)
print(perro.ladrido)
print(perro.pelaje)

perro.caminar()
perro.corre()
perro.ladrar()

