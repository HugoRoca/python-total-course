from random import shuffle

myList = ['-', '--', '---', '----']


# Mix list
def mixed(param):
    shuffle(param)
    return param


# ask try
def testLucky():
    attempt = ''

    while attempt not in ['1', '2', '3', '4']:
        attempt = input('Choice a number between 1 and 4: ')

    return int(attempt)


def verifyAttempt(listParam, attempt):
    if listParam[attempt - 1] == '-':
        print("You have to wash the dishes!")
    else:
        print("You are safe!")

    print(f"You have {listParam[attempt - 1]}")


mix = mixed(myList)
attempt = testLucky()
verifyAttempt(mix, attempt)
