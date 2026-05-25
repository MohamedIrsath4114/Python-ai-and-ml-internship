# Simple Calculator Program

# Function for Addition
def addition(a, b):
    return a + b


# Function for Subtraction
def subtraction(a, b):
    return a - b


# Function for Multiplication
def multiplication(a, b):
    return a * b


# Function for Division
def division(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Main program using while loop
while True:
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Exit condition
    if choice == '5':
        print("Calculator closed successfully!")
        break

    # Check valid choice
    if choice in ['1', '2', '3', '4']:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = addition(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")

        elif choice == '2':
            result = subtraction(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")

        elif choice == '3':
            result = multiplication(num1, num2)
            print(f"Result: {num1} × {num2} = {result}")

        elif choice == '4':
            result = division(num1, num2)
            print(f"Result: {result}")

    else:
        print("Invalid choice! Please select a valid option.")
