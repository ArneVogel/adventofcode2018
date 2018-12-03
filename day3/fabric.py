import sys

def part_one(lines):
    offsetX = 0
    offsetY = 0
    width = 0
    height = 0
    areas = {}
    for line in lines:
        split_line = line.split(" ")
        offsetX = int(split_line[2].split(",")[0])
        offsetY = int(split_line[2].split(",")[1].replace(":", ""))
        width = int(split_line[3].split("x")[0])
        height = int(split_line[3].split("x")[1].replace("\n", ""))
        for i in range(width):
            for j in range(height):
                x = i + offsetX
                y = j + offsetY
                if (x,y) in areas:
                    areas[(x,y)].append("x")
                else:
                    areas[(x,y)] = ["x"]
    print("part one")
    total = 0
    for a in areas:
        if len(areas[a]) >= 2:
            total += 1
    print(total)

def part_two(lines):
    offsetX = 0
    offsetY = 0
    width = 0
    height = 0
    areas = {}
    valid_areas = set()
    for line_number, line in enumerate(lines):
        valid_areas.add(line_number+1) # line numbers start at 1
        split_line = line.split(" ")
        offsetX = int(split_line[2].split(",")[0])
        offsetY = int(split_line[2].split(",")[1].replace(":", ""))
        width = int(split_line[3].split("x")[0])
        height = int(split_line[3].split("x")[1].replace("\n", ""))
        for i in range(width):
            for j in range(height):
                x = i + offsetX
                y = j + offsetY
                if (x,y) in areas:
                    areas[(x,y)].append(line_number)
                else:
                    areas[(x,y)] = [line_number]
    print("part two")
    for a in areas:
        if len(areas[a]) >= 2:
            for i in areas[a]:
                if i in valid_areas:
                    valid_areas.remove(i)
    print(valid_areas)
    pass

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
