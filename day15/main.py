
import time
from functools import cache
from itertools import chain

def move(warehouse, i: int, j: int, dir: str):
    passable = True
    new_i, new_j = i,j
    if dir == '^':
        if i <= 0 or warehouse[i-1][j] == '#':
            passable = False
        else:
            new_i = i - 1
    elif dir == '>':
        if j >= len(warehouse[0]) - 1 or warehouse[i][j+1] == '#':
            passable = False
        else:
            new_j = j + 1
    elif dir == 'v':
        if i >= len(warehouse) - 1 or warehouse[i+1][j] == '#':
            passable = False
        else:
            new_i = i + 1
    elif dir == '<':
        if j <= 0 or warehouse[i][j-1] == '#':
            passable = False
        else:
            new_j = j - 1
    return (new_i, new_j, passable)

def moveRobot(warehouse, i: int, j: int, dir: str):
    new_robot_i, new_robot_j, passable = move(warehouse, i, j, dir)
    new_i, new_j = new_robot_i, new_robot_j
    if not passable:
        return i,j
    while warehouse[new_i][new_j] == 'O':
        new_i, new_j, passable = move(warehouse, new_i, new_j, dir)
        if not passable:
            return i, j
    warehouse[new_i][new_j] = 'O'
    warehouse[new_robot_i][new_robot_j] = '@'
    warehouse[i][j] = '.'

    return new_robot_i, new_robot_j

def part1(filename):
    warehouse = []
    movements = ""
    with open(filename) as fp:
        for line in fp.readlines():
            if '#' in line:
                warehouse.append(list(line.strip()))
            else:
                movements += line.strip()
    r_pos = None
    for i, line in enumerate(warehouse):
        for j, square in enumerate(line):
            if square == "@":
                r_pos = (i,j)

    for movement in movements:
        r_pos = moveRobot(warehouse, *r_pos, dir=movement)

    total = 0
    for i, line in enumerate(warehouse):
        for j, square in enumerate(line):
            if square == 'O':
                total += 100*i + j
    print(total)

def recurmove(warehouse, i: int, j: int, dir: str):
    new_i, new_j, passable = move(warehouse, i, j, dir)
    if not passable:
        return i, j, passable
    if warehouse[new_i][new_j] != '.':
        _,_, passable = recurmove(warehouse, new_i, new_j, dir)
    if dir == '^' or dir == 'v':
        if warehouse[new_i][new_j] == '[':
            _,_, _passable = recurmove(warehouse, new_i, new_j+1, dir)
            passable = passable and _passable
        elif warehouse[new_i][new_j] == ']':
            _,_, _passable = recurmove(warehouse, new_i, new_j-1, dir)
            passable = passable and _passable
    return new_i, new_j, passable

def moveWide(warehouse, i: int, j: int, dir: str, flag: bool = False):
    value = warehouse[i][j]
    if value == '.':
        return i, j

    twin_pos = None
    if dir == '^' or dir == 'v':
        if value == '[':
            twin_pos = (i, j+1)
        elif value == ']':
            twin_pos = (i, j-1)

    new_i, new_j, passable = recurmove(warehouse, i, j, dir)
    new_i2, new_j2 = new_i, new_j
    if twin_pos:
        new_i2, new_j2, _passable = recurmove(warehouse, *twin_pos, dir)
        passable = passable and _passable

    if not passable:
        return i,j

    moveWide(warehouse, new_i, new_j, dir)
    moveWide(warehouse, new_i2, new_j2, dir)

    if twin_pos and flag is False:
        moveWide(warehouse, *twin_pos, dir, True)

    if warehouse[new_i][new_j] != '.':
        return i, j
    warehouse[new_i][new_j] = value
    warehouse[i][j] = '.'

    return new_i, new_j


def part2(filename):
    warehouse = []
    movements = ""
    with open(filename) as fp:
        for line in fp.readlines():
            if '#' in line:
                row = list(line.strip())
                def convert(ch):
                    if ch == 'O':
                        return ['[', ']']
                    elif ch == '@':
                        return ['@', '.']
                    else:
                        return [ch, ch]
                new_row = list(chain(*[convert(ch) for ch in row]))
                warehouse.append(new_row)
            else:
                movements += line.strip()

    r_pos = None
    for i, line in enumerate(warehouse):
        for j, square in enumerate(line):
            if square == "@":
                r_pos = (i,j)

    for movement in movements:
        r_pos = moveWide(warehouse, *r_pos, dir=movement)

    total = 0
    for i, line in enumerate(warehouse):
        for j, square in enumerate(line):
            if square == '[':
                total += 100*i + j
    print(total)


if __name__ == "__main__":
    filename = "example.txt"
    filename = "example_small.txt"
    filename = "input.txt"

    t0 = time.perf_counter_ns()
    part1(filename)
    t1 = time.perf_counter_ns()
    part2(filename)
    t2 = time.perf_counter_ns()
    print(f"Part 1: {(t1-t0)/1e9} s")
    print(f"Part 2: {(t2-t1)/1e9} s")
