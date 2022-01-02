import random

# pseudo code
# for i = 0, 13
#     w = input()
#     x = z % 26 + [11, 12, 10, -8, 15, 15, -11, 10, -3, 15, -3, -1, -10, -16][i]
#     z /=         [ 1,  1,  1, 26,  1,  1,  26,  1, 26,  1, 26, 26,  26,  26][i]
#     if x != w
#         z *= 26
#         z += w + [ 8,  8, 12, 10,  2,  8,   4,  9, 10,  3,  7,  7,   2,   2][i]

# stack
# 00 push w+8
# 01 push w+8
# 02 push w+12
# 03 pop (-8)
# 04 push w+2
# 05 push w+8
# 06 pop (-11)
# 07 push w+9
# 08 pop (-3)
# 09 push w+3
# 10 pop (-3)
# 11 pop (-1)
# 12 pop (-10)
# 13 pop (-16)

# constraints
# [02] + 4 == [03]
# [05] - 3 == [06]
# [07] + 6 == [08]
# [09] + 0 == [10]
# [04] + 1 == [11]
# [01] - 2 == [12]
# [00] - 8 == [13]


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    return [line.split() for line in text.split("\n")]


def check_model_num(instructs, model_num):
    model_str = str(model_num)
    regs = {"w": 0, "x": 0, "y": 0, "z": 0}
    i = 0
    for instruct in instructs:
        op = instruct[0]
        reg = instruct[1]
        b = None
        if len(instruct) == 3:
            s = instruct[2]
            if s in regs:
                b = regs[s]
            else:
                b = int(s)
        if op == "inp":
            regs[reg] = int(model_str[i])
            i += 1
        elif op == "add":
            regs[reg] += b
        elif op == "mul":
            regs[reg] *= b
        elif op == "div":
            if b == 0:
                return False
            regs[reg] //= b
        elif op == "mod":
            regs[reg] %= b
        elif op == "eql":
            regs[reg] = int(regs[reg] == b)
    return regs["z"] == 0


def part1():
    instructs = read_input()
    model_num = 99598963999971
    assert check_model_num(instructs, model_num)
    return model_num


def part2():
    instructs = read_input()
    model_num = 93151411711211
    assert check_model_num(instructs, model_num)
    return model_num


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
