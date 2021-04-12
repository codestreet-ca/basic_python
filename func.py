# Do not write this

def waterbottle(ml):
    liters = ml/1000
    return liters


def can_drive(age):  # age = int("20") = 20
    if age > 15:
        return True
    return False

#############################

age = input("How old are you")  # age = "20"

if can_drive(int(age)):  # int(age) = int("20")
    print("You can drive")
else:
    print("You can not drive")

"""
print(), input(), open()
list(), string(), int()
float("12.1") -> 12.1
range()

"123".replace("2", "3")
file.readlines()
"""
