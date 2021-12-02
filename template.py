import re


def read_int_list():
    lines = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            entry = int(line)
            lines.append(entry)
    return lines


def part1():
    pass


def part2():
    pass


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
