class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # corner
        if not board or not board[0] or  not word:
            return False

        # dfs, for each level, check neighbor
        # return false when reach the boundary
        def dfs(row, col, w):
            if w >= len(word):
                return True

            if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1:
                return False  
            if board[row][col] != word[w]:
                return False

            tem = board[row][col]
            board[row][col] = '#'

            found = (dfs(row+1, col, w+1) or
                    dfs(row, col+1, w+1) or
                    dfs(row, col-1, w+1) or
                    dfs(row-1, col, w+1)
            )

            board[row][col] = tem
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False