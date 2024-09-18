## \033[<style>;<foreground>;<background>m


def show_ascii_dog():
    print(
        "\033[1;92;92m"
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
        + "\033[0m"
    )


def main():
    show_ascii_dog()


if __name__ == "__main__":
    main()
