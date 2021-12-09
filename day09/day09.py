
def parse_text(text, sep=None, trans=None):
    if not trans:
        trans = lambda x: x
    return [trans(s) for s in text.split(sep)]


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    trans = lambda x: [int(h) for h in x]
    return parse_text(text, "\n", trans)


HMAP = read_input()
WIDTH = len(HMAP[0])
HEIGHT = len(HMAP)
X_END = WIDTH - 1
Y_END = HEIGHT - 1


def is_lowpoint(x, y):
    h = HMAP[y][x]
    if x > 0 and HMAP[y][x - 1] <= h:
        return False
    if x < X_END and HMAP[y][x + 1] <= h:
        return False
    if y > 0 and HMAP[y - 1][x] <= h:
        return False
    if y < Y_END and HMAP[y + 1][x] <= h:
        return False
    return True


def get_lowpoints():
    low_points = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if is_lowpoint(x, y):
                low_points.append((x, y))
    return low_points


def part1():
    low_points = get_lowpoints()
    heights = [HMAP[y][x] for x, y in low_points]
    return sum(heights) + len(low_points)


def get_basin(x, y, basin):
    if (x, y) in basin:
        return
    if HMAP[y][x] == 9:
        return
    basin.add((x, y))
    if x > 0:
        get_basin(x - 1, y, basin)
    if x < X_END:
        get_basin(x + 1, y, basin)
    if y > 0:
        get_basin(x, y - 1, basin)
    if y < Y_END:
        get_basin(x, y + 1, basin)


def part2():
    low_points = get_lowpoints()
    sizes = []
    for x, y in low_points:
        basin = set()
        get_basin(x, y, basin)
        sizes.append(len(basin))
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
