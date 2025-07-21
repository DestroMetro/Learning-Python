
unit1 = (input("Enter tempurature unit, Celcius, Fahrenheit (C/F): "))
temp = float(input("Enter your tempurature: "))

if unit1 == "C":
    temp = round((temp * 9) / 5 + 32 , 1)
    print(f"Your tempurature is, {temp}°F)")
elif unit1 == "F":
    temp = round((temp - 32) * 5/9, 1)
    print(f"Your tempurature is, {temp}°C)")
else:
    print(f"{unit} is not a valid unit of measurement")

# Exercise 1: Pennies to Pounds

unit2 = (input("Pennies to Pounds or Pounds to Pennies? (A/B): "))
total = int(input("Enter your total: "))
if unit2 == "A":
    total = total / 100
    print(f"Your total is, £{total}.")
elif unit2 == "B":
    total = total * 100
    print(f"Your total is, {total}p.")
else:
    print(f"{unit2} is not an option!")


