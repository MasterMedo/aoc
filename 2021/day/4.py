with open("../input/4.txt") as f:
    numbers = [int(n) for n in f.readline().split(",")]
    f.readline()  # discard the first empty line
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
for number in numbers:
    for board_index, board in enumerate(boards):
        if board_index in seen_boards:
            continue

        for i, j in ((i, j) for i in range(5) for j in range(5)):
            if board[i][j][0] == number:
                board[i][j][1] = True
                break
        else:
            continue

        row = all(board[x][j][1] for x in range(5))
        col = all(board[i][y][1] for y in range(5))
        if row or col:
            sum_ = sum(x for row in board for x, seen in row if not seen)

            if part_1 is None:
                part_1 = sum_ * number

            part_2 = sum_ * number
            seen_boards.add(board_index)

print(part_1)
print(part_2)
