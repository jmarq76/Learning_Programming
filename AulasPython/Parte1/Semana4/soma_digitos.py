n = int(input("Digite um número inteiro: "))

tamanho = len(str(n))

i = 0
total = 0
while i < tamanho:
    singleNum = n % 10
    total += singleNum
    n = n // 10
    i += 1
    
print(total)