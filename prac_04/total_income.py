"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


# def main():
# #     """Display income report for incomes over a given number of months."""
# #     incomes = []
# #     months = int(input("How many months? "))
# #
# #     for month in range(1, months + 1):
# #         income = float(input("Enter income for month " + str(month) + ": "))
# #         incomes.append(income)
# #
# #     print("\nIncome Report\n-------------")
# #     total = 0
# #     for month in range(1, months + 1):
# #         income = incomes[month - 1]
# #         total += income
# #         print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
# #
# #
# # main()


"""
CP1404/CP5632 Practical
Refactored code for cumulative total income program
"""


def total_income_report():
    incomes = []
    n = int(input("How many months? "))
    for i in range(1, n + 1):
        incomes.append(float(input(f"Enter income for month {i}: ")))

    print("\nIncome Report\n-------------")
    total = 0
    for i, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {i:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def input_numbers_until_negative():
    numbers = []
    count = 1
    while True:
        num = int(input(f"Number {count}: "))
        if num < 0:
            break
        numbers.append(num)
        count += 1

    if numbers:
        print(f"The first number is {numbers[0]}")
        print(f"The last number is {numbers[-1]}")
        print(f"The smallest number is {min(numbers)}")
        print(f"The largest number is {max(numbers)}")
        print(f"The average of the numbers is {sum(numbers)/len(numbers):.1f}")
    else:
        print("No numbers entered.")


def find_repeated_strings():
    strings = []
    while True:
        s = input("Enter a string (empty to stop): ")
        if not s:
            break
        strings.append(s)

    repeated = {x for x in strings if strings.count(x) > 1}
    if repeated:
        print("Strings repeated:", ", ".join(repeated))
    else:
        print("No repeated strings entered.")


def add_memberwise(list1, list2):
    length = max(len(list1), len(list2))
    return [(list1[i] if i < len(list1) else 0) + (list2[i] if i < len(list2) else 0) for i in range(length)]


def main():
    total_income_report()
    print()
    input_numbers_until_negative()
    print()
    find_repeated_strings()
    print()
    print(add_memberwise([1, 2, 3], [4, 5, 6]))
    print(add_memberwise([1, 2, 3], [1, 2, 3, 4]))


if __name__ == "__main__":
    main()


