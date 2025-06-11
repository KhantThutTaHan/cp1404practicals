"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


# def main():
#     """Read and display student scores from scores file."""
#     scores_file = open("scores.csv")
#     scores_data = scores_file.readlines()
#     print(scores_data)
#     subjects = scores_data[0].strip().split(",")
#     score_values = []
#     for score_line in scores_data[1:]:
#         score_strings = score_line.strip().split(",")
#         score_numbers = [int(value) for value in score_strings]
#         score_values.append(score_numbers)
#     scores_file.close()
#     for i in range(len(subjects)):
#         print(subjects[i], "Scores:")
#         for score in score_values[i]:
#             print(score)
#         print("Max:", max(score_values[i]))
#         print()
#
#
# main()


def read_scores(filename="scores.csv"):
    with open(filename) as file:
        lines = file.readlines()

    subjects = lines[0].strip().split(",")
    # Convert each student's scores to integers
    scores_by_student = [
        [int(x) for x in line.strip().split(",")] for line in lines[1:]
    ]

    # Transpose to get scores per subject
    scores_per_subject = list(zip(*scores_by_student))
    return subjects, scores_per_subject


def print_report(subjects, scores_per_subject):
    print(f"{'Subject':10} {'Min':>3} {'Max':>3} {'Avg':>5} Scores")
    print("-" * 40)
    for i, subject in enumerate(subjects):
        scores = scores_per_subject[i]
        minimum = min(scores)
        maximum = max(scores)
        average = sum(scores) / len(scores)
        print(f"{subject:10} {minimum:3} {maximum:3} {average:5.2f} {scores}")


def is_valid_format(s):
    for ch in s.lower():
        if ch not in ('c', 'v'):
            return False
    return True


def get_word_format():
    while True:
        fmt = input("Enter word format (c and v only): ")
        if is_valid_format(fmt):
            print("Valid format:", fmt)
            break
        else:
            print("Invalid format, try again.")


def main():
    subjects, scores = read_scores()
    print_report(subjects, scores)

    print("\nWord format checker")
    get_word_format()


if __name__ == "__main__":
    main()

