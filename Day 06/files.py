my_file = open('test___1.txt', 'a')

# print(my_file.read())
# print(my_file.readline()) # first line
# print(my_file.readline().rstrip()) # second line
# print(my_file.readline().upper()) # thirty line

# for line in my_file:
#    print(line)

my_file.write('probandaia')
#print(my_file.readlines())

# Always exec for free memory
my_file.close()
