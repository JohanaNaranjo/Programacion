#POO Programación Orientada a Objetos.
#Se tiene clases, atributos y objetos y acciones

class Auto:
    #Se crea un constructor para los objetos
    def __init__(self, marca, color, cantidad_ruedas, velocidad_maxima):
        self.marca = marca
        self.color = color
        self.cantidad_ruedas = cantidad_ruedas
        self.velocidad_maxima = velocidad_maxima
        self.motor = 2.0
        self.motores = [2.0,3.9,4.5,9.0]
        self.marcas_establecidas =  {"Alta gama" : "Ferrari", "Baja gama" : "Renault"}

    def __str__(self):
        return f"Auto: {self.marca}, {self.color}, {self.cantidad_ruedas}, {self.velocidad_maxima}, {self.motor}"

    #Metdodos
    def acelerar(self):
        print(f"El auto ha acelerado hasta {self.velocidad_maxima} km")

    def frenar(self):
        print("El auto ha frenado")

#objeto instansia de la clase
tipo_carro = Auto("Lamborghini", "Blanco", 4, 320)
Huracan = Auto("Audi", "Azul", 4, 350)
print(tipo_carro)
print(tipo_carro.color)
print(Huracan)
print(Huracan.color)

tipo_carro.acelerar()
tipo_carro.frenar()
Huracan.acelerar()

#Si le quiero cambiar los atributos
tipo_carro.color = "Amarillo"
print(tipo_carro)


print(tipo_carro.motores[-1]) 
print(Huracan.marcas_establecidas["Alta gama"])