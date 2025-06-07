import random

def create_temp_file(filename="temps_input.txt", count=10):
    with open(filename, "w") as file:
        for _ in range(count):
            temp = round(random.uniform(-200, 200), 2)
            file.write(f"{temp}\n")
    print(f"{count} temperatures written to {filename}.")

create_temp_file()
