"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - A ValueError will occur if the user enters something that is not a valid integer
     (e.g., letters, special characters, or a blank input).

2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError will occur if the user enters 0 as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, by checking if the denominator is zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
