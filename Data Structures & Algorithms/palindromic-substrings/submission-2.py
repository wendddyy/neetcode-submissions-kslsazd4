class Solution:
    def countSubstrings(self, s: str) -> int:
        # permutation + palindrome check
        n = len(s)
        res = 0

        def expand(left, right):
            nonlocal res
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)
            expand(i, i+1)

        return res