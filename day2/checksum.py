import sys

def get_char_counts(line):
    d = {}
    for char in line:
        d[char] = d.get(char, 0) + 1
    return d

def dict_contains_value(d, value):
    for _, dv in d.items():
        if value is dv:
            return True
    return False

def part_one(lines):
    count_two = 0
    count_three = 0
    for line in lines:
        if dict_contains_value(get_char_counts(line), 2):
            count_two += 1
        if dict_contains_value(get_char_counts(line), 3):
            count_three += 1
    print("part 1")
    print("count_two: " + str(count_two))
    print("count_three: " + str(count_three))
    print("checksum: " + str(count_two*count_three))

def similar(line1, line2):
    count_diff = 0
    for i in range(0, len(line1)):
        if line1[i] is not line2[i]:
            count_diff += 1
    return count_diff <= 1

def part_two(lines):
    print("part two")
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            if similar(lines[i], lines[j]):
                print("id 1: " + lines[i])
                print("id 2: " + lines[j])
                print("common: ", end="")
                for k in range(len(lines[i])):
                    if lines[i][k] is lines[j][k]:
                        print(lines[i][k], end="")
                print("")


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
