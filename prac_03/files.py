# ------------------------------
# 1. Ask user for name and write it to name.txt using open() and close()
# ------------------------------
name = input("Enter your name: ")
out_file = open("name.txt", 'w')
out_file.write(name)
out_file.close()

# ------------------------------
# 2. Read name from name.txt and print a greeting using open() and close()
# ------------------------------
in_file = open("name.txt", 'r')
name_from_file = in_file.read()
in_file.close()
print(f"Hi {name_from_file}!")

# ------------------------------
# 3. Read first two numbers from numbers.txt, add them, print the result
# Use with statement and readlines()
# ------------------------------
with open("numbers.txt", 'r') as in_file:
    lines = in_file.readlines()
    number1 = int(lines[0])
    number2 = int(lines[1])
    print(number1 + number2)  # Should print 59

# ------------------------------
# 4. Read all numbers from numbers.txt and print their total
# Use with statement and for loop
# ------------------------------
total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        total += int(line)
print(total)
