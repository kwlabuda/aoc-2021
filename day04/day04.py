
def read_input():
    lines = []
    with open("input.txt") as f:
        text = f.read().strip()
    entries = text.split("\n\n")
    called = [int(n) for n in entries[0].split(",")]
    boards = []
    for entry in entries[1:]:
        entry = entry.replace("\n", " ")
        boards.append([int(n) for n in entry.split()])
    return called, boards


def mark_number(board, num):
    i = 0
    for row in range(5):
        for col in range(5):
            if board[i] == num:
                board[i] = -1
                if check_row_complete(board, row):
                    return True
                if check_column_complete(board, col):
                    return True
            i += 1
    return False


def check_row_complete(board, row):
    i = row * 5
    return all(board[n] == -1 for n in range(i, i + 5))


def check_column_complete(board, col):
    return all(board[n] == -1 for n in range(col, col + 25, 5))


def sum_of_unmarked(board):
    return sum(n for n in board if n != -1)


def print_board(board):
    for row in range(5):
        i = row * 5
        print(" ".join(f"{n:02}" for n in board[i:i + 5]))
    print()


def part1():
    called, boards = read_input()
    for num in called:
        for board in boards:
            if mark_number(board, num):
                total = sum_of_unmarked(board)
                return total * num


def part2():
    called, boards = read_input()
    for num in called:
        remain_boards = []
        for board in boards:
            if mark_number(board, num):
                if len(boards) == 1:
                    print_board(board)
                    total = sum_of_unmarked(board)
                    return total * num
            else:
                remain_boards.append(board)
        boards = remain_boards


if __name__ == "__main__":
    print(f"Part 1:")
    print(part1())
    print(f"Part 2:")
    print(part2())
