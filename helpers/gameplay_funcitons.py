import random

from helpers.colors import BLUE, GREEN, PURPLE, RED, RESET, YELLOW
from helpers.dog_breeds import DOG_BREEDS


def _choose_breed():
    """Randomly selects a breed from the list."""
    return random.choice(DOG_BREEDS)


def _display_word(breed, guesses):
    """Displays the current state of the guessed breed, with spaces and underscores."""
    return " ".join(
        [
            letter if letter.lower() in guesses or letter == " " else "_"
            for letter in breed
        ]
    )


def _get_user_guess(guessed_letters):
    """Asks the user to type in a letter, making sure it's a valid single letter."""
    while True:
        guess = input(f"{GREEN}Please enter a letter: {RESET}").lower()

        if (not guess.isalpha() or len(guess) != 1) or guess == ".":
            print(f"{RED}INVALID ENTRY!\nPlease enter a single letter.{RESET}")
        elif guess in guessed_letters:
            print(f"{PURPLE}You already guessed that letter.{RESET}")
        else:
            return guess


# def _print_title():
#     print(
#         f"\n{YELLOW}{'☆' * 10}{RESET} WELCOME TO GUESS MY BREED!{YELLOW} {'☆' * 10}{RESET}\n"
#     )
#     print(f"{YELLOW}Try to guess the dog breed!{RESET}")


def _print_title(message="WELCOME TO GUESS MY BREED"):
    print(YELLOW)
    print()
    print("☆" * 80)
    print("☆" + " " * 78 + "☆")
    num_of_hash_before_and_after = (
        (80 - len(message)) // 2 - 1 if len(message) < 80 else 0
    )
    print(
        "☆"
        + " " * num_of_hash_before_and_after
        + RESET
        + message
        + " "
        + YELLOW
        + " " * num_of_hash_before_and_after
        + "☆"
    )
    print("☆" + " " * 78 + "☆")
    print("☆" * 80)

    print()
    print(RESET)
    # print("Type EXIT to any input to exit the game!")
    # print()
