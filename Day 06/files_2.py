# w -> replace the txt
# a -> add text in the end
# file = open('test_1.txt', 'w')
# file.write('''
# Im the new text
# Second line''')
#
# file.writelines(['hi', 'hello', 'world'])

file = open('test_1.txt', 'a')
file.write('\nadd')
file.close()