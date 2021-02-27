print("hi, how old are you")
age = input()
age = int(age)

print("Do you live in the U.S? Yes or No")
us = input()

if us == "Yes":
    if age > 13:
        print("Congrats, you can take the driving test")
    else:
        years = 14 - age
        print(f"You have {years} years until you are able to drive")
else:
    pass

input()

"integer: ..., -3, -2, -1, 0, 1, 2, 3, ..."
"float (examples): 10.9, -0.00001, 3/4. -2/1, 1.0, 10/1"
"""
Suggestions:
-) How many years until you are able to drive?
-) Different countries.
"""
