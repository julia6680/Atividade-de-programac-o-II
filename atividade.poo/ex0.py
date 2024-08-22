class Retangulo:
    def __init__(self):
        self.largura = 1.0
        self.altura = 2.0

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


ret1 = Retangulo()
print("Área do retângulo 1:", ret1.area())
print("Perímetro do retângulo 1:", ret1.perimetro())

ret2 = Retangulo()
print("Área do retângulo 2:", ret2.area())
print("Perímetro do retângulo 2:", ret2.perimetro())