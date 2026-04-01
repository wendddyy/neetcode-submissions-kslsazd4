class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # backtracking
        # mark visited and record island area 

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 0
            if grid[row][col] == 0:
                return 0
            else:
                grid[row][col] = 0
                return (1
                + dfs(row+1, col)
                + dfs(row-1, col)
                + dfs(row, col+1)
                + dfs(row, col-1))
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                else:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area