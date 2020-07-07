def insertion_sort(lista):
    for i in range(len(lista)):
        while i > 0:
            if lista[i-1] > lista[i]:
                lista[i], lista[i-1] = lista[i-1], lista[i]
            else:
                break

            i -= 1

    return lista
