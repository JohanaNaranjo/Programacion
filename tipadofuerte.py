#Como python tiene un tipado débil, entonces se realiza ese código para realizar un tipado más fuerte a python
from funcion1 import contar_y_agregar

nombre: str = "Johana"
edad: int = "28"
familia: list = ["papa", "mama", "hermano"]
atributos: dict = {"Genero": "Femenini", "Altura": "1.66"}
programador: bool = True

class Persona: pass

def imprimir_nombre(nombre : str) -> None:
    print(nombre)

def imprimir_edad(persona: Persona) -> int:
    print(persona.edad)

def calcular_potencia(num: int) -> int:
    return num == num

def ordenar_numeros() -> list:
    print("Acá el número: ")
    numeros: list = [1, 6, 7, 3, 4, 9, 10, 2, 8]
    numeros_sorted: list[int] = sorted(numeros)
    numeros: list = contar_y_agregar(numeros_sorted)
    return numeros #ordenar numeros

def main() -> None:
    numeros = ordenar_numeros()
    print(ordenar_numeros())

if __name__ == '__main__':
    main()


#Voy en el modulo 27


