import os
from pathlib import Path
from os import system, makedirs

name_folder_base = "Recipes"


def select_and_return_option(data):
    print(f"[x] - return main")
    option = input("Enter an option: ")
    if option.upper() == 'X':
        return ''

    while not option.isnumeric() or int(option) not in range(1, len(data) + 1):
        print("Invalid option!")
        option = input("Enter an option: ")
        if option.upper() == 'X':
            return ''

    return data[int(option) - 1]


def welcome_window():
    system('clear')
    print("  ____               _             _       ")
    print(" |  _ \\ ___  ___ ___| |_ __ _ _ __(_) ___  ")
    print(" | |_) / _ \\/ __/ _ \\ __/ _` | '__| |/ _ \\ ")
    print(" |  _ <  __/ (_|  __/ || (_| | |  | | (_) |")
    print(" |_| \\_\\___|\\___\\___|\\__\\__,_|_|  |_|\\___/ ")
    print("                                           ")

    route = Path.home() / name_folder_base
    print("Route: ", route)

    route = Path(name_folder_base)
    count = 0

    for txt in Path(route).glob("**/*.txt"):
        count += 1

    print("Exist", count, "recipes")
    print("[1] - Read recipe")
    print("[2] - Create recipe")
    print("[3] - Create category")
    print("[4] - Delete recipe")
    print("[5] - Delete category")
    print("[6] - End program")

    option = input("Enter a option: ")

    while not option.isnumeric() or int(option) not in range(1, 7):
        print("Invalid option!")
        option = input("Enter an option: ")

    return int(option)


def list_and_choice_category_window():
    system('clear')
    route = Path(name_folder_base)
    count = 1
    categories = []

    print("List of categories: ")
    for folder in route.iterdir():
        if folder.name != '.DS_Store':
            print(f"[{count}] - {folder.name}")
            categories.append(folder)
            count += 1

    return select_and_return_option(categories)


def list_recipes_window(route):
    if route == '':
        return ''

    system('clear')
    count = 1
    recipes = []
    for txt in Path(route).glob("**/*.txt"):
        print(f"[{count}] - {txt.name}")
        count += 1
        recipes.append(txt)

    return select_and_return_option(recipes)


def read_file(route):
    if route == '':
        return ''

    system('clear')
    file = open(route)
    print(file.read())
    input("\nPress any keyboard for return...")
    file.close()


def create_recipe(route):
    route_new_file = ""
    validate = False
    while not validate:
        name_new_file = input("Enter the new name of file: ")
        route_new_file = Path(route, name_new_file + ".txt")
        if name_new_file != '' and os.path.exists(route_new_file):
            print("Exist file, try again")
        else:
            validate = True

    content = input("Enter the content of file: ")
    Path.write_text(route_new_file, content)
    print("File create successfully!")


def create_folder():
    route_new_folder = ''
    validate = False

    while not validate:
        name_folder = input("Enter the name folder: ")
        route_new_folder = Path(name_folder_base, name_folder)
        if name_folder != '' and os.path.exists(route_new_folder):
            print("Exist file, try again")
        else:
            validate = True

    Path.mkdir(route_new_folder)
    print("Folder create successfully!")


def delete_file(route):
    option = input("You sure? y/n")
    validate = False

    while not validate:
        if option.upper() in ['Y', 'N']:
            validate = True
        else:
            print("Invalid option, try again!")
            option = input("You sure? y/n")

    Path.rmdir(route)
    print("Delete successfully!")


end_program = False

while not end_program:
    choice = int(welcome_window())

    match choice:
        case 1:
            category_route = list_and_choice_category_window()
            recipe_route = list_recipes_window(category_route)
            read_file(recipe_route)
        case 2:
            category_route = list_and_choice_category_window()
            create_recipe(category_route)
        case 3:
            create_folder()
        case 4:
            category_route = list_and_choice_category_window()
            recipe_route = list_recipes_window(category_route)
            delete_file(recipe_route)
        case 5:
            category_route = list_and_choice_category_window()
            delete_file(category_route)
        case 6:
            print("Bye!!")
            end_program = True
