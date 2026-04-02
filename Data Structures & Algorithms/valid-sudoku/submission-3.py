class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        freq_box = {}
        for i in range(len(board)):
            row_set = set()
            col_set = set()
            for j in range(len(board)):
                box = (i//3, j//3)
                if board[i][j] != "." and board[i][j] in row_set:
                    print(f"{board[i][j]} is duplicated in row {i}")
                    return False
                if board[j][i] != "." and board[j][i] in col_set:
                    print(f"{board[j][i]} is duplicated in col {i}")
                    return False
                if board[i][j] != '.' and box in freq_box and board[i][j] in freq_box[box]:
                    return False
                row_set.add(board[i][j])
                col_set.add(board[j][i])
                if box not in freq_box:
                    freq_box[box] = set()
                freq_box[box].add(board[i][j])


        return True