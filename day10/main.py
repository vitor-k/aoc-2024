
import time

def climb(hmap, i: int, j: int):
    value = hmap[i][j]

    paths = []
    if i <= 0:
        pass
    elif hmap[i-1][j] == value + 1:
        paths.append((i-1, j))

    if j >= len(hmap[0]) - 1:
        pass
    elif hmap[i][j+1] == value + 1:
        paths.append((i, j+1))

    if i >= len(hmap) - 1:
        pass
    elif hmap[i+1][j] == value + 1:
        paths.append((i+1, j))

    if j <= 0:
        pass
    elif hmap[i][j-1] == value + 1:
        paths.append((i,j-1))

    return paths

def recusive_climb(hmap, i, j):

    if hmap[i][j] == 9:
        return set([(i,j)]), 1

    paths = climb(hmap, i, j)
    score = set()
    rating = 0
    for path in paths:
        path_score, path_rating = recusive_climb(hmap, *path)
        score |= path_score
        rating += path_rating

    return score, rating

def part12(filename):
    hmap = []
    with open(filename) as fp:
        for line in fp.readlines():
            hmap.append(list(map(int, line.strip())))

    trailheads = []
    for i, line in enumerate(hmap):
        for j, value in enumerate(line):
            if value == 0:
                trailheads.append((i,j))

    score = 0
    rating = 0
    for trailhead in trailheads:
        trailhead_score, trailhead_rating = recusive_climb(hmap, *trailhead)
        score += len(trailhead_score)
        rating += trailhead_rating

    print(score)
    print(rating)

if __name__ == "__main__":
    filename = "example_small.txt"
    filename = "example_large.txt"
    filename = "input.txt"

    t0 = time.perf_counter_ns()
    part12(filename)
    t1 = time.perf_counter_ns()
    print(f"{(t1-t0)/1e9} s")
