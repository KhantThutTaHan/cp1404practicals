import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    quick_picks = int(input("How many quick picks? "))

    for _ in range(quick_picks):
        numbers = generate_unique_numbers(NUMBERS_PER_PICK, MIN_NUMBER, MAX_NUMBER)
        numbers.sort()
        print_numbers(numbers)


def generate_unique_numbers(count, min_num, max_num):
    """Generate a list of unique random numbers (without using random.sample)."""
    numbers = []
    while len(numbers) < count:
        num = random.randint(min_num, max_num)
        if num not in numbers:
            numbers.append(num)
    return numbers


def print_numbers(numbers):
    """Print numbers in a line, each number right-aligned in width 2."""
    print(" ".join(f"{num:2}" for num in numbers))


main()
