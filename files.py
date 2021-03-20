# You do not have to write with me
# If you want, no one can stop you

names = []
for i in range(3):
    name = input("Give me a name! ")
    names.append(name)

story = f"\n{names[0]} went to the store. {names[0]} saw {names[1]}.\n{names[1]} was talking to {names[2]}. {names[0]} left the store with {names[2]}"

# open(name, mode)
file = open("story.txt", "w")  # If mode "w", python will erase the file
file.write("The Author is Python 3\n")
file.write(story)
file.close()
