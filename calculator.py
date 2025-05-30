print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
print("Welcome to the calculator!")
print("Available operations: +, -, *, /, celsius_to_fahrenheit(c2f)")
operation = input("Enter the operation you want to perform: ")  
if operation in ['+', '-', '*', '/']:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    print(f"The result of {num1} {operation} {num2} is: {result}")
elif operation == 'celsius_to_fahrenheit' or 'c2f':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}")
else:
    print("Invalid operation. Please try again.")