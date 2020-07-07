def dimensoes(matriz):
    lin = len(matriz)
    for j in matriz:
        col = len(j)
        break
    return lin, col

def sao_multiplicaveis(m1, m2):
    dim1 = dimensoes(m1)
    dim2 = dimensoes(m2)
    if dim1[1] == dim2[0]:
        return True
    else:
        return False
    
def teste():
    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    sao_multiplicaveis(m1, m2)
