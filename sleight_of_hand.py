from collections import Counter
from typing import Dict


def sleight_of_hand(num_buttons: int, keyboard: Dict[int, int]) -> int:
    max_points: int = 0

    for butt_val in keyboard.values():
        if butt_val <= 2 * num_buttons:
            max_points += 1

    return max_points


def main():
    num_buttons = int(input())
    keyboard = Counter(
        int(button) for _ in range(4) for button in input() if button != "."
        )
    print(sleight_of_hand(num_buttons, keyboard))


if __name__ == '__main__':
    main()
