def dimensoes(matriz):
    lin = len(matriz)
    for j in matriz:
        col = len(j)
        break
    print(str(lin) + "X" + str(col))
