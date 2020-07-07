valor = int(input("Digite um número inteiro: "))

resto1 = valor % 3
resto2 = valor % 5

if resto1 == 0 and resto2 == 0:
    print("FizzBuzz")
else:
    print(valor)