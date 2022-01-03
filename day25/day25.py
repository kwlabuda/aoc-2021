
def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    cukes = [line for line in text.splitlines()]
    east_cukes = set()
    south_cukes = set()
    width = len(cukes[0])
    height = len(cukes)
    for y in range(height):
        for x in range(width):
            cuke = cukes[y][x]
            if cuke == ">":
                east_cukes.add((x, y))
            elif cuke == "v":
                south_cukes.add((x, y))
    return east_cukes, south_cukes, width, height


def print_cukes(cukes):
    print("\n".join("".join(row) for row in cukes))


def move_herd(cukes, other, dx, dy, width, height):
    moved = False
    next_cukes = set()
    for x, y in cukes:
        # move by (dx, dy)
        nx = (x + dx) % width
        ny = (y + dy) % height
        pt = (nx, ny)
        if pt in cukes or pt in other:
            # can't move cuke
            next_cukes.add((x, y))
        else:
            # move cuke
            next_cukes.add(pt)
            moved = True
    return next_cukes, moved


def part1():
    east_cukes, south_cukes, width, height = read_input()
    step = 0
    while True:
        step += 1
        # move east
        east_cukes, east_moved = move_herd(
            east_cukes, south_cukes, 1, 0, width, height)
        # move south
        south_cukes, south_moved = move_herd(
            south_cukes, east_cukes, 0, 1, width, height)
        # check if done moving
        if not east_moved and not south_moved:
            break
    return step


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
