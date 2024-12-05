
ordering = []

class PageNumber():
    def __init__(self, number) -> None:
        self.number = number
    def __lt__(self, other) -> bool:
        if (self.number, other.number) in ordering:
            return True
        else:
            return False
    def __str__(self) -> str:
        return str(self.number)
    def __repr__(self) -> str:
        return str(self.number)

def part1(filename):
    ordering.clear()
    with open(filename) as fp:
        middle_page_numbers = 0
        for line in fp.readlines():
            if not line.strip():
                continue
            if '|' in line:
                n1, n2 = map(int, line.strip().split('|'))
                ordering.append((n1,n2))
            else:
                numbers = list(map(int, line.strip().split(',')))
                numbers = [PageNumber(n) for n in numbers]

                if numbers == sorted(numbers):
                    middle_page_numbers += numbers[len(numbers)//2].number

        print(middle_page_numbers)

def part2(filename):
    ordering.clear()
    with open(filename) as fp:
        middle_page_numbers = 0
        for line in fp.readlines():
            if not line.strip():
                continue
            if '|' in line:
                n1, n2 = map(int, line.strip().split('|'))
                ordering.append((n1,n2))
            else:
                numbers = list(map(int, line.strip().split(',')))
                numbers = [PageNumber(n) for n in numbers]

                if numbers != sorted(numbers):
                    numbers.sort()
                    middle_page_numbers += numbers[len(numbers)//2].number

        print(middle_page_numbers)

if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    part1(filename)
    part2(filename)
