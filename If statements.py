# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("What is your age?: "))

if age >= 100:
    print("Wow you are way too old to sign up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You do not exist!")
else:
    print("You cannot sign up, you must be 18+! Get out!")
# The code following an if or else must be indented
# Also if an 'if' statement is true, then the rest of the code is ignored


response = input("Would you like food?: (Y/N)")
if response == "Y":
# For comparisons, use double equals, because a single equal is assigning something to another thing
    print("Here is a chocolate vanilla swirl with cookie crunch, please enjoy!")
else:
    print("I guess you won't be getting a chocolate vanilla swirl with cookie crunch, please leave.")


name = input("What is your name?: ")
if name == "":
    print("You didn't enter a name stupid!")
else:
    print(f"Hello, {name}!")


for_sale = True
if for_sale:
    print("This item is for sale!")
else:
    print("This item is NOT for sale!")

# Booleans can be used in this way for 'if' statements like this

