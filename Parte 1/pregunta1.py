# Código errróneo que no cumple el principio SOLID "Open/Closed"

class CalculoArea:
    def __init__(self, formas):
        self.formas = formas

    def area_total(self):
        area_total = 0
        for formas in self.formas:
            if formas.tipo == 'circulo':
                area_total += formas.radio ** 2 * 3.14
            elif formas.tipo == 'rectangulo':
                area_total += formas.ancho * formas.altura
        return area_total
    
# Código corregido
class Forma:
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.radio ** 2 * 3.14
    
class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto
    
class CalculoArea:

    def __init__(self, formas):
        self.formas = formas

    def area_total(self):
        return sum([forma.area() for forma in self.formas])
    
if __name__ == '__main__':
    formas = [Circulo(5), Rectangulo(3, 4)]
    calculo = CalculoArea(formas)
    print(calculo.area_total())




    
