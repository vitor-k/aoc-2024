
from itertools import permutations

def part1(filename):

    antennas = {}
    width = None
    height = None
    with open(filename) as fp:
        for i, line in enumerate(fp.readlines()):
            height = i
            if not width:
                width = len(line.strip())
            for j, ch in enumerate(line.strip()):
                if ch == '.':
                    continue
                else:
                    if ch in antennas:
                        antennas[ch].append((i,j))
                    else:
                        antennas[ch] = [(i,j)]
    height += 1

    antinodes = set()
    for antenna, locations in antennas.items():
        for a,b in permutations(locations, 2):
            antinode = (2*b[0] - a[0], 2*b[1] -a[1])
            if (0 <= antinode[0] < height) and (0 <= antinode[1] < width):
                antinodes.add(antinode)
    print(len(antinodes))


def part2(filename):
    antennas = {}
    width = None
    height = None
    with open(filename) as fp:
        for i, line in enumerate(fp.readlines()):
            height = i
            if not width:
                width = len(line.strip())
            for j, ch in enumerate(line.strip()):
                if ch == '.':
                    continue
                else:
                    if ch in antennas:
                        antennas[ch].append((i,j))
                    else:
                        antennas[ch] = [(i,j)]
    height += 1

    antinodes = set()
    for antenna, locations in antennas.items():
        for a,b in permutations(locations, 2):
            for i in range(max(width, height)):
                antinode = (b[0] + i*(b[0] - a[0]), b[1] + i*(b[1] -a[1]))
                if (0 <= antinode[0] < height) and (0 <= antinode[1] < width):
                    antinodes.add(antinode)
                else:
                    break
    print(len(antinodes))


if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    part1(filename)
    part2(filename)
