import re

points = list()
ticks = 50000


def tick(point):
    point["position"] = (point["position"][0]+point["velocity"][0], point["position"][1]+point["velocity"][1])
    return point


def print_points(min_y, max_y, min_x, max_x, cur_map):
    lines = list()
    for y in range(min_y, max_y):
        line = ""
        for x in range(min_x, max_x):
            if (x, y) in cur_map:
                line += "#"
            else:
                line += "."
        lines.append(line)
    return lines


with open("input1.txt") as f:
    for index, row in enumerate(f):
        p_tuple = tuple([int(x) for x in re.findall('<([^>]+)', row)[0].split(",")])
        v_tuple = tuple([int(x) for x in re.findall('<([^>]+)', row)[1].split(",")])
        points.append(dict(id=index, position=p_tuple, velocity=v_tuple))


for x in range(0, 11000):
    current_points = dict()
    for p in points:
        p = tick(p)
        current_points[p['position']] = "#"
    print(x)
    if 10630 < x < 10640:
        current_lines = print_points(100, 400, 0, 350, current_points)
        # current_lines.reverse()
        printed_points = 0
        # for y in current_lines:
        #     if "#" in y:
        #         printed_points += 1
        print("tick {}".format(x))
        for y in current_lines:
            print(y)
        print(" ")
