
CHARS = "ABCD"
ENERGY = [1, 10, 100, 1000]
HALL_SIZE = 11
ENTRANCES = [2, 4, 6, 8]


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    return text.splitlines()


def parse_input(lines):
    text = "".join(lines)
    d = {c: i for i, c in enumerate(CHARS)}
    d["."] = -1
    return [d[c] for c in text if c in d]


def print_diagram(spots):
    s = CHARS + "."
    idx = HALL_SIZE
    diagram = [
        "#############",
        "#" + "".join(s[c] for c in spots[:idx]) + "#",
        "###" + "#".join(s[c] for c in spots[idx:idx + 4]) + "###",
    ]
    idx += 4
    while idx < len(spots):
        diagram.append(
            "  #" + "#".join(s[c] for c in spots[idx:idx + 4]) + "#")
        idx += 4
    diagram.append("  #########")
    print("\n".join(diagram))


def get_initial_remaining(spots):
    remaining = [i for i, ap in enumerate(spots) if ap != -1]
    for ap in range(4):
        idx = len(spots) - 4 + ap
        while idx >= HALL_SIZE and spots[idx] == ap:
            remaining.remove(idx)
            idx -= 4
    return remaining


def get_reachable_hallway(spots, idx, dist):
    reachable_hall = {}
    reachable_entr = {}
    left_dist = right_dist = dist
    for i in range(idx - 1, -1, -1):
        left_dist += 1
        if i in ENTRANCES:
            reachable_entr[i] = left_dist
        elif spots[i] == -1:
            reachable_hall[i] = left_dist
        else:
            break
    for i in range(idx + 1, HALL_SIZE):
        right_dist += 1
        if i in ENTRANCES:
            reachable_entr[i] = right_dist
        elif spots[i] == -1:
            reachable_hall[i] = right_dist
        else:
            break
    return reachable_hall, reachable_entr


def can_enter_room(spots, ap, dist):
    # go into room
    idx = HALL_SIZE + ap
    while idx < len(spots) and spots[idx] == -1:
        idx += 4
        dist += 1
    if dist == 0:
        return {}
    moves = {idx - 4: dist}
    # check remainder is correct
    while idx < len(spots):
        if spots[idx] != ap:
            return {}
        idx += 4
    return moves


def get_valid_moves(spots, idx):
    ap = spots[idx]
    dist = 0
    from_room = idx >= HALL_SIZE
    if from_room:
        # try leaving room
        col = (idx - HALL_SIZE) % 4
        idx -= 4
        dist += 1
        while idx >= HALL_SIZE and spots[idx] == -1:
            idx -= 4
            dist += 1
        if idx >= HALL_SIZE:
            return {}
        idx = ENTRANCES[col]
    # check if destination room can be reached
    r_hall, r_entr = get_reachable_hallway(spots, idx, dist)
    dst_entr = ENTRANCES[ap]
    if dst_entr in r_entr:
        dist = r_entr[dst_entr]
        moves = can_enter_room(spots, ap, dist)
        if moves:
            return moves
    return r_hall if from_room else {}


def move(spots, remaining, energy, lowest):
    if len(remaining) == 0:
        return energy
    least = 1E12
    for i in remaining:
        ap = spots[i]
        moves = get_valid_moves(spots, i)
        for new_idx, dist in moves.items():
            new_spots = list(spots)
            # move amphipod
            new_spots[new_idx] = ap
            new_spots[i] = -1
            new_nrg = energy + ENERGY[ap] * dist
            # check against lowest
            key = tuple(new_spots)
            if key in lowest and lowest[key] <= new_nrg:
                continue
            lowest[key] = new_nrg
            # check if reached destination
            new_remain = list(remaining)
            new_remain.remove(i)
            if new_idx < HALL_SIZE:
                new_remain.append(new_idx)
            total = move(new_spots, new_remain, new_nrg, lowest)
            least = min(total, least)
    return least


def part1():
    lines = read_input()
    spots = parse_input(lines)
    remaining = get_initial_remaining(spots)
    return move(spots, remaining, 0, {})


def part2():
    lines = read_input()
    lines.insert(-2, "  #D#C#B#A#")
    lines.insert(-2, "  #D#B#A#C#")
    spots = parse_input(lines)
    remaining = get_initial_remaining(spots)
    return move(spots, remaining, 0, {})


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
