from collections import defaultdict


def parse_text(text, sep=None, trans=None):
    if not trans:
        trans = lambda x: x
    return [trans(s) for s in text.split(sep)]


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    trans = lambda x: tuple(x.split("-"))
    return parse_text(text, "\n", trans)


START = "start"
END = "end"


def find_paths(allow_twice):
    # get graph from input
    pairs = read_input()
    connections = defaultdict(set)
    for a, b in pairs:
        connections[a].add(b)
        connections[b].add(a)
    # visit caves
    paths = 0
    stack = [(START, set(), allow_twice)]
    while len(stack) > 0:
        cave, visited, allow_twice = stack.pop()
        if cave == END:
            paths += 1
            continue
        if cave.islower():
            if cave in visited:
                if not allow_twice or cave == START:
                    continue
                allow_twice = False
            else:
                visited.add(cave)
        for dst in connections[cave]:
            stack.append((dst, set(visited), allow_twice))
    return paths


if __name__ == "__main__":
    print("Part 1:")
    print(find_paths(False))
    print("Part 2:")
    print(find_paths(True))
