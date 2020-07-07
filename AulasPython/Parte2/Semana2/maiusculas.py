def maiusculas(frase):
    ''' Recebe uma frase e devolve string com as letras maiúsculas que existem
        nesta frase, na ordem que elas aparecem'''
    maiusculas = ""
    for i in frase:
        if ord(i) > 64 and ord(i) < 91:
            maiusculas = maiusculas + i

    return maiusculas
