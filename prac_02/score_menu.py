def get_valid_score():
    """Prompt user until a valid score (0–100 inclusive) is entered."""
    while True:
        try:
            score = float(input("Enter score (0–100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_result(score):
    """Return the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print as many stars as the score."""
    print('*' * int(score))


def print_menu():
    """Print the menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def main():
    print("Welcome to the score program!")
    score = get_valid_score()  # Ensure we start with a valid score

    while True:
        print_menu()
        choice = input(">>> ").strip().upper()

        if choice == 'G':
            score = get_valid_score()

        elif choice == 'P':
            result = get_result(score)
            print(f"Result: {result}")

        elif choice == 'S':
            show_stars(score)

        elif choice == 'Q':
            print("Farewell!")
            break

        else:
            print("Invalid option. Please choose from the menu.")

main()

# For Testing
#
# Choose P before G — it should print the result of the original score.
# Choose G to enter a new score.
# Choose S to see a line of stars.
# Enter invalid menu choices to check error handling.
# Quit using Q to see the farewell message.