class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        arrayFrom0 = [0] * len(nums)
        arrayFrom1 = [0] * len(nums)

        # init
        arrayFrom0[0], arrayFrom0[1] = nums[0], max(nums[0], nums[1])
        arrayFrom1[0], arrayFrom1[1], arrayFrom1[2] = 0, nums[1], max(nums[1], nums[2])
        for i in range(2, len(nums) - 1):
            arrayFrom0[i] = max(arrayFrom0[i - 2] + nums[i], arrayFrom0[i - 1])
        
        for i in range(3, len(nums)):
            arrayFrom1[i] = max(arrayFrom1[i - 2] + nums[i], arrayFrom1[i - 1])

        return max(arrayFrom0[len(nums) - 2], arrayFrom1[len(nums) - 1])