
#n = 1
#while n > 0:
#    n = int(input("Digite um numero inteiro maior que zero, para parar digite 0: "))
#    i = n
#    while i > 1:
#        n = n * (i - 1)
#        i -= 1
#    print(n)

n = int(input("Digite um número inteiro: "))
while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
    n = int(input("Digite um número inteiro: "))
