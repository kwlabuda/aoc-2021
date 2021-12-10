
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


def adjacent_points(x, y):
    points = []
    if x > 0:
        points.append((x - 1, y))
    if x < X_END:
        points.append((x + 1, y))
    if y > 0:
        points.append((x, y - 1))
    if y < Y_END:
        points.append((x, y + 1))
    return points


def is_lowpoint(x, y):
    h = HMAP[y][x]
    pts = adjacent_points(x, y)
    return all(HMAP[v][u] > h for u, v in pts)


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


def get_basin(x, y):
    basin = set()
    stack = [(x, y)]
    while len(stack) > 0:
        x, y = stack.pop()
        if (x, y) in basin:
            continue
        if HMAP[y][x] == 9:
            continue
        basin.add((x, y))
        stack += adjacent_points(x, y)
    return basin


def part2():
    low_points = get_lowpoints()
    sizes = []
    for x, y in low_points:
        basin = get_basin(x, y)
        sizes.append(len(basin))
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
