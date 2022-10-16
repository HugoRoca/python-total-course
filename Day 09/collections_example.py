from collections import Counter, defaultdict, namedtuple

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(Counter(numbers))

phrase = 'al pan pan y al vino vino'
print(Counter(phrase))

serie = Counter([1,1,1,1,2,2,2,2,3,3,3,4,4,4,4, 4])
print(serie.most_common())
print(serie.most_common(1))
print(list(serie))

# my_dic = {'uno': 'verde', 'dos': 'red', 'tres': 'azul'}
my_dic = defaultdict(lambda: 'nothing')
my_dic['uno'] = 'green'
print(my_dic['dos'])


# my_tupla = (500, 18, 65)
# print(my_tupla[1])

Person = namedtuple('Person', ['name', 'height', 'weight'])
ariel = Person('Ariel', 1.40, 20)
print(ariel.height)
print(ariel[1])

