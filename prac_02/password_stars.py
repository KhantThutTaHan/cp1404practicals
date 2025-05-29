def main():
    MIN_LENGTH = 8
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

def get_password(MIN_LENGTH):
    while True:
        password = input("Enter a password: ")
        if len(password) < MIN_LENGTH:
            print(f"Password must be at least {MIN_LENGTH} characters long. Please try again.")
        else:
            return password

def print_asterisks(password):
    print("*" * len(password))

if __name__ == "__main__":
    main()

