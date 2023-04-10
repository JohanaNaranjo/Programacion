#Encapsulamiento


class Curso:

    #Vamos a crear un atributo privato se reliza haciendo dos guión al piso al principio de la declaración de la variable __

    __titulo = "Backend Python 3"
    __duracion = 20

    def __adquirir_curso(self):
        print("Has adquirido este curso")
    
    #Para poder acceder a los metods privados desde fuera hacemos lo siguiente
    def get_adquirir_curso(self):
        return self.__adquirir_curso()
    
    def get_titulo(self):
        return self.__titulo
    
    #Para modificar el titulo privado desde afuera, creo un set

    def set_titulo(self, titulo):
        self.__titulo = titulo

curso = Curso()
curso.get_adquirir_curso()
print(curso.get_titulo())
#Aqui puedo modificar el titulo de una clase privado realizando el set en la clase con SET
curso.set_titulo("Backend Python PRO")
print(curso.get_titulo())


