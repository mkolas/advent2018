marbles = [0]
scores = dict()
players = 428

for x in range(1, players+1):
    scores[x] = 0

current = 1
index = 1
turn = 1

for x in range(7206100):
    if len(marbles) == 1:
        marbles.append(current)
    elif current % 23 == 0:
        scores[turn] += current
        index = (index - 7) % len(marbles)
        if index == 0:
            index = len(marbles)
        scores[turn] += marbles.pop(index)
    else:
        index = (index + 2) % len(marbles)
        if index == 0:
            index = len(marbles)
        marbles.insert(index, current)

    turn += 1
    turn = turn % players
    if turn == 0:
        turn = players
    current += 1
    # print(marbles)

print(scores[max(scores, key=scores.get)])
