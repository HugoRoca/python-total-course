cond = 10 == 9

if cond:
    print("All good")
else:
    print("Error!")

pet = "dog"
if pet == 'cat':
    print("You have a cat")
elif pet == 'dog':
    print("You have a dog")
elif pet == "fish":
    print("You have a fish")
else:
    print("I don't know what's your pet")

print("###########")
age = 16
note = 9

if age < 18:
    print("You are a child")
    if note >= 7:
        print("Approved")
    else:
        print("Not approved®")
else:
    print("You are an adult")