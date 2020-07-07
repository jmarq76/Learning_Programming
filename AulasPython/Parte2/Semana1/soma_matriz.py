def dimensoes(matriz):
    lin = len(matriz)
    for j in matriz:
        col = len(j)
        break
    return lin, col

def soma_matrizes(m1, m2):
    dim1 = dimensoes(m1)
    dim2 = dimensoes(m2)
    if dim1 == dim2:
        soma = []
        n = 0
        for i in m1:
            linha = []
            tamanho = len(i)
            j = 0
            while j < tamanho:
                linha.append(m1[n][j] + m2[n][j])
                j += 1
            n += 1
            soma.append(linha)
        return soma
    else:
        return False

def teste():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    soma_matrizes(m1, m2)
    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    soma_matrizes(m1, m2)
    
