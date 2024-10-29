from abc import ABC, abstractmethod
class IntegracionStrategy(ABC):
    @abstractmethod
    def integrar(self, f, a, b, n):
        pass
class MetodoTrapecio(IntegracionStrategy):
    def integrar(self, f, a, b, n):
        h = (b - a) / n
        resultado = 0.5 * (f(a) + f(b))
        for i in range(1, n):
            resultado += f(a + i * h)
        return resultado * h
class MetodoSimpson(IntegracionStrategy):
    def integrar(self, f, a, b, n):
        if n % 2 == 1:
            n += 1  
        h = (b - a) / n
        resultado = f(a) + f(b)
        for i in range(1, n, 2):
            resultado += 4 * f(a + i * h)
        for i in range(2, n-1, 2):
            resultado += 2 * f(a + i * h)
        return resultado * h / 3

class CalculadoraIntegracion:
    def __init__(self, estrategia: IntegracionStrategy):
        self.estrategia = estrategia

    def cambiar_estrategia(self, nueva_estrategia: IntegracionStrategy):
        self.estrategia = nueva_estrategia

    def calcular_integral(self, f, a, b, n):
        return self.estrategia.integrar(f, a, b, n)

if __name__ == "__main__":
    def funcion(x):
        return x ** 2 

    a, b = 0, 1  
    n = 100     

    calculadora = CalculadoraIntegracion(MetodoTrapecio())
    resultado_trapecio = calculadora.calcular_integral(funcion, a, b, n)
    print(f"Integral usando el método del trapecio: {resultado_trapecio}")

    calculadora.cambiar_estrategia(MetodoSimpson())
    resultado_simpson = calculadora.calcular_integral(funcion, a, b, n)
    print(f"Integral usando el método de Simpson: {resultado_simpson}")
