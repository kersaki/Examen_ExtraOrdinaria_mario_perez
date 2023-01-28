class Artefactos():
    def __init__(self, peso, nombre, precio, caducidad):
        self.peso=peso
        self.nombre=nombre
        self.precio=precio
        self.caducidad=caducidad

    def __str__(self):
        return 'El peso es {}, su nombre es {}, su precio es de {} €, y su caducidad es de {}'.format(self.peso, self.nombre, self.precio, self.caducidad)                
print(Artefactos)

Artefacto1 = Artefactos(24, 'Corona', 1000, '21 de Enero del 2222')
print(Artefacto1)