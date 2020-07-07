def remove_repetidos(lista):
    i = 1
    n = 1
    for num in lista:
        tamanho = len(lista)
        while i < tamanho:
            if num == lista[i]:
                del lista[i]
                tamanho = len(lista)
                i -= 1
            i += 1
        i = 0
        n += 1
        i += n
    lista.sort()
    return lista

lista = [7,3,33,12,3,3,3,7,12,100]

remove_repetidos(lista)
