class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        cur = []
        def dfs(i, remain):
            if remain == 0:
                res.append(cur.copy())
                return
            if remain < 0 or i >= len(candidates):
                return

            cur.append(candidates[i])
            dfs(i+1, remain - candidates[i])
            cur.pop()

            j = i
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1
            dfs(j, remain)

        dfs(0, target)
        return res