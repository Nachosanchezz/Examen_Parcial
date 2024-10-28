"""Provee una interfaz o clase abstracta (creator) que permite encapsular la
lógica de creación de los objetos en subclases y éstas deciden qué clase
instanciar. Los objetos se crean a partir de un método (factory method) y
no a través de un constructor como se hace normalmente. Además, los
ConcreteCreators devuelven siempre la interfaz (Product), esto permite que
el cliente trate a los productos por igual, tengan una implementación u otra.


La estructura típica del patrón Factory method es la siguiente:

● Product: definición de las interfaces para la familia de productos
genéricos.

● ConcreteProduct: implementación de los diferentes productos.

● Creator: declara el factory method que se encargará de instanciar
nuevos objetos. Es importante que este método devuelva la interfaz
Product. Normalmente el Creator suele ser una clase abstracta con
cierta lógica de negocio relacionada con los productos a crear.
Dependiendo de la instancia de producto que se devuelva, se puede
seguir un flujo u otro.

● ConcreteCreator: crea la instancia del producto concreto.

"""

# Implementación del patrón Factory

class Integral:
    def calcular(self, a, b):
        pass

class IntegralPrimera(Integral):  
    def calcular(self, a, b):
        return (b ** 2 - a ** 2) / 2
    
class IntegralSegunda(Integral):
    def calcular(self, a, b):
        return (b ** 3 - a ** 3) / 3
    
class IntegralTercera(Integral):
    def calcular(self, a, b):
        return (b ** 4 - a ** 4) / 4
    
class IntegralFactory:
    def crear_integral(self, tipo):
        if tipo == 1:
            return IntegralPrimera()
        elif tipo == 2:
            return IntegralSegunda()
        elif tipo == 3:
            return IntegralTercera()
        else:
            raise ValueError('Tipo de integral no válido')
        
if __name__ == '__main__':
    factory = IntegralFactory()
    integral = factory.crear_integral(2)
    print(integral.calcular(2, 4))
    
    
    
