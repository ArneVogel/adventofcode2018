import sys

def parse_line(line):
    operator = line[0]
    operand = int(line[1:])
    return (operator, operand)

def do_operation(operation, frequency):
    if operation[0] == "+":
        frequency += operation[1]
    if operation[0] == "-":
        frequency -= operation[1]
    return frequency

def main():
    frequency = 0
    first_twice = 0
    frequency_set = set()
    frequency_set.add(0)
    no_freqency_twice = True
    
    input_lines = []


    if len(sys.argv) > 1:
        for line in sys.argv[1:]:
            input_lines.append(line)
    else:
        for line in sys.stdin:
            input_lines.append(line)
    while no_freqency_twice:
        for line in input_lines:
            frequency = do_operation(parse_line(line), frequency)
            if frequency in frequency_set and no_freqency_twice:
                no_freqency_twice = False 
                first_twice = frequency
            frequency_set.add(frequency)
        print("frequency=" + str(frequency))

    print("first_twice=" + str(first_twice))

if __name__ == "__main__":
    main()
