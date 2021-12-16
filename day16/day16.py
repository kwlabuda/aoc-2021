
class BitArray():
    def __init__(self, hex_str):
        hex_num = int(hex_str, 16)
        num_bits = len(hex_str) * 4
        bit_str = f"{hex_num:b}"
        padding = "0" * (num_bits - len(bit_str))
        self.bits = padding + bit_str
        self.pos = 0

    def read_chars(self, size):
        start = self.pos
        self.pos += size
        return self.bits[start:self.pos]

    def read_bits(self, size):
        return int(self.read_chars(size), 2)

    def read_literal(self):
        lit = ""
        while True:
            b = self.read_bits(1)
            lit += self.read_chars(4)
            if b == 0:
                break
        return int(lit, 2)

    def read_packet(self):
        version = self.read_bits(3)
        type_id = self.read_bits(3)
        value = None

        if type_id == 4:
            value = self.read_literal()
        else:
            # parse subpackets
            len_type = self.read_bits(1)
            sub_vals = []
            if len_type == 0:
                sp_bits = self.read_bits(15)
                end = self.pos + sp_bits
                while self.pos != end:
                    ver, val = self.read_packet()
                    version += ver
                    sub_vals.append(val)
            else:
                num_sp = self.read_bits(11)
                for _ in range(num_sp):
                    ver, val = self.read_packet()
                    version += ver
                    sub_vals.append(val)
            # get operator type
            if type_id == 0:
                value = sum(sub_vals)
            elif type_id == 1:
                value = 1
                for sv in sub_vals:
                    value *= sv
            elif type_id == 2:
                value = min(sub_vals)
            elif type_id == 3:
                value = max(sub_vals)
            elif type_id == 5:
                value = 1 if sub_vals[0] > sub_vals[1] else 0
            elif type_id == 6:
                value = 1 if sub_vals[0] < sub_vals[1] else 0
            elif type_id == 7:
                value = 1 if sub_vals[0] == sub_vals[1] else 0
        return version, value


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    return BitArray(text)


if __name__ == "__main__":
    bits = read_input()
    version, value = bits.read_packet()
    print("Part 1:")
    print(version)
    print("Part 2:")
    print(value)
