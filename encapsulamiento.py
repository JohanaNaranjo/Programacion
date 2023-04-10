#Forma más moderna que tiene Python de trabajar con encapsulamiento
class Person:

    def __init__(self, name: str, age: int, mail: str) -> None:
        self.__name = name
        self.__age= age
        self.__mail = mail

    @property
    def name(self) -> str:
        return self.__name
    
#Hacer un set para poder utiizar el metodo por fuera de la clase
    @name.setter
    def name(self, name:str)-> None:
        self.__name = name
#Hacer un delet un borrado del metodo. los @ son decoradores que tiene python para saber que es lo que se esta haciendo por dentro 
    @name.deleter
    def name(self) -> None:
        del self.__name

def main()-> None:
    person = Person(name="Johana", age=22, mail="johis99@hotmail.es")
    print(person.name)
    person.name = "Johis"
    print(person.name)
    #del person.name
    #print(person.name)

if __name__ == "__main__":
    main()



