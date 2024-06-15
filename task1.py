def calculator():
    # Prompt user for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Display operation choices
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    # Prompt user for operation choice
    operation = input("Enter the number of the operation you want to perform (1/2/3/4): ")

    # Perform the selected operation
    if operation == '1':
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice. Please select a valid operation.")

# Run the calculator function
if __name__ == "__main__":
    calculator()
