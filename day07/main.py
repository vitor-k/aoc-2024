
from itertools import product


def applyOperators(operands, operators):
    result = operands[0]
    for operand, operator in zip(operands[1:], operators):
        match operator:
            case '+':
                result += operand
            case '*':
                result *= operand
            case '||':
                result = int(str(result) + str(operand))
    return result

def part1(filename):

    with open(filename) as fp:
        total = 0
        for line in fp.readlines():
            result, operands = line.strip().split(':')
            result = int(result)
            operands = list(map(int, operands.split()))
            for operators in product(['+', '*'], repeat=len(operands)-1):
                possible_result = applyOperators(operands, operators)
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
            operands = list(map(int, operands.split()))
            for operators in product(['+', '*', '||'], repeat=len(operands)-1):
                possible_result = applyOperators(operands, operators)
                if possible_result == result:
                    total += result
                    break

    print(total)

if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    part1(filename)
    part2(filename)
