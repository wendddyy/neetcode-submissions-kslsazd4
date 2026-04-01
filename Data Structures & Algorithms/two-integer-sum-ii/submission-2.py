class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            while left < right and numbers[left] == numbers[left+1]:
                left += 1
            while left < right and numbers[right] == numbers[right-1]:
                right -= 1
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[right] + numbers[left] > target:
                right -= 1
            else:
                return [left+1, right+1]       