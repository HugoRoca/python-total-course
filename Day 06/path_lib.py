from pathlib import Path, PureWindowsPath

folder = Path('/Users/hugoroca/personalProjects/python-total-course/Day 06')
file = folder / 'test_1.txt'

print(file.suffix)
if not file.exists():
    print("This file don't exists")
else:
    print(file.read_text())