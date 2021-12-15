
def read_int_list():
    with open("input.txt") as f:
        return [int(line) for line in f]


DEPTHS = read_int_list()


def count_increases(depths):
    increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increases += 1
    return increases


def part1():
    return count_increases(DEPTHS)


def part2():
    triplets = []
    for i in range(len(DEPTHS) - 2):
        total = DEPTHS[i] + DEPTHS[i + 1] + DEPTHS[i + 2]
        triplets.append(total)
    return count_increases(triplets)


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
