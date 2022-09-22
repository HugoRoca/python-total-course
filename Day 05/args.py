def suma(a, b):
    return a + b


print(suma(1, 3))


########
def new_plus(*args):
    total = 0

    for arg in args:
        total += arg

    return total


print(new_plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
