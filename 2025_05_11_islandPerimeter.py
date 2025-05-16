class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = set()

        def dfs(r, c):

            stack = [(r, c)]

            res = 0

            while stack:

                y, x = stack.pop()

                if y < 0 or y >= ROWS or x < 0 or x >= COLS or grid[y][x] == 0:
                    res += 1
                    continue

                if (y, x) in visited:
                    continue

                visited.add((y, x))

                for dy, dx in direction:
                    stack.append((y + dy, x + dx))

            return res

        for y in range(ROWS):
            for x in range(COLS):

                if grid[y][x] == 1:
                    return dfs(y, x)


# 3 3 3 2 3 2
# -> 16
