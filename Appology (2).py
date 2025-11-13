import os, time, sys

RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

HEART = [
    "         ***       ***         ",
    "      *******   *******        ",
    "    ************************   ",
    "   **************************  ",
    "  **************************** ",
    "  **************************** ",
    "  **************************** ",
    "   **************************  ",
    "    ************************   ",
    "      ********************     ",
    "        ****************       ",
    "           **********          ",
    "              ****             ",
    "               **              "
]


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def animate_heart():
    name = "MAHANA"
    w = len(HEART[0])
    pos = w // 2 - len(name) // 2

    for beats in range(12):
        clear()
        for i, row in enumerate(HEART):
            color = RED if beats % 2 == 0 else WHITE
            if i == len(HEART) // 2 and beats % 2 == 0:

                line = list(row)
                for j, ch in enumerate(name):
                    if 0 <= pos + j < len(line):
                        line[pos + j] = f"\033[1m{WHITE}{ch}{RESET}{color}"
                print(color + "".join(line) + RESET)
            else:
                print(color + row + RESET)
        sys.stdout.flush()
        time.sleep(0.4)

    clear()
    final_msg = f"{RED}❤ {WHITE} {RED}❤\n{RESET}"
    print(final_msg)
    print("This heart was coded just to say:")
    print(f"{WHITE} I wish you all peace and success.{RESET}")
    print("\n— H.M")


if __name__ == "__main__":
    animate_heart()
