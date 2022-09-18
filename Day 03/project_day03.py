inputText = input("Enter text: ").lower()
letters = []
letters.append(input("Enter first letter: ").lower())
letters.append(input("Enter second letter: ").lower())
letters.append(input("Enter thirty letter: ").lower())
print("--------------")
countLetterOne = inputText.count(letters[0])
countLetterTwo = inputText.count(letters[1])
countLetterThree = inputText.count(letters[2])
print(f"Letter: {letters[0]}, there is {countLetterOne}")
print(f"Letter: {letters[1]}, there is {countLetterTwo}")
print(f"Letter: {letters[2]}, there is {countLetterThree}")
print("--------------")
words = inputText.split(" ")
print(f"There is {len(words)} words")
print("--------------")
letterStar = inputText[0]
letterEnd = inputText[-1]
print(f"Letter start {letterStar}, letter end {letterEnd}")
print("--------------")
words.reverse()
wordsReverse = ' '.join(words)
print("Reverse text: ", wordsReverse)
print("--------------")
findPython = 'pytho' in inputText
dic = { True: 'exists', False: 'no exists'}

print(f"The word 'pyton' {dic[findPython]}")