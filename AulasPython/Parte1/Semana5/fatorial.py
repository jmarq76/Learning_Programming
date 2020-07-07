def fatorial(n, k):
    import math
    n1 = math.factorial(n)
    k1 = math.factorial(k)
    nk = math.factorial(n - k)
    return n1 / (k1 * nk)
