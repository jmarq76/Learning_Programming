#programa que calcula raizes de 2º grau
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = (b ** 2) - 4 * a * c

if delta < 0:
    print("Esta equação não possui raizes reais")
else:
    raiz = math.sqrt(delta)
    if delta == 0:
        raiz = math.sqrt(delta)
        x1 = (-b + raiz) / (2 * a)
        print("A raiz desta equação é", x1)
    else:
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
        print("As raizes da equação são:", x1,"e", x2)