"""El patrón de diseño "Observer" permite que un objeto notifique a otros objetos sobre los cambios en su estado. 

"""
class SerieFibonacci:
    def __init__(self):
        self.observadores = []  

    def agregar_observador(self, observador):
        """Añadir un nuevo observador a la lista."""
        self.observadores.append(observador)

    def notificar_observadores(self, nuevo_termino):
        """Notificar a todos los observadores sobre un nuevo término."""
        for observador in self.observadores:
            observador.actualizar(nuevo_termino)

    def calcular(self, n_terminos):
        """Calcular la serie de Fibonacci hasta n términos."""
        a, b = 0, 1
        for _ in range(n_terminos):
            self.notificar_observadores(a)  
            a, b = b, a + b  


class RegistroTerminos:
    def actualizar(self, nuevo_termino):
        """Actualizar el registro con un nuevo término de la serie."""
        print(f"Nueva término de Fibonacci calculado: {nuevo_termino}")

if __name__ == "__main__":
    
    serie_fibonacci = SerieFibonacci()

    registro = RegistroTerminos()

    serie_fibonacci.agregar_observador(registro)

    serie_fibonacci.calcular(n_terminos=10)

