class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('Pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'black'
        print(f"Now, the bird is {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False

    @staticmethod
    def mirar():
        print("The bird see our")

Pajaro.poner_huevos(3)
print(Pajaro.alas)