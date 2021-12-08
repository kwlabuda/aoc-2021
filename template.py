import re


def read_input(sep, trans):
    with open("input.txt") as f:
        text = f.read().strip()
    return parse_text(text, sep, trans)


def parse_text(text, sep, trans):
    return [trans(s) for s in text.split(sep)]


def part1():
    pass


def part2():
    pass


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
