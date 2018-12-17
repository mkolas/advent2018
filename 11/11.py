cells = dict()
serial = 2187


def get_power_for_coord_with_size(input_x, input_y, size):
    power = 0
    for x in range(input_x, input_x+size):
        for y in range(input_y, input_y+size):
            power += cells[(x, y)]
    return power


for x in range(1, 301):
    for y in range(1, 301):
        rack_id = 10 + x
        power_level = rack_id * y
        power_level += serial
        power_level *= rack_id
        power_level = (power_level // 100) % 10  # divide by 100, mod 10 for hundredths place
        power_level -= 5
        cells[(x, y)] = power_level


# part 1

max_power = 0
max_coord = (0, 0)
for x in range(1, 298):
    for y in range(1, 298):
        coord_power = get_power_for_coord_with_size(x, y, 3)
        if coord_power > max_power:
            max_power = coord_power
            max_coord = (x, y)

print(max_power)
print(max_coord)


# part 2
max_power = 0
max_coord = 0
max_size = 0

for x in range(1, 301):
    for y in range(1, 301):
        size = 1
        while x+size < 301 and y+size < 301:
                print("checking x {}, y {}, size {}".format(x, y, size))
                coord_power = get_power_for_coord_with_size(x, y, size)
                if coord_power > max_power:
                    max_power = coord_power
                    max_coord = (x, y)
                    max_size = size
                size += 1

print(max_power)
print(max_coord)
print(max_size)
