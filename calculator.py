def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("That's not a valid number. Please enter a number like 3 or 4.5.")


def main():
    print("Welcome to your Python calculator lesson.")
    print("You will learn how to get input, use variables, and do math.")

    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")

    print("\nHere are the results:")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Cannot divide by zero.")
    print(f"{a} ** {b} = {a ** b}")
    print(f"{a} % {b} = {a % b}")

    print("\nPython data types used here:")
    print("  a is", type(a))
    print("  b is", type(b))
    print("  a converted to string is", type(str(a)))

    print("\nTry editing this file to add more math operations or repeat the calculator.")


if __name__ == "__main__":
    main()
