class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for i in range(len(board)):
            row = [num for num in board[i] if num != '.']
            if len(row) != len(set(row)):
                return False

        # col check
        for i in range(len(board)):
            buf = []
            for j in range(len(board[i])):
                if board[j][i] != '.':
                    buf.append(board[j][i])
            if len(buf) != len(set(buf)):
                return False

        def check_squre(row: int, col: int) -> bool:
            buf = []
            for i in range(3):
                for j in range(3):
                    val = board[row + i][col + j]
                    if val != '.':
                        buf.append(val)
            return len(buf) == len(set(buf))

        # squre check
        row = 0
        while row < len(board):
            col = 0
            while col < len(board[0]):
                if not check_squre(row, col):
                    return False
                col += 3
            row += 3
        return True