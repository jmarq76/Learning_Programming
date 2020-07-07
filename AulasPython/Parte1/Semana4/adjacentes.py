n = int(input("Digite um número inteiro: "))

tamanho = len(str(n))
count = 0
i = 0
adjacentes = False

while i < tamanho:
    n1 = n % 10
    n = n // 10
    n2 = n % 10
    if n1 == n2:
        count += 2
        adjacentes = True
    i += 1
        
if adjacentes:
    print("Existem", count, "números adjacentes")
else:
    print(" Não existem números adjacentes")