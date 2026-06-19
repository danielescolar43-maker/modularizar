def quick_sort(lista, mostrar=None):
    # Selecciona un pivote y separa los elementos menores y mayores
    # para ordenar cada parte de forma recursiva.
    movimientos = 0

    def particion(inicio, fin):
        nonlocal movimientos

        pivote = lista[fin]
        i = inicio - 1

        for j in range(inicio, fin):
            if lista[j] <= pivote:
                i += 1

                if i != j:
                    lista.swap(i, j)
                    movimientos += 1

                    if mostrar is not None:
                        mostrar(lista, movimientos)

        if i + 1 != fin:
            lista.swap(i + 1, fin)
            movimientos += 1

            if mostrar is not None:
                mostrar(lista, movimientos)

        return i + 1

    def quick_sort_aux(inicio, fin):
        if inicio < fin:
            indice_pivote = particion(inicio, fin)
            quick_sort_aux(inicio, indice_pivote - 1)
            quick_sort_aux(indice_pivote + 1, fin)

    quick_sort_aux(0, lista.size - 1)
    return movimientos
