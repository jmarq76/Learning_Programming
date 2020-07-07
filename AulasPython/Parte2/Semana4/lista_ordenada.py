def ordenada(lista):
     length = len(lista)
     for i in range(length - 1):
         if lista[i] > lista[i + 1]:
             return False
     return True
