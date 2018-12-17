pots = dict()
rules = dict()


def get_local_range(index):
    return ''.join([pots[x] for x in range(index-2, index+2)])


with open("testinput.txt") as file:
    for row in file:
        if "initial state" in row:
            pot_string = row.split(" ")[2]
            for i, c in enumerate(list(pot_string)):
                pots[i] = c
        else:
            rule_left = row.split(" ")[0]
            rule_right = row.split(" ")[2]
            rules[rule_left] = rule_right

for x in range(21):
    new_pots = dict()
    for key, value in pots.items():
        if get_local_range(key) in rules:
            new_pots[key] = get_local_range(key)
        else:
            new_pots[key] = value
    pots = new_pots
