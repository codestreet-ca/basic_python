# This program takes in UK Year and tells you Canadian Grade
year = input("What is your UK year?")  # This is the user's UK year
year = int(year)

if year < 1:
    print("Sorry, that doesn't make sense!")
elif year > 11:
    print("Sorry, that doesn't make sense!")
else:
    grade = year - 1
    print(f"You are in Candian grade {grade}!")

input()

"""
HW
CanadaGrade.py: from Canada Grade to UK year
CanadaAge.py: from Canada Grade to Age
UKAge.py: from UK year to Age
"""
