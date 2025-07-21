
name1 = input("Enter your full name: ")
name2 = input("Enter your full name: ")

result1 = len(name1)
# The 'len' function gives the number of characters a string has
result2 = name1.find("d")
# The '.find' function will help to find the first occurence of a given character
result3 = name1.rfind("o")
# The '.rfind' function will help to find the last occurence of a given character
# you can tell its the last occurence because the r stands for retribution
name1 = name1.capitalize()
# This will capitalize the first letter of a string, even if the string contains two words
name2 = name2.upper()
# This will put the entire string in uppercase, there is also a '.lower function' for lowercase
result4 = name2.isdigit()
# this will return 'True' if the input is all digits
result5 = name2.isalpha()
# This will return 'True' if the input is all alphabetical characters, a space is not an alphabetical character


print(result1, result2, result3, name1, name2, result4, result5)

# Exercise 1: Phone numbers

phone_number = input("Enter your phone number: ")
result6 = phone_number.count("-")
# This counts how many of one specific character there is in a string
phone_number = phone_number.replace("-","")

print(result6, phone_number)

# Test 1 validate user input exercise
# 1. Username must not be longer than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

username = input("Enter your username: ")
if len(username) > 12:
    print("Your username is too long! Get out!")
elif not username.find(" ") == -1:
    print("Your username cannot have any spaces! Get out!")
elif not username.isalpha():
    print("Your username cannot have any digits! Get out!")
else:
    print("Your username is valid!")