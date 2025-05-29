
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
    # Ask user how many scores to generate
    try:
        num_scores = int(input("Enter number of scores to generate: "))
    except ValueError:
        print("Invalid number. Exiting program.")
        return

    with open("results.txt", "w") as file:
        for _ in range(num_scores):
            score = random.randint(0, 100)  # Inclusive range
            result = get_result(score)
            file.write(f"{score} is {result}\n")

    print(f"{num_scores} scores written to results.txt.")

main()