import random


DICE_COUNT = 2
TOTAL_ROLL_COUNT = 1_000_000


def roll_dice() -> int:
    return random.randint(1, 6)


def print_roll_stats(roll2count: dict[int, int]) -> None:
    total = sum(roll2count.values())
    for roll, count in roll2count.items():
        percent = count / total * 100
        print(f"{roll:-2}: {percent:-8.1f} %")


def main() -> None:
    roll2count: dict[int, int] = {}
    min_dice = 1 * DICE_COUNT
    max_dice = 6 * DICE_COUNT
    for i in range(min_dice, max_dice+1):
        roll2count[i] = 0
    for _ in range(TOTAL_ROLL_COUNT):
        roll = sum([roll_dice() for _ in range(DICE_COUNT)])
        roll2count[roll] += 1
    print_roll_stats(roll2count)


if __name__ == '__main__':
    main()

