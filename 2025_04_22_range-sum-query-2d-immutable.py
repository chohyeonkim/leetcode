class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for y in range(1, ROWS + 1):
            prefix = 0
            for x in range(1, COLS + 1):

                prefix += matrix[y - 1][x - 1]
                above = self.prefix[y - 1][x]
                self.prefix[y][x] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottom_right = self.prefix[row2][col2]
        left = self.prefix[row2][col1 - 1]
        top_right = self.prefix[row1 - 1][col2]
        top_left = self.prefix[row1 - 1][col1 - 1]

        res = bottom_right - left - top_right + top_left
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
