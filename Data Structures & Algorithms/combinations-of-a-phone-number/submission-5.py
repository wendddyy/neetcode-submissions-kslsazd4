class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # back tracking + for loop
        # create map
        m = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if not digits:
            return []
        
        res = []
        cur = []
        def dfs(index):
            if len(cur) == len(digits):
                res.append("".join(cur))
                return
            cur_list = m[digits[index]]
            for i in range(len(cur_list)):
                cur.append(cur_list[i])
                dfs(index + 1)
                cur.pop()
        dfs(0)
        return res