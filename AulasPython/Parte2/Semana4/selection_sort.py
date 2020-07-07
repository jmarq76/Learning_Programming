def ordena(lista):
    for i in range(len(lista)):
        posicao_minima = i

        for j in range(i +1, len(lista)):
            if lista[posicao_minima] > lista[j]:
                posicao_minima = j

        lista[i], lista[posicao_minima] = lista[posicao_minima], lista[i]

    return lista
