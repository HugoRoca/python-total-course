from random import choice

words = ['park', 'airplane', 'card', 'person', 'soccer']
incorrect_word = []
correct_word = []
attempts = 6
hits = 0
endGame = False


def choice_word_list(list_words):
    choice_word = choice(list_words)
    unique_letters = len(set(choice_word))

    return choice_word, unique_letters


def ask_letter():
    choice_letter = ''
    is_valid = False
    abc = 'abcdefghijklmnopqrstuvxyzñ'

    while not is_valid:
        choice_letter = input("Choice a word: ").lower()
        if choice_letter in abc and len(choice_letter) == 1:
            is_valid = True
        else:
            print("Enter a correct letter!!")

    return choice_letter


def show_new_table(choice_word):
    hide_list = []

    for letter in choice_word:
        if letter in correct_word:
            hide_list.append(letter)
        else:
            hide_list.append('_')

    print(' '.join(hide_list))


def verify_letter(choice_letter, hide_word, lives, match):
    end = False

    if choice_letter in hide_word and choice_letter not in correct_word:
        correct_word.append(choice_letter)
        match += 1
    elif choice_letter in hide_word and choice_letter in correct_word:
        print("The letter exists, try again!")
    else:
        incorrect_word.append(choice_letter)
        lives -= 1

    if lives == 0:
        end = lose()
    elif match == unique_letter:
        end = win(hide_word)

    return lives, end, match


def lose():
    print("You don't have lives! YOU LOSE")
    print("The hide word was", word)

    return True


def win(hide_word):
    show_new_table(hide_word)
    print("YOU WIN!!")

    return True


word, unique_letter = choice_word_list(words)

while not endGame:
    print('\n' + '*' * 20 + '\n')
    show_new_table(word)
    print('\n')
    print('Incorrect letters:', ' '.join(incorrect_word))
    print('Lives', attempts)
    print('\n' + '*' * 20 + '\n')
    letter = ask_letter()
    attempts, endGame, hits = verify_letter(letter, word, attempts, hits)