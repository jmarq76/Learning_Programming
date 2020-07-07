n = int(input("Digite um número inteiro: "))

numPrimo = True

if n == 2 or n == 3 or n == 5:
    numPrimo = True
elif n % 7 == 0:
    numPrimo = False
elif n % 5 == 0:
    numPrimo = False
elif n % 3 == 0:
    numPrimo = False
elif n % 2 == 0:
    numPrimo = False

if numPrimo == True:
    print("primo")
else:
    print("não primo")
    
