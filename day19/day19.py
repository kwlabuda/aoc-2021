from itertools import combinations


class Scanner():
    def __init__(self, index, points):
        self.index = index
        self.points = points
        self.offset = None
        # get manhattan distance between points
        self.distances = []
        for pt1 in points:
            row = [distance(pt1, pt2) for pt2 in points]
            self.distances.append(row)


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    scanner_strs = text.split("\n\n")
    scanners = []
    for i, scanner_str in enumerate(scanner_strs):
        points = []
        pt_strs = scanner_str.split("\n")[1:]
        for pt_str in pt_strs:
            pt = tuple(int(c) for c in pt_str.split(","))
            points.append(pt)
        scanner = Scanner(i, points)
        scanners.append(scanner)
    scanners[0].offset = (0, 0, 0)
    return scanners


def distance(pt1, pt2):
    x1, y1, z1 = pt1
    x2, y2, z2 = pt2
    return sum(abs(pt1[i] - pt2[i]) for i in range(3))


ROTATIONS = [
    lambda x, y, z: ( x,  y,  z),
    lambda x, y, z: ( x,  z, -y),
    lambda x, y, z: ( x, -y, -z),
    lambda x, y, z: ( x, -z,  y),
    lambda x, y, z: (-x,  y, -z),
    lambda x, y, z: (-x,  z,  y),
    lambda x, y, z: (-x, -y,  z),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: ( y,  x, -z),
    lambda x, y, z: ( y,  z,  x),
    lambda x, y, z: ( y, -x,  z),
    lambda x, y, z: ( y, -z, -x),
    lambda x, y, z: (-y,  x,  z),
    lambda x, y, z: (-y,  z, -x),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (-y, -z,  x),
    lambda x, y, z: ( z,  x,  y),
    lambda x, y, z: ( z,  y, -x),
    lambda x, y, z: ( z, -x, -y),
    lambda x, y, z: ( z, -y,  x),
    lambda x, y, z: (-z,  x, -y),
    lambda x, y, z: (-z,  y,  x),
    lambda x, y, z: (-z, -x,  y),
    lambda x, y, z: (-z, -y, -x)
]


def rotate_pt(pt, n):
    x, y, z = pt
    return ROTATIONS[n](x, y, z)


def add_pts(pt1, pt2):
    x1, y1, z1 = pt1
    x2, y2, z2 = pt2
    return x1 + x2, y1 + y2, z1 + z2


def sub_pts(pt1, pt2):
    x1, y1, z1 = pt1
    x2, y2, z2 = pt2
    return x1 - x2, y1 - y2, z1 - z2


def check_overlap(scanner1, scanner2):
    for i in range(len(scanner1.points)):
        s1 = set(scanner1.distances[i])
        for j in range(len(scanner2.points)):
            s2 = set(scanner2.distances[j])
            overlapping = s1 & s2
            if len(overlapping) >= 12:
                translate_pts(scanner1, i, scanner2, j)
                return True
    return False


def translate_pts(scanner1, idx1, scanner2, idx2):
    pt1 = scanner1.points[idx1]
    s1 = set(scanner1.points)
    for r in range(24):
        rotated2 = [rotate_pt(pt, r) for pt in scanner2.points]
        pt2 = rotated2[idx2]
        diff = sub_pts(pt1, pt2)
        moved = [add_pts(pt, diff) for pt in rotated2]
        overlapping = s1 & set(moved)
        if len(overlapping) >= 12:
            scanner2.points = moved
            scanner2.offset = diff
            return
    raise ValueError("Translation not found")


def get_scanners():
    scanners = read_input()
    known = [scanners[0]]
    unknown = scanners[1:]
    while len(unknown) > 0:
        new_known = None
        for scanner1 in known:
            for scanner2 in unknown:
                if check_overlap(scanner1, scanner2):
                    new_known = scanner2
                    break
            if new_known is not None:
                break
        assert new_known is not None
        unknown.remove(new_known)
        known.append(new_known)
    return scanners


def get_num_beacons(scanners):
    beacons = set(pt for s in scanners for pt in s.points)
    return len(beacons)


def find_furthest(scanners):
    furthest = -1
    pairs = combinations(scanners, 2)
    return max(distance(s1.offset, s2.offset) for s1, s2 in pairs)


if __name__ == "__main__":
    scanners = get_scanners()
    print("Part 1:")
    print(get_num_beacons(scanners))
    print("Part 2:")
    print(find_furthest(scanners))
