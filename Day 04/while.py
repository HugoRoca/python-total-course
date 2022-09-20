coins = 5

while coins > 0:
    print(f"I have {coins} coins")
    coins -= 1
else:
    print("I dont have more money")

print("##########################")

result = 's'

while result == 's':
    result = input("Continuos? (s/n)")
else:
    print("Thanks")

print("##########################")

result = 's'

while result == 's':
    pass  # for pass to next line

while result == 's':
    break  # for broke the loop

while result == 's':
    continue  # for ignore the current loop and pass the next cycle

print("Hi")
