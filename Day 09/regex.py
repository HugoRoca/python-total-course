import re

text = "Si necesitas ayuda llama al (321) 555-1234 o al (321) 555-4321 las 24 horas al servicio al cliente."

pattern = "si"

search = re.search(pattern, text)

print(search) # this return object re.Match
print(search.span()) # this return tuple with start and end position
print(search.end()) # this return end position

find = re.findall(pattern, text) # this return list with all matches

for match in find:
    print(match) # this return all matches


# --------------------------------------------
otherText = "Lorem ipsum 564-654-9875 right now!"
otherPattern = r"\d{3}-\d{3}-\d{4}"

result = re.search(otherPattern, otherText)
print(result) # this return object re.Match
print(result.group()) # this return match
print(result.group(2)) # this return group with index 2


# --------------------------------------------
password = input("Enter your password: ")
pattern = r'\D{1}\w{7}'
valid = re.search(pattern, password)
print(valid) # this return object re.Match

# --------------------------------------------
text = "Is closed on Monday and Tuesday"
search = re.search(r"monday|tuesday", text)
print(search) # this return object re.Match

pattern = r'[^\s]+]' # similar to split(" ")