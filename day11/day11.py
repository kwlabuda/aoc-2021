
def parse_text(text, sep=None, trans=None):
    if not trans:
        trans = lambda x: x
    return [trans(s) for s in text.split(sep)]


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    trans = lambda x: [int(c) for c in x]
    return parse_text(text, "\n", trans)


OCTOPI = read_input()
WIDTH = len(OCTOPI[0])
HEIGHT = len(OCTOPI)
ADJ = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]

def in_bounds(x, y):
    return x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT


def get_adjacent(x, y):
    points = [(x + dx, y + dy) for dx, dy in ADJ]
    return [(x, y) for x, y in points if in_bounds(x, y)]


def print_octopi():
    for row in OCTOPI:
        print("".join(str(c) for c in row))
    print()


def do_step():
    # increase all by 1
    stack = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            OCTOPI[y][x] += 1
            if OCTOPI[y][x] > 9:
                stack.append((x, y))
    # handle flashes
    flashed = set()
    while len(stack) > 0:
        x, y = stack.pop()
        if OCTOPI[y][x] > 9:
            if (x, y) in flashed:
                continue
            flashed.add((x, y))
            for u, v in get_adjacent(x, y):
                OCTOPI[v][u] += 1
                stack.append((u, v))
    # reset
    for x, y in flashed:
        OCTOPI[y][x] = 0
    return len(flashed)


def part1():
    return sum(do_step() for _ in range(100))


def part2():
    # this is probably bad form
    global OCTOPI
    OCTOPI = read_input()
    all_octopi = WIDTH * HEIGHT
    step = 0
    while True:
        flashes = do_step()
        step += 1
        if flashes == all_octopi:
            return step


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
