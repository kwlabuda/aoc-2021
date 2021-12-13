
def parse_text(text, sep=None, trans=None):
    if not trans:
        trans = lambda x: x
    return [trans(s) for s in text.split(sep)]


def parse_point(text):
    x, y = text.split(",")
    return int(x), int(y)


def parse_fold(text):
    k, v = text.split("=")
    return k[-1], int(v)


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    dots, folds = parse_text(text, "\n\n")
    dots = parse_text(dots, "\n", parse_point)
    folds = parse_text(folds, "\n", parse_fold)
    return dots, folds


def print_paper(dots):
    x_end, y_end = max(dots)
    for y in range(y_end + 1):
        line = ""
        for x in range(x_end + 1):
            line += "#" if (x, y) in dots else "."
        print(line)
    print()


def fold_paper(one_fold):
    dots, folds = read_input()
    dots = set(dots)
    if one_fold:
        folds = folds[:1]
    for axis, pos in folds:
        new_dots = set()
        for x, y in dots:
            if axis == "x":
                if x > pos:
                    x = pos - (x - pos)
            elif axis == "y":
                if y > pos:
                    y = pos - (y - pos)
            new_dots.add((x, y))
        dots = new_dots
    return dots


def part1():
    dots = fold_paper(True)
    return len(dots)


def part2():
    dots = fold_paper(False)
    print_paper(dots)


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    part2()
