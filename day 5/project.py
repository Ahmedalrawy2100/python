# Welcome Message

print("Welcome to Movie Recommendation System")


# Menu

menu = [
    "Get Recommendation",
    "About Program",
    "Exit"
]


# Functions

def show_menu():
    i = 1

    for choice in menu:
        print(f"{i}-{choice}")
        i += 1


def get_name():
    name = input("What's your name? ")
    return name


def get_age():
    while True:
        age = int(input("How old are you? "))

        if age > 0:
            return age

        print("Please enter a valid age.")


def get_category():

    print("\nChoose your favorite category:")
    print("1- Action")
    print("2- Horror")
    print("3- Comedy")
    print("4- Technology")

    category = input("Choose a category: ")

    return category


def show_recommendation(name, age, category):

    print(f"\nHello {name}")
    print("We recommend:\n")

    if category == "1":
        print("John Wick")
        print("Mission Impossible")
        print("The Matrix")

    elif category == "2":

        if age < 16:
            print("Sorry! Horror movies are for +16 only.")

        else:
            print("Halloween")
            print("Friday the 13th")
            print("A Nightmare on Elm Street")

    elif category == "3":
        print("Mr. Bean's Holiday")
        print("Home Alone")
        print("The Mask")

    elif category == "4":
        print("The Social Network")
        print("Steve Jobs")
        print("Mr. Robot")

    else:
        print("Invalid Category.")

    print("\nEnjoy Watching.")


def about_program():
    print("\nThis program recommends movies")
    print("based on your age and favorite category.")


# Main Program

while True:

    show_menu()

    num_choose = input("\nEnter your choice: ")

    if num_choose == "1":

        name = get_name()
        age = get_age()
        category = get_category()

        show_recommendation(name, age, category)

    elif num_choose == "2":
        about_program()

    elif num_choose == "3":
        print("Goodbye Ahmed.")
        break

    else:
        print("Invalid Choice.")

    print()