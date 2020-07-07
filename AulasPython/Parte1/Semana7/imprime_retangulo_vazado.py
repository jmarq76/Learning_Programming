largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
i = 2
n = altura

while altura > 0:
    print("#", end='')
    while i < largura:
        if n == altura or altura == 1:
            print("#", end='')
        else:
            print(" ", end='')
        i = i + 1
    print("#", end='')
    print()
    altura = altura - 1
    i = 2
