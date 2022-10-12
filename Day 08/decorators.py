def decorator_greeting(func):
    def other_func(word):
        print("hola")
        func(word)
        print("bye")

    return other_func


# @decorator_greeting
def upper_text(word):
    print(word.upper())


# @decorator_greeting
def lower_text(word):
    print(word.lower())


upper_decorator = decorator_greeting(upper_text)
upper_decorator('Only word')
upper_text('Only word')

# def change_text(option):
#     def upper_text(text):
#         print(text.upper())
#
#     def lower_text(text):
#         print(text.lower())
#
#     if option == 'upper':
#         return upper_text
#     else:
#         return lower_text
#
#
# operation = change_text('upper')
# operation('word')

# my_function = upper_text
# my_function('python')
#
#
# def a_function(func):
#     return func
#
#
# a_function(upper_text('text'))
