import sys

def part_one(lines):
    lines = lines[0].replace("\n", "")
    old_lines = lines
    to_remove = ["aA", "bB", "cC", "dD","eE","fF","gG","hH","iI","jJ","kK","lL","mM","nN","oO","pP","qQ","rR","sS","tT","uU","vV","wW","xX","yY","zZ", "Aa","Bb","Cc","Dd","Ee","Ff","Gg","Hh","Ii","Jj","Kk","Ll","Mm","Nn","Oo","Pp","Qq","Rr","Ss","Tt","Uu","Vv","Ww","Xx","Yy","Zz"]
    first = True # simulate do while loop
    while old_lines is not lines or first:
        first = False
        old_lines = lines
        for r in to_remove:
            lines = lines.replace(r, "")

    print("part one")
    #print(lines)
    print(len(lines))

def part_two(lines):
    print("part two")
    lines = lines[0].replace("\n", "")
    lines_copy = lines

    smallest_polymer = lines
    smallest_polymer_len = len(lines)
    smallest_unit = ""
    
    old_lines = lines
    to_remove = ["aA", "bB", "cC", "dD","eE","fF","gG","hH","iI","jJ","kK","lL","mM","nN","oO","pP","qQ","rR","sS","tT","uU","vV","wW","xX","yY","zZ", "Aa","Bb","Cc","Dd","Ee","Ff","Gg","Hh","Ii","Jj","Kk","Ll","Mm","Nn","Oo","Pp","Qq","Rr","Ss","Tt","Uu","Vv","Ww","Xx","Yy","Zz"]
    units = ["aA", "bB", "cC", "dD","eE","fF","gG","hH","iI","jJ","kK","lL","mM","nN","oO","pP","qQ","rR","sS","tT","uU","vV","wW","xX","yY","zZ"]
    for unit in units:
        lines = lines_copy
        lines = lines.replace(unit[0], "")
        lines = lines.replace(unit[1], "")
        old_lines = lines
        first = True # simulate do while loop
        while old_lines is not lines or first:
            first = False
            old_lines = lines
            for r in to_remove:
                lines = lines.replace(r, "")
        if len(lines) < smallest_polymer_len:
            smallest_polymer_len = len(lines)
            smallest_polymer = lines
            smallest_unit = unit


    print(smallest_polymer_len)

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
