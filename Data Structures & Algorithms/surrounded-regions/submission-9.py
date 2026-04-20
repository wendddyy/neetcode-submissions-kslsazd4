class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # queue + outside to inside
        invalid = set()
        queue = deque()
        row = len(board)
        col = len(board[0])
        dic = ([1, 0], [-1, 0], [0, 1], [0, -1])

        # four boarders
        for r in range(row):
            if board[r][0] == 'O':
                queue.append((r, 0))
            if board[r][col - 1] == 'O':
                queue.append((r, col - 1))
        for c in range(col):
            if board[0][c] == 'O':
                queue.append((0, c))
            if board[row - 1][c] == 'O':
                queue.append((row - 1, c))
        
        while queue:
            r, c = queue.popleft()
            invalid.add((r, c))
            for dr, dc in dic:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == 'O':
                    if (nr, nc) not in invalid:
                        queue.append((nr, nc))

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i, j) not in invalid:
                    board[i][j] = 'X'        
