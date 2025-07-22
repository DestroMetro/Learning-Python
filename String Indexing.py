# indexing = accessing elements of a sequence [] (indexing operator)
#            [start : end : step]
#            [1:x     x:1   ::1 ]

credit_number = "1234-5678-9101-1123"

print(credit_number[1])
print(credit_number[0 : 4])
# the starting index is inclusive, and the ending index is exclusive, which is why 4 does not include the '-'
print(credit_number[:9])
# Having no number before the colon, python assumes it goes to the first character
print(credit_number[5:])
# Having no number after the colon, python assumes it goes to the last character
print(credit_number[-5])
# Negative indexes read the variable backwards, it is inclusive because you cant have negative 0
print(credit_number[::2])
# This will print every second character in the string, change the number to change the size of the gaps.

# Exercise 1

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")