import math
# ^You need this if you want math functions

x = 9.1
y = 9.9
# print(math.pi)
# ^This is for the value of pi

# print(math.e)
# ^This is for the maths symbol e

result1 = math.sqrt(x)
# ^This is how to square root function

result2 = math.ceil(x)
# This will always round UP a floating point number

result3 = math.floor(y)
# This will always round DOWN a floating point number

# print(result1, result2, result3)


# Exercise 1: Circumference of a Circle (2 * pi * r)

radius1 = float(input("What is the radius of your circle?: "))
circumference = radius1 * 2 * math.pi
print(f"the circumference of your circle is {round(circumference, 2)}cm")

# Exercise 2: Area of a Circle (pi * r^2)

radius2 = float(input("What is the radius of your circle?: "))
area = pow(radius2, 2) * math.pi
print(f"The area of your circle is {round(area, 2)}cm^2")

# Exercise 3: Finding the hypotenuse of a right angle triangle (sqrt (a^2 + b^2))

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a,2) + pow(b, 2))1
print(f"The hypotenuse of your triangle is {round(c, 2)}cm")
