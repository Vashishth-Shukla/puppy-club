import random
import sys

from dog_breed import fetch_bread_character_wiki

DOG_BREEDS = [
    "German Shepard",
    "Labrador Retriever",
    "Greyhound",
    "Cocker Spaniels",
    "Border Collie",
    "Rottweiler",
    "St.Bernard",
    "Siberian Husky",
    "Jack Russell Terrier",
    "Dobermann",
    "Bull Terrier",
    "American Staffordshire Terrier",
    "French Bulldog",
    "Kangal Shepherd Dog",
    "Arabian Greyhound",
    "Irish Wolfhound",
    "Bulldog",
    "Jack Russell Terrier",
    "Dalmatian dog",
    "Cane Corso",
    "Shiba Inu",
]


def print_title(message):
    print()
    print()
    print("#" * 80)
    print("#" + " " * 78 + "#")
    num_of_hash_before_and_after = (
        (80 - len(message)) // 2 - 1 if len(message) < 80 else 0
    )
    print(
        "#"
        + " " * num_of_hash_before_and_after
        + message
        + " " * num_of_hash_before_and_after
        + "#"
    )
    print("#" + " " * 78 + "#")
    print("#" * 80)

    print()
    print()
    print("Type EXIT to any input to exit the game!")
    print()


def exit_function():
    print("Thank you for playing the game. \nSee you later, aligator!")
    sys.exit()


def check_if_exit(inp):
    if inp == "EXIT":
        exit_function()


def print_rules():
    print()
    print("The rules are:")
    print("Blah blah blah\n" * 3)
    print()


def opening_input():
    while True:
        user_input = input("Press 0 to start the game or 1 to know the rules: ")
        check_if_exit(user_input)
        if user_input == "0":
            return user_input
        elif user_input == "1":
            print_rules()
        else:
            print("Please enter 0 or 1 to continue or type EXIT to exit the game!")


def main():
    print_title("Welcome to the PuppyClub")
    opening_screen_selection = opening_input()
    if opening_screen_selection == "0":
        game_control()


if __name__ == "__main__":
    main()
