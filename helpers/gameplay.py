import textwrap

from helpers.colors import BLUE, GREEN, PURPLE, RED, RESET, YELLOW
from helpers.gameplay_funcitons import (
    _choose_breed,
    _display_word,
    _get_user_guess,
    _print_title,
)
from helpers.preview_image import delete_image, preview_image
from helpers.show_ascii_dog import show_ascii_dog
from helpers.url_and_description import url_and_description


def play_game():
    """Handles the gameplay loop for guessing the breed."""
    word = _choose_breed()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    _initialize_game(word)

    while incorrect_guesses < max_incorrect:
        _display_game_status(word, guessed_letters, incorrect_guesses, max_incorrect)
        guess = _get_user_guess(guessed_letters)

        if _is_correct_guess(guess, word):
            guessed_letters.add(guess)
            _handle_correct_guess(guess)
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            _handle_incorrect_guess(guess)

        if _is_word_guessed(word, guessed_letters):
            _handle_game_won(word)
            break
    else:
        delete_image()
        _handle_game_lost(word)


def ask_to_play_again():
    """Asks the user if they want to play again."""
    play_again = input(
        f"\n{GREEN}Press Enter ⮐ to play again or type 'q' to quit: {RESET}"
    ).lower()
    return play_again != "q"


def _initialize_game(word):
    """Initializes the game by printing the title, showing ASCII dog art, and displaying breed image."""
    _print_title()
    show_ascii_dog()
    print()
    print(PURPLE + "LET THE GAME BEGIN!" + RESET)
    print()
    input("Press Enter ⮐ to get the first clue...")
    print()

    img_url, summary = url_and_description(word)

    summary = summary.replace(word, "'--funny little puddle--'")
    print(YELLOW + "Description of the breed: " + RESET)
    print(textwrap.fill(summary, width=75))
    print()
    input("Press Enter ⮐ to get the second clue...")
    preview_image(img_url)
    print()
    print(YELLOW + "Now, guess the breed: " + RESET)


def _display_game_status(word, guessed_letters, incorrect_guesses, max_incorrect):
    """Displays the current state of the game: guessed letters and remaining guesses."""
    print(_display_word(word, guessed_letters))
    print(f"\nYou have {PURPLE}{max_incorrect - incorrect_guesses}{RESET} guesses left")


def _is_correct_guess(guess, word):
    """Checks if the guessed letter is in the word."""
    return guess in word.lower()


def _handle_correct_guess(guess):
    """Handles correct guesses by giving feedback."""
    print(
        f"{YELLOW}GREAT GUESS!{RESET}\n{guess.upper()} {YELLOW}is in the name of the breed.{RESET}"
    )


def _handle_incorrect_guess(guess):
    """Handles incorrect guesses by giving feedback."""
    print(
        f"{RED}WRONG GUESS!{RESET}\n{guess.upper()} {RED}is not in the name of the breed.{RESET}"
    )


def _is_word_guessed(word, guessed_letters):
    """Checks if the entire word has been guessed."""
    return all(letter.lower() in guessed_letters or letter == " " for letter in word)


def _handle_game_won(word):
    """Handles the case where the player has successfully guessed the word."""
    print(
        f"\n{BLUE}{'☆' * 10}{RESET} CONGRATULATIONS! {BLUE}{'☆' * 10}{RESET}\n"
        f"You guessed the breed: {BLUE}{word}{RESET}"
    )


def _handle_game_lost(word):
    """Handles the case where the player has run out of guesses."""
    print(
        f"{RED}☹︎ SORRY, YOU RAN OUT OF GUESSES!{RESET}\nThe breed was: {YELLOW}{word}{RESET}"
    )
