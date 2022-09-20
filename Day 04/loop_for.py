list = ['a', 'b', 'c']

for item in list:
    numberItem = list.index(item) + 1
    print('>>', item, 'number item', numberItem)

names = ['Hugo', 'Luis', 'Julia', 'Paola']

for item in names:
    if item.startswith('L'):
        print('The name has the letter L', item)
    else:
        print(item, 'Dont have L')

print("#############")
numbers = [1,2,3,4,5,6,7,8,9,0]
myValue = 0

for item in numbers:
    myValue = myValue + item

print(myValue)
print("#############")

word = 'python'
for item in word:
    print(item)
print("#############")

for a, b in [[1,2],[3,4], [5,6]]:
    print(a)
    print(b)
print("#############")

dic = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)

for a, b in dic.items():
    print(a, '--', b)