import os
import shutil
import send2trash

print(os.getcwd())

# file = open('course.txt', 'w')
# file.write('text of test')
# file.close()

print(os.listdir())

#########################
# shutil.move('Course.txt', '/users/hugoroca/Desktop')
# shutil.rmtree()

#send2trash.send2trash('ruta')

route = '/Users/hugoroca/personalProjects/python-total-course'

for folder, subfolder, file in os.walk(route):
    print(f'In folder {folder}')
    print(f'Subfolders are: ')

    for sub in subfolder:
        print(f'\t{sub}')

    for fil in file:
        print(f'\t{fil}')

    print('\n')
