class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_row = defaultdict(set)
        set_col = defaultdict(set)
        set_square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in set_row[r] or board[r][c] in set_col[c] or board[r][c] in set_square[(r//3, c//3)]:
                    return False
                
                set_row[r].add(board[r][c])
                set_col[c].add(board[r][c])
                set_square[(r//3,c//3)].add(board[r][c])

        return True
