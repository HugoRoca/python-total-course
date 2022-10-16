# import zipfile
import shutil

# my_zip = zipfile.ZipFile('compress_file.zip', 'w')
# my_zip.write('mi_texto_A.txt')
# my_zip.write('mi_texto_B.txt')
# my_zip.close()

# # For extract
# my_zip = zipfile.ZipFile('compress_file.zip', 'r')
# my_zip.extractall()


import shutil

shutil.unpack_archive('project_day_09.zip', 'route/dest')