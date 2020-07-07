#Escrever uma função que recebe uma lista de strings contendo nomes de
#pessoas como parâmetro e devolve o nome mais curto, o nome mais curto
#que tiver dentro dessa lista de strings. A função deve ignorar espaços
#antes e depois do nome e deve devolver o nome, entre aspas,
#capitalizado, ou seja, apenas com a primeira letra maiúscula.

def menor_nome(nomes):
    i = 1
    for nome in nomes:
        tamanho = len(nome.strip())
        while i < len(nomes):
            if tamanho > len(nomes[i].strip()):
                break
            i += 1
        if i == len(nomes):
            break

    return nome.strip().capitalize()
