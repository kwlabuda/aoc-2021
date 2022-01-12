import heapq


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
    start = (0, 0)
    end = (width - 1, height - 1)

    # heuristic function
    h = lambda target, pos: (target[0] - pos[0]) + (target[1] - pos[1])
    # cheapest paths for each node
    g_score = {start: 0}
    # priority queue of discovered nodes sorted by f score
    pq = [(h(end, start), *start)]

    while len(pq) > 0:
        _, x, y = heapq.heappop(pq)
        pos = (x, y)
        risk = g_score[pos]
        if pos == end:
            return risk
        # for each neighbor
        for dx, dy in ADJ:
            u = x + dx
            v = y + dy
            if u < 0 or u >= width or v < 0 or v >= height:
                continue
            # compute cumulative risk
            rx, row = divmod(u, tile_width)
            ry, col = divmod(v, tile_height)
            step = cave[col][row] + rx + ry
            if step > 9:
                step -= 9
            next_risk = risk + step
            # check for lower risk path
            n = (u, v)
            if n not in g_score or next_risk < g_score[n]:
                g_score[n] = next_risk
                f_score = next_risk + h(end, n)
                heapq.heappush(pq, (f_score, u, v))
    raise ValueError()


if __name__ == "__main__":
    print("Part 1:")
    print(find_path(1))
    print("Part 2:")
    print(find_path(5))
