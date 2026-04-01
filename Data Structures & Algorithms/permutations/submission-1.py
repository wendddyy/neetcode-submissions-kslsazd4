class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # initialize
        res = []
        cur = []
        n = len(nums)
        used = [False]*n

        def dfs():
            if len(cur) == n:
                res.append(cur.copy())
                return

            for i in range(n):
                if used[i] == True:
                    continue
                cur.append(nums[i])
                used[i] = True
                dfs()
                cur.pop()
                used[i] = False

        dfs()
        return res