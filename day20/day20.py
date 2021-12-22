
LIGHT = "#"
DARK = "."

class Image():
    def __init__(self, algo, pixels):
        self.algo = algo
        self.start = 0
        self.x_end = len(pixels[0]) - 1
        self.y_end = len(pixels) - 1
        # create set of lit pixels
        self.lit_pixels = set()
        for y, row in enumerate(pixels):
            for x, px in enumerate(row):
                if px == LIGHT:
                    self.lit_pixels.add((x, y))

    def get_grid(self, lit_outside, padding=2):
        top_left = self.start - padding
        right = self.x_end + 1 + padding
        bottom = self.y_end + 1 + padding
        grid = []
        for y in range(top_left, bottom):
            row = []
            for x in range(top_left, right):
                if ((x, y) in self.lit_pixels
                    or lit_outside and self.is_outside(x, y)):
                    row.append(LIGHT)
                else:
                    row.append(DARK)
            grid.append("".join(row))
        return "\n".join(grid)

    def is_outside(self, x, y):
        return (x <= self.start or x >= self.x_end
            or y <= self.start or y >= self.y_end)

    def output_pixel(self, x, y, lit_outside):
        val = 256
        index = 0
        for v in range(y - 1, y + 2):
            for u in range(x - 1, x + 2):
                if ((u, v) in self.lit_pixels
                    or lit_outside and self.is_outside(u, v)):
                    index |= val
                val >>= 1
        return self.algo[index] == LIGHT

    def enhance(self, rounds):
        lit_outside = False
        for _ in range(rounds):
            # update boundaries
            self.start -= 1
            self.x_end += 1
            self.y_end += 1
            new_pixels = set()
            # update which pixels are lit
            for y in range(self.start, self.y_end + 1):
                for x in range(self.start, self.x_end + 1):
                    if self.output_pixel(x, y, lit_outside):
                        new_pixels.add((x, y))
            self.lit_pixels = new_pixels
            # check to swap pixels outside image
            if lit_outside:
                if self.algo[-1] == DARK:
                    lit_outside = False
            elif self.algo[0] == LIGHT:
                lit_outside = True


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    algo, pixel_str = text.split("\n\n")
    pixels = pixel_str.split("\n")
    return algo, pixels


def part1():
    algo, pixels = read_input()
    image = Image(algo, pixels)
    image.enhance(2)
    return len(image.lit_pixels)


def part2():
    algo, pixels = read_input()
    image = Image(algo, pixels)
    image.enhance(50)
    return len(image.lit_pixels)


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
