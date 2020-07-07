def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x-1)

def teste():
    print(fatorial(2))
    print(fatorial(3))
    print(fatorial(4))
    print(fatorial(5))
    print(fatorial(0))
