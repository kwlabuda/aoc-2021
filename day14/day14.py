from collections import Counter, defaultdict


def parse_text(text, sep=None, trans=None):
    if not trans:
        trans = lambda x: x
    return [trans(s) for s in text.split(sep)]


def parse_rule(text):
    left, right = text.split(" -> ")
    return left, right


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    template, rules = parse_text(text, "\n\n")
    rules = parse_text(rules, "\n", parse_rule)
    rules = {k: v for k, v in rules}
    return template, rules


def get_most_least_diff(polymer):
    counts = Counter(polymer).most_common()
    most = counts[0]
    least = counts[-1]
    return most[1] - least[1]


def part1():
    polymer, rules = read_input()
    for _ in range(10):
        new_polymer = ""
        for i in range(len(polymer) - 1):
            pair = polymer[i:i+2]
            new_polymer += pair[0] + rules[pair]
        polymer = new_polymer + polymer[-1]
    return get_most_least_diff(polymer)


def part2():
    template, rules = read_input()
    # get pair counts
    pair_counts = defaultdict(int)
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        pair_counts[pair] += 1
    # do steps
    for _ in range(40):
        new_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            p1 = pair[0] + rules[pair]
            p2 = rules[pair] + pair[1]
            new_counts[p1] += count
            new_counts[p2] += count
        pair_counts = new_counts
    # get element counts by counting first item in each pair
    elem_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        elem_counts[pair[0]] += count
    # account for last item
    elem_counts[template[-1]] += 1
    return get_most_least_diff(elem_counts)


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
