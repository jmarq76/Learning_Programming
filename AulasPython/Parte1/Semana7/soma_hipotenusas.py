import math

def é_hipotenusa(n):
    i = 1
    k = 0
    while i < n:
        j = i + 1
        while n != k and j <= n:
            k = math.sqrt((i ** 2) + (j ** 2))
            j += 1
        i += 1
        if n == k:
            return int(k)
        
def soma_hipotenusas(n):
    i = 1
    k = 0
    while i <= n:
        if é_hipotenusa(i) == i:
            k = é_hipotenusa(i) + k
        i += 1
    return k
