class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        maxL = 0
        lastSeen = {}
        for right in range(len(s)):
            if s[right] not in lastSeen:
                lastSeen[s[right]] = right
            else:
                left = max(left, lastSeen[s[right]] + 1)
                lastSeen[s[right]] = right
            maxL = max(maxL, right - left + 1)
        
        return maxL