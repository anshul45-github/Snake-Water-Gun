print("** Calculator **")
print("\n")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n")

print("Select operation:")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

Entered_operation = input("Enter operation (1/2/3/4): ")

if Entered_operation == '1':
    result = num1 + num2
    operation = "Addition"

elif Entered_operation == '2':
    result = num1 - num2
    operation = "Subtraction"

elif Entered_operation == '3':
    result = num1 * num2
    operation = "Multiplication"

elif Entered_operation == '4':
    if num2 != 0:
        result = num1 / num2
        operation = "Division"
    else:
        result = "Error! Division by zero."
        operation = "Division"

else:
    result = "Invalid operation selected."
    operation = "Unknown"

print(f"\nResult of {operation}: {result}")

print("\nThank you for using the calculator!")

print("** End of Calculator **")