class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows, n_cols = len(matrix), len(matrix[0])
        
        l, r = 0, n_rows - 1
        mid = 0
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][n_cols - 1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        if l > r:
            return False
        
        row = mid
        l, r = 0, n_cols - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False