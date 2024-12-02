
def checkSafe(report):
    differences = set([x-y for x,y in zip(report[1:], report[:-1])])
    if differences <= set([1,2,3]) or differences <= set([-1, -2, -3]):
        return True
    return False

def part1():
    safe = 0
    with open("input.txt") as fp:
        for line in fp.readlines():
            report = [int(x) for x in line.strip().split()]
            # reports.append(report)
            safe += checkSafe(report)
    print(safe)


def part2():
    safe = 0
    with open("input.txt") as fp:
        for line in fp.readlines():
            report = [int(x) for x in line.strip().split()]

            if checkSafe(report):
                safe += 1
            else:
                for i,x in enumerate(report):
                    new_report = report[:]
                    new_report.pop(i)
                    if checkSafe(new_report):
                        safe += 1
                        break
    print(safe)

if __name__ == "__main__":
    part1()
    part2()
