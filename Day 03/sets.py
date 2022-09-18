# st = unique value
mySet = set([1, 2, 3, 4, 5, 6])
print(type(mySet))
print(mySet)

mySet = { 1, 2, 3, (1, 2, 3)}
print(type(mySet))
print(mySet)

print(len(mySet)) # 4
print(2 in mySet) # find

myNewSet = {4, 5, 6}

mySet.add(7) # -> for add
mySet.remove(1) # -> for remove
mySet.discard(2) # similar to remove
popSet = mySet.pop() # -> remove random
print("pop remove random", popSet)

newSetUnion = mySet.union(myNewSet)
print(newSetUnion)
mySet.clear()
print(mySet)