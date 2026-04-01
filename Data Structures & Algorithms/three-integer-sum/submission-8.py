class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # loop + 2sum
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue

            left, right = i+1, len(nums) -1
            # 2sum
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum + nums[i] > 0:
                    right -= 1
                elif cur_sum + nums[i] < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res