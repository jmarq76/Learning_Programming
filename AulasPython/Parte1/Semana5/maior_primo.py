def maior_primo(k):
    éprimo = False
    n = 2
    while (éprimo == False):
        while (n < k // 2):
            if k % n == 0:
                k -= 1
                n = 2
            else:
                n += 1
        éprimo = True
    return k
    
    
k = int(input("Digite um número inteiro maior ou igual a 2: "))

print(maior_primo(k))
