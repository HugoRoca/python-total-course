newList = [item for item in 'python']
print(newList)

newList = [n/2 for n in range(0, 21, 2)]
print(newList)

newList = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
print(newList)

newList = [10, 20, 30, 40, 50]
metro = [p * 3.281 for p in newList]
print(metro)