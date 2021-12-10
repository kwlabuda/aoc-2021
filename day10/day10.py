
def parse_text(text, sep=None, trans=None):
    if not trans:
        trans = lambda x: x
    return [trans(s) for s in text.split(sep)]


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    trans = lambda x: x.strip()
    return parse_text(text, "\n", trans)


OPEN = {"(", "[", "{", "<"}
PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"}
POINTS1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
POINTS2 = {"(": 1, "[": 2, "{": 3, "<": 4}


def parse_line(line):
    stack = []
    for c in line:
        if c in OPEN:
            stack.append(c)
        elif c in PAIRS:
            if stack.pop() != PAIRS[c]:
                return POINTS1[c], stack
    return 0, stack


def part1():
    lines = read_input()
    total = 0
    for line in lines:
        pts, _ = parse_line(line)
        total += pts
    return total


def part2():
    lines = read_input()
    scores = []
    for line in lines:
        pts, stack = parse_line(line)
        if pts != 0:
            continue
        stack.reverse()
        pts = 0
        for c in stack:
            pts *= 5
            pts += POINTS2[c]
        scores.append(pts)
    scores.sort()
    idx = len(scores) // 2
    return scores[idx]


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
