import heapq
import math


def parse_text(text, sep=None, trans=None):
    if not trans:
        trans = lambda x: x
    return [trans(s) for s in text.split(sep)]


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    trans = lambda x: [int(c) for c in x]
    return parse_text(text, "\n", trans)


ADJ = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def find_path(tiles):
    # get cave and dimensions
    cave = read_input()
    tile_width = len(cave[0])
    tile_height = len(cave)
    width = tile_width * tiles
    height = tile_height * tiles
    end = (width - 1, height - 1)

    # set tentative risk to infinity for all except start
    best_risks = [[math.inf for _ in range(width)] for _ in range(height)]
    best_risks[0][0] = 0
    # priority queue with risk, x, y
    pq = [(0, 0, 0)]

    while len(pq) > 0:
        risk, x, y = heapq.heappop(pq)
        pos = (x, y)
        if pos == end:
            return risk
        # check unvisited neighbors
        for dx, dy in ADJ:
            u = x + dx
            v = y + dy
            if u < 0 or u >= width or v < 0 or v >= height:
                continue
            # compute cumulative risk
            rx, row = divmod(u, tile_width)
            ry, col = divmod(v, tile_height)
            next_risk = cave[col][row] + rx + ry
            if next_risk > 9:
                next_risk -= 9
            next_risk += risk
            # check for lower risk path
            if next_risk >= best_risks[v][u]:
                continue
            best_risks[v][u] = next_risk
            heapq.heappush(pq, (next_risk, u, v))
    raise ValueError()


if __name__ == "__main__":
    print("Part 1:")
    print(find_path(1))
    print("Part 2:")
    print(find_path(5))
