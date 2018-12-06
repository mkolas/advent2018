coordinate_area_size = dict()
area_map = dict()
area_key = dict()
max_x = 0
max_y = 0
min_x = 9999
min_y = 9999


def get_manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def get_closest(this_x, this_y):
    # print("checking neighbors for {}, {}", this_x, this_y)
    if (this_x, this_y) in coordinate_area_size:
        # print("found")
        return this_x, this_y
    step = 1
    while True:
        found_in_this_step = list()
        current_x, current_y = this_x, this_y + step
        # move to left
        while current_y > this_y:
            # print("checking {}, {}".format(x,y))
            if (current_x, current_y) in coordinate_area_size:
                found_in_this_step.append((current_x, current_y))
            current_x -= 1
            current_y -= 1
        while current_x < this_x:
            # print("checking {}, {}".format(x,y))
            if (current_x, current_y) in coordinate_area_size:
                found_in_this_step.append((current_x, current_y))
            current_x += 1
            current_y -= 1
        while current_y < this_y:
            # print("checking {}, {}".format(x,y))
            if (current_x, current_y) in coordinate_area_size:
                found_in_this_step.append((current_x, current_y))
            current_x += 1
            current_y += 1
        while current_x > this_x:
            # print("checking {}, {}".format(x,y))
            if (current_x, current_y) in coordinate_area_size:
                found_in_this_step.append((current_x, current_y))
            current_x -= 1
            current_y += 1

        if len(found_in_this_step) == 1:
            return found_in_this_step[0]
        if len(found_in_this_step) > 1:
            return None
        step += 1


with open("input1.txt") as file:
    for i, row in enumerate(file):
        x = int(row.split(",")[0].strip())
        y = int(row.split(",")[1].strip())
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        coordinate_area_size[(x, y)] = 0

# part 1
for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        closest = get_closest(x, y)
        if closest is not None:
            coordinate_area_size[closest] += 1

# for the simplest approximation, just check that these areas don't extend past 100 in any direction
cleaned_areas = dict()
for key, value in coordinate_area_size.items():
    if get_closest(key[0]+100, key[1]) != key and get_closest(key[0]-100, key[1]) != key and get_closest(key[0], key[1]+100 != key) and get_closest(key[0], key[1]-100 != key):
            cleaned_areas[key] = value

print(cleaned_areas[max(cleaned_areas, key=cleaned_areas.get)])


# part 2

acceptable_locations = 0

for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        total_distance = 0
        for coordinate in coordinate_area_size.keys():
            total_distance += get_manhattan_distance((x, y), coordinate)
            if total_distance >= 10000:
                break
        if total_distance < 10000:
            acceptable_locations += 1

print(acceptable_locations)
