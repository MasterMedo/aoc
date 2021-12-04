with open("../input/4.txt") as f:
    tickets = list(map(int, next(f).strip().split(",")))
    next(f)
    boards = []
    for board_string in f.read()[:-1].split("\n\n"):
        board = {}
        for i, line in enumerate(board_string.split("\n")):
            for j, n in enumerate(map(int, line.strip().split())):
                board[i, j] = [n, False]

        boards.append(board)

part_1 = None
part_2 = None
seen_boards = set()
for ticket in tickets:
    for board_index, board in enumerate(boards):
        if board_index in seen_boards:
            continue

        for i, j in board:
            if board[i, j][0] == ticket:
                board[i, j][1] = True

                row = all(board[x, j][1] for x in range(5))
                col = all(board[i, y][1] for y in range(5))
                if row or col:
                    sum_ = sum(n for n, b in board.values() if not b) * ticket
                    if part_1 is None:
                        part_1 = sum_

                    part_2 = sum_
                    seen_boards.add(board_index)

print(part_1)
print(part_2)
