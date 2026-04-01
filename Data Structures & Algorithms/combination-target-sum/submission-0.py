class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        cur = []
        def dfs(i, remain):
            # base case:
            if remain == 0:
                res.append(cur.copy())
                return
            if remain < 0:
                return
            if i > len(nums) - 1:
                return

            # recursive call
            cur.append(nums[i])
            dfs(i, remain - nums[i])
            cur.pop()

            dfs(i+1, remain)

        dfs(0, target)
        return res