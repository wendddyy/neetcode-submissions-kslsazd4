class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if [mid, right] has turning point, if cur > right and cur < mid, cur is in another part, if cur<right, in this part
        # if [mid, right] doesn't has turning point, if cur > mid and cur < right, in this part, else in another part
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] > nums[right]:
                if target > nums[right] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return left if nums[left] == target else -1