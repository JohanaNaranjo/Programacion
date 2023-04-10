#Polimorfismo y encapsulamiento
# Actua de diferentes formas en las clases
# Acción que realiza un mismo metodo pero de diferente manera

class Arma:

    def __init__(self, balas, pesos):
        self.balas = balas
        self.pesos = pesos

    def disparar(self):
        print("El arma dispara")


class Pistola(Arma):

    def disparar(self):
        #Metodo de su super clase en este caso Arma
        #return super().disparar()
    #Tambien se puede hacer otro tipo de cosa en el metodo
        print("El arma dispara lento")

class Ametralladora(Arma):

    def disparar(self):
        print("El arma dispara rápido")

arma = Arma(14, 7)
arma.disparar()

pistola = Pistola(12, 5)
pistola.disparar()

ametralladora = Ametralladora(15, 8)
ametralladora.disparar()
