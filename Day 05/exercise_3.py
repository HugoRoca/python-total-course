def count_zeros(*args):
    count = 1
    for n in args:
        if n == count and n == 0:
            return True
        count = n

    return False


print(count_zeros(1, 2, 3, 4, 0, 0, 2, 20, 23, 2))
