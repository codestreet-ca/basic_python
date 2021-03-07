# You will give it a word and it will spell it out

word = input("What word do you want me to spell? ")

for letter in word:
    print(letter)

print()

i = 0  # This is a counter for while loop
# i = 5
while i < len(word):  # word is "hello"
    print(word[i])
    i = i + 1

print("This is how you spell a word in two different ways")
input()
