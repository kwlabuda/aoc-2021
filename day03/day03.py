from collections import Counter


def read_int_list():
    lines = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            #entry = int(line)
            lines.append(line)
    return lines


NUMS = read_int_list()


def part1():
    num_bits = len(NUMS[0])
    gamma = ""
    epsilon = ""
    for b in range(num_bits):
        counter = Counter([num[b] for num in NUMS])
        zeros = counter["0"]
        ones = counter["1"]
        if zeros >= ones:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    g = int(gamma, 2)
    e = int(epsilon, 2)
    print(g, e)
    return g * e


def split_by_bits(num_list, bit):
    zeros = []
    ones = []
    for num in num_list:
        if num[bit] == "0":
            zeros.append(num)
        else:
            ones.append(num)
    return zeros, ones


def part2():
    num_bits = len(NUMS[0])
    # oxygen generator rating
    ogr_nums = NUMS
    ogr = None
    for b in range(num_bits):
        zeros, ones = split_by_bits(ogr_nums, b)
        if len(zeros) > len(ones):
            ogr_nums = zeros
        else:
            ogr_nums = ones
        if len(ogr_nums) == 1:
            ogr = int(ogr_nums[0], 2)
            break
    # CO2 scrubber rating
    csr_nums = NUMS
    csr = None
    for b in range(num_bits):
        zeros, ones = split_by_bits(csr_nums, b)
        if len(zeros) > len(ones):
            csr_nums = ones
        else:
            csr_nums = zeros
        if len(csr_nums) == 1:
            csr = int(csr_nums[0], 2)
            break
    print(ogr, csr)
    return ogr * csr


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
