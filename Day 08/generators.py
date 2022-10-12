# def my_generator():
#     yield 4
def normal_function():
    result = []
    for x in range(1, 5):
        result.append(x * 10)

    return result


def my_generator():
    for x in range(1, 5):
        yield x * 10


print(normal_function())
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

