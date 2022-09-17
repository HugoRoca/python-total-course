list = ['a', 'b', 'c']
list_2 = ['hi', 55, 6.1]
list_3 = list + list_2
length = len(list)
result = list[0]
result_1 = list[0:2]
result_2 = list + list_2

list_3[0] = 'alpha'
list_3.append('g') # for add new item to array
list_3.pop() # without param, delete last one in the array, if you enter param delete that index item

print(type(list), length, result, result_1, list_3)


new_list = ['g','a','d','b']
new_list.sort()

print(new_list)

new_list.reverse()
print(new_list)