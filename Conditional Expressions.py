# Conditional expression = A one-line shortcut for the if-else statement(ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y (Formula)
from ctypes import HRESULT

num1 = 5
print("Positive." if num1 > 0 else "Negative.")


num2 = 3
Result = "Even" if num2 % 2 == 0 else "Odd"

print(Result)

a = 9
b = 7

max_num = a if a > b else b
min_num = a if a < b else b

print(max_num)
print(min_num)

age = 17

status = "Adult" if age >= 18 else "Child"
print(status)

tempurature = 10

weather = "HOT" if tempurature >= 20 else "COLD"
print(weather)

user_role = "not admin"
access = "Full access granted." if user_role == "admin" else "Limited access."
print(access)