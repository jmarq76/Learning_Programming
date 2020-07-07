n = int(input("Digite um número inteiro >1: "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade == 1 and n == fator:
        print("fator", fator, "multiplicidade = ", multiplicidade)
        print("é numero primo")
    if multiplicidade >= 1:
        print("fator", fator, "multiplicidade = ", multiplicidade)
        print("não é numero primo")
    fator = fator + 1
    multiplicidade = 0
