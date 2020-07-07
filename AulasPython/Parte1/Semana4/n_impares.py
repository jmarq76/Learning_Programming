n = int(input("Digite um número inteiro: "))

i = 0
count = 0
while count < n:
    if i % 2 == 1:
        print(i)
        i += 1
        count += 1
    else:
        i += 1