
def part1():
    left = []
    right = []
    with open("input.txt") as fp:
        for line in fp.readlines():
            l, r = map(int, line.strip().split())
            left.append(l)
            right.append(r)
    print(sum(map(lambda tup: abs(tup[0]-tup[1]), zip(sorted(left), sorted(right)))))

def part2():
    left = []
    right = []
    with open("input.txt") as fp:
        for line in fp.readlines():
            l, r = map(int, line.strip().split())
            left.append(l)
            right.append(r)

    score = 0
    for n in left:
        score += n * right.count(n)

    print(score)

if __name__ == "__main__":
    part1()
    part2()
