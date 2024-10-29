"""El antipatrón God Object (o "Objeto Dios") se refiere a una clase o componente en un sistema que tiene demasiadas responsabilidades, 
concentra la mayoría de la lógica y conoce demasiado sobre otras partes del sistema. Este antipatrón surge cuando un solo objeto o clase 
maneja muchas funcionalidades o responsabilidades que idealmente deberían estar distribuidas entre diferentes objetos, violando el principio 
de responsabilidad única (Single Responsibility Principle) y otros principios SOLID.

- Código difícil de modificar: Como todas las funciones están en una sola clase, cualquier cambio podría impactar otras funciones de manera negativa.
- Riesgo de errores: Modificaciones en una función pueden afectar otras partes del código.
- Dificultad de reutilización: No se puede reutilizar partes específicas sin llevar consigo dependencias innecesarias.

"""

class SistemaGestion:
    def registrar_usuario(self, nombre, email):
        return 'Usuario registrado'

    def autenticar_usuario(self, usuario, contraseña):
        return 'Usuario autenticado'

    def agregar_producto(self, producto):
        return 'Producto agregado'

    def calcular_precio(self, producto, cantidad):
        return 'Precio calculado'

    def generar_reporte(self):
        return 'Reporte generado'

    def enviar_correo(self, destinatario, asunto, mensaje):
        return 'Correo enviado'    

# Refactorización del código para evitar el antipatrón God Object
class Usuario:
    def registrar(self, nombre, email):
        return 'Usuario registrado'

    def autenticar(self, usuario, contraseña):
        return 'Usuario autenticado'

class Producto:
    def agregar(self, producto):
        return 'Producto agregado'

    def calcular_precio(self, producto, cantidad):
        return 'Precio calculado'

class Reporte:
    def generar(self):
        return 'Reporte generado'

class Correo:
    def enviar(self, destinatario, asunto, mensaje):
        return 'Correo enviado'

if __name__ == '__main__':
    usuario = Usuario()
    usuario.registrar('Nacho', '    ')  
    producto = Producto()
    producto.agregar('Ordenador')
    reporte = Reporte()
    reporte.generar()
    correo = Correo()
    correo.enviar('   ', 'Oferta', '¡Descuento especial!')