
import numpy as np

def part1(filename):

    with open(filename) as fp:
        grid = []
        for line in fp.readlines():
            grid.append(list(line.strip()))

        grid = np.array(grid)
        xmas = 0

        # Horizontal
        for i in range(grid.shape[0]):
            line = ''.join(grid[i])
            xmas += line.count("XMAS") + line.count("SAMX")

        # Vertical
        for i in range(grid.shape[1]):
            line = ''.join(grid.T[i])
            xmas += line.count("XMAS") + line.count("SAMX")

        # Diagonals
        for i in range(grid.shape[0]-3):
            for j in range(grid.shape[1]-3):
                diag = grid[i,j]
                for k in range(1,4):
                    diag += grid[i+k,j+k]
                if diag == "XMAS" or diag == "SAMX":
                    xmas += 1
        for i in range(3, grid.shape[0]):
            for j in range(grid.shape[1]-3):
                diag = grid[i,j]
                for k in range(1,4):
                    diag += grid[i-k,j+k]
                if diag == "XMAS" or diag == "SAMX":
                    xmas += 1
    print(xmas)

def part2(filename):
    with open(filename) as fp:
        grid = []

        for line in fp.readlines():
            grid.append(line.strip())

        xmas = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                match grid[i][j], grid[i+2][j], grid[i+1][j+1], grid[i][j+2], grid[i+2][j+2]:
                    case 'M', 'M', 'A', 'S', 'S':
                        xmas += 1
                    case 'S', 'S', 'A', 'M', 'M':
                        xmas += 1
                    case 'M', 'S', 'A', 'M', 'S':
                        xmas += 1
                    case 'S', 'M', 'A', 'S', 'M':
                        xmas += 1
    print(xmas)

if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
