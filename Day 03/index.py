text = "This is a test"
# in negative, start from right text[-2]
# result = text.index('test', 1, 9)
result = text.rindex('t')
print(result)