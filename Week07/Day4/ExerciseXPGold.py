import random
"""
Exercise 1 : Double Dice
"""


def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    times = 1
    while throw_dice() != throw_dice():
        times += 1
    return times


def main():
    collection = [throw_until_doubles() for _ in range(100)]
    print(f"Total throws: {sum(collection)}")
    print(f"Average throws to reach doubles: {sum(collection)/100}")

main()
