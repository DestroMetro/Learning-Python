# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you?: "))

age = age + 1

print(f"Hello {name}!")
print("Happy birthday!")
print(f"You are {age} years old.")

# First test: Calculating the area of a rectangle

Length = float(input("What is the length of your rectangle?"))
Width = float(input("What is the width of your rectangle"))
Area = Length * Width
print(f"The area of your rectangle is {Area}")

# Second test Shopping Cart Program

item = input("What item are you buying?: ")
price = float(input("What is the price of your item?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity}x {item}/s")
print(f"Your total is: ${total}")




