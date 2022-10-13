# import time
import timeit

def test_for(number):
  new_list = []
  for num in range(1, number + 1):
    new_list.append(num)
  
  return new_list


def test_while(num):
  new_list = []
  count = 1

  while count <= num:
    new_list.append(count)
    count += 1

  return new_list


# start = time.time()
# test_for(1500)
# end = time.time()
# print(end - start)

# start = time.time()
# test_while(1500)
# end = time.time()
# print(end - start)

declarate = """
test_for(100)
"""

setup = """
def test_for(number):
  new_list = []
  for num in range(1, number + 1):
    new_list.append(num)
  
  return new_list
"""

duration = timeit.timeit(declarate, setup, number = 100000)
print(duration)


declarate2 = """
test_while(100)
"""

setup2 = """
def test_while(num):
  new_list = []
  count = 1

  while count <= num:
    new_list.append(count)
    count += 1

  return new_list
"""

duration2 = timeit.timeit(declarate2, setup2, number = 100000)
print(duration2)