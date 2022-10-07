# class Animal:
#     def __init__(self, edad, color):
#         self.color = color
#         self.edad = edad
#
#     def nacer(self):
#         print("Este animal a nacido")
#
#     def hablar(self):
#         print("Este animal habla")
#
#
# class Pajaro(Animal):
#     def __init__(self, edad, color, altura):
#         super().__init__(edad, color)
#         self.altura = altura
#
#     def hablar(self):
#         print("pio pio")
#
#     def volar(self, metros):
#         print(f"El pajaro vuela ${metros} metros")

class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print("ja ja ja")

    def hablar(self):
        print("que tal?")

# Prioriza la primera herencia
class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()

print(Nieto.__mro__)