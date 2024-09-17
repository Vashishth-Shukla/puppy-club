import random

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
RESET = "\033[0m"


dog_breeds = [
    "German Shepherd",
    "Labrador Retriever",
    "Greyhound",
    "Cocker Spaniel",
    "Border Collie",
    "Rottweiler",
    "St.Bernard",
    "Siberian Husky",
    "Jack Russell Terrier",
    "Dobermann",
    "Bullterrier",
    "American Staffordshire Terrier",
    "French Bulldog",
    "Kangal Shepherd",
    "Arabian Greyhound",
    "Irish Wolfhound",
    "Bulldog",
    "Jack Russell Terrier",
    "Dalmatian",
    "Cane Corso",
    "Shiba Inu",
]


def choose_breed():
    """Randomly selects a breed from the list."""
    return random.choice(dog_breeds)


def display_word(breed, guesses):
    """Displays the current state of the guessed breed, with spaces and underscores."""
    return " ".join(
        [
            letter if letter.lower() in guesses or letter == " " else "_"
            for letter in breed
        ]
    )


def get_user_guess(guessed_letters):
    """Asks the user to type in a letter, making sure it's a valid single letter."""
    while True:
        guess = input(f"{GREEN}Please enter a letter: {RESET}").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(f"{RED}INVALID ENTRY!\nPlease enter a single letter.{RESET}")
        elif guess in guessed_letters:
            print(f"{PURPLE}You already guessed that letter.{RESET}")
        else:
            return guess


def play_game():
    """Handles the gameplay loop for guessing the breed."""
    word = choose_breed()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print(
        f"\n{YELLOW}{'☆' * 10}{RESET} WELCOME TO GUESS MY BREED!{YELLOW} {'☆' * 10}{RESET}\n"
    )
    print(f"{YELLOW}Try to guess the dog breed!{RESET}")

    while incorrect_guesses < max_incorrect:
        # Displays the added letters in the word(breed) as it is being guessed
        print(display_word(word, guessed_letters))
        print(
            f"\nYou have {PURPLE}{max_incorrect - incorrect_guesses}{RESET} guesses left"
        )

        guess = get_user_guess(guessed_letters)

        if guess in word.lower():
            guessed_letters.add(guess)
            print(
                f"{YELLOW}GREAT GUESS!{RESET}\n{guess.upper()} {YELLOW}is in the name of the breed.{RESET}"
            )
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(
                f"{RED}WRONG GUESS!{RESET}\n{guess.upper()} {RED}is not in the name of the breed.{RESET}"
            )

        if all(letter.lower() in guessed_letters or letter == " " for letter in word):
            print(
                f"\n{BLUE}{'☆' * 10}{RESET} CONGRATULATIONS! {BLUE}{'☆' * 10}{RESET}\n"
                f"You guessed the breed: {BLUE}{word}{RESET}"
            )
            break
    else:
        print(
            f"{RED}☹︎ SORRY, YOU RAN OUT OF GUESSES!{RESET}\nThe breed was: {YELLOW}{word}{RESET}"
        )


def ask_to_play_again():
    """Asks the user if they want to play again."""
    play_again = input(
        f"\n{GREEN}Press Enter ⮐ to play again or type 'n' to quit: {RESET}"
    ).lower()
    return play_again != "n"


def main():
    """Main function to run the game and handle replay."""
    while True:
        play_game()
        if not ask_to_play_again():
            print(f"{PURPLE}Thanks for playing!{RESET}")
            break


if __name__ == "__main__":
    main()
