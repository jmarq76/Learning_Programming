n = int(input("Digite um número inteiro: "))

tamanho = len(str(n))

adjacente = False
i = 0
while i < tamanho and not adjacente:
    if tamanho == 1:
        break
    anterior = n % 10
    n = n // 10
    atual = n % 10
    if anterior == atual:
        adjacente = True
    i += 1
        
if adjacente == True:
    print("sim")
else:
    print("não")