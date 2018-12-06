import sys

def print_grid(grid, minX, maxX, minY, maxY):
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            if len(grid[(x,y)]) == 1:
                print(grid[(x,y)][0][0], end="")
            else:
                print(".", end="")
        print()

def get_areas(lines, overlap=1):
    minX = min(int(l.split(", ")[0]) for l in lines)-overlap
    maxX = max(int(l.split(", ")[0]) for l in lines)+overlap
    minY = min(int(l.split(", ")[1]) for l in lines)-overlap
    maxY = max(int(l.split(", ")[1]) for l in lines)+overlap
    grid = {}
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            grid[(x,y)] = [(99999,9999999)] # (shortest node, distance to node)
    for counter, line in enumerate(lines):
        lx = int(line.split(", ")[0])
        ly = int(line.split(", ")[1])
        for x in range(minX, maxX):
            for y in range(minY, maxY):
                distance = abs(x - lx) + abs(y - ly) 
                if distance < grid[(x,y)][0][1]:
                    grid[(x,y)] = [(counter, distance)]
                elif distance == grid[(x,y)][0][1]:
                    grid[(x,y)].append((counter, distance))
    area = {}
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            if len(grid[(x,y)]) == 1:
                area[grid[(x,y)][0][0]] = area.get(grid[(x,y)][0][0], 0) +1
    #print_grid(grid, minX, maxX, minY, maxY)
    return area


def part_one(lines):
    offset1 = get_areas(lines, overlap=1)
    offset3 = get_areas(lines, overlap=3)
    max_area = 0
    for o in offset1:
        if offset1[o] == offset3[o] and offset1[o] > max_area:
            max_area = offset1[o]
    print("part one")
    print(max_area)

def part_two(lines):
    print("part two")
    overlap = 1
    minX = min(int(l.split(", ")[0]) for l in lines)-overlap
    maxX = max(int(l.split(", ")[0]) for l in lines)+overlap
    minY = min(int(l.split(", ")[1]) for l in lines)-overlap
    maxY = max(int(l.split(", ")[1]) for l in lines)+overlap
    grid = {}
    points = []
    for line in lines:
        x = int(line.split(", ")[0])
        y = int(line.split(", ")[1])
        points.append((x,y))

    for x in range(minX, maxX):
        for y in range(minY, maxY):
            total_distance = 0
            for point in points:
                total_distance += abs(point[0]-x) + abs(point[1]-y)
            grid[(x,y)] = total_distance
    #print(grid) 
    max_distance = 10000
    sum_coordinates = 0
    for p in grid:
        if grid[p] < max_distance:
            sum_coordinates += 1
    print(sum_coordinates)


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
