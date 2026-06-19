def selection_sort(lista, mostrar=None):
    # Busca el elemento más pequeño de la parte no ordenada
    # y lo coloca en su posición correcta.
    movimientos = 0

    for i in range(lista.size):
        indice_menor = i

        for j in range(i + 1, lista.size):
            if lista[j] < lista[indice_menor]:
                indice_menor = j

        if indice_menor != i:
            lista.swap(i, indice_menor)
            movimientos += 1

            if mostrar is not None:
                mostrar(lista, movimientos)

    return movimientos
