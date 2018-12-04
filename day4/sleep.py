import sys

def sort_list(lines):
    lines.sort(key=lambda r:(" ").join(r.split(" ")[:-2]))
    return lines

def part_one(lines):
    print("part one")
    lines = sort_list(lines)
    guards = {}
    guard = ""
    asleep = 0
    for l in lines:
        if l.split(" ")[3] not in ["asleep\n", "up\n"]:
            guard = l.split(" ")[3]
        if l.split(" ")[3] == "asleep\n":
            asleep=int(l.split(" ")[1].split(":")[1][:-1])
        if l.split(" ")[3] == "up\n":
            up=int(l.split(" ")[1].split(":")[1][:-1])
            #update the sleep schedule of the guard, the schedule is a dict with minutes as keys and found sleeping at that minute as value
            schedule = guards.get(guard, {})
            for i in range(asleep, up):
                schedule[i] = schedule.get(i, 0) + 1
            guards[guard] = schedule

    max_sleeper = "#0"
    max_sleep = 0
    for guard in guards:
        sum_sleep = 0
        for minute in guards[guard]:
            sum_sleep += guards[guard][minute] 
        if sum_sleep > max_sleep:
            max_sleep = sum_sleep
            max_sleeper = guard

    max_min = 0
    max_min_value = 0
    for minute in guards[max_sleeper]:
        if guards[max_sleeper][minute] >= max_min_value:
            max_min = minute 
            max_min_value = guards[max_sleeper][minute]
    
    g = int(max_sleeper[1:])
    print(g * max_min)
            


def part_two(lines):
    print("part two")
    lines = sort_list(lines)
    guards = {}
    guard = ""
    asleep = 0
    for l in lines:
        if l.split(" ")[3] not in ["asleep\n", "up\n"]:
            guard = l.split(" ")[3]
        if l.split(" ")[3] == "asleep\n":
            asleep=int(l.split(" ")[1].split(":")[1][:-1])
        if l.split(" ")[3] == "up\n":
            up=int(l.split(" ")[1].split(":")[1][:-1])
            #update the sleep schedule of the guard, the schedule is a dict with minutes as keys and found sleeping at that minute as value
            schedule = guards.get(guard, {})
            for i in range(asleep, up):
                schedule[i] = schedule.get(i, 0) + 1
            guards[guard] = schedule
    
    max_sleeper = 0
    max_min = 0
    max_min_value = 0
    for guard in guards:
        for minute in guards[guard]:
            if guards[guard][minute] > max_min_value:
                max_min = minute
                max_min_value = guards[guard][minute]
                max_sleeper = guard 

    g = int(max_sleeper[1:])
    print(g * max_min)
    

def main():
    input_lines = []
    if len(sys.argv) > 1:
        for line in sys.argv[1:]:
            input_lines.append(line)
    else:
        for line in sys.stdin:
            input_lines.append(line)
    part_one(input_lines)
    part_two(input_lines)

if __name__ == "__main__":
    main()
