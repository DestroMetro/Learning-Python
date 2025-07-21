# Logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temp1 = 0
is_raining = True

if temp1 > 35 or temp1 < 0 or is_raining:
    print("The outdoor event is cancelled! Get in!")
else:
    print("The outdoor event is still scheduled, get out!")

# Part 2

temp2 = 100
is_sunny = True

if temp2 >= 28 and is_sunny:
    print("It is HOT outside!")
    print("It is SUNNY!")
elif temp2 <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 0 < temp2 < 28 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY!")
elif temp2 >= 28 and not is_sunny:
    print("It is HOT outside!")
    print("It is CLOUDY!")
elif temp2 <= 0 and not is_sunny:
   print("It is COLD outside")
   print("It is CLOUDY")
elif 0 < temp2 < 28 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY!")