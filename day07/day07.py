
def read_crabs():
    with open("input.txt") as f:
        line = f.read().strip()
    return [int(d) for d in line.split(",")]


def get_median(lst):
    lst.sort()
    count = len(lst)
    mid = count // 2
    if count % 2 == 0:
        return (lst[mid - 1] + lst[mid]) // 2
    return lst[mid]


def part1():
    crabs = read_crabs()
    med = get_median(crabs)
    return sum(abs(med - c) for c in crabs)


def calc_cost(pos):
    return pos * (pos + 1) // 2


def part2():
    crabs = read_crabs()
    # find best position
    furthest = max(crabs)
    best_pos = None
    best_cost = calc_cost(furthest) * len(crabs)
    for x in range(0, furthest + 1):
        cost = sum(calc_cost(abs(x - c)) for c in crabs)
        if cost < best_cost:
            best_pos = x
            best_cost = cost
    return best_cost


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
