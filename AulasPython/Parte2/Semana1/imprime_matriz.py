def imprime_matriz(matriz):
    for i in matriz:
        tamanho = len(i)
        contador = 1
        for j in i:
            if contador != tamanho:
                print(j, end=" ")
                contador += 1
            else:
                print(j, end= "")
        print()
