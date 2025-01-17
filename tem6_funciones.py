import os
from time import sleep

def funcion1():
    """
    Esta funcion devuelve un saludo
    """
    print("Hola mundo la funcion 1")

def funcion2(x:int):
    """
    Esta funcion devuelve un saludo
    """
    print(f"Hola mundo {x}")

def limpiar():
    """
    Esta funcion devuelve un saludo
    """
    sleep(2)
    os.system("cls")

def menu():
    textoMenu = """
    Menu de opciones
    1- Sumar dos numeros
    2- Otras opcion
    3.- Salir
    """
    opcion = int(input("Ingresa una opción"))
    limpiar()


if __name__ == "__main__":
    menu()