names = ["Ana", "Hugo", "Valeria"]
ages = [65, 30, 50]
cities = ["", "Madrid", "Mexico"]

mixes = list(zip(names, ages, cities))
print(mixes)

for name, age, city in mixes:
    print(f"{name} is {age} years old and live in {city}")
