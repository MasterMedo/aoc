with open("../input/4.txt") as f:
    numbers = [int(n) for n in next(f).split(",")]
    next(f)  # discard the first empty line
    boards = []
    board = []
    for line in f:
        if line.strip():
            board.append([[int(n), False] for n in line.split()])
        else:
            boards.append(board)
            board = []

part_1 = None
part_2 = None
seen_boards = set()
for n in numbers:
    for board_index, board in enumerate(boards):
        if board_index in seen_boards:
            continue

        for i in range(5):
            for j in range(5):
                if board[i][j][0] == n:
                    board[i][j][1] = True

                    row = all(board[x][j][1] for x in range(5))
                    col = all(board[i][y][1] for y in range(5))
                    if row or col:
                        sum_ = 0
                        for row in board:
                            for number, seen in row:
                                if not seen:
                                    sum_ += number

                        if part_1 is None:
                            part_1 = sum_ * n

                        part_2 = sum_ * n
                        seen_boards.add(board_index)

print(part_1)
print(part_2)
