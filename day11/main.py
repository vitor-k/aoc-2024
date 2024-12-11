
import time

memoization = {}

def recurseStone(value: int, it: int):
    if it <= 0:
        return 1

    if (value, it) in memoization:
        return memoization[(value, it)]

    if value == 0:
        result = recurseStone(1, it-1)
    elif (ndigits := len(str(value))) % 2 == 0:
        leftValue, rightValue = int(str(value)[:ndigits//2]), int(str(value)[ndigits//2:])

        result = recurseStone(leftValue, it-1) + recurseStone(rightValue, it-1)
    else:
        result = recurseStone(value*2024, it-1)

    memoization[(value, it)] = result

    return result

def part1(filename):

    stones = []
    with open(filename) as fp:
        line = fp.read().strip()
        stones = map(int, line.split())

    total = 0
    for stone in stones:
        final_stones = recurseStone(stone, 25)
        total += final_stones
    print(total)

def part2(filename):
    stones = []
    with open(filename) as fp:
        line = fp.read().strip()
        stones = map(int, line.split())

    total = 0
    for stone in stones:
        final_stones = recurseStone(stone, 75)
        total += final_stones
    print(total)

if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"

    t0 = time.perf_counter_ns()
    part1(filename)
    t1 = time.perf_counter_ns()
    part2(filename)
    t2 = time.perf_counter_ns()
    print(f"Part 1: {(t1-t0)/1e9} s")
    print(f"Part 2: {(t2-t1)/1e9} s")
