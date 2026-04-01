class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs
        # spread from all treasures

        # corner
        if not grid or not grid[0]:
            return None
        
        # pre-process grid
        INF = 2147483647
        row, col = len(grid), len(grid[0])
        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        # process queue
        while queue:
            r, c = queue.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                cr, cc = r + dr, c + dc
                # skip conditions
                if cr < 0 or cc < 0 or cr >= row or cc >= col:
                    continue
                if grid[cr][cc] == -1:
                    continue
                # process islands 
                if grid[cr][cc] == INF:
                    grid[cr][cc] = grid[r][c] + 1
                    queue.append((cr, cc))

