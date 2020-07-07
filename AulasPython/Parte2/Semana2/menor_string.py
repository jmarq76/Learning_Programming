'''Escreva uma função que recebe um array de strings como parâmetro e
devolve o primeiro string na ordem lexicográfica, ignorando-se letras
maiúsculas e minúsculas.'''

def primeiro_lex(lista):
    i = 1
    for string in lista:
        strmin = string.lower()
        while i < len(lista):
            if strmin > lista[i].lower():
                break
            i += 1
        if i == len(lista):
            break

    return string.lower()


def teste_menor_string():
    if primeiro_lex(['oĺá', 'A', 'a', 'casa']) == 'A':
        print("Passed!")
    else:
        print("Failed!")
    if primeiro_lex(['AAAAAA', 'b']) == 'AAAAAA':
        print("Passed!")
    else:
        print("Failed!")
