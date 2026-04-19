class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pac = []
        atl = []
        res = []
        dic = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            
            visited.append((r, c))
            for dr, dc in dic:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)
            
        # pac
        for r in range(row):
            dfs(r, 0, pac)
        for c in range(col):
            dfs(0, c, pac)
        # atl
        for r in range(row):
            dfs(r, col-1, atl)
        for c in range(col):
            dfs(row-1, c, atl)
        
        for i in range(row):
            for j in range(col):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])

        return res