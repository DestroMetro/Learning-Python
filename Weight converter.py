# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Is this weight in kilograms or pounds (K/L)")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight, 3)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 3)} {unit}")
else:
    print(f"{unit} is not valid")