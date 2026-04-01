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
            while j + 1 < len(candidates) and candidates[i] == candidates[j + 1]:
                j += 1
            dfs(j+1, remain)

        dfs(0, target)
        return res