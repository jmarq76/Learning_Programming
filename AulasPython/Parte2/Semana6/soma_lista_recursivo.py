def soma_lista(lista):
    i = len(lista)
    if i == 1:
        return lista[0]
    else:
        total = lista.pop() + soma_lista(lista)
        return total
