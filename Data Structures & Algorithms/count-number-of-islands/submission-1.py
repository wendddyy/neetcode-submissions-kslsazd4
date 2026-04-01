class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # backtracking
        if not grid or not grid[0]:
            return 0

        def dfs(row, col):
            if row >= len(grid) or row < 0 or col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                else:
                    result += 1
                    dfs(i, j)

        return result
