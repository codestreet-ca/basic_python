sentence = input("Write a sentence please! ")
count = 0
i = 0

while i < len(sentence):
    if sentence[i] in "aeiou":
        count += 1
    i += 1

print(f"You have {count} vowels")
