class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c
    
    def semelhantes(self, triangulo):
        result = 0
        lista1 = [self.a, self.b, self.c]
        lista2 = [triangulo.a, triangulo.b, triangulo.c]
        if lista1 > lista2:
            for i in range(lista1):
                if lista1 % lista2 == 0:
                    result += 1
        else:
            for i in lista1:
                if lista2 % lista1 == 0:
                    result += 1

        if result == 3:
            return True
        else:
            return False

        
        
def main():
    t = Triangulo(1, 1, 1)
    
