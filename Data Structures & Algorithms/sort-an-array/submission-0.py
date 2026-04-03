class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def heapify(i, n):
            largest = i
            l = i * 2 + 1
            r = i * 2 + 2
            if l < n and nums[largest] < nums[l]:
                largest = l
            if r < n and nums[largest] < nums[r]:
                largest = r
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                heapify(largest, n) # why heapify here?

        for i in range(n // 2 - 1, -1, -1):
            heapify(i, n)
        
        for end in range(len(nums) - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            heapify(0, end)
        
        return nums
        