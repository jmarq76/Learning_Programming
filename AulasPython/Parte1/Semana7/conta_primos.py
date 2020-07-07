def n_primos(x):
    count = 0
    while x >= 2:
        if x == 2:
            count = count + 1
        else:
            n = (x - 1)
            while n >= 2:
                if x % n == 0:
                    break
                n -= 1
                if n == 1:
                    count = count + 1
        x -= 1
    return count

def main():
    n = int(input("Digite um número inteiro >2: "))
    print(n_primos(n))
    

main()
