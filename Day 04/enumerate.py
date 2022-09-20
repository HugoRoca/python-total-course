letters = ["a", "b", "c"]

for index, item in enumerate(letters):
    print(index, item)

for index, item in enumerate(range(50, 56)):
    print(index, item)

myTuple = list(enumerate(letters))
print(myTuple[1][0])
