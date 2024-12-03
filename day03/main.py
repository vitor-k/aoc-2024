
import re

def part1(filename):
    total = 0
    with open(filename) as fp:
        line = fp.read()
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
        for matched in matches:
            a,b = matched
            total += int(a) * int(b)
    print(total)


def part2(filename):
    total = 0
    with open(filename) as fp:
        line = fp.read()
        enabled_sections = line.split("do()")
        for section in enabled_sections:
            section = section.split("don't()")[0]
            matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", section)
            for matched in matches:
                a,b = matched
                total += int(a) * int(b)
    print(total)

if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
