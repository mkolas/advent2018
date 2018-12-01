instructions = list()
historical_freqs = list()
starting_freq = 0
historical_freqs.append(0)

with open("input1.txt") as file:
    for row in file:
        instructions.append(int(row))


# part 1
for item in instructions:
    starting_freq += item
    historical_freqs.append(starting_freq)
print(starting_freq)

# part 2
while True:
    for item in instructions:
        starting_freq += item
        if starting_freq in historical_freqs:
            print(starting_freq)
            exit()
        historical_freqs.append(starting_freq)





