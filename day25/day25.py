
def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    return [list(line) for line in text.splitlines()]


def print_cukes(cukes):
    print("\n".join("".join(row) for row in cukes))


def part1():
    cukes = read_input()
    width = len(cukes[0])
    height = len(cukes)
    step = 0

    while True:
        step += 1
        moved = False
        next_cukes = [list(row) for row in cukes]
        # move east
        for y in range(height):
            for x in range(width):
                cuke = cukes[y][x]
                if cuke != ">":
                    continue
                nx = (x + 1) % width
                if cukes[y][nx] == ".":
                    next_cukes[y][x] = "."
                    next_cukes[y][nx] = ">"
                    moved = True
        cukes = next_cukes
        next_cukes = [list(row) for row in cukes]
        # move south
        for y in range(height):
            for x in range(width):
                cuke = cukes[y][x]
                if cuke != "v":
                    continue
                ny = (y + 1) % height
                if cukes[ny][x] == ".":
                    next_cukes[y][x] = "."
                    next_cukes[ny][x] = "v"
                    moved = True
        # check if done moving
        if not moved:
            break
        cukes = next_cukes
    return step


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
