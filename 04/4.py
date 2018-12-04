logs = list()
guard_time = dict()
guard_logs = dict()

with open("input1.txt") as file:
    for row in file:
        logs.append(row.strip())
        if "begins shift" in row:
            guard_time[int(row.split(" ")[3][1:])] = 0
            guard_logs[int(row.split(" ")[3][1:])] = dict()
            for x in range(60):
                guard_logs[int(row.split(" ")[3][1:])][x] = 0

logs.sort()

current_guard = 0
sleep = False
start_time = 0
for log in logs:
    if "begins shift" in log or current_guard == 0:
        sleep = False
        current_guard = int(log.split(" ")[3][1:])
    else:
        if "falls" in log:
            start_time = int(log.split(" ")[1][3:5])
            sleep = True
        if "wakes" in log:
            wake_time = int(log.split(" ")[1][3:5])
            guard_time[current_guard] += (wake_time - start_time)
            for x in range(start_time, wake_time):
                guard_logs[current_guard][x] += 1
            sleep = False

# part 1
sleepiest_guard = max(guard_time, key=guard_time.get)
sleepiest_minute = max(guard_logs[sleepiest_guard], key=guard_logs[sleepiest_guard].get)
print(sleepiest_guard*sleepiest_minute)

# part 2
most_frequently_asleep_guard = 0
most_frequently_asleep_minute = 0
most_frequently_asleep_value = 0
for guard, guard_log in guard_logs.items():
    for minute, value in guard_log.items():
        if value > most_frequently_asleep_value:
            print("found new sleepier: {}".format(value))
            most_frequently_asleep_guard = guard
            most_frequently_asleep_minute = minute
            most_frequently_asleep_value = value

print(most_frequently_asleep_guard*most_frequently_asleep_minute)
