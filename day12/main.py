
import time
from enum import IntEnum
from itertools import chain

def neighbours(hmap, i: int, j: int):
    value = hmap[i][j]

    if i > 0 and hmap[i-1][j] == value:
        yield (i-1, j)

    if j + 1 < len(hmap[0]) and hmap[i][j+1] == value:
        yield (i, j+1)

    if i + 1 < len(hmap) and hmap[i+1][j] == value:
        yield (i+1, j)

    if j > 0 and hmap[i][j-1] == value:
        yield (i,j-1)

def perimeter(hmap, i: int, j: int):
    return 4 - len(list(neighbours(hmap, i, j)))

def clusterize(hmap, i: int, j: int, cluster: set|None = None):
    if cluster is None:
        cluster = set()

    cluster |= set([(i,j)])

    for neighbour in neighbours(hmap, i, j):
        if neighbour not in cluster:
            cluster |= clusterize(hmap, *neighbour, cluster=cluster)
    return cluster


def part1(filename):
    farm = []
    with open(filename) as fp:
        for line in fp.readlines():
            farm.append(list(line.strip()))

    regions = {}
    for i, line in enumerate(farm):
        for j, plot in enumerate(line):
            if plot in regions:
                for region in regions[plot]:
                    if (i,j) in region:
                        break
                else:
                    regions[plot].append(clusterize(farm, i, j))
            else:
                regions[plot] = [clusterize(farm, i, j)]

    total = 0
    for plant, clusters in regions.items():
        for cluster in clusters:
            area, per = len(cluster), sum(perimeter(farm,i,j) for i,j in cluster)
            total += area * per

    print(total)


class direction(IntEnum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __lt__(self, other) -> bool:
        if self.x == other.x:
            return self.y < other.y
        if self.y == other.y:
            return self.x < other.x
        return False
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    def __hash__(self):
        return hash(tuple((self.x, self.y)))

class Line:
    def __init__(self, p1: Point, p2: Point, dir: direction):
        self.p1 = p1
        self.p2 = p2
        self.dir = dir

    def __repr__(self):
        return f"Line(p1={self.p1}, p2={self.p2})"

    def __eq__(self, other):
        return (self.p1 == other.p1 and self.p2 == other.p2) or (self.p1 == other.p2 and self.p2 == other.p1)

    def __hash__(self):
        return hash(tuple((min(self.p1, self.p2), max(self.p1, self.p2))))

    def colinear(self, other):
        d1 = self.p2 - self.p1
        d2 = other.p2 - other.p1
        match d1, d2:
            case (Point(x=0,y=0), _) | (_, Point(x=0,y=0)):
                return False
            case Point(x=x1, y=0), Point(x=x2, y=0) if self.p1.y == other.p1.y:
                return True
            case Point(x=0, y=y1), Point(x=0, y=y2) if self.p1.x == other.p1.x:
                return True
            case _:
                return False

    def join(self, other):
        if not self.colinear(other) or self.dir != other.dir:
            return None
        if self.p2 == other.p1:
            return Line(self.p1, other.p2, self.dir)
        elif self.p1 == other.p2:
            return Line(other.p1, self.p2, self.dir)

    @staticmethod
    def fromPlot(i:int, j:int, dir: direction):
        if dir == direction.UP:
            p1 = Point(j , i)
            p2 = Point(j+1 , i)
        elif dir == direction.RIGHT:
            p1 = Point(j+1, i)
            p2 = Point(j+1, i+1)
        elif dir == direction.DOWN:
            p1 = Point(j , i+1)
            p2 = Point(j+1, i+1)
        elif dir == direction.LEFT:
            p1 = Point(j , i)
            p2 = Point(j , i+1)
        return Line(p1, p2, dir)

def freeSides(hmap, i: int, j: int):
    value = hmap[i][j]

    if i <= 0 or hmap[i-1][j] != value:
        yield Line.fromPlot(i, j, direction.UP)

    if j + 1 >= len(hmap[0]) or hmap[i][j+1] != value:
        yield Line.fromPlot(i, j, direction.RIGHT)

    if i + 1 >= len(hmap) or hmap[i+1][j] != value:
        yield Line.fromPlot(i, j, direction.DOWN)

    if j <= 0 or hmap[i][j-1] != value:
        yield Line.fromPlot(i, j, direction.LEFT)

def sides(farm, cluster):
    sideset = list(chain(*filter(None, [list(freeSides(farm, *x)) for x in cluster])))
    sideset = set(sideset)
    change = True
    while change:
        change = False
        for side1 in sideset:
            for side2 in sideset:
                if side1 == side2:
                    continue
                if (side3 := side1.join(side2)):
                    sideset.add(side3)
                    sideset -= set((side1, side2))
                    change = True
                    break
            if change:
                break

    return sideset


def part2(filename):
    farm = []
    with open(filename) as fp:
        for line in fp.readlines():
            farm.append(list(line.strip()))

    regions = {}
    for i, line in enumerate(farm):
        for j, plot in enumerate(line):
            if plot in regions:
                for region in regions[plot]:
                    if (i,j) in region:
                        break
                else:
                    regions[plot].append(clusterize(farm, i, j))
            else:
                regions[plot] = [clusterize(farm, i, j)]

    total = 0
    for plant, clusters in regions.items():
        for cluster in clusters:
            area, sideset = len(cluster), sides(farm, cluster)
            total += area * len(sideset)

    print(total)

if __name__ == "__main__":
    filename = "example_small.txt"
    filename = "example_small_2.txt"
    filename = "example_small_3.txt"
    filename = "example_small_4.txt"
    filename = "example_large.txt"
    filename = "input.txt"

    t0 = time.perf_counter_ns()
    part1(filename)
    t1 = time.perf_counter_ns()
    part2(filename)
    t2 = time.perf_counter_ns()
    print(f"Part 1: {(t1-t0)/1e9} s")
    print(f"Part 2: {(t2-t1)/1e9} s")
