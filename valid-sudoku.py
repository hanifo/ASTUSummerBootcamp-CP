class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] != ".":
                            if board[r][c] in seen:
                                return False
                            seen.add(board[r][c])
        return True
