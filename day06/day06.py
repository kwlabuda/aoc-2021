
def read_fish():
    with open("input.txt") as f:
        line = f.read().strip()
    return [int(d) for d in line.split(",")]


def part1():
    fish = read_fish()
    num_days = 80
    for _ in range(num_days):
        new_fish = []
        for i in range(len(fish)):
            f = fish[i]
            if f == 0:
                fish[i] = 6
                new_fish.append(8)
            else:
                fish[i] = f - 1
        fish += new_fish
    return len(fish)


def part2():
    # get counts of initial fish
    initial_fish = read_fish()
    fish = [0 for _ in range(9)]
    for f in initial_fish:
        fish[f] += 1
    # go through each day
    num_days = 256
    for _ in range(num_days):
        fish0 = fish[0]
        for i in range(1, 9):
            fish[i - 1] = fish[i]
        fish[6] += fish0
        fish[8] = fish0
    return sum(fish)


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
