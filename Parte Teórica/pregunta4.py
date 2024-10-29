"""- DRY: Don't Repeat Yourself. Es un principio de desarrollo de software que promueve 
la reducción de la duplicación de lógica en los sistemas.
- KISS: Keep It Simple, Stupid. Este principio nos dice que la mayoría de sistemas 
funcionan mejor si se mantienen simples en lugar de complicados.

"""

# Ejemplo que no cumple DRY y KISS
class CalculadorPrecios:
    def calcular_precio_producto1(self, precio, descuento):
        if descuento == "bajo":
            precio_final = precio - (precio * 0.05)
        elif descuento == "medio":
            precio_final = precio - (precio * 0.1)
        elif descuento == "alto":
            precio_final = precio - (precio * 0.2)
        else:
            precio_final = precio
        return precio_final

    def calcular_precio_producto2(self, precio, descuento):
        if descuento == "bajo":
            precio_final = precio - (precio * 0.05)
        elif descuento == "medio":
            precio_final = precio - (precio * 0.1)
        elif descuento == "alto":
            precio_final = precio - (precio * 0.2)
        else:
            precio_final = precio
        return precio_final

    def calcular_precio_producto3(self, precio, descuento):
        if descuento == "bajo":
            precio_final = precio - (precio * 0.05)
        elif descuento == "medio":
            precio_final = precio - (precio * 0.1)
        elif descuento == "alto":
            precio_final = precio - (precio * 0.2)
        else:
            precio_final = precio
        return precio_final

# Ejemplo que cumple DRY y KISS
class CalculadorPrecios:
    def calcular_precio(self, precio, descuento):
        if descuento == "bajo":
            descuento_aplicado = 0.05
        elif descuento == "medio":
            descuento_aplicado = 0.1
        elif descuento == "alto":
            descuento_aplicado = 0.2
        else:
            descuento_aplicado = 0.0
        return precio * (1 - descuento_aplicado)
