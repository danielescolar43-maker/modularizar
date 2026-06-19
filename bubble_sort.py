def bubble_sort(lista, mostrar=None):
    # Compara elementos adyacentes e intercambia los que estén en desorden.
    # Los valores más grandes van quedando al final de la lista.
    movimientos = 0

    for i in range(lista.size):
        for j in range(0, lista.size - 1 - i):
            if lista[j] > lista[j + 1]:
                lista.swap(j, j + 1)
                movimientos += 1

                if mostrar is not None:
                    mostrar(lista, movimientos)

    return movimientos
