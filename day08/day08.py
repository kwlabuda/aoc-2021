
def parse_text(text, sep=None, trans=None):
    if not trans:
        trans = lambda x: x
    return [trans(s) for s in text.split(sep)]


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    trans = lambda x: tuple(parse_text(x, "|", parse_text))
    return parse_text(text, "\n", trans)


# Segments: Digits
# 2: 1
# 3: 7
# 4: 4
# 5: 2, 3, 5
# 6: 0, 6, 9
# 7: 8


def part1():
    entries = read_input()
    total = 0
    segments = {2, 3, 4, 7}
    for _, output in entries:
        total += sum(1 for s in output if len(s) in segments)
    return total


def find_subset(subset, set_list):
    for i in range(len(set_list)):
        if subset < set_list[i]:
            return set_list.pop(i)


def part2():
    entries = read_input()
    total = 0
    for patterns, output in entries:
        digits = [None for _ in range(10)]
        fives = []
        sixes = []
        # find 1, 4, 7, 8
        for pattern in patterns:
            size = len(pattern)
            pat_set = set(pattern)
            if size == 2:
                digits[1] = pat_set
            elif size == 4:
                digits[4] = pat_set
            elif size == 3:
                digits[7] = pat_set
            elif size == 7:
                digits[8] = pat_set
            elif size == 5:
                fives.append(pat_set)
            elif size == 6:
                sixes.append(pat_set)

        # digit "3" is only 5-segment that contains "1"
        digits[3] = find_subset(digits[1], fives)
        # digit "5" is only 5-segment that contains "b"
        digits[5] = find_subset(digits[4] - digits[1], fives)
        # digit "2" is last remaining 5-segment
        assert len(fives) == 1
        digits[2] = fives[0]

        # digit "9" is only 6-segment that contains "4"
        digits[9] = find_subset(digits[4], sixes)
        # digit "0" is remaining 6-segment that contains "1"
        digits[0] = find_subset(digits[1], sixes)
        # digit "6" is last remaining of 6-segment
        assert len(sixes) == 1
        digits[6] = sixes[0]

        # get output value and add to total
        sort_str = lambda x: "".join(sorted(x))
        signals = {sort_str(digits[d]): str(d) for d in range(10)}
        num_str = "".join(signals[sort_str(s)] for s in output)
        total += int(num_str)
    return total


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
