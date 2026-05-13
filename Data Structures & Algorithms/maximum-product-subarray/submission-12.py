class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = nums[0], nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            temp_max = cur_max * nums[i]
            temp_min = cur_min * nums[i]

            cur_max = max(nums[i], temp_max, temp_min)
            cur_min = min(nums[i], temp_max, temp_min)

            res = max(res, cur_max)
        return res