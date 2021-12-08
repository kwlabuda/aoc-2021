import re


def read_input():
    entries = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            patterns, output = line.split("|")
            p = patterns.split()
            o = output.split()
            entries.append((p, o))
    return entries


# Digit: Segments
# 0: 6
# 1: 2*
# 2: 5
# 3: 5
# 4: 4*
# 5: 5
# 6: 6
# 7: 3*
# 8: 7*
# 9: 6

# Segments: Digits
# 3: 7
# 4: 4
# 5: 2, 3, 5
# 6: 0, 6, 9
# 7: 8


def part1():
    entries = read_input()
    count = 0
    segment_nums = {2, 4, 3, 7}
    for _, output in entries:
        count += sum(1 for d in output if len(d) in segment_nums)
    return count


def find_subset(subset, set_list):
    ans = None
    for s in set_list:
        if subset < s:
            ans = s
            break
    set_list.remove(ans)
    return ans


def find_not_subset(subset, set_list):
    ans = None
    for s in set_list:
        if not subset < s:
            ans = s
            break
    set_list.remove(ans)
    return ans


def part2():
    entries = read_input()
    total = 0
    segment_nums = {2, 4, 3, 7}
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
        # digit "6" is only 6-segment that doesn't contain "1"
        digits[6] = find_not_subset(digits[1], sixes)
        # wire "e" is "3" and "4" removed from "6"
        e_wire = digits[6] - digits[3] - digits[4]
        assert len(e_wire) == 1
        # digit "2" is remaining 5-segment that contains "e"
        digits[2] = find_subset(e_wire, fives)
        # digit "5" is last remaining of 5-segment
        assert len(fives) == 1
        digits[5] = fives[0]
        # digit "0" is remaining 6-segment that contains "e"
        digits[0] = find_subset(e_wire, sixes)
        # digit "9" is last remaining of 6-segment
        assert len(sixes) == 1
        digits[9] = sixes[0]

        # get output value and add to total
        wire_digits = {}
        for d in range(10):
            w = "".join(sorted(digits[d]))
            wire_digits[w] = str(d)
        num_str = ""
        for v in output:
            w = "".join(sorted(v))
            num_str += wire_digits[w]
        total += int(num_str)
    return total


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
