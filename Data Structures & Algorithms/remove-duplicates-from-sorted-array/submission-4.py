class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # slow fast pointers
        # swap when found difference
        # then slow = fast, keep exploring

        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1
