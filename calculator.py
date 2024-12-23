# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."

# Main function to run the calculator
def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Get user input for operation
        choice = input("Enter choice (1/2/3/4/5): ")

        # Exit condition
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Validate the operation choice
        if choice not in ('1', '2', '3', '4'):
            print("Invalid Input! Please choose a valid operation (1, 2, 3, or 4).")
            continue

        # Get user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numerical values.")
            continue  # Prompt for numbers again if invalid

        # Perform the chosen operation
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()
