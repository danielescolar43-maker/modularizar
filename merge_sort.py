def merge_sort(lista, mostrar=None):
    # Divide la lista en partes pequeñas, las ordena
    # y después las combina nuevamente en orden.
    movimientos = 0

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
            izquierda.append(lista[i])

        for i in range(mitad + 1, fin + 1):
            derecha.append(lista[i])

        i = 0
        j = 0
        k = inicio

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] <= derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            movimientos += 1

            if mostrar is not None:
                mostrar(lista, movimientos)

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
            movimientos += 1

            if mostrar is not None:
                mostrar(lista, movimientos)

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
            movimientos += 1

            if mostrar is not None:
                mostrar(lista, movimientos)

    merge_sort_aux(0, lista.size - 1)
    return movimientos
