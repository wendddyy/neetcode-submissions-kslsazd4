class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        res = [0] * (n + 1)

        res[0] = 1
        res[1] = 1

        for i in range(2, n + 1):
            if s[i - 1] != '0':
                res[i] += res[i - 1]

            if 10 <= int(s[i - 2 : i]) <= 26:
                res[i] += res[i - 2]

        return res[n]
        