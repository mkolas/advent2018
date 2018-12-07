steps = dict()
answer = list()


class Step:
    name = ""
    prereqs = list()

    def __init__(self, letter_name):
        self.name = letter_name
        self.prereqs = []


# create list of tasks
with open("input1.txt") as file:
    for row in file:
        this_step = row.split(" ")[7]
        if this_step not in steps:
            steps[this_step] = Step(this_step)
        this_step = row.split(" ")[1]
        if this_step not in steps:  # there will be some without prereqs
            steps[this_step] = Step(this_step)

# add pre reqs
with open("input1.txt") as file:
    for row in file:
        prerequisite = row.split(" ")[1]
        this_step = row.split(" ")[7]
        steps[this_step].prereqs.append(prerequisite)

while len(steps) > 0:
    # get items with no preqrequisites
    item_to_process = sorted([x for x, y in steps.items() if len(y.prereqs) == 0])[0]
    answer.append(item_to_process)
    del steps[item_to_process]
    # for each that have been completed, clear out list
    dependents = sorted([x for x, y in steps.items() if item_to_process in y.prereqs])
    for d in dependents:
        steps[d].prereqs.remove(item_to_process)

print(''.join(answer))

# part 2 (lets recreate our objects)

# create list of tasks
with open("input1.txt") as file:
    for row in file:
        this_step = row.split(" ")[7]
        if this_step not in steps:
            steps[this_step] = Step(this_step)
        this_step = row.split(" ")[1]
        if this_step not in steps:  # there will be some without prereqs
            steps[this_step] = Step(this_step)

# add pre reqs
with open("input1.txt") as file:
    for row in file:
        prerequisite = row.split(" ")[1]
        this_step = row.split(" ")[7]
        steps[this_step].prereqs.append(prerequisite)

answer = []


def get_char_time(character):
    return ord(character.lower()) - 96 + 60


class Job:
    name = ""
    time_left = 0

    def __init__(self, name, time_left):
        self.name = name
        self.time_left = time_left


time = 0
workers = 5
worker_map = dict()

# populate workers
for x in range(workers):
    worker_map[x] = Job("?", 0)

while True:
    # inc each worker task
    for k in worker_map.keys():
        if worker_map[k].time_left >= 1:
            worker_map[k].time_left -= 1
        if worker_map[k].time_left == 0:
            # resolve children prereqs
            dependents = sorted([x for x, y in steps.items() if worker_map[k].name in y.prereqs])
            for d in dependents:
                steps[d].prereqs.remove(worker_map[k].name)

            # snag new task
            items_to_process = sorted([x for x, y in steps.items() if len(y.prereqs) == 0])
            if len(items_to_process) != 0:
                item_to_process = items_to_process[0]
                answer.append(item_to_process)
                del steps[item_to_process]
                worker_map[k] = Job(item_to_process, get_char_time(item_to_process))
    time += 1
    if len([k for k, v in worker_map.items() if v.time_left > 0]) == 0:
        print("".join(answer))
        print(time-1)
        exit()
