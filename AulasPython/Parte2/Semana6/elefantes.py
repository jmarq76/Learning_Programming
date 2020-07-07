def incomodam(n):
    texto = "incomodam "
    if n == 1:
        return texto
    elif n < 1:
        return ""
    else:
        texto = texto + incomodam(n-1)
        return texto

def elefantes(n, i = 1):
    if n < 1:
        return ""
    elif i == 1:
        return "Um elefante incomoda muita gente" + elefantes(n - 1, i + 1)
    else:
        elefs = "\n" + str(i) + " elefantes " + incomodam(i) + "muito mais"
        elef = "\n" + str(i) + " elefantes incomodam muita gente"
        if n == 1:
            cancao = elefs + elefantes(n - 1, i + 1)
        else:
            cancao = elefs + elef + elefantes(n - 1, i + 1)
        return cancao



def teste():
    print(incomodam(4))
    print(incomodam(6))
    print(incomodam(-1))
    print(elefantes(4))
    print(elefantes(6))
    print(elefantes(-1))
