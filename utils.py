import os
import random
from llist import llist


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def imprimir_histograma(lista, movimientos=0):
    limpiar_pantalla()

    print("_  _   _ PARA VER ORDENAMIENTOS _  _  _")
    print("---------------------------------------")
    print(f"Movimientos: {movimientos}")
    print()

    for i in range(len(lista)):
        valor = lista[i]
        print(f"{valor:2} | " + "#" * valor)

    print()
    print(lista)


def crear_lista_aleatoria(tamano):
    lista = llist()

    for _ in range(tamano):
        lista.append(random.randint(1, 20))

    return lista


def pedir_tamano():
    minimo = 5
    maximo = 20

    while True:
        try:
            tamano = int(input(f"Ingresa el tamaño de la lista ({minimo}-{maximo}): "))

            if minimo <= tamano <= maximo:
                return tamano

            print("El tamaño está fuera del rango.")

        except ValueError:
            print("Debes poner un número entero.")


def pedir_velocidad():
    print()
    print("Velocidad de ordenamiento:")
    print("1. Lenta")
    print("2. Media")
    print("3. Rápida")

    while True:
        opcion = input("Opción: ")

        if opcion == "1":
            return 0.7

        if opcion == "2":
            return 0.3

        if opcion == "3":
            return 0.08

        print("Opción inválida.")


def pausar():
    input("Presiona ENTER para continuar...")


def menu_principal():
    print("ORDENAMIENTOS CON LISTAS LIGADAS")
    print("--------------------------------")
    print("1. Bubble sort")
    print("2. Selection sort")
    print("3. Insertion sort")
    print("4. Merge sort")
    print("5. Quick sort")
    print("6. Salir")
