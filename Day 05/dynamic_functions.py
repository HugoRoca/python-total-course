def verify_1(number):
    return number in range(100, 1000)


plus = 586 + 402
result = verify_1(plus)
print(result)
print("#################")


def verify_2(myList):
    for n in myList:
        if n in range(100, 1000):
            return True
        else:
            pass

    return False


result = verify_2([50, 100, 999])
print(result)
print("#################")

def verify_3(myList):
    newList = []
    for n in myList:
        if n in range(100, 1000):
            newList.append(n)
        else:
            pass

    return newList


result = verify_3([50, 100, 999])
print(result)
