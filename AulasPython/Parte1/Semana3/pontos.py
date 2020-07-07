import math

x1 = float(input("Digite a 1ª coordenada x: "))
y1 = float(input("Digite a 1ª coordenada y: "))
x2 = float(input("Digite a 2ª coordenada x: "))
y2 = float(input("Digite a 2ª coordenada y: "))

x = (x1 - x2) ** 2
y = (y1 - y2) ** 2

d = math.sqrt(x + y)

if d >= 10:
    print("longe")
else:
    print("perto")