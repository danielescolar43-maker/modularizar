def insertion_sort(lista, mostrar=None):
    # Toma cada elemento y lo inserta en la posición correcta
    # dentro de la parte que ya se encuentra ordenada.
    movimientos = 0

    for i in range(1, lista.size):
        valor_actual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            movimientos += 1

            if mostrar is not None:
                mostrar(lista, movimientos)

            j -= 1

        lista[j + 1] = valor_actual
        movimientos += 1

        if mostrar is not None:
            mostrar(lista, movimientos)

    return movimientos
