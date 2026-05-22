class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we keep 1 num fixed, and do 2sum for the remaining

        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1

            while left < right:
                target = - nums[i]
                cur_sum = nums[left] + nums[right]
                if cur_sum == target:
                    res.append([nums[left], nums[right], nums[i]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1

        return res
