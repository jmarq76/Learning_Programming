class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def retangulo(self):
        if (self.a ** 2 + self.b ** 2) == self.c ** 2:
            return True
        else:
            return False

def main():
    t = Triangulo(1, 1, 1)
    
