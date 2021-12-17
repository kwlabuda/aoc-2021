import re


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    pattern = r"x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)"
    match = re.search(pattern, text)
    return (int(n) for n in match.groups())


def part1():
    _, _, y1, _ = read_input()
    return sum(range(abs(y1)))


def fire_probe(x_vel, y_vel, x1, x2, y1, y2):
    x = 0
    y = 0
    while x < x2 and y > y1:
        # update position
        x += x_vel
        y += y_vel
        # check if in target
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return True
        # update velocity
        if x_vel > 0:
            x_vel -= 1
        y_vel -= 1
    return False


def part2():
    x1, x2, y1, y2 = read_input()
    min_y_vel = y1
    max_y_vel = abs(y1) - 1
    min_x_vel = 0
    max_x_vel = x2
    velocities = 0

    for y_vel in range(min_y_vel, max_y_vel + 1):
        for x_vel in range(min_x_vel, max_x_vel + 1):
            if fire_probe(x_vel, y_vel, x1, x2, y1, y2):
                velocities += 1
    return velocities


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
