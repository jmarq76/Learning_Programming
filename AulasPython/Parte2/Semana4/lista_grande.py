import random

def lista_grande(n):
    lista_alt = []
    for i in range(n):
        lista_alt.append(random.randrange(n))

    return lista_alt
