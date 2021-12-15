
def read_list():
    lines = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            s1, s2 = line.split()
            entry = (s1, int(s2))
            lines.append(entry)
    return lines


CMDS = read_list()
FWD = "forward"
DOWN = "down"
UP = "up"


def part1():
    depth = 0
    x_pos = 0
    for move, amt in CMDS:
        if move == FWD:
            x_pos += amt
        elif move == DOWN:
            depth += amt
        elif move == UP:
            depth -= amt
        else:
            raise ValueError("Invalid move")
    print(f"Depth: {depth}, X: {x_pos}")
    return depth * x_pos


def part2():
    depth = 0
    x_pos = 0
    aim = 0
    for move, amt in CMDS:
        if move == FWD:
            x_pos += amt
            depth += aim * amt
        elif move == DOWN:
            aim += amt
        elif move == UP:
            aim -= amt
        else:
            raise ValueError("Invalid move")
    print(f"Depth: {depth}, X: {x_pos}")
    return depth * x_pos


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
