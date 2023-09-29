# Define a function to perform basic arithmetic operations
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed."
    else:
        return "Invalid operation"

# Main program
while True:
    try:
        # Prompt the user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        # Calculate and display the result
        result = calculate(num1, num2, operation)
        print(f"Result: {result}")

        # Ask if the user wants to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != "yes":
            break
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
