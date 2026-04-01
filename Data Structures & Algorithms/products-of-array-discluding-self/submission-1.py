class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create an array with the same length
        result = [1] * len(nums)

        # go through the array from left to right and record the product
        prefix = 1
        for i in range(len(result)):
            result[i] = prefix
            # update prefix product
            prefix *= nums[i]

        suffix = 1
        for i in range(len(result) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        
        return result