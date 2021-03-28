# You do not have to write with me
# If you want, no one can stop you

file = open("map.txt", "r")
map = file.readlines()  # ["line 1", "line 2"]
file.close()

# These are the coordinates of the player
player = [-1, -1]  # The first coor is the vertical, second is horizontal

# map = ["xxxx", "xp0x", "x00x", "x0gx", "xxxx"]

# x = 1, y = 1

for x in range(len(map)):  # 0, 1, 2, 3
    map[x] = map[x].replace("0", " ")  # "x00x" -> "x  x"
    map[x] = list(map[x])  # list("x  x") -> ["x", " ", " ", "x"]

    for y in range(len(map[x])):  # range(len("xxxx")) -> 0, 1, 2, 3
        if map[x][y] == "p":
            player = [x, y]

if (player[0] == -1) or (player[1] == -1):  # Checks player character
    print("The map file is corrupted")
else:
    won = False  # Tells us if the player has won the game

    while won != True:  # While the game is not won, play the game

        # Print the map
        for x in range(len(map)):  # Iterate over every single line
            for y in range(len(map[x])):  # Iterate over every single character in a line
                print(map[x][y], end="")  # Print the characters without a newline at the end

        move = input("Please enter w, a, s, d to move: ")

        # Calculates the new position of the player
        # move = "w", coor [1, 1] -> []
        if move == "w":
            pos = [player[0] - 1, player[1]]
        elif move == "s":
            pos = [player[0] + 1, player[1]]
        elif move == "a":
            pos = [player[0], player[1] - 1]
        elif move == "d":
            pos = [player[0], player[1] + 1]
        else:
            print("Invalid move!")
            continue  # Restart the while loop if invalid move

        if map[pos[0]][pos[1]] == "x":
            continue
        elif map[pos[0]][pos[1]] == "g":
            won = True
        else:
            map[pos[0]][pos[1]] = "p"
            map[player[0]][player[1]] = " "
            player = pos

    print("You won the map!!")
