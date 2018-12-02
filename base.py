import sys

def part_one():
    pass

def part_two():
    pass

def main():
    input_lines = []
    if len(sys.argv) > 1:
        for line in sys.argv[1:]:
            input_lines.append(line)
    else:
        for line in sys.stdin:
            input_lines.append(line)

if __name__ == "__main__":
    main()
