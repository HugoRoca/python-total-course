from random import *

aleatorio = randint(1, 50)
print(aleatorio)

aleatorio = round(uniform(1, 50), 1)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colors = ['azul', 'red', 'yellow', 'green']
aleatorio = choice(colors)
print(aleatorio)

newList = list(range(5, 50, 5))
shuffle(newList)
print(newList)
