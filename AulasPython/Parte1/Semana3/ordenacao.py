numero1 = int(input("Digite o 1º numero: "))
numero2 = int(input("Digite o 2º numero: "))
numero3 = int(input("Digite o 3º numero: "))

if numero1 < numero2 and numero2 < numero3:
    print("crescente")
else:
    print("não está em ordem crescente")