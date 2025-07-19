# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Destro Metro"
age = 25
gpa = 2.2
is_student = False

name = bool(name)

print(name)
print(type(name))

# This can be useful when you ask a user to enter some information, as it prints "False" if no name is entered

age = float(age)
print (age)
print (type(age))

# This makes the integer a decimal number

gpa = int(gpa)
print (gpa)
print (type(gpa))

# This makes a float an integer by truncating the decimal values

is_student = str(is_student)
print (is_student)
print(type(is_student))

# This makes the boolean a string


