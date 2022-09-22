def count(num):
    numbers = []
    for n in range(1, num):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        if count == 2:
            numbers.append(n)

    return numbers


print(count(20))
