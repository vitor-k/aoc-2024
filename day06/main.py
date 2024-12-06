
from enum import Enum
from copy import deepcopy

class direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

def guardmove(guard_map, posx: int, posy: int, dir: direction):
    if dir == direction.UP:
        if posy <= 0:
            return None
        elif guard_map[posy-1][posx] == '#':
            dir = direction.RIGHT
        else:
            posy = posy - 1
    elif dir == direction.RIGHT:
        if posx >= len(guard_map[0]) - 1:
            return None
        elif guard_map[posy][posx+1] == '#':
            dir = direction.DOWN
        else:
            posx = posx + 1
    elif dir == direction.DOWN:
        if posy >= len(guard_map) - 1:
            return None
        elif guard_map[posy+1][posx] == '#':
            dir = direction.LEFT
        else:
            posy = posy + 1
    elif dir == direction.LEFT:
        if posx <= 0:
            return None
        elif guard_map[posy][posx-1] == '#':
            dir = direction.UP
        else:
            posx = posx - 1
    return (posx, posy, dir)

def part1(filename):
    guard_map = []
    with open(filename) as fp:
        for line in fp.readlines():
            guard_map.append(list(line.strip()))
    original_guard_map = deepcopy(guard_map)

    guard_posy = None
    guard_posx = None
    guarddir = direction.UP
    for i, line in enumerate(guard_map):
        if "^" in line:
            guard_posy = i
            guard_posx = line.index("^")
            line[guard_posx] = "X"
    original_pos = (guard_posx, guard_posy)

    run = True
    while (guard := guardmove(guard_map, guard_posx, guard_posy, guarddir)):
        guard_posx, guard_posy, guarddir = guard
        guard_map[guard_posy][guard_posx] = 'X'

    print(sum(line.count('X') for line in guard_map))

    ## Part 2
    #  ----------------------------------------------------------------------
    possible_obstructions = 0

    # Remove the starting guard position from possible locations
    guard_map[original_pos[1]][original_pos[0]] = '.'
    possible_locations = []
    for i, line in enumerate(guard_map):
        for j, ch in enumerate(line):
            if ch == 'X':
                possible_locations.append((i, j))

    # This is rather slow due to bruteforce but it works
    for i,j in possible_locations:
        guard_posx, guard_posy = original_pos
        guarddir = direction.UP
        guard_map = deepcopy(original_guard_map)
        guard_map[i][j] = '#'

        visited_locations = []
        visited_locations.append((guard_posx, guard_posy, guarddir))
        while (guard := guardmove(guard_map, guard_posx, guard_posy, guarddir)):
            if guard in visited_locations:
                possible_obstructions += 1
                break
            visited_locations.append(guard)
            guard_posx, guard_posy, guarddir = guard

    print(possible_obstructions)

if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    part1(filename)
