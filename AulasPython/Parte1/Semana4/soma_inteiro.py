# 1 numero inteiro com n digitos, calcular a soma dos digitos desse numero

x = int(input("Digite um número inteiro: "))
tamanho = len(str(x))
soma = 0

i = 1
while i <= tamanho:
    ultimo = x % 10
    x = x // 10
    soma = ultimo + soma
    i = i + 1
    
print("A soma do número inteiro é: ", soma)
