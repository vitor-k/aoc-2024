
import time
from functools import cache
from itertools import chain
from enum import IntEnum
from math import inf

class Direction(IntEnum):
    UP = 1
    RIGHT = 2
    DOWN = 4
    LEFT = 8

    @staticmethod
    def opposites(a,b):
        if a+b == 5: # UP and DOWN
            return True
        if a+b == 10: # LEFT and RIGHT
            return True
        return False
    
    def opposite(self):
        match self:
            case Direction.UP:
                return Direction.DOWN
            case Direction.RIGHT:
                return Direction.LEFT
            case Direction.DOWN:
                return Direction.UP
            case Direction.LEFT:
                return Direction.RIGHT

class Node:
    def __init__(self, i,j, dir, edges):
        self.i = i
        self.j = j
        self.dir = dir
        self.edges = edges
        self.start = False
        self.end = False
        self.distance = inf
    def setStart(self):
        self.start = True
        self.distance = 0
    def ij(self):
        return (self.i, self.j)
    def getKey(self):
        return (self.i, self.j, self.dir)
    def __lt__(self, other):
        return self.distance < other.distance

def neighbours(track, i: int, j: int):
    if i > 0 and track[i-1][j] != '#':
        yield (i-1, j, Direction.UP)

    if j + 1 < len(track[0]) and track[i][j+1] != '#':
        yield (i, j+1, Direction.RIGHT)

    if i + 1 < len(track) and track[i+1][j] != '#':
        yield (i+1, j, Direction.DOWN)

    if j > 0 and track[i][j-1] != '#':
        yield (i,j-1, Direction.LEFT)

def buildGraph(track, graph, i: int, j: int, dir: Direction):

    ungraphed = [(i,j,dir)]

    while ungraphed:
        i,j,dir = ungraphed.pop()
        nbs = neighbours(track, i, j)

        node = Node(i,j,dir, [])
        for nb in nbs:
            node.edges.append(nb)
            if nb not in graph:
                ungraphed.append(nb)
        graph[(i,j,dir)] = node


def djikstra(graph):
    unvisited = set(graph.values())

    while unvisited:
        current = min(unvisited)
        if current.end:
            return current
        for edge in current.edges:
            neighbour = graph[edge]
            if neighbour not in unvisited:
                continue
            distance = current.distance+1
            if neighbour.dir != current.dir:
                distance += 1000
            neighbour.distance = min(neighbour.distance, distance)
        unvisited.remove(current)

    return None

def backtrack(graph, endnodes):
    best_paths = set()
    best_paths.add(endnodes[0].getKey())

    unvisited = []
    unvisited.extend(endnodes)

    while unvisited:
        node = unvisited.pop()
        for nb in node.edges:
            for dir in Direction:
                nb = (nb[0], nb[1], dir)
                if nb in best_paths:
                    continue
                if nb not in graph:
                    continue
                neighbour = graph[nb]
                if neighbour.dir == node.dir and neighbour.distance == node.distance - 1:
                    unvisited.append(neighbour)
                elif neighbour.distance == node.distance - 1001:
                    unvisited.append(neighbour)
        best_paths.add(node.getKey())

    return set([node[:2] for node in best_paths])

def part1(filename):
    track = []
    with open(filename) as fp:
        for line in fp.readlines():
            if '#' in line:
                track.append(list(line.strip()))
    start = None
    end = None
    for i, line in enumerate(track):
        for j, square in enumerate(line):
            if square == "S":
                start = (i,j)
            if square == "E":
                end = (i,j)
    graph = {}
    buildGraph(track, graph, *start, Direction.RIGHT)
    graph[(*start, Direction.RIGHT)].setStart()
    for key, node in graph.items():
        match key:
            case i, j, dir if (i,j)==end:
                node.end = True
            case _:
                pass
    endnode = djikstra(graph)

    endnodes = [node for node in graph.values() if node.end]
    mindistance = min(node.distance for node in endnodes)
    print(mindistance)

    return graph

def part2(graph):
    endnodes = [node for node in graph.values() if node.end]
    mindistance = min(node.distance for node in endnodes)
    endnodes = [node for node in endnodes if node.distance == mindistance]

    bestpath = backtrack(graph, endnodes)
    print(len(bestpath))

if __name__ == "__main__":
    filename = "example.txt"
    filename = "example2.txt"
    filename = "input.txt"

    t0 = time.perf_counter_ns()
    graph = part1(filename)
    t1 = time.perf_counter_ns()
    part2(graph)
    t2 = time.perf_counter_ns()
    print(f"Part 1: {(t1-t0)/1e9} s")
    print(f"Part 2: {(t2-t1)/1e9} s")
