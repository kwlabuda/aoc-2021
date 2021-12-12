
def parse_text(text, sep=None, trans=None):
    if not trans:
        trans = lambda x: x
    return [trans(s) for s in text.split(sep)]


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    trans = lambda x: [int(c) for c in x]
    return parse_text(text, "\n", trans)


ADJ = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]

def in_bounds(grid, x, y):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)


def get_adjacent(grid, x, y):
    points = [(x + dx, y + dy) for dx, dy in ADJ]
    return [(x, y) for x, y in points if in_bounds(grid, x, y)]


def print_grid(grid):
    for row in grid:
        print("".join(str(c) for c in row))
    print()


def do_step(octopi):
    # increase all by 1
    height = len(octopi)
    width = len(octopi[0])
    stack = []
    for y in range(height):
        for x in range(width):
            octopi[y][x] += 1
            if octopi[y][x] > 9:
                stack.append((x, y))
    # handle flashes
    flashed = set()
    while len(stack) > 0:
        x, y = stack.pop()
        if octopi[y][x] > 9:
            if (x, y) in flashed:
                continue
            flashed.add((x, y))
            for u, v in get_adjacent(octopi, x, y):
                octopi[v][u] += 1
                stack.append((u, v))
    # reset
    for x, y in flashed:
        octopi[y][x] = 0
    return len(flashed)


def part1():
    octopi = read_input()
    return sum(do_step(octopi) for _ in range(100))


def part2():
    octopi = read_input()
    all_octopi = len(octopi[0]) * len(octopi)
    step = 0
    while True:
        flashes = do_step(octopi)
        step += 1
        if flashes == all_octopi:
            return step


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
