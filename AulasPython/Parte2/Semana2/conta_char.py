def conta_letras(frase, contar="vogais"):
    if contar == "vogais":
        return conta_vogais(frase)
    else:
        return conta_consoantes(frase)

def conta_vogais(frase):
    vogal = 0
    frase = frase.lower()
    for i in frase:
        if ord(i) == 97 or ord(i) == 101 or ord(i) == 105 or ord(i) == 111 or ord(i) == 117:
            vogal += 1

    return vogal

def conta_consoantes(frase):
    consoante = 0
    frase = frase.lower()
    for i in frase:
        if ord(i) != 97 and ord(i) != 101 and ord(i) != 105 and ord(i) != 111 and ord(i) != 117 and ord(i) != 32:
            consoante += 1

    return consoante
