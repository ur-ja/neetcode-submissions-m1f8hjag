class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows, n_cols = len(matrix), len(matrix[0])
        l, r = 0, n_rows * n_cols - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // n_cols
            col = mid % n_cols

            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        
        return False