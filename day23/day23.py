import heapq


CHARS = "ABCD"
ENERGY = (1, 10, 100, 1000)
HALL_SIZE = 11
ENTRANCES = (2, 4, 6, 8)


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    return text.splitlines()


def parse_input(lines):
    text = "".join(lines)
    d = {c: i for i, c in enumerate(CHARS)}
    d["."] = -1
    return [d[c] for c in text if c in d]


def row_str(chars, row):
    if row == 0:
        left = right = "#"
        sep = ""
        i = 0
        j = HALL_SIZE
    else:
        if row == 1:
            left = right = "###"
        else:
            left = "  #"
            right = "#"
        sep = "#"
        i = HALL_SIZE + (row - 1) * 4
        j = i + 4
    return left + sep.join(chars[i:j]) + right


def print_diagram(spots):
    s = CHARS + "."
    chars = "".join(s[c] for c in spots)
    rows = (len(spots) - HALL_SIZE) // 4 + 1
    diagram = ["#############"]
    diagram += [row_str(chars, r) for r in range(rows)]
    diagram.append("  #########")
    print("\n".join(diagram))


def get_room(spots, col):
    return list(range(HALL_SIZE + col, len(spots), 4))


def finished_moving(spots, idx):
    pod = spots[idx]
    # not done if in different room
    room = get_room(spots, pod)
    if idx not in room:
        return False
    # not done if other types underneath
    j = room.index(idx) + 1
    return all(spots[r] == pod for r in room[j:])


def finished(spots):
    for i in range(HALL_SIZE, len(spots)):
        if spots[i] == -1 or spots[i] != (i - HALL_SIZE) % 4:
            return False
    return True


def try_enter_room(spots, col):
    room = get_room(spots, col)
    # check how far we can enter
    if spots[room[0]] != -1:
        return None
    d = 1
    while d < len(room) and spots[room[d]] == -1:
        d += 1
    # make sure remaining pods are correct type
    if any(spots[r] != col for r in room[d:]):
        return None
    idx = room[d - 1]
    return idx, d


def get_possible_moves(spots, idx):
    pod = spots[idx]
    dist = 0

    # check if in a room
    start_in_room = idx >= HALL_SIZE
    if start_in_room:
        if finished_moving(spots, idx):
            return []
        # check can enter hallway
        col = (idx - HALL_SIZE) % 4
        room = get_room(spots, col)
        j = room.index(idx)
        if any(spots[r] != -1 for r in room[:j]):
            return []
        # move to entrance
        idx = ENTRANCES[col]
        dist = j + 1

    # in hallway
    reachable = set()
    # check spots to left
    for i in range(idx - 1, -1, -1):
        if spots[i] != -1:
            break
        reachable.add(i)
    # check spots to right
    for i in range(idx + 1, HALL_SIZE):
        if spots[i] != -1:
            break
        reachable.add(i)
    reachable_entrs = set(ENTRANCES) & reachable
    reachable_hall = reachable - reachable_entrs

    # check can enter room
    entr = ENTRANCES[pod]
    if entr in reachable_entrs:
        res = try_enter_room(spots, pod)
        if res is not None:
            i, d = res
            dist += abs(entr - idx) + d
            return [(i, dist)]
    # couldn't enter room
    if start_in_room:
        return [(i, abs(i - idx) + dist) for i in reachable_hall]
    return []


def find_best_score(spots):
    t = tuple(spots)
    pq = [(0, t)]
    best_paths = {t: 0}

    while len(pq) > 0:
        score, spots = heapq.heappop(pq)

        if finished(spots):
            return score

        # for each possible move
        pod_locs = [i for i, p in enumerate(spots) if p != -1]
        for i in pod_locs:
            pod = spots[i]
            moves = get_possible_moves(spots, i)
            for j, dist in moves:
                new_spots = list(spots)
                new_spots[i] = -1
                new_spots[j] = pod
                new_score = score + (dist * ENERGY[pod])
                key = tuple(new_spots)
                if key not in best_paths or new_score < best_paths[key]:
                    best_paths[key] = new_score
                    heapq.heappush(pq, (new_score, key))
    raise ValueError()


def part1():
    lines = read_input()
    spots = parse_input(lines)
    return find_best_score(spots)


def part2():
    lines = read_input()
    lines.insert(-2, "  #D#C#B#A#")
    lines.insert(-2, "  #D#B#A#C#")
    spots = parse_input(lines)
    return find_best_score(spots)


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
