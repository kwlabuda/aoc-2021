
def parse_text(text, sep=None, trans=None):
    if not trans:
        trans = lambda x: x
    return [trans(s) for s in text.split(sep)]


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    trans = lambda x: x
    return parse_text(text, "\n", trans)


def part1():
    pass


def part2():
    pass


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
