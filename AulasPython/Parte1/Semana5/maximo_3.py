def maximo(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
        
x = int(input("Digite o primeiro numero inteiro: "))
y = int(input("Digite o segundo numero inteiro: "))
z = int(input("Digite o terceiro numero inteiro: "))

maximo(x, y, z)
