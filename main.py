from helpers.colors import PURPLE, RESET
from helpers.gameplay import ask_to_play_again, play_game


def main():
    """Main function to run the game and handle replay."""
    while True:
        play_game()
        if not ask_to_play_again():
            print(f"{PURPLE}Thanks for playing!{RESET}")
            break


if __name__ == "__main__":
    main()
