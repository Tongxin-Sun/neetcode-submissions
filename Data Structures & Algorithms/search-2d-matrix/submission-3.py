class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                left, right = 0, len(matrix[0]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if target == matrix[m][mid]:
                        return True
                    if target < matrix[m][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1 
        return False