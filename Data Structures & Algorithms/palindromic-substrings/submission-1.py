class Solution:
    def countSubstrings(self, s: str) -> int:
        # permutation + palindrome check
        n = len(s)
        res = 0

        def isPalindric(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for i in range(n):
            for j in range(i, n):
                if isPalindric(i, j):
                    res += 1

        return res