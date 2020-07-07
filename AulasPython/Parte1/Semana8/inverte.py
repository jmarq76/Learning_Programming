n = int(input("Digite um número inteiro, para finalizar digite 0: "))
lista = []
k = 1

while n != 0:
    lista.append(n)
    n = int(input("Digite um número inteiro, para finalizar digite 0: "))
    
tamanho = len(lista) - 1

while tamanho >= 0:
    print(lista[tamanho])
    tamanho -= 1
