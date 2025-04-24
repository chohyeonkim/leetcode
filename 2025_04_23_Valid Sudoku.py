from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        row_map = defaultdict(set)
        col_map = defaultdict(set)
        sub_box_map = defaultdict(set)

        for y in range(ROWS):
            for x in range(COLS):

                if board[y][x] == ".":
                    continue

                else:

                    if (
                        board[y][x] in row_map[y]
                        or board[y][x] in col_map[x]
                        or board[y][x] in sub_box_map[(y // 3, x // 3)]
                    ):
                        return False

                    row_map[y].add(board[y][x])
                    col_map[x].add(board[y][x])
                    sub_box_map[(y // 3, x // 3)].add(board[y][x])

        return True
