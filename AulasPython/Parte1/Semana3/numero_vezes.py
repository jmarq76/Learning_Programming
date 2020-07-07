def main():
    n = int(input("Digite o valor de n (n > 0): "))
    d = int(input("Digite o valor de d (0<=d<=9): "))
    
    n2 = n
    tamanho = len(str(n))
    i = 0
    count = 0
    while i < tamanho:
        n1 = n2 % 10
        if n1 == d:
            count += 1
        n2 = n2 // 10
        i += 1
    print("O dígito", d, "ocorre", count, "vezes em", n)

main()