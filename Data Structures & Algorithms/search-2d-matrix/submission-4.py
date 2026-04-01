class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        # mid in 2d: [mid / row, mid % col]
        # loop terminate condition: right < left

        # corner:
        if not matrix or not matrix[0]:
            return False

        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            cur = matrix[row][col]
            if cur == target:
                return True
            if cur < target:
                left = mid + 1
            elif cur > target:
                right = mid - 1
        
        return False

        