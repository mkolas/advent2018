two_ids_count = 0
three_ids_count = 0


def compare(string1, string2):
    length = len(string1)
    differences = 0
    i = 0
    while i < length:
        if string1[i] != string2[i]:
            differences += 1
            if differences == 2:
                return False
        i += 1
    return True


# part 1
with open("input1.txt") as file:
    for row in file:
        # check for two chars
        char_counts = dict()
        two = False
        three = False
        for c in row:
            if c in char_counts:
                char_counts[c] += 1
            else:
                char_counts[c] = 1

        for k, v in char_counts.items():
            if v == 2:
                two = True
            if v == 3:
                three = True

        if two:
            two_ids_count += 1
        if three:
            three_ids_count += 1

print(two_ids_count*three_ids_count)


# part 2
boxes = list()
with open("input1.txt") as file:
    for row in file:
        boxes.append(row.strip())

for i, first_box in enumerate(boxes):
    j = i + 1
    while j < len(boxes):
        second_box = boxes[j]
        if compare(first_box, second_box):
            print(first_box)
            print(second_box)
            exit()
        j += 1

