
import time
import numpy as np

def part1(filename):
    machines = []
    with open(filename) as fp:
        a, b, prize = None, None, None
        for line in fp.readlines():
            if len(line.strip()) == 0:
                continue
            if a is None:
                a = [int(s.strip(" XY=")) for s in line.split(":")[1].strip().split(',')]
            elif b is None:
                b = [int(s.strip(" XY=")) for s in line.split(":")[1].strip().split(',')]
            elif prize is None:
                prize = [int(s.strip(" XY=")) for s in line.split(":")[1].strip().split(',')]
                machines.append(np.array([a,b,prize]).T)
                a, b, prize = None, None, None

    total = 0
    for machine in machines:
        if np.linalg.det(machine[:,:2]) == 0:
            continue
        solution = np.linalg.solve(machine[:,:2], machine[:,2:])
        if np.any(np.abs(solution - np.rint(solution)) > np.array([1e-6, 1e-6])):
            continue
        total += (np.array([3,1]) @ solution)[0]

    print(total)

def part2(filename):
    machines = []
    with open(filename) as fp:
        a, b, prize = None, None, None
        for line in fp.readlines():
            if len(line.strip()) == 0:
                continue
            if a is None:
                a = [int(s.strip(" XY=")) for s in line.split(":")[1].strip().split(',')]
            elif b is None:
                b = [int(s.strip(" XY=")) for s in line.split(":")[1].strip().split(',')]
            elif prize is None:
                prize = [int(s.strip(" XY=")) + 10000000000000 for s in line.split(":")[1].strip().split(',')]
                machines.append(np.array([a,b,prize]).T)
                a, b, prize = None, None, None

    total = 0
    for machine in machines:
        if np.linalg.det(machine[:,:2]) == 0:
            continue
        solution = np.linalg.solve(machine[:,:2], machine[:,2:])
        if np.any(np.abs(solution - np.rint(solution)) > np.array([1e-4, 1e-4])):
            continue
        total += (np.array([3,1]) @ solution)[0]

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
