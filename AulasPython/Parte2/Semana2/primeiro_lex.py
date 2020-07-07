'''Escreva uma função que recebe um array de strings como parâmetro e
devolve o primeiro string na ordem lexicográfica, ignorando-se letras
maiúsculas e minúsculas.'''

def primeiro_lex(lista):
    i = 1
    for string in lista:
        while i < len(lista):
            if string > lista[i]:
                break
            i += 1
        if i == len(lista):
            break

    return string
