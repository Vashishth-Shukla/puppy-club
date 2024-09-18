from helpers.colors import BOLD_GREEN, RESET


def show_ascii_dog():
    print(
        BOLD_GREEN
        + r"""
       /^-^\         /^-----^\
      / o o \        V  o o  V
     /   Y   \        |  Y  |
     V \ v / V         \ Q /
       / - \           / - \
      /    |           |    \
(    /     |           |     \     )
 ===/___) ||           || (___\====
"""
        + RESET
    )


def main():
    show_ascii_dog()


if __name__ == "__main__":
    main()
