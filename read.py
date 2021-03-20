# You do not have to write with me
# If you want, no one can stop you

file = open("story.txt", "r")  # if you open with "r", you cannot write
story = file.read()
file.close()

file = open("story.txt", "w")
story = story.replace("Python 3", "Taqi")
file.write(story)
file.close()

# for line in story:
#     if "Author" in line:
#         file.write("The Author is Taqi\n")
#     else:
#         file.write(line)
