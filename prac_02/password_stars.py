# Set the minimum password length
MIN_LENGTH = 8

# Ask the user for a password, with error-checking
while True:
    password = input("Enter a password: ")
    if len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long. Please try again.")
    else:
        break

# Print asterisks equal to the length
