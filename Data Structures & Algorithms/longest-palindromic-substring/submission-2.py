class Solution:
    def longestPalindrome(self, s: str) -> str:
        # corner
        if len(s) < 1:
            return ""

        bestLeft, bestRight = 0, 0
        maxSub = 0

        def findSubStr(left, right):
            nonlocal bestLeft, bestRight, maxSub
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 >= maxSub:
                    maxSub = right - left + 1
                    bestLeft = left
                    bestRight = right
                left -= 1
                right += 1
        
        for i in range(len(s)):
            findSubStr(i, i)
            findSubStr(i, i+1)

        return s[bestLeft : bestRight + 1]