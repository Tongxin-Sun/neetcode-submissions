class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        i = l
        while l < r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m - 1
                i = l
            elif matrix[m][0] <= target <= matrix[m][-1]:
                i = m
                break
            else:
                l = m + 1
                i = l
        row = matrix[i]
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if target == row[m]:
                return True
            elif target > row[m]:
                l = m + 1
            else:
                r = m - 1
        return False