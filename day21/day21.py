from collections import Counter


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    line1, line2 = text.split("\n", 1)
    start1 = int(line1.split(": ")[1])
    start2 = int(line2.split(": ")[1])
    return start1, start2


def part1():
    pos1, pos2 = read_input()
    # make player position and die rolls 0 based
    pos1 -= 1
    pos2 -= 1
    # pattern repeats every 10
    die_rolls = [sum(range(i, i + 3)) % 10 for i in range(1, 11)]

    score1 = 0
    score2 = 0
    die_pos = 0
    rolls = 0
    target = 1000

    while True:
        # player 1
        pos1 = (pos1 + die_rolls[die_pos]) % 10
        die_pos = (die_pos + 3) % 10
        rolls += 3
        score1 += pos1 + 1
        if score1 >= target:
            break
        # player 2
        pos2 = (pos2 + die_rolls[die_pos]) % 10
        die_pos = (die_pos + 3) % 10
        rolls += 3
        score2 += pos2 + 1
        if score2 >= target:
            break
    return rolls * min(score1, score2)


class Game():
    def __init__(self, positions, scores, player):
        self.positions = tuple(positions)
        self.scores = tuple(scores)
        self.player = player

    def __hash__(self):
        return hash((self.positions, self.scores, self.player))


def get_quantum_die_rolls():
    quantum_rolls = {}
    totals = []
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                totals.append(i + j + k)
    return tuple(Counter(totals).items())


def part2():
    pos1, pos2 = read_input()
    # make player position 0 based
    pos1 -= 1
    pos2 -= 1

    quantum_rolls = get_quantum_die_rolls()
    games = {Game((pos1, pos2), (0, 0), 0): 1}
    target = 21
    wins = [0, 0]

    while len(games) > 0:
        game, game_count = games.popitem()
        positions = game.positions
        scores = game.scores
        player = game.player
        for roll, roll_count in quantum_rolls:
            new_count = roll_count * game_count
            new_pos = (positions[player] + roll) % 10
            new_score = scores[player] + new_pos + 1
            if new_score >= target:
                wins[player] += new_count
            else:
                new_positions = None
                new_scores = None
                if player == 0:
                    new_positions = (new_pos, positions[1])
                    new_scores = (new_score, scores[1])
                else:
                    new_positions = (positions[0], new_pos)
                    new_scores = (scores[0], new_score)
                new_game = Game(new_positions, new_scores, player ^ 1)
                if new_game in games:
                    games[new_game] += new_count
                else:
                    games[new_game] = new_count
    return max(wins)


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
