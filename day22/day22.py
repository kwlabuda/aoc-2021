import re


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    lines = text.split("\n")
    steps = []
    for line in lines:
        on = line.startswith("on")
        bounds = tuple(int(d) for d in re.findall(r"-?\d+", line))
        assert len(bounds) == 6
        steps.append((on, bounds))
    return steps


def part1():
    min_pos = -50
    max_pos = 50
    steps = read_input()
    cubes = set()

    for step in steps:
        on, pts = step
        x_min, x_max, y_min, y_max, z_min, z_max = pts
        x_min = max(x_min, min_pos)
        x_max = min(x_max, max_pos)
        y_min = max(y_min, min_pos)
        y_max = min(y_max, max_pos)
        z_min = max(z_min, min_pos)
        z_max = min(z_max, max_pos)
        for z in range(z_min, z_max + 1):
            for y in range(y_min, y_max + 1):
                for x in range(x_min, x_max + 1):
                    if on:
                        cubes.add((x, y, z))
                    else:
                        cubes.discard((x, y, z))
    return len(cubes)


class Cuboid():
    def __init__(self, bounds):
        self.x_min = bounds[0]
        self.x_max = bounds[1]
        self.y_min = bounds[2]
        self.y_max = bounds[3]
        self.z_min = bounds[4]
        self.z_max = bounds[5]
        self.gaps = []

    def volume(self):
        a = self.x_max - self.x_min + 1
        b = self.y_max - self.y_min + 1
        c = self.z_max - self.z_min + 1
        return (a * b * c) - sum(gap.volume() for gap in self.gaps)

    def overlap(self, other):
        x_min = max(self.x_min, other.x_min)
        x_max = min(self.x_max, other.x_max)
        if x_max - x_min < 0:
            return None
        y_min = max(self.y_min, other.y_min)
        y_max = min(self.y_max, other.y_max)
        if y_max - y_min < 0:
            return None
        z_min = max(self.z_min, other.z_min)
        z_max = min(self.z_max, other.z_max)
        if z_max - z_min < 0:
            return None
        points = (x_min, x_max, y_min, y_max, z_min, z_max)
        return Cuboid(points)

    def remove(self, other):
        shared = self.overlap(other)
        if shared is None:
            return
        for gap in self.gaps:
            gap.remove(shared)
        self.gaps.append(shared)


def part2():
    steps = read_input()
    cuboids = []
    for step in steps:
        on, bounds = step
        cuboid = Cuboid(bounds)
        for existing in cuboids:
            existing.remove(cuboid)
        if on:
            cuboids.append(cuboid)
    return sum(cuboid.volume() for cuboid in cuboids)


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
