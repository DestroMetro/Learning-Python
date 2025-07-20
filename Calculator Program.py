# Python Calculator

operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

if operator == "+":
    result = num1 + num2
    print(f"Your number is {result}!")
elif operator == "*":
    result = num1 * num2
    print(f"Your number is {result}!")
elif operator == "-":
    result = num1 - num2
    print(f"Your number is {result}!")
elif operator == "/":
    result = num1 / num2
    print(f"Your number is {result}!")
else:
    print(f"{operator} is an invalid operator, get out!")

