dictionary = {'c1': 'value1', 'c2': 'value2'}
print(type(dictionary))

result = dictionary['c1']
print(result)

client = {'name': 'Hugo', 'lastname': 'Roca', 'cellphone': '987654321'}
query = (client['name'])
print(query)

dictionary = {'c1': 'value1', 'c2': 'value2', 'c3': [1, 2, 3, 'a'], 'c4': { 'key': 'value' } }
print(dictionary['c4'])
print(dictionary['c3'][3].upper())

dictionary['xxx'] = 'xxx'
dictionary['c1'] = 'value of replace'
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())