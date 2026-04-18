class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i, j])
        
        while queue and fresh > 0:
            size = len(queue)
            while size > 0:
                r, c = queue.popleft()
                # up, down, left, right
                if r + 1 < row and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    fresh -= 1
                    queue.append([r + 1, c])
                if r -1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    fresh -= 1
                    queue.append([r - 1, c])
                if c + 1 < col and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    fresh -= 1
                    queue.append([r, c + 1])
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    fresh -= 1
                    queue.append([r, c - 1])
                size -= 1
            minutes += 1

        if fresh > 0:
            return -1

        return minutes
        
                