# You do not have to write with me
# If you want, no one can stop you

file = open("map.txt", "r")
map = file.readlines()
file.close()

player = [-1, -1]

["xxxx", "x0px", "x00x", "xxxx"]

for x in range(len(map)):  # 0, 1, 2, 3
    map[x] = map[x].replace("0", " ")
    map[x] = list(map[x])    

    for y in range(len(map[x])):
        if map[x][y] == "p":
            player = [x, y]

if (player[0] == -1) or (player[1] == -1):
    print("The map file is corrupted")
else:
    won = False

    while won != True:

        for x in range(len(map)):
            for y in range(len(map[x])):
                print(map[x][y], end="")

        move = input("Please enter w, a, s, d to move: ")

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
            continue

        if map[pos[0]][pos[1]] == "x":
            continue
        elif map[pos[0]][pos[1]] == "g":
            won = True
        else:
            map[pos[0]][pos[1]] = "p"
            map[player[0]][player[1]] = " "
            player = pos

    print("You won the map!!")
