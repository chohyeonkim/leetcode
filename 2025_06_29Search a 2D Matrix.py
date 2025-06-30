class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        left = 0
        right = ROWS - 1

        # find ROWS

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] == target:
                return True

            if matrix[mid][0] > target:
                right = mid - 1

            else:
                left = mid + 1

        r = right

        left = 0
        right = COLS - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[r][mid] == target:
                return True

            if matrix[r][mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return False
