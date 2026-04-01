class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # sliding window
        # corner
        if not s:
            return 0

        max_l = 0
        left = 0
        for right in range(1, len(s)):
            for temp in range(left, right):
                if s[temp] == s[right]:
                    left = temp + 1
                    break
            max_l = max(max_l, right - left)

        return max_l + 1