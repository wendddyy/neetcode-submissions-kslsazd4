class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # corner case
        if nums is None:
            return [[]]


        nums.sort()
        res = []

        cur = []
        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()

            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[i]:
                j += 1
            dfs(j + 1)

        
        dfs(0)
        return res
            
