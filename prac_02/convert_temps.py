def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def convert_file(input_file="temps_input.txt", output_file="temps_output.txt"):
    """Read Fahrenheit temps from input_file, convert to Celsius, and write to output_file."""
    try:
        with open(input_file, "r") as infile:
            fahrenheit_values = infile.readlines()

        with open(output_file, "w") as outfile:
            for line in fahrenheit_values:
                try:
                    fahrenheit = float(line.strip())
                    celsius = fahrenheit_to_celsius(fahrenheit)
                    outfile.write(f"{celsius}\n")
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")

        print(f"Converted temperatures written to {output_file}.")

    except FileNotFoundError:
        print(f"File {input_file} not found.")

convert_file()
