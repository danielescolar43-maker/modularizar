import os
import random
import time


class llist:
    def __init__(self, *vals, first=None, rest=None):
        if first is not None and rest is not None:
            self.__size = rest.size + 1
            self.value = first
            self.rest = rest
        elif not vals:
            self.__size = 0
        else:
            first, *others = vals
            self.value = first
            self.rest = llist(*others)
            self.__size = 1 + self.rest.size

    @property
    def size(self):
        return self.__size

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.size:
            raise IndexError(f"Index '{idx}' out of bound for llist with size {self.size}")
        if idx == 0:
            return self.value
        return self.rest.__getitem__(idx - 1)

    def __setitem__(self, idx, value):
        if idx < 0 or idx >= self.size:
            raise IndexError(f"Index out of bound for llist with size {self.size}")
        if idx == 0:
            self.value = value
        else:
            self.rest.__setitem__(idx - 1, value)

    def swap(self, i, j):
        if i < 0 or i >= self.size or j < 0 or j >= self.size:
            raise IndexError(f"Invalid index for list with size: {self.size}")
        self[i], self[j] = self[j], self[i]

    def insert(self, idx, value):
        if idx < 0 or idx > self.size:
            raise IndexError(f"Index out of bound for llist with size {self.size}")
        if idx == 0:
            if self.size != 0:
                self.rest = llist(first=self.value, rest=self.rest)
            else:
                self.rest = llist()
            self.value = value
            self.__size += 1
        else:
            self.rest.insert(idx - 1, value)
            self.__size += 1

    def append(self, value):
        self.insert(self.size, value)

    def __str__(self):
        as_str = "["
        for i in range(0, self.size):
            as_str += f"{self.__getitem__(i)}, "
        if as_str.endswith(" "):
            as_str = as_str[0:-2]
        as_str += "]"
        return as_str

    def bubble_sort(self, mostrar=None):
        movimientos = 0
# Bubble Sort:
# Compara los elementos adyacentes e intercambia los que estén en desorden.
# Los valores más grandes "suben" al final de la lista.

        for i in range(self.size):
            for j in range(0, self.size - 1 - i):
                if self[j] > self[j + 1]:
                    self.swap(j, j + 1)
                    movimientos += 1
                    if mostrar is not None:
                        mostrar(self, movimientos)

        return movimientos

    def selection_sort(self, mostrar=None):
        movimientos = 0
# Selection Sort:
# Busca el elemento más pequeño de la parte no ordenada
# y lo coloca en la posición correcta.

        for i in range(self.size):
            indice_menor = i

            for j in range(i + 1, self.size):
                if self[j] < self[indice_menor]:
                    indice_menor = j

            if indice_menor != i:
                self.swap(i, indice_menor)
                movimientos += 1
                if mostrar is not None:
                    mostrar(self, movimientos)

        return movimientos

    def insertion_sort(self, mostrar=None):
        movimientos = 0
# Insertion Sort:
# Toma un elemento y lo inserta en la posición correcta
# dentro de la parte que ya está ordenada.

        for i in range(1, self.size):
            valor_actual = self[i]
            j = i - 1

            while j >= 0 and self[j] > valor_actual:
                self[j + 1] = self[j]
                movimientos += 1
                if mostrar is not None:
                    mostrar(self, movimientos)
                j -= 1

            self[j + 1] = valor_actual
            movimientos += 1
            if mostrar is not None:
                mostrar(self, movimientos)

        return movimientos

    def merge_sort(self, mostrar=None):
        movimientos = 0
# Merge Sort:
# Divide la lista en partes más pequeñas, las ordena
# recursivamente y luego las combina ordenadas.

        def merge_sort_aux(inicio, fin):
            nonlocal movimientos

            if inicio >= fin:
                return

            mitad = (inicio + fin) // 2

            merge_sort_aux(inicio, mitad)
            merge_sort_aux(mitad + 1, fin)

            izquierda = []
            derecha = []

            for i in range(inicio, mitad + 1):
                izquierda.append(self[i])

            for i in range(mitad + 1, fin + 1):
                derecha.append(self[i])

            i = 0
            j = 0
            k = inicio

            while i < len(izquierda) and j < len(derecha):
                if izquierda[i] <= derecha[j]:
                    self[k] = izquierda[i]
                    i += 1
                else:
                    self[k] = derecha[j]
                    j += 1

                movimientos += 1
                if mostrar is not None:
                    mostrar(self, movimientos)
                k += 1

            while i < len(izquierda):
                self[k] = izquierda[i]
                i += 1
                k += 1
                movimientos += 1
                if mostrar is not None:
                    mostrar(self, movimientos)

            while j < len(derecha):
                self[k] = derecha[j]
                j += 1
                k += 1
                movimientos += 1
                if mostrar is not None:
                    mostrar(self, movimientos)

        merge_sort_aux(0, self.size - 1)
        return movimientos

    def quick_sort(self, mostrar=None):
        movimientos = 0
# Quick Sort:
# Selecciona un pivote y divide los elementos en menores
# y mayores que él para ordenarlos recursivamente.

        def particion(inicio, fin):
            nonlocal movimientos

            pivote = self[fin]
            i = inicio - 1

            for j in range(inicio, fin):
                if self[j] <= pivote:
                    i += 1
                    if i != j:
                        self.swap(i, j)
                        movimientos += 1
                        if mostrar is not None:
                            mostrar(self, movimientos)

            if i + 1 != fin:
                self.swap(i + 1, fin)
                movimientos += 1
                if mostrar is not None:
                    mostrar(self, movimientos)

            return i + 1

        def quick_sort_aux(inicio, fin):
            if inicio < fin:
                indice_pivote = particion(inicio, fin)
                quick_sort_aux(inicio, indice_pivote - 1)
                quick_sort_aux(indice_pivote + 1, fin)

        quick_sort_aux(0, self.size - 1)
        return movimientos


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
        movimientos = lista.bubble_sort(mostrar)
        nombre = "Bubble sort"

    elif opcion == "2":
        movimientos = lista.selection_sort(mostrar)
        nombre = "Selection sort"

    elif opcion == "3":
        movimientos = lista.insertion_sort(mostrar)
        nombre = "Insertion sort"

    elif opcion == "4":
        movimientos = lista.merge_sort(mostrar)
        nombre = "Merge sort"

    elif opcion == "5":
        movimientos = lista.quick_sort(mostrar)
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
