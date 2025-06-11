# numbers = [3, 1, 4, 1, 5, 9, 2]

numbers = [3, 1, 4, 1, 5, 9, 2]

# === Predictions (without running the code) ===
# numbers[0] → 3
# numbers[-1] → 2
# numbers[3] → 1
# numbers[:-1] → [3, 1, 4, 1, 5, 9]
# numbers[3:4] → [1]
# 5 in numbers → True
# 7 in numbers → False
# "3" in numbers → False  (string not equal to integer)
# numbers + [6, 5, 3] → [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# === Run the code to check values ===
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

# === List modifications ===
numbers[0] = "ten"     # Change first element to "ten"
numbers[-1] = 1        # Change last element to 1

# === Print slice and check membership ===
print(numbers[2:])     # All elements except the first two
print(9 in numbers)    # Check if 9 is in the list
