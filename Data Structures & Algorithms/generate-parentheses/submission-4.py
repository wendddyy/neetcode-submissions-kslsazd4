class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # left must >= right parentheses
        # use loop to go through all posibilities?
        # if left == right: must add left
        # if left > right: add left / add right, and pop

        if not n:
            return []
        
        res = []
        cur = []
        def dfs(left_remain, right_remain):
            if left_remain == 0 and right_remain == 0:
                res.append("".join(cur))
                return

            if left_remain > 0:
                cur.append('(')
                dfs(left_remain - 1, right_remain)
                cur.pop()
            if left_remain < right_remain:
                cur.append(')')
                dfs(left_remain, right_remain - 1)
                cur.pop()

        dfs(n, n)
        return res