from collections import defaultdict
import re


def read_lines():
    lines = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            match = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line)
            entry = (int(d) for d in match.groups())
            lines.append(entry)
    return lines


def count_points(allow_diagonal):
    lines = read_lines()
    points = defaultdict(int)
    for line in lines:
        x1, y1, x2, y2 = line
        x_delta = None
        y_delta = None
        num_pts = None
        if x1 == x2:
            # vertical
            x_delta = 0
            y_delta = 1 if y1 < y2 else -1
            num_pts = abs(y2 - y1) + 1
        elif y1 == y2:
            # horizontal
            y_delta = 0
            x_delta = 1 if x1 < x2 else -1
            num_pts = abs(x2 - x1) + 1
        else:
            # diagonal
            if not allow_diagonal:
                continue
            x_delta = 1 if x1 < x2 else -1
            y_delta = 1 if y1 < y2 else -1
            num_pts = abs(x2 - x1) + 1
        for _ in range(num_pts):
            points[(x1, y1)] += 1
            x1 += x_delta
            y1 += y_delta
    return sum(1 for c in points.values() if c >= 2)


if __name__ == "__main__":
    print(f"Part 1:")
    print(count_points(False))
    print(f"Part 2:")
    print(count_points(True))
