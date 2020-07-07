def encontra_impares(lista):
    impares = []
    i = len(lista) - 1
    if i == 0:
        if lista[i] % 2 == 1:
            return [lista[i]]
        else:
            return []
    else:
        if lista[i] % 2 == 1:
            impares = [lista[i]]
        impares.extend(encontra_impares(lista[:i]))
        return impares
            
def teste():
    print(encontra_impares([1,2,3,4,5,6,7,8,9,10,11]))
    print(encontra_impares([2,3,4,5,6,7,8,9,10,11,12]))
    print(encontra_impares([2]))
    print(encontra_impares([3]))

