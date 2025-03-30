# Define a function to perform mathematical operations
def math_operation(num1, num2, operation):
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
            return "Error: Division by zero is not allowed"
    else:
        return "Error: Invalid operation"

# Main program
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    result = math_operation(num1, num2, operation)
    print(f"The result of {num1} {operation} {num2} is: {result}")

# Call the main function
if __name__ == "__main__":
    main()
    

    