fabric = dict()
claims = list([])
x_counter = 0

with open("input1.txt") as file:
    for i, row in enumerate(file):
        words = row.split()
        start_x = int(words[2].split(",")[0])
        start_y = int(words[2].split(",")[1][:-1])
        width = int(words[3].split("x")[0])
        height = int(words[3].split("x")[1])
        claims.append([start_x, start_y, width, height])
        for x in range(start_x, start_x+width):
            for y in range(start_y, start_y+height):
                if (x, y) not in fabric:
                    fabric[(x, y)] = i+1
                elif fabric[(x, y)] != "X":
                    fabric[(x, y)] = "X"
                    x_counter += 1

print("X squares: {}".format(x_counter))

# part 2
for i, claim in enumerate(claims):
    result = True
    for x in range(claim[0], claim[0]+claim[2]):
        for y in range(claim[1], claim[1]+claim[3]):
            if fabric[(x, y)] == "X":
                result = False

    if result:
        print("clean claim: {}".format(i+1))
        exit()
