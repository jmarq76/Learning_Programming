largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
i = 0
n = altura
x = largura

while altura > 0:
    while i < largura:
            print("#", end='')
            i = i + 1
    print()
    altura = altura - 1
    i = 0
