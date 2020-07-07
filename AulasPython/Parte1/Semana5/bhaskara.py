import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def raiz(a, b):
    raiz = math.sqrt(delta())
    if delta() == 0:
        x1 = (-b + raiz) / (2 * a)
        print("a raiz desta equação é", x1)
    else:
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
        if x1 < x2:
            print("as raízes da equação são", x1, "e", x2)
        else:
            print("as raízes da equação são", x2, "e", x1)

delta(a, b, c)
