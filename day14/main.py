
import time
import re

def part1(filename):
    robots = []
    with open(filename) as fp:
        for line in fp.readlines():
            if len(line.strip()) == 0:
                continue
            matched = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
            x,y,vx,vy = map(int, matched.groups())
            robots.append([x,y,vx,vy])

    width, height = 101, 103
    dt = 100
    if filename == "example.txt":
        width, height = 11, 7

    quadrants = [0,0,0,0]
    for robot in robots:
        position = (robot[0] + dt * robot[2]) % width, (robot[1] + dt * robot[3]) % height
        if position[0] < width // 2 and position[1] < height // 2:
            quadrants[0] += 1
        if position[0] > width // 2 and position[1] < height // 2:
            quadrants[1] += 1
        if position[0] > width // 2 and position[1] > height // 2:
            quadrants[2] += 1
        if position[0] < width // 2 and position[1] > height // 2:
            quadrants[3] += 1

    sf = 1
    for q in quadrants:
        sf *= q
    print(sf)

def part2(filename):
    robots = []
    with open(filename) as fp:
        for line in fp.readlines():
            if len(line.strip()) == 0:
                continue
            matched = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
            x,y,vx,vy = map(int, matched.groups())
            robots.append([x,y,vx,vy])

    width, height = 101, 103
    if filename == "example.txt":
        width, height = 11, 7

    for t in range(72,1000000, 103):
        positions = set()
        quadrants = [0,0,0,0]
        for robot in robots:
            position = (robot[0] + t * robot[2]) % width, (robot[1] + t * robot[3]) % height
            positions.add(position)
            if position[0] < width // 2 and position[1] < height // 2:
                quadrants[0] += 1
            if position[0] > width // 2 and position[1] < height // 2:
                quadrants[1] += 1
            if position[0] > width // 2 and position[1] > height // 2:
                quadrants[2] += 1
            if position[0] < width // 2 and position[1] > height // 2:
                quadrants[3] += 1
        quadrants.sort()
        # if sum(quadrants[2:]) > 2* sum(quadrants[:2]):
        #     print(t)
        print(t)
        for i in range(height):
            for j in range(width):
                if (j,i) in positions:
                    print('*', end='')
                else:
                    print('.', end='')
            print()
        input()

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
