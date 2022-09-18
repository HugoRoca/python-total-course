myTuple = (1, 2, (10, 20), 4)
print(type(myTuple))
print(myTuple[1])
print(myTuple[2][1])

myTuple = list(myTuple)
print(type(myTuple))

myTuple = tuple(myTuple)
print(type(myTuple))

myTuple = (1, 2, 3)
x, y, z = myTuple
print(x, y, z)

myTuple = (1, 2, 3, 1)
print(len(myTuple))
print(myTuple.count(1)) # count repetitions
print(myTuple.index(2)) # get index
