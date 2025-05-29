"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)

    # Generate and test a random score
    random_score = random.uniform(0, 100)
    random_result = get_result(random_score)
    print(f"Random score: {random_score:.2f} - Result: {random_result}")

main()







