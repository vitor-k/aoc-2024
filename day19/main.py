
import time
from functools import cache

@cache
def fmatch(patterns: tuple[str], line: str):
    if not line:
        return True
    for pattern in patterns:
        if line.startswith(pattern):
            if fmatch(patterns, line.removeprefix(pattern)):
                return True
    return False

@cache
def fMatchCount(patterns: tuple[str], line: str) -> int:
    if not line:
        return 1
    count = 0
    for pattern in patterns:
        if line.startswith(pattern):
            p_count = fMatchCount(patterns, line[len(pattern):])
            count += p_count
    return count

def part1(filename):
    total = 0
    with open(filename) as fp:
        patterns = [pt.strip() for pt in fp.readline().split(",")]

        remove = [f"{x}{y}" for x in patterns for y in patterns if f"{x}{y}" in patterns]

        patterns = set(patterns) - set(remove)
        patterns = tuple(patterns)

        for line in fp.readlines():
            if not line.strip():
                continue
            matchy = fmatch(patterns, line.strip())
            if matchy:
                total += 1

    print(total)


def part2(filename):
    total = 0
    with open(filename) as fp:
        patterns = tuple([pt.strip() for pt in fp.readline().split(",")])

        for line in fp.readlines():
            if not line.strip():
                continue
            total += fMatchCount(patterns, line.strip())

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
