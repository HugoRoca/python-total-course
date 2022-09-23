# import os
from pathlib import Path

# route = os.getcwd() # /python-total-course/Day 06
# route = os.chdir(path) # for change directory
# route = os.makedirs('/python-total-course/Day 06/test') # create folder

# route = '/Users/hugoroca/personalProjects/python-total-course/Day 06/text.txt'
# item = os.path.basename(route) # text.txt
# item = os.path.dirname(route) # /python-total-course/Day 06
# item = os.path.split(route) # ('/python-total-course/Day 06', 'text.txt')

# os.rmdir('/python-total-course/Day 06/test')  # for delete
# print(item)

folder = Path('/Users/hugoroca/personalProjects/python-total-course/Day 06')
file = folder / 'test_1.txt'

my_file = open(file)
print(my_file.read())
