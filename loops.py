# DO NOT WRITE THIS
age = input("How old you are you? ")
age = int(age)  # age is 5

if age < 0:
    print("You cannot be younger than 0 years old")
else:
    i = 0  # Counter for while Loop
    # i = 5
    while i < age:  # Age is 5
        print(i)
        print("Happy Birthday")
        print()
        i = i + 1

    print("I am finally done!")

    for i in range(age):  # age is 5
        print(i)

    print("I am done! Finally!")


"""
range(5) -> 0, 1, 2, 3, 4

2 Data Types for Numbers:
-) Integers: 5, 6, 11, -21, -100, 10000
-) Floats: 0.01, -0.01, 1.0, 1.602, 0.000

Data Type for Writing:
-) Strings "Hello", "hfud", "135"
1.0 = 1.000 = 1.00000000000

Data Type for Truth:
-) Boolean: True or False

2 Loops:
-) While Loop
-) For Loop
"""
