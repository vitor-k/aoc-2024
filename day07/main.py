
from itertools import product
import time

def applyOperators(operands, operators, expected_result):
    result = operands[0]
    for operand, operator in zip(operands[1:], operators):
        if operator == '+':
            result += operand
        elif operator == '*':
            result *= operand
        elif operator == '||':
            result = int(f"{result}{operand}")

        if result > expected_result: # early abort
            break
    return result

def part1(filename):

    with open(filename) as fp:
        total = 0
        for line in fp.readlines():
            result, operands = line.strip().split(':')
            result = int(result)
            operands = tuple(map(int, operands.split()))
            for operators in product(('+', '*'), repeat=len(operands)-1):
                possible_result = applyOperators(operands, operators, result)
                if possible_result == result:
                    total += result
                    break

    print(total)

def part2(filename):
    with open(filename) as fp:
        total = 0
        for line in fp.readlines():
            result, operands = line.strip().split(':')
            result = int(result)
            operands = tuple(map(int, operands.split()))
            for operators in product(('+', '*', '||'), repeat=len(operands)-1):
                possible_result = applyOperators(operands, operators, result)
                if possible_result == result:
                    total += result
                    break

    print(total)

if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    t0 = time.time_ns()
    part1(filename)
    t1 = time.time_ns()
    part2(filename)
    t2 = time.time_ns()

    print(f"Part 1: {(t1-t0)/1e9} s\nPart 2: {(t2-t1)/1e9} s")
