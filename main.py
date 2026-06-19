import time

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

from utils import (
    limpiar_pantalla,
    imprimir_histograma,
    crear_lista_aleatoria,
    pedir_tamano,
    pedir_velocidad,
    pausar,
    menu_principal,
)


def ejecutar_ordenamiento(opcion):
    tamano = pedir_tamano()
    intervalo = pedir_velocidad()

    lista = crear_lista_aleatoria(tamano)

    def mostrar(lista_actual, movimientos):
        imprimir_histograma(lista_actual, movimientos)
        time.sleep(intervalo)

    imprimir_histograma(lista, 0)
    time.sleep(1)

    if opcion == "1":
        movimientos = bubble_sort(lista, mostrar)
        nombre = "Bubble sort"

    elif opcion == "2":
        movimientos = selection_sort(lista, mostrar)
        nombre = "Selection sort"

    elif opcion == "3":
        movimientos = insertion_sort(lista, mostrar)
        nombre = "Insertion sort"

    elif opcion == "4":
        movimientos = merge_sort(lista, mostrar)
        nombre = "Merge sort"

    elif opcion == "5":
        movimientos = quick_sort(lista, mostrar)
        nombre = "Quick sort"

    imprimir_histograma(lista, movimientos)
    print(f"La lista ya está ordenada con {nombre}.")
    print(f"Movimientos totales: {movimientos}")
    print()

    pausar()


def main():
    while True:
        limpiar_pantalla()
        menu_principal()

        opcion = input("Elige una opción: ")

        if opcion in ["1", "2", "3", "4", "5"]:
            ejecutar_ordenamiento(opcion)

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")
            pausar()


if __name__ == "__main__":
    main()
